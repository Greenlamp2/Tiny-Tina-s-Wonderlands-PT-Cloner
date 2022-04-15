# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: OakProfile.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import OakShared_pb2 as OakShared__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10OakProfile.proto\x12\x07OakSave\x1a\x0fOakShared.proto\"C\n\x19PlayerInputBinding_Button\x12\x13\n\x0brebind_name\x18\x01 \x01(\t\x12\x11\n\tkey_names\x18\x02 \x03(\t\"P\n\x1bPlayerInputBinding_Axis_Key\x12\x10\n\x08key_name\x18\x01 \x01(\t\x12\x1f\n\x08scale_3d\x18\x02 \x01(\x0b\x32\r.OakSave.Vec3\"b\n\x17PlayerInputBinding_Axis\x12\x13\n\x0brebind_name\x18\x01 \x01(\t\x12\x32\n\x04keys\x18\x02 \x03(\x0b\x32$.OakSave.PlayerInputBinding_Axis_Key\"\xa6\x01\n\x19PlayerInputBinding_Schema\x12\x13\n\x0bschema_name\x18\x01 \x01(\t\x12;\n\x0f\x62utton_bindings\x18\x02 \x03(\x0b\x32\".OakSave.PlayerInputBinding_Button\x12\x37\n\raxis_bindings\x18\x03 \x03(\x0b\x32 .OakSave.PlayerInputBinding_Axis\"J\n\x13PlayerInputBindings\x12\x33\n\x07schemas\x18\x01 \x03(\x0b\x32\".OakSave.PlayerInputBinding_Schema\"T\n!OakProfileLastInventoryFilterInfo\x12\x14\n\x0cslot_type_id\x18\x01 \x01(\t\x12\x19\n\x11last_filter_index\x18\x02 \x01(\x05\"}\n\x1aOakProfileMenuTutorialInfo\x12\x16\n\x0eseen_tutorials\x18\x01 \x03(\t\x12\x1a\n\x12tutorials_disabled\x18\x02 \x01(\x08\x12+\n#tutorials_allowed_in_non_game_modes\x18\x03 \x01(\x08\"M\n\x16OakFriendEncounterData\x12\x16\n\x0enum_encounters\x18\x01 \x01(\r\x12\x1b\n\x13time_last_encounter\x18\x02 \x01(\x03\"o\n\x14GearSoldByFriendData\x12\x1a\n\x12gear_serial_number\x18\x01 \x01(\t\x12$\n\x1cplayer_class_identifier_hash\x18\x02 \x01(\x05\x12\x15\n\rfriend_net_id\x18\x03 \x01(\t\"\x99\x01\n\x19PlayerPrestigeProfileData\x12\x1b\n\x13prestige_experience\x18\x01 \x01(\x03\x12\x1f\n\x17last_upgrade_tree_index\x18\x02 \x01(\x05\x12#\n\x1bpoints_spent_by_index_order\x18\x03 \x03(\x05\x12\x19\n\x11has_seen_tutorial\x18\x04 \x01(\x08\"l\n\x11RecentlyMetPlayer\x12\x17\n\x0fshift_player_id\x18\x01 \x01(\t\x12\x1d\n\x15\x66irst_party_player_id\x18\x02 \x01(\t\x12\x1f\n\x17show_shift_player_entry\x18\x03 \x01(\x08\"2\n\x13\x41\x63\x63\x65ptedOfflineEULA\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0f\n\x07version\x18\x02 \x01(\t\"\xf2\x34\n\x07Profile\x12\x19\n\x11\x65nable_aim_assist\x18\x01 \x01(\x08\x12\x1b\n\x13gamepad_invert_look\x18\x02 \x01(\x08\x12\x1b\n\x13gamepad_invert_turn\x18\x03 \x01(\x08\x12\x1b\n\x13gamepad_invert_move\x18\x04 \x01(\x08\x12\x1d\n\x15gamepad_invert_strafe\x18\x05 \x01(\x08\x12\x18\n\x10\x65nable_vibration\x18\x06 \x01(\x08\x12\x1a\n\x12invert_mouse_pitch\x18\x07 \x01(\x08\x12\x1e\n\x16\x65nable_mouse_smoothing\x18\x08 \x01(\x08\x12\x13\n\x0bmouse_scale\x18\t \x01(\x02\x12\x1b\n\x13show_damage_numbers\x18\n \x01(\x08\x12 \n\x18show_damage_number_icons\x18\x0b \x01(\x08\x12 \n\x18\x65nable_training_messages\x18\x0c \x01(\x08\x12\x16\n\x0eshow_text_chat\x18\r \x01(\x08\x12\x18\n\x10\x63\x65nter_crosshair\x18\x0e \x01(\x08\x12\x15\n\rtoggle_sprint\x18\x0f \x01(\x08\x12\x15\n\rtoggle_crouch\x18\x10 \x01(\x08\x12\x16\n\x0e\x63\x65nsor_content\x18\x11 \x01(\x08\x12\x14\n\x0cmusic_volume\x18\x12 \x01(\x02\x12\x1c\n\x14sound_effects_volume\x18\x13 \x01(\x02\x12\x11\n\tvo_volume\x18\x14 \x01(\x02\x12\x14\n\x0cvoice_volume\x18\x15 \x01(\x02\x12\x1a\n\x12\x65nable_optional_vo\x18\x16 \x01(\x08\x12\x14\n\x0cpush_to_talk\x18\x17 \x01(\x08\x12\x1f\n\x17\x65nable_controller_audio\x18\x18 \x01(\x08\x12\x1b\n\x13speaker_angle_front\x18\x19 \x01(\x02\x12\x1a\n\x12speaker_angle_side\x18\x1a \x01(\x02\x12\x1a\n\x12speaker_angle_back\x18\x1b \x01(\x02\x12\x15\n\rspeaker_setup\x18\x1c \x01(\r\x12 \n\x18mute_audio_on_focus_loss\x18\x1d \x01(\x08\x12\x36\n\x0e\x63hallenge_data\x18\x1e \x03(\x0b\x32\x1e.OakSave.ChallengeSaveGameData\x12\'\n\x1f\x64\x65\x66\x61ult_dead_zone_inner_updated\x18  \x01(\x08\x12\x1d\n\x15\x64isable_event_content\x18! \x01(\x08\x12#\n\x1bhide_strict_nat_help_dialog\x18\" \x01(\x08\x12;\n\x15player_input_bindings\x18# \x01(\x0b\x32\x1c.OakSave.PlayerInputBindings\x12\x13\n\x0bnews_hashes\x18$ \x03(\r\x12\x1d\n\x15last_used_savegame_id\x18% \x01(\r\x12%\n\x1dgamepad_hip_sensitivity_level\x18& \x01(\x05\x12(\n gamepad_zoomed_sensitivity_level\x18\' \x01(\x05\x12)\n!gamepad_vehicle_sensitivity_level\x18( \x01(\x05\x12$\n\x1cgamepad_movement_dead_zone_x\x18) \x01(\x02\x12$\n\x1cgamepad_movement_dead_zone_y\x18* \x01(\x02\x12&\n\x1egamepad_look_dead_zone_inner_x\x18+ \x01(\x02\x12&\n\x1egamepad_look_dead_zone_outer_x\x18, \x01(\x02\x12&\n\x1egamepad_look_dead_zone_inner_y\x18- \x01(\x02\x12&\n\x1egamepad_look_dead_zone_outer_y\x18. \x01(\x02\x12,\n$gamepad_vehicle_movement_dead_zone_x\x18/ \x01(\x02\x12,\n$gamepad_vehicle_movement_dead_zone_y\x18\x30 \x01(\x02\x12.\n&gamepad_vehicle_look_dead_zone_inner_x\x18\x31 \x01(\x02\x12.\n&gamepad_vehicle_look_dead_zone_outer_x\x18\x32 \x01(\x02\x12.\n&gamepad_vehicle_look_dead_zone_inner_y\x18\x33 \x01(\x02\x12.\n&gamepad_vehicle_look_dead_zone_outer_y\x18\x34 \x01(\x02\x12$\n\x1cgamepad_left_dead_zone_inner\x18\x35 \x01(\x02\x12$\n\x1cgamepad_left_dead_zone_outer\x18\x36 \x01(\x02\x12%\n\x1dgamepad_right_dead_zone_inner\x18\x37 \x01(\x02\x12%\n\x1dgamepad_right_dead_zone_outer\x18\x38 \x01(\x02\x12*\n\"gamepad_look_axial_dead_zone_scale\x18\x39 \x01(\x02\x12*\n\"gamepad_move_axial_dead_zone_scale\x18: \x01(\x02\x12-\n%gamepad_use_advanced_hip_aim_settings\x18; \x01(\x08\x12\x30\n(gamepad_use_advanced_zoomed_aim_settings\x18< \x01(\x08\x12\x31\n)gamepad_use_advanced_vehicle_aim_settings\x18= \x01(\x08\x12\x1c\n\x14gamepad_hip_yaw_rate\x18> \x01(\x02\x12\x1e\n\x16gamepad_hip_pitch_rate\x18? \x01(\x02\x12\x1d\n\x15gamepad_hip_extra_yaw\x18@ \x01(\x02\x12\x1f\n\x17gamepad_hip_extra_pitch\x18\x41 \x01(\x02\x12 \n\x18gamepad_hip_ramp_up_time\x18\x42 \x01(\x02\x12!\n\x19gamepad_hip_ramp_up_delay\x18\x43 \x01(\x02\x12\x1f\n\x17gamepad_zoomed_yaw_rate\x18\x44 \x01(\x02\x12!\n\x19gamepad_zoomed_pitch_rate\x18\x45 \x01(\x02\x12 \n\x18gamepad_zoomed_extra_yaw\x18\x46 \x01(\x02\x12\"\n\x1agamepad_zoomed_extra_pitch\x18G \x01(\x02\x12#\n\x1bgamepad_zoomed_ramp_up_time\x18H \x01(\x02\x12$\n\x1cgamepad_zoomed_ramp_up_delay\x18I \x01(\x02\x12 \n\x18gamepad_vehicle_yaw_rate\x18J \x01(\x02\x12\"\n\x1agamepad_vehicle_pitch_rate\x18K \x01(\x02\x12!\n\x19gamepad_vehicle_extra_yaw\x18L \x01(\x02\x12#\n\x1bgamepad_vehicle_extra_pitch\x18M \x01(\x02\x12$\n\x1cgamepad_vehicle_ramp_up_time\x18N \x01(\x02\x12%\n\x1dgamepad_vehicle_ramp_up_delay\x18O \x01(\x02\x12\x1c\n\x14ironsight_aim_assist\x18P \x01(\x08\x12\x1f\n\x17walking_joystick_scheme\x18Q \x01(\r\x12\x1f\n\x17\x64riving_joystick_scheme\x18R \x01(\r\x12\x17\n\x0fmouse_ads_scale\x18S \x01(\x02\x12\x1b\n\x13mouse_vehicle_scale\x18T \x01(\x02\x12\"\n\x1amouse_ironsight_aim_assist\x18U \x01(\x08\x12\x1a\n\x12vehicle_input_mode\x18V \x01(\r\x12\x19\n\x11weapon_aim_toggle\x18W \x01(\x08\x12\x1e\n\x16mantle_requires_button\x18X \x01(\x08\x12\x1e\n\x16\x66ixed_minimap_rotation\x18Y \x01(\x08\x12\x18\n\x10map_invert_pitch\x18Z \x01(\x08\x12\x16\n\x0emap_invert_yaw\x18[ \x01(\x08\x12\x12\n\ndifficulty\x18\\ \x01(\r\x12 \n\x18swap_dual_wield_controls\x18] \x01(\x08\x12\x10\n\x08\x62\x61se_fov\x18^ \x01(\x02\x12%\n\x1d\x63rosshair_neutral_color_frame\x18_ \x01(\r\x12#\n\x1b\x63rosshair_enemy_color_frame\x18` \x01(\r\x12\"\n\x1a\x63rosshair_ally_color_frame\x18\x61 \x01(\r\x12\x18\n\x10\x65nable_subtitles\x18\x62 \x01(\x08\x12\x1e\n\x16\x65nable_closed_captions\x18\x63 \x01(\x08\x12\x1d\n\x15last_status_menu_page\x18\x64 \x01(\t\x12P\n\x1cinventory_screen_last_filter\x18\x65 \x03(\x0b\x32*.OakSave.OakProfileLastInventoryFilterInfo\x12:\n\rtutorial_info\x18\x66 \x01(\x0b\x32#.OakSave.OakProfileMenuTutorialInfo\x12\x1c\n\x14\x64\x65\x66\x61ult_network_type\x18g \x01(\r\x12\x1b\n\x13\x64\x65\x66\x61ult_invite_type\x18h \x01(\r\x12\x1a\n\x12matchmaking_region\x18i \x01(\t\x12\x19\n\x11streaming_service\x18j \x01(\r\x12 \n\x18max_cached_friend_events\x18k \x01(\x05\x12\"\n\x1amax_cached_friend_statuses\x18l \x01(\x05\x12\x15\n\rfriend_events\x18m \x03(\t\x12\x17\n\x0f\x66riend_statuses\x18n \x03(\t\x12&\n\x1elast_whisper_fetch_events_time\x18o \x01(\x03\x12(\n last_whisper_fetch_statuses_time\x18p \x01(\x03\x12\x42\n\x11\x66riend_encounters\x18\x85\x01 \x03(\x0b\x32&.OakSave.Profile.FriendEncountersEntry\x12\"\n\x19max_friend_encounter_size\x18\x86\x01 \x01(\x05\x12:\n\x12profile_stats_data\x18\x87\x01 \x03(\x0b\x32\x1d.OakSave.GameStatSaveGameData\x12I\n\x1c\x62\x61nk_inventory_category_list\x18\x88\x01 \x03(\x0b\x32\".OakSave.InventoryCategorySaveData\x12&\n\x1dtwo_player_splitscreen_layout\x18\x89\x01 \x01(\r\x12!\n\x18lost_loot_inventory_list\x18\x8a\x01 \x03(\x0c\x12-\n\x0enpc_mail_items\x18\x8b\x01 \x03(\x0b\x32\x14.OakSave.OakMailItem\x12\x13\n\nmail_guids\x18\x8c\x01 \x03(\t\x12\x1a\n\x11unread_mail_guids\x18\x8d\x01 \x03(\t\x12<\n\x14gear_sold_by_friends\x18\x8e\x01 \x03(\x0b\x32\x1d.OakSave.GearSoldByFriendData\x12\x36\n\x10profile_sdu_list\x18\x8f\x01 \x03(\x0b\x32\x1b.OakSave.OakSDUSaveGameData\x12G\n\x17unlocked_customizations\x18\x90\x01 \x03(\x0b\x32%.OakSave.OakCustomizationSaveGameData\x12[\n&unlocked_inventory_customization_parts\x18\x91\x01 \x03(\x0b\x32*.OakSave.OakInventoryCustomizationPartInfo\x12\'\n\x1e\x66ixed_initial_zonemap_rotation\x18\x95\x01 \x01(\x08\x12\"\n\x19\x65nable_mouse_acceleration\x18\x96\x01 \x01(\x08\x12\x1d\n\x14\x65nable_gamepad_input\x18\x97\x01 \x01(\x08\x12\"\n\x19use_classic_gamepad_input\x18\x98\x01 \x01(\x08\x12\x16\n\rmaster_volume\x18\x99\x01 \x01(\x02\x12\x1d\n\x14monitor_display_type\x18\x9a\x01 \x01(\r\x12\x16\n\rgraphics_mode\x18\x9b\x01 \x01(\r\x12\x19\n\x10\x66rame_rate_limit\x18\x9c\x01 \x01(\r\x12\x19\n\x10\x62\x61se_vehicle_fov\x18\x9d\x01 \x01(\x02\x12\x19\n\x10graphics_quality\x18\x9e\x01 \x01(\r\x12\x1e\n\x15\x61nisotropic_filtering\x18\x9f\x01 \x01(\r\x12\x17\n\x0eshadow_quality\x18\xa0\x01 \x01(\r\x12\"\n\x19\x64isplay_performance_stats\x18\xa1\x01 \x01(\r\x12\x17\n\x0etexture_detail\x18\xa2\x01 \x01(\r\x12\x16\n\rdraw_distance\x18\xa3\x01 \x01(\r\x12\x10\n\x07\x63lutter\x18\xa4\x01 \x01(\r\x12\x15\n\x0ctessellation\x18\xa5\x01 \x01(\r\x12\x10\n\x07\x66oliage\x18\xa6\x01 \x01(\r\x12\x18\n\x0f\x66oliage_shadows\x18\xa7\x01 \x01(\x08\x12\x1b\n\x12planar_reflections\x18\xa8\x01 \x01(\x08\x12\x17\n\x0evolumetric_fog\x18\xa9\x01 \x01(\r\x12!\n\x18screen_space_reflections\x18\xaa\x01 \x01(\r\x12!\n\x18\x63haracter_texture_detail\x18\xab\x01 \x01(\r\x12\x19\n\x10\x63haracter_detail\x18\xac\x01 \x01(\r\x12\"\n\x19\x61mbient_occlusion_quality\x18\xad\x01 \x01(\r\x12\x1b\n\x12object_motion_blur\x18\xae\x01 \x01(\x08\x12\x13\n\nlens_flare\x18\xaf\x01 \x01(\x08\x12\"\n\x19\x63ombat_number_long_format\x18\xb0\x01 \x01(\x08\x12!\n\x18show_minimap_legendaries\x18\xb1\x01 \x01(\x08\x12\x1c\n\x13use_player_callouts\x18\xb2\x01 \x01(\x08\x12+\n\"friend_event_notification_lifetime\x18\xb3\x01 \x01(\r\x12,\n#friend_event_notification_frequency\x18\xb4\x01 \x01(\r\x12%\n\x1ctrade_request_reception_type\x18\xb5\x01 \x01(\r\x12\x17\n\x0ehead_bob_scale\x18\xb6\x01 \x01(\x02\x12\x1e\n\x15has_reset_console_fov\x18\xb7\x01 \x01(\x08\x12\x1c\n\x13has_seen_first_boot\x18\xb8\x01 \x01(\x08\x12\x1d\n\x14\x62\x61\x64\x61ss_event_enabled\x18\xb9\x01 \x01(\x08\x12\x1d\n\x14pinata_event_enabled\x18\xba\x01 \x01(\x08\x12\'\n\x1emin_time_between_badass_events\x18\xbb\x01 \x01(\x05\x12\x1e\n\x15\x64isable_spatial_audio\x18\xbc\x01 \x01(\x08\x12\x15\n\x0csubs_cc_size\x18\xbd\x01 \x01(\x02\x12#\n\x1a\x63\x63_subs_background_opacity\x18\xbe\x01 \x01(\x02\x12\x1e\n\x15walking_button_scheme\x18\xbf\x01 \x01(\r\x12\x1e\n\x15\x64riving_button_scheme\x18\xc0\x01 \x01(\r\x12\x13\n\nglyph_mode\x18\xc1\x01 \x01(\r\x12\x10\n\x07use_MPH\x18\xc2\x01 \x01(\x08\x12Z\n$registered_downloadable_entitlements\x18\xc3\x01 \x03(\x0b\x32+.OakSave.RegisteredDownloadableEntitlements\x12\x18\n\x0fseen_news_items\x18\xc4\x01 \x03(\t\x12\x1f\n\x16\x61uto_centering_enabled\x18\xc5\x01 \x01(\x08\x12)\n increased_chance_for_subscribers\x18\xc6\x01 \x01(\x08\x12!\n\x18rare_chest_event_enabled\x18\xc7\x01 \x01(\x08\x12\x1d\n\x14hud_scale_multiplier\x18\xc8\x01 \x01(\x02\x12\x1f\n\x16total_playtime_seconds\x18\xc9\x01 \x01(\x05\x12 \n\x17\x64\x65sired_crossplay_state\x18\xca\x01 \x01(\r\x12\"\n\x19\x64\x65sired_friend_sync_state\x18\xcb\x01 \x01(\r\x12\x1f\n\x16needs_shift_first_boot\x18\xcc\x01 \x01(\x08\x12\x39\n\x14recently_met_players\x18\xcd\x01 \x03(\x0b\x32\x1a.OakSave.RecentlyMetPlayer\x12 \n\x17\x65nable_trigger_feedback\x18\xce\x01 \x01(\x08\x12\x1b\n\x12\x63\x61mera_shake_scale\x18\xcf\x01 \x01(\x02\x12<\n\x0fplayer_prestige\x18\xd0\x01 \x01(\x0b\x32\".OakSave.PlayerPrestigeProfileData\x12\'\n\x1eneeds_shift_first_boot_primary\x18\xd1\x01 \x01(\x08\x12=\n\x16\x61\x63\x63\x65pted_offline_eulas\x18\xd2\x01 \x03(\x0b\x32\x1c.OakSave.AcceptedOfflineEULA\x12 \n\x17override_audio_language\x18\xd3\x01 \x01(\t\x12\x43\n\x13\x62\x61nk_inventory_list\x18\xd4\x01 \x03(\x0b\x32%.OakSave.OakInventoryItemSaveGameData\x1aT\n\x15\x46riendEncountersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12.\n\x05value\x18\x02 \x01(\x0b\x32\x1f.OakSave.OakFriendEncounterData')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'OakProfile_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PLAYERINPUTBINDING_BUTTON._serialized_start=46
  _PLAYERINPUTBINDING_BUTTON._serialized_end=113
  _PLAYERINPUTBINDING_AXIS_KEY._serialized_start=115
  _PLAYERINPUTBINDING_AXIS_KEY._serialized_end=195
  _PLAYERINPUTBINDING_AXIS._serialized_start=197
  _PLAYERINPUTBINDING_AXIS._serialized_end=295
  _PLAYERINPUTBINDING_SCHEMA._serialized_start=298
  _PLAYERINPUTBINDING_SCHEMA._serialized_end=464
  _PLAYERINPUTBINDINGS._serialized_start=466
  _PLAYERINPUTBINDINGS._serialized_end=540
  _OAKPROFILELASTINVENTORYFILTERINFO._serialized_start=542
  _OAKPROFILELASTINVENTORYFILTERINFO._serialized_end=626
  _OAKPROFILEMENUTUTORIALINFO._serialized_start=628
  _OAKPROFILEMENUTUTORIALINFO._serialized_end=753
  _OAKFRIENDENCOUNTERDATA._serialized_start=755
  _OAKFRIENDENCOUNTERDATA._serialized_end=832
  _GEARSOLDBYFRIENDDATA._serialized_start=834
  _GEARSOLDBYFRIENDDATA._serialized_end=945
  _PLAYERPRESTIGEPROFILEDATA._serialized_start=948
  _PLAYERPRESTIGEPROFILEDATA._serialized_end=1101
  _RECENTLYMETPLAYER._serialized_start=1103
  _RECENTLYMETPLAYER._serialized_end=1211
  _ACCEPTEDOFFLINEEULA._serialized_start=1213
  _ACCEPTEDOFFLINEEULA._serialized_end=1263
  _PROFILE._serialized_start=1266
  _PROFILE._serialized_end=8036
  _PROFILE_FRIENDENCOUNTERSENTRY._serialized_start=7952
  _PROFILE_FRIENDENCOUNTERSENTRY._serialized_end=8036
# @@protoc_insertion_point(module_scope)
