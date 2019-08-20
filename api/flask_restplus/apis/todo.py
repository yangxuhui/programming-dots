# -*- coding: utf-8 -*-
from flask import Blueprint
from flask_restplus import Api, Resource, fields

blueprint = Blueprint('todo', __name__)
api = Api(blueprint, version='1.0', title='TodoMVC API',
          description='A simple TodoMVC API',
          doc='/doc/')


model = api.model('Todo', {
    'id': fields.Integer(readonly=True, description='The task unique identifier'),
    'task': fields.String(required=True, description='The task details')
})


class TodoDAO:
    def __init__(self):
        self.counter = 0
        self.todos = []

    def get(self, id):
        for todo in self.todos:
            if todo['id'] == id:
                return todo
        api.abort(404, "Todo {} doesn't exist".format(id))

    def create(self, data):
        todo = data
        self.counter += 1
        todo['id'] = self.counter
        self.todos.append(todo)
        return todo

    def update(self, id, data):
        todo = self.get(id)
        self.todos.remove(todo)


DAO = TodoDAO()


@api.route('/')
class TodoList(Resource):
    '''Shows a list of all todos, and lets you POST to add new tasks'''
    @api.doc('list_todos')
    @api.marshal_list_with(model)
    def get(self):
        '''List all tasks'''
        return DAO.todos

    @api.doc('create_todo')
    @api.expect(model)
    @api.marshal_with(model, code=201)
    def post(self):
        '''Create a new task'''
        return DAO.create(api.payload), 201


@api.route('/<int:id>')
@api.response(404, 'Todo not found')
@api.param('id', 'The task identifier')
class Todo(Resource):
    @api.doc('get_todo')
    @api.marshal_with(model)
    def get(self, id):
        '''Fetch a given resource'''
        return DAO.get(id)

    @api.doc('delete_todo')
    @api.response(204, 'Todo deleted')
    def delete(self, id):
        DAO.delete(id)
        return '', 204

    @api.expect(model)
    @api.marshal_with(model)
    def put(self, id):
        '''Update a task given its identifier'''
        return DAO.update(id, api.payload)
