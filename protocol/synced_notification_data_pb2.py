# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: synced_notification_data.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import synced_notification_render_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='synced_notification_data.proto',
  package='sync_pb',
  serialized_pb='\n\x1esynced_notification_data.proto\x12\x07sync_pb\x1a synced_notification_render.proto\"F\n\x1cSyncedNotificationIdentifier\x12\x0e\n\x06\x61pp_id\x18\x01 \x01(\t\x12\x16\n\x0e\x63oalescing_key\x18\x02 \x01(\t\"O\n\x19SyncedNotificationCreator\x12\x0f\n\x07gaia_id\x18\x01 \x01(\x03\x12\x11\n\tis_system\x18\x02 \x01(\x08\x12\x0e\n\x06\x61pp_id\x18\x03 \x01(\t\"/\n\x1cSyncedNotificationRecipients\x12\x0f\n\x07gaia_id\x18\x01 \x03(\x03\"\x93\x01\n\x12SyncedNotification\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x13\n\x0b\x65xternal_id\x18\x02 \x01(\t\x12\x33\n\x07\x63reator\x18\x03 \x01(\x0b\x32\".sync_pb.SyncedNotificationCreator\x12%\n\x0b\x63lient_data\x18\x04 \x01(\x0b\x32\x10.sync_pb.MapData\"\x84\x04\n\x1b\x43oalescedSyncedNotification\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x0e\n\x06\x61pp_id\x18\x02 \x01(\t\x12\x31\n\x0cnotification\x18\x03 \x03(\x0b\x32\x1b.sync_pb.SyncedNotification\x12:\n\x0brender_info\x18\x04 \x01(\x0b\x32%.sync_pb.SyncedNotificationRenderInfo\x12\x42\n\nread_state\x18\x05 \x01(\x0e\x32..sync_pb.CoalescedSyncedNotification.ReadState\x12\x1a\n\x12\x63reation_time_msec\x18\x06 \x01(\x04\x12?\n\x08priority\x18\x07 \x01(\x0e\x32-.sync_pb.CoalescedSyncedNotification.Priority\x12\x19\n\x11user_action_token\x18\x08 \x01(\t\x12\x1d\n\x15last_modified_version\x18\t \x01(\x04\x12\x14\n\x0csort_version\x18\n \x01(\x04\":\n\tReadState\x12\n\n\x06UNREAD\x10\x01\x12\x08\n\x04READ\x10\x02\x12\r\n\tDISMISSED\x10\x03\x12\x08\n\x04SEEN\x10\x04\",\n\x08Priority\x12\r\n\tINVISIBLE\x10\x01\x12\x07\n\x03LOW\x10\x02\x12\x08\n\x04HIGH\x10\x03\"^\n\x16SyncedNotificationList\x12\x44\n\x16\x63oalesced_notification\x18\x01 \x03(\x0b\x32$.sync_pb.CoalescedSyncedNotification\"d\n\x07MapData\x12%\n\x05\x65ntry\x18\x01 \x03(\x0b\x32\x16.sync_pb.MapData.Entry\x1a\x32\n\x05\x45ntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1c\n\x05value\x18\x02 \x01(\x0b\x32\r.sync_pb.Data\"\xa7\x01\n\x04\x44\x61ta\x12\x15\n\rboolean_value\x18\x01 \x01(\x08\x12\x11\n\tint_value\x18\x02 \x01(\x05\x12\x13\n\x0b\x66loat_value\x18\x03 \x01(\x01\x12\x14\n\x0cstring_value\x18\x04 \x01(\t\x12%\n\nlist_value\x18\x05 \x01(\x0b\x32\x11.sync_pb.ListData\x12#\n\tmap_value\x18\x06 \x01(\x0b\x32\x10.sync_pb.MapData\"(\n\x08ListData\x12\x1c\n\x05value\x18\x01 \x03(\x0b\x32\r.sync_pb.Data\"\xc6\x02\n\rRenderContext\x12\x36\n\x0b\x64\x65vice_type\x18\x01 \x01(\x0e\x32!.sync_pb.RenderContext.DeviceType\x12\x15\n\rlanguage_code\x18\x02 \x01(\t\"\xe5\x01\n\nDeviceType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x12\n\x0eIOS_NON_RETINA\x10\x01\x12\x0e\n\nIOS_RETINA\x10\x02\x12\x10\n\x0c\x41NDROID_MDPI\x10\x03\x12\x10\n\x0c\x41NDROID_HDPI\x10\x04\x12\x11\n\rANDROID_XHDPI\x10\x05\x12\x11\n\rANDROID_TVDPI\x10\x06\x12\x16\n\x12\x44\x45SKTOP_NON_RETINA\x10\x07\x12\x12\n\x0e\x44\x45SKTOP_RETINA\x10\x08\x12\x12\n\x0e\x41NDROID_XXHDPI\x10\t\x12\r\n\tCHROME_1X\x10\n\x12\r\n\tCHROME_2X\x10\x0b\"o\n\x07\x41ppList\x12.\n\x04type\x18\x01 \x01(\x0e\x32\x15.sync_pb.AppList.Type:\tWHITELIST\x12\x0e\n\x06\x61pp_id\x18\x02 \x03(\t\"$\n\x04Type\x12\r\n\tWHITELIST\x10\x01\x12\r\n\tBLACKLIST\x10\x02\"t\n\rServerContext\x12.\n\x0erender_context\x18\x01 \x01(\x0b\x32\x16.sync_pb.RenderContext\x12\"\n\x08\x61pp_list\x18\x02 \x01(\x0b\x32\x10.sync_pb.AppList\x12\x0f\n\x07view_id\x18\x03 \x01(\tB\x04H\x03`\x01')



