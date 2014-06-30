# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: history_delete_directive_specifics.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='history_delete_directive_specifics.proto',
  package='sync_pb',
  serialized_pb='\n(history_delete_directive_specifics.proto\x12\x07sync_pb\"\x95\x01\n\x1fHistoryDeleteDirectiveSpecifics\x12\x37\n\x13global_id_directive\x18\x01 \x01(\x0b\x32\x1a.sync_pb.GlobalIdDirective\x12\x39\n\x14time_range_directive\x18\x02 \x01(\x0b\x32\x1b.sync_pb.TimeRangeDirective\"V\n\x11GlobalIdDirective\x12\x11\n\tglobal_id\x18\x01 \x03(\x03\x12\x17\n\x0fstart_time_usec\x18\x02 \x01(\x03\x12\x15\n\rend_time_usec\x18\x03 \x01(\x03\"D\n\x12TimeRangeDirective\x12\x17\n\x0fstart_time_usec\x18\x01 \x01(\x03\x12\x15\n\rend_time_usec\x18\x02 \x01(\x03\x42\x04H\x03`\x01')




_HISTORYDELETEDIRECTIVESPECIFICS = _descriptor.Descriptor(
  name='HistoryDeleteDirectiveSpecifics',
  full_name='sync_pb.HistoryDeleteDirectiveSpecifics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='global_id_directive', full_name='sync_pb.HistoryDeleteDirectiveSpecifics.global_id_directive', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='time_range_directive', full_name='sync_pb.HistoryDeleteDirectiveSpecifics.time_range_directive', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=54,
  serialized_end=203,
)


_GLOBALIDDIRECTIVE = _descriptor.Descriptor(
  name='GlobalIdDirective',
  full_name='sync_pb.GlobalIdDirective',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='global_id', full_name='sync_pb.GlobalIdDirective.global_id', index=0,
      number=1, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start_time_usec', full_name='sync_pb.GlobalIdDirective.start_time_usec', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end_time_usec', full_name='sync_pb.GlobalIdDirective.end_time_usec', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=205,
  serialized_end=291,
)


_TIMERANGEDIRECTIVE = _descriptor.Descriptor(
  name='TimeRangeDirective',
  full_name='sync_pb.TimeRangeDirective',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start_time_usec', full_name='sync_pb.TimeRangeDirective.start_time_usec', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end_time_usec', full_name='sync_pb.TimeRangeDirective.end_time_usec', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=293,
  serialized_end=361,
)

_HISTORYDELETEDIRECTIVESPECIFICS.fields_by_name['global_id_directive'].message_type = _GLOBALIDDIRECTIVE
_HISTORYDELETEDIRECTIVESPECIFICS.fields_by_name['time_range_directive'].message_type = _TIMERANGEDIRECTIVE
DESCRIPTOR.message_types_by_name['HistoryDeleteDirectiveSpecifics'] = _HISTORYDELETEDIRECTIVESPECIFICS
DESCRIPTOR.message_types_by_name['GlobalIdDirective'] = _GLOBALIDDIRECTIVE
DESCRIPTOR.message_types_by_name['TimeRangeDirective'] = _TIMERANGEDIRECTIVE

class HistoryDeleteDirectiveSpecifics(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _HISTORYDELETEDIRECTIVESPECIFICS

  # @@protoc_insertion_point(class_scope:sync_pb.HistoryDeleteDirectiveSpecifics)

class GlobalIdDirective(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GLOBALIDDIRECTIVE

  # @@protoc_insertion_point(class_scope:sync_pb.GlobalIdDirective)

class TimeRangeDirective(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TIMERANGEDIRECTIVE

  # @@protoc_insertion_point(class_scope:sync_pb.TimeRangeDirective)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), 'H\003`\001')
# @@protoc_insertion_point(module_scope)
