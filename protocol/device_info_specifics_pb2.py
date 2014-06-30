# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: device_info_specifics.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import sync_enums_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='device_info_specifics.proto',
  package='sync_pb',
  serialized_pb='\n\x1b\x64\x65vice_info_specifics.proto\x12\x07sync_pb\x1a\x10sync_enums.proto\"\xa3\x01\n\x13\x44\x65viceInfoSpecifics\x12\x12\n\ncache_guid\x18\x01 \x01(\t\x12\x13\n\x0b\x63lient_name\x18\x02 \x01(\t\x12\x32\n\x0b\x64\x65vice_type\x18\x03 \x01(\x0e\x32\x1d.sync_pb.SyncEnums.DeviceType\x12\x17\n\x0fsync_user_agent\x18\x04 \x01(\t\x12\x16\n\x0e\x63hrome_version\x18\x05 \x01(\tB\x04H\x03`\x01')




_DEVICEINFOSPECIFICS = _descriptor.Descriptor(
  name='DeviceInfoSpecifics',
  full_name='sync_pb.DeviceInfoSpecifics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cache_guid', full_name='sync_pb.DeviceInfoSpecifics.cache_guid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='client_name', full_name='sync_pb.DeviceInfoSpecifics.client_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='device_type', full_name='sync_pb.DeviceInfoSpecifics.device_type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sync_user_agent', full_name='sync_pb.DeviceInfoSpecifics.sync_user_agent', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='chrome_version', full_name='sync_pb.DeviceInfoSpecifics.chrome_version', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_start=59,
  serialized_end=222,
)

_DEVICEINFOSPECIFICS.fields_by_name['device_type'].enum_type = sync_enums_pb2._SYNCENUMS_DEVICETYPE
DESCRIPTOR.message_types_by_name['DeviceInfoSpecifics'] = _DEVICEINFOSPECIFICS

class DeviceInfoSpecifics(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DEVICEINFOSPECIFICS

  # @@protoc_insertion_point(class_scope:sync_pb.DeviceInfoSpecifics)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), 'H\003`\001')
# @@protoc_insertion_point(module_scope)