_COALESCEDSYNCEDNOTIFICATION_READSTATE = _descriptor.EnumDescriptor(
  name='ReadState',
  full_name='sync_pb.CoalescedSyncedNotification.ReadState',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNREAD', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='READ', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DISMISSED', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SEEN', index=3, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=842,
  serialized_end=900,
)

_COALESCEDSYNCEDNOTIFICATION_PRIORITY = _descriptor.EnumDescriptor(
  name='Priority',
  full_name='sync_pb.CoalescedSyncedNotification.Priority',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INVISIBLE', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOW', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HIGH', index=2, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=902,
  serialized_end=946,
)

_RENDERCONTEXT_DEVICETYPE = _descriptor.EnumDescriptor(
  name='DeviceType',
  full_name='sync_pb.RenderContext.DeviceType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IOS_NON_RETINA', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IOS_RETINA', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ANDROID_MDPI', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ANDROID_HDPI', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ANDROID_XHDPI', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ANDROID_TVDPI', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DESKTOP_NON_RETINA', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DESKTOP_RETINA', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ANDROID_XXHDPI', index=9, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHROME_1X', index=10, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHROME_2X', index=11, number=11,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1456,
  serialized_end=1685,
)

_APPLIST_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='sync_pb.AppList.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='WHITELIST', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BLACKLIST', index=1, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1762,
  serialized_end=1798,
)


_SYNCEDNOTIFICATIONIDENTIFIER = _descriptor.Descriptor(
  name='SyncedNotificationIdentifier',
  full_name='sync_pb.SyncedNotificationIdentifier',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='app_id', full_name='sync_pb.SyncedNotificationIdentifier.app_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='coalescing_key', full_name='sync_pb.SyncedNotificationIdentifier.coalescing_key', index=1,
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
  serialized_start=77,
  serialized_end=147,
)


_SYNCEDNOTIFICATIONCREATOR = _descriptor.Descriptor(
  name='SyncedNotificationCreator',
  full_name='sync_pb.SyncedNotificationCreator',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gaia_id', full_name='sync_pb.SyncedNotificationCreator.gaia_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_system', full_name='sync_pb.SyncedNotificationCreator.is_system', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='app_id', full_name='sync_pb.SyncedNotificationCreator.app_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=149,
  serialized_end=228,
)


_SYNCEDNOTIFICATIONRECIPIENTS = _descriptor.Descriptor(
  name='SyncedNotificationRecipients',
  full_name='sync_pb.SyncedNotificationRecipients',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gaia_id', full_name='sync_pb.SyncedNotificationRecipients.gaia_id', index=0,
      number=1, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=230,
  serialized_end=277,
)


_SYNCEDNOTIFICATION = _descriptor.Descriptor(
  name='SyncedNotification',
  full_name='sync_pb.SyncedNotification',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='sync_pb.SyncedNotification.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='external_id', full_name='sync_pb.SyncedNotification.external_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='creator', full_name='sync_pb.SyncedNotification.creator', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='client_data', full_name='sync_pb.SyncedNotification.client_data', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  serialized_start=280,
  serialized_end=427,
)


