# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: managed_user_setting_specifics.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='managed_user_setting_specifics.proto',
  package='sync_pb',
  serialized_pb='\n$managed_user_setting_specifics.proto\x12\x07sync_pb\":\n\x1bManagedUserSettingSpecifics\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\tB\x04H\x03`\x01')




_MANAGEDUSERSETTINGSPECIFICS = _descriptor.Descriptor(
  name='ManagedUserSettingSpecifics',
  full_name='sync_pb.ManagedUserSettingSpecifics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='sync_pb.ManagedUserSettingSpecifics.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='sync_pb.ManagedUserSettingSpecifics.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=49,
  serialized_end=107,
)

DESCRIPTOR.message_types_by_name['ManagedUserSettingSpecifics'] = _MANAGEDUSERSETTINGSPECIFICS

class ManagedUserSettingSpecifics(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MANAGEDUSERSETTINGSPECIFICS

  # @@protoc_insertion_point(class_scope:sync_pb.ManagedUserSettingSpecifics)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), 'H\003`\001')
# @@protoc_insertion_point(module_scope)
