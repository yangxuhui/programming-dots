# Protobuf
## 基本使用
### 代码生成
* python: `protoc -I=$SRC_DIR --python_out=$DST_DIR $SRC_DIR/addressbook.proto`
* go: `protoc -I=$SRC_DIR --go_out=$DST_DIR $SRC_DIR/addressbook.proto`
* c++: `protoc -I=$SRC_DIR --cpp_out=$DST_DIR $SRC_DIR/addressbook.proto`
### API
#### python
* > You cannot assign a value to an embedded message field. Instead, assigning a value to any field within the child message implies setting the message field in the parent.
    * `CopyFrom`