_COALESCEDSYNCEDNOTIFICATION = _descriptor.Descriptor(
  name='CoalescedSyncedNotification',
  full_name='sync_pb.CoalescedSyncedNotification',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='sync_pb.CoalescedSyncedNotification.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='app_id', full_name='sync_pb.CoalescedSyncedNotification.app_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='notification', full_name='sync_pb.CoalescedSyncedNotification.notification', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='render_info', full_name='sync_pb.CoalescedSyncedNotification.render_info', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='read_state', full_name='sync_pb.CoalescedSyncedNotification.read_state', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='creation_time_msec', full_name='sync_pb.CoalescedSyncedNotification.creation_time_msec', index=5,
      number=6, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='priority', full_name='sync_pb.CoalescedSyncedNotification.priority', index=6,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user_action_token', full_name='sync_pb.CoalescedSyncedNotification.user_action_token', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='last_modified_version', full_name='sync_pb.CoalescedSyncedNotification.last_modified_version', index=8,
      number=9, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sort_version', full_name='sync_pb.CoalescedSyncedNotification.sort_version', index=9,
      number=10, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _COALESCEDSYNCEDNOTIFICATION_READSTATE,
    _COALESCEDSYNCEDNOTIFICATION_PRIORITY,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=430,
  serialized_end=946,
)


_SYNCEDNOTIFICATIONLIST = _descriptor.Descriptor(
  name='SyncedNotificationList',
  full_name='sync_pb.SyncedNotificationList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='coalesced_notification', full_name='sync_pb.SyncedNotificationList.coalesced_notification', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=948,
  serialized_end=1042,
)


_MAPDATA_ENTRY = _descriptor.Descriptor(
  name='Entry',
  full_name='sync_pb.MapData.Entry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='sync_pb.MapData.Entry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='sync_pb.MapData.Entry.value', index=1,
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
  serialized_start=1094,
  serialized_end=1144,
)

_MAPDATA = _descriptor.Descriptor(
  name='MapData',
  full_name='sync_pb.MapData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entry', full_name='sync_pb.MapData.entry', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_MAPDATA_ENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1044,
  serialized_end=1144,
)


_DATA = _descriptor.Descriptor(
  name='Data',
  full_name='sync_pb.Data',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='boolean_value', full_name='sync_pb.Data.boolean_value', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='int_value', full_name='sync_pb.Data.int_value', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='float_value', full_name='sync_pb.Data.float_value', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='string_value', full_name='sync_pb.Data.string_value', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='list_value', full_name='sync_pb.Data.list_value', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='map_value', full_name='sync_pb.Data.map_value', index=5,
      number=6, type=11, cpp_type=10, label=1,
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
  serialized_start=1147,
  serialized_end=1314,
)


_LISTDATA = _descriptor.Descriptor(
  name='ListData',
  full_name='sync_pb.ListData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='sync_pb.ListData.value', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=1316,
  serialized_end=1356,
)


_RENDERCONTEXT = _descriptor.Descriptor(
  name='RenderContext',
  full_name='sync_pb.RenderContext',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='device_type', full_name='sync_pb.RenderContext.device_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='language_code', full_name='sync_pb.RenderContext.language_code', index=1,
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
    _RENDERCONTEXT_DEVICETYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1359,
  serialized_end=1685,
)


_APPLIST = _descriptor.Descriptor(
  name='AppList',
  full_name='sync_pb.AppList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='sync_pb.AppList.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='app_id', full_name='sync_pb.AppList.app_id', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _APPLIST_TYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1687,
  serialized_end=1798,
)


_SERVERCONTEXT = _descriptor.Descriptor(
  name='ServerContext',
  full_name='sync_pb.ServerContext',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='render_context', full_name='sync_pb.ServerContext.render_context', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='app_list', full_name='sync_pb.ServerContext.app_list', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='view_id', full_name='sync_pb.ServerContext.view_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=1800,
  serialized_end=1916,
)

