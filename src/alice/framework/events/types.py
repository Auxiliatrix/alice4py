from enum import Enum

class EventType(Enum):
    RAW_APP_COMMAND_PERMISSIONS_UPDATE = "raw_app_command_permissions_update"
    APP_COMMAND_COMPLETION = "app_command_completion"
    AUTOMOD_RULE_CREATE = "automod_rule_create"
    AUTOMOD_RULE_UPDATE = "automod_rule_update"
    AUTOMOD_RULE_DELETE = "automod_rule_delete"
    AUTOMOD_ACTION = "automod_action"
    GUILD_CHANNEL_CREATE = "guild_channel_create"
    GUILD_CHANNEL_DELETE = "guild_channel_delete"
    GUILD_CHANNEL_UPDATE = "guild_channel_update"
    GUILD_CHANNEL_PINS_UPDATE = "guild_channel_pins_update"
    PRIVATE_CHANNEL_UPDATE = "private_channel_update"
    PRIVATE_CHANNEL_PINS_UPDATE = "private_channel_pins_update"
    TYPING = "typing"
    RAW_TYPING = "raw_typing"
    CONNECT = "connect"
    DISCONNECT = "disconnect"
    SHARD_CONNECT = "shard_connect"
    SHARD_DISCONNECT = "shard_disconnect"
    ERROR = "error"
    SOCKET_EVENT_TYPE = "socket_event_type"
    SOCKET_RAW_RECEIVE = "socket_raw_receive"
    SOCKET_RAW_SEND = "socket_raw_send"
    ENTITLEMENT_CREATE = "entitlement_create"
    ENTITLEMENT_DELETE = "entitlement_delete"
    READY = "ready"
    RESUMED = "resumed"
    GUILD_AVAILABLE = "guild_available"
    GUILD_UNAVAILABLE = "guild_unavailable"
    GUILD_REMOVE = "guild_remove"
    GUILD_UPDATE = "guild_update"
    GUILD_EMOJIS_UPDATE = "guild_emojis_update"
    GUILD_STICKERS_UPDATE = "guild_stickers_update"
    AUDIT_LOG_ENTRY_CREATE = "audit_log_entry_create"
    INVITE_CREATE = "invite_create"
    INVITE_DELETE = "invite_delete"
    INTEGRATION_CREATE = "integration_create"
    INTEGRATION_UPDATE = "integration_update"
    GUILD_INTEGRATIONS_UPDATE = "guild_integrations_update"
    WEBHOOKS_UPDATE = "webhooks_update"
    RAW_INTEGRATION_DELETE = "raw_integration_delete"
    INTERACTION = "interaction"
    MEMBER_JOIN = "member_join"
    MEMBER_REMOVE = "member_remove"
    RAW_MEMBER_REMOVE = "raw_member_remove"
    MEMBER_UPDATE = "member_update"
    USER_UPDATE = "user_update"
    MEMBER_BAN = "member_ban"
    MEMBER_UNBAN = "member_unban"
    PRESENCE_UPDATE = "presence_update"
    MESSAGE = "message"
    MESSAGE_EDIT = "message_edit"
    MESSAGE_DELETE = "message_delete"
    BULK_MESSAGE_DELETE = "bulk_message_delete"
    RAW_MESSAGE_EDIT = "raw_message_edit"
    RAW_MESSAGE_DELETE = "raw_message_delete"
    RAW_BULK_MESSAGE_DELETE = "raw_bulk_message_delete"
    POLL_VOTE_ADD = "poll_vote_add"
    POLL_VOTE_REMOVE = "poll_vote_remove"
    RAW_POLL_VOTE_ADD = "raw_poll_vote_add"
    RAW_POLL_VOTE_REMOVE = "raw_poll_vote_remove"
    REACTION_ADD = "reaction_add"
    REACTION_REMOVE = "reaction_remove"
    REACTION_CLEAR = "reaction_clear"
    REACTION_CLEAR_EMOJI = "reaction_clear_emoji"
    RAW_REACTION_ADD = "raw_reaction_add"
    RAW_REACTION_REMOVE = "raw_reaction_remove"
    RAW_REACTION_CLEAR = "raw_reaction_clear"
    RAW_REACTION_CLEAR_EMOJI = "raw_reaction_clear_emoji"
    GUILD_ROLE_CREATE = "guild_role_create"
    GUILD_ROLE_DELETE = "guild_role_delete"
    GUILD_ROLE_UPDATE = "guild_role_update"
    SCHEDULED_EVENT_CREATE = "scheduled_event_create"
    SCHEDUELD_EVENT_DELETE = "scheduled_event_delete"
    SCHEDULED_EVENT_UPDATE = "schedule_event_update"
    SCHEDULED_EVENT_USER_ADD = "scheduled_event_user_add"
    SCHEDULED_EVENT_USER_REMOVE = "scheduld_event_user_remove"
    STAGE_INSTANCE_CREATE = "stage_instance_create"
    STAGE_INSTANCE_DELETE = "stage_instance_delete"
    STAGE_INSTANCE_UPDATE = "stage_instance_update"
    THREAD_CREATE = "thread_create"
    THREAD_JOIN = "thread_join"
    THREAD_UPDATE = "thread_update"
    THREAD_REMOVE = "thread_remove"
    THREAD_DELETE = "thread_delete"
    RAW_THREAD_UPDATE = "raw_thread_update"
    RAW_THREAD_DELETE = "rraw_thread_delete"
    THREAD_MEMBER_JOIN = "thread_member_join"
    THREAD_MEMBER_REMOVE = "thread_member_remove"
    RAW_THREAD_MEMBER_REMOVE = "raw_thread_member_remove"
    VOICE_STATE_UPDATE = "voice_state_update"