_SYNCEDNOTIFICATION.fields_by_name['creator'].message_type = _SYNCEDNOTIFICATIONCREATOR
_SYNCEDNOTIFICATION.fields_by_name['client_data'].message_type = _MAPDATA
_COALESCEDSYNCEDNOTIFICATION.fields_by_name['notification'].message_type = _SYNCEDNOTIFICATION
_COALESCEDSYNCEDNOTIFICATION.fields_by_name['render_info'].message_type = synced_notification_render_pb2._SYNCEDNOTIFICATIONRENDERINFO
_COALESCEDSYNCEDNOTIFICATION.fields_by_name['read_state'].enum_type = _COALESCEDSYNCEDNOTIFICATION_READSTATE
_COALESCEDSYNCEDNOTIFICATION.fields_by_name['priority'].enum_type = _COALESCEDSYNCEDNOTIFICATION_PRIORITY
_COALESCEDSYNCEDNOTIFICATION_READSTATE.containing_type = _COALESCEDSYNCEDNOTIFICATION;
_COALESCEDSYNCEDNOTIFICATION_PRIORITY.containing_type = _COALESCEDSYNCEDNOTIFICATION;
_SYNCEDNOTIFICATIONLIST.fields_by_name['coalesced_notification'].message_type = _COALESCEDSYNCEDNOTIFICATION
_MAPDATA_ENTRY.fields_by_name['value'].message_type = _DATA
_MAPDATA_ENTRY.containing_type = _MAPDATA;
_MAPDATA.fields_by_name['entry'].message_type = _MAPDATA_ENTRY
_DATA.fields_by_name['list_value'].message_type = _LISTDATA
_DATA.fields_by_name['map_value'].message_type = _MAPDATA
_LISTDATA.fields_by_name['value'].message_type = _DATA
_RENDERCONTEXT.fields_by_name['device_type'].enum_type = _RENDERCONTEXT_DEVICETYPE
_RENDERCONTEXT_DEVICETYPE.containing_type = _RENDERCONTEXT;
_APPLIST.fields_by_name['type'].enum_type = _APPLIST_TYPE
_APPLIST_TYPE.containing_type = _APPLIST;
_SERVERCONTEXT.fields_by_name['render_context'].message_type = _RENDERCONTEXT
_SERVERCONTEXT.fields_by_name['app_list'].message_type = _APPLIST
DESCRIPTOR.message_types_by_name['SyncedNotificationIdentifier'] = _SYNCEDNOTIFICATIONIDENTIFIER
DESCRIPTOR.message_types_by_name['SyncedNotificationCreator'] = _SYNCEDNOTIFICATIONCREATOR
DESCRIPTOR.message_types_by_name['SyncedNotificationRecipients'] = _SYNCEDNOTIFICATIONRECIPIENTS
DESCRIPTOR.message_types_by_name['SyncedNotification'] = _SYNCEDNOTIFICATION
DESCRIPTOR.message_types_by_name['CoalescedSyncedNotification'] = _COALESCEDSYNCEDNOTIFICATION
DESCRIPTOR.message_types_by_name['SyncedNotificationList'] = _SYNCEDNOTIFICATIONLIST
DESCRIPTOR.message_types_by_name['MapData'] = _MAPDATA
DESCRIPTOR.message_types_by_name['Data'] = _DATA
DESCRIPTOR.message_types_by_name['ListData'] = _LISTDATA
DESCRIPTOR.message_types_by_name['RenderContext'] = _RENDERCONTEXT
DESCRIPTOR.message_types_by_name['AppList'] = _APPLIST
DESCRIPTOR.message_types_by_name['ServerContext'] = _SERVERCONTEXT

class SyncedNotificationIdentifier(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SYNCEDNOTIFICATIONIDENTIFIER

  # @@protoc_insertion_point(class_scope:sync_pb.SyncedNotificationIdentifier)

class SyncedNotificationCreator(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SYNCEDNOTIFICATIONCREATOR

  # @@protoc_insertion_point(class_scope:sync_pb.SyncedNotificationCreator)

class SyncedNotificationRecipients(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SYNCEDNOTIFICATIONRECIPIENTS

  # @@protoc_insertion_point(class_scope:sync_pb.SyncedNotificationRecipients)

class SyncedNotification(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SYNCEDNOTIFICATION

  # @@protoc_insertion_point(class_scope:sync_pb.SyncedNotification)

class CoalescedSyncedNotification(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _COALESCEDSYNCEDNOTIFICATION

  # @@protoc_insertion_point(class_scope:sync_pb.CoalescedSyncedNotification)

class SyncedNotificationList(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SYNCEDNOTIFICATIONLIST

  # @@protoc_insertion_point(class_scope:sync_pb.SyncedNotificationList)

class MapData(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType

  class Entry(_message.Message):
    __metaclass__ = _reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _MAPDATA_ENTRY

    # @@protoc_insertion_point(class_scope:sync_pb.MapData.Entry)
  DESCRIPTOR = _MAPDATA

  # @@protoc_insertion_point(class_scope:sync_pb.MapData)

class Data(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DATA

  # @@protoc_insertion_point(class_scope:sync_pb.Data)

class ListData(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _LISTDATA

  # @@protoc_insertion_point(class_scope:sync_pb.ListData)

class RenderContext(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RENDERCONTEXT

  # @@protoc_insertion_point(class_scope:sync_pb.RenderContext)

class AppList(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _APPLIST

  # @@protoc_insertion_point(class_scope:sync_pb.AppList)

class ServerContext(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SERVERCONTEXT

  # @@protoc_insertion_point(class_scope:sync_pb.ServerContext)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), 'H\003`\001')
# @@protoc_insertion_point(module_scope)
