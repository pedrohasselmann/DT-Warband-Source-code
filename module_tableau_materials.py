#from header_common import *
from ID_animations import *
#from header_mission_templates import *
#from header_tableau_materials import *
#from header_items import *
from module_constants import *
from compiler import *

####################################################################################################################
#  Each tableau material contains the following fields:
#  1) Tableau id (string): used for referencing tableaux in other files. The prefix tab_ is automatically added before each tableau-id.
#  2) Tableau flags (int). See header_tableau_materials.py for a list of available flags
#  3) Tableau sample material name (string).
#  4) Tableau width (int).
#  5) Tableau height (int).
#  6) Tableau mesh min x (int): divided by 1000 and used when a mesh is auto-generated using the tableau material
#  7) Tableau mesh min y (int): divided by 1000 and used when a mesh is auto-generated using the tableau material
#  8) Tableau mesh max x (int): divided by 1000 and used when a mesh is auto-generated using the tableau material
#  9) Tableau mesh max y (int): divided by 1000 and used when a mesh is auto-generated using the tableau material
#  10) Operations block (list): A list of operations. See header_operations.py for reference.
#     The operations block is executed when the tableau is activated.
# 
####################################################################################################################

#banner height = 200, width = 85 with wood, 75 without wood

tableaus = [
  ("game_character_sheet", 0, "tableau_with_transparency", 1024, 1024, 0, 0, 266, 532,
   [
       (store_script_param, ":troop_no", 1),
       (cur_tableau_set_background_color, 0xFF888888),
       (cur_tableau_set_ambient_light, 10,11,15),
       (set_fixed_point_multiplier, 100),
       (cur_tableau_set_camera_parameters, 0, 40, 40, 0, 100000),

       (init_position, pos1),
       (position_set_z, pos1, 100),
       (position_set_x, pos1, -20),
       (position_set_y, pos1, -20),
       (cur_tableau_add_tableau_mesh, "tableau_troop_character_color", ":troop_no", pos1, 0, 0),
       (position_set_z, pos1, 200),
       (cur_tableau_add_tableau_mesh, "tableau_troop_character_alpha_mask", ":troop_no", pos1, 0, 0),
       (position_set_z, pos1, 300),
       ]),

  ("game_inventory_window", 0, "tableau_with_transparency", 1024, 1024, 0, 0, 180, 270,
   [
       (store_script_param, ":troop_no", 1),
       (cur_tableau_set_background_color, 0xFF888888),
       (cur_tableau_set_ambient_light, 10,11,15),
       (set_fixed_point_multiplier, 100),
       (cur_tableau_set_camera_parameters, 0, 40, 40, 0, 100000),

       (init_position, pos1),
       (position_set_z, pos1, 100),
       (position_set_x, pos1, -20),
       (position_set_y, pos1, -20),
       (cur_tableau_add_tableau_mesh, "tableau_troop_inventory_color", ":troop_no", pos1, 0, 0),
       (position_set_z, pos1, 200),
       (cur_tableau_add_tableau_mesh, "tableau_troop_inventory_alpha_mask", ":troop_no", pos1, 0, 0),
       (position_set_z, pos1, 300),
       ]),

  ("game_profile_window", 0, "tableau_with_transparency", 1024, 1024, 0, 0, 320, 480, [
    (store_script_param, ":profile_no", 1),
    (assign, ":gender", ":profile_no"),
    (val_mod, ":gender", 2),
    (try_begin),
      (eq, ":gender", 0),
      (assign, ":troop_no", "trp_multiplayer_profile_troop_male"),
    (else_try),
      (assign, ":troop_no", "trp_multiplayer_profile_troop_female"),
    (try_end),
    (troop_set_face_key_from_current_profile, ":troop_no"),
    (cur_tableau_set_background_color, 0xFF888888),
    (cur_tableau_set_ambient_light, 10,11,15),
    (set_fixed_point_multiplier, 100),
    (cur_tableau_set_camera_parameters, 0, 40, 40, 0, 100000),

    (init_position, pos1),
    (position_set_z, pos1, 100),
    (position_set_x, pos1, -20),
    (position_set_y, pos1, -20),
    (cur_tableau_add_tableau_mesh, "tableau_troop_profile_color", ":troop_no", pos1, 0, 0),
    (position_set_z, pos1, 200),
    (cur_tableau_add_tableau_mesh, "tableau_troop_profile_alpha_mask", ":troop_no", pos1, 0, 0),
    ]),

  ("game_party_window", 0, "tableau_with_transparency", 1024, 1024, 0, 0, 300, 300,
   [
       (store_script_param, ":troop_no", 1),
       (cur_tableau_set_background_color, 0xFF888888),
       (cur_tableau_set_ambient_light, 10,11,15),
       (set_fixed_point_multiplier, 100),
       (cur_tableau_set_camera_parameters, 0, 40, 40, 0, 100000),

       (init_position, pos1),
       (position_set_z, pos1, 100),
       (position_set_x, pos1, -20),
       (position_set_y, pos1, -20),
       (cur_tableau_add_tableau_mesh, "tableau_troop_party_color", ":troop_no", pos1, 0, 0),
       (position_set_z, pos1, 200),
       (cur_tableau_add_tableau_mesh, "tableau_troop_party_alpha_mask", ":troop_no", pos1, 0, 0),
       (position_set_z, pos1, 300),
       ]),

  ("game_troop_label_banner", 0, "tableau_with_transparency", 256, 256, -128, 0, 128, 256,
   [
       (store_script_param, ":banner_mesh", 1),

       (cur_tableau_set_background_color, 0xFF888888),
       (set_fixed_point_multiplier, 100),
       (cur_tableau_set_camera_parameters, 0, 100, 100, 0, 100000),

       (init_position, pos1),
       (position_set_y, pos1, 120),
       (cur_tableau_add_mesh, ":banner_mesh", pos1, 120, 0),
	   
       #(init_position, pos1),
       #(position_set_z, pos1, 10),
       #(cur_tableau_add_mesh, "mesh_troop_label_banner", pos1, 112, 0),
       ]),
	   
  ("round_shield_1", 0, "sample_shield_round_1", 512, 256, 0, 0, 0, 0,
   [
       (store_script_param, ":banner_mesh", 1),

       (set_fixed_point_multiplier, 100),

       (init_position, pos1),
       (position_set_x, pos1, -50),
       (position_set_y, pos1, 125),
       (cur_tableau_add_mesh, ":banner_mesh", pos1, 120, 0),
       (init_position, pos1),
       (position_set_z, pos1, 10),
       (cur_tableau_add_mesh, "mesh_tableau_mesh_shield_round_1", pos1, 0, 0),
       (cur_tableau_set_camera_parameters, 0, 200, 100, 0, 100000),
       ]),
  ("round_shield_2", 0, "sample_shield_matte", 512, 256, 0, 0, 0, 0,
   [
       (store_script_param, ":banner_mesh", 1),

       (set_fixed_point_multiplier, 100),

       (init_position, pos1),
       (position_set_x, pos1, -50),
       (position_set_y, pos1, 120),
       (cur_tableau_add_mesh, ":banner_mesh", pos1, 116, 0),
       (init_position, pos1),
       (position_set_z, pos1, 10),
       (cur_tableau_add_mesh, "mesh_tableau_mesh_shield_round_2", pos1, 0, 0),
       (cur_tableau_set_camera_parameters, 0, 200, 100, 0, 100000),
       ]),
  ("round_shield_3", 0, "sample_shield_matte", 512, 256, 0, 0, 0, 0,
   [
       (store_script_param, ":banner_mesh", 1),

       (set_fixed_point_multiplier, 100),

       (init_position, pos1),
       (position_set_x, pos1, -50),
       (position_set_y, pos1, 120),
       (cur_tableau_add_mesh, ":banner_mesh", pos1, 116, 0),
       (init_position, pos1),
       (position_set_z, pos1, 10),
       (cur_tableau_add_mesh, "mesh_tableau_mesh_shield_round_3", pos1, 0, 0),
       (cur_tableau_set_camera_parameters, 0, 200, 100, 0, 100000),
       ]),
  
  ("round_shield_4", 0, "sample_shield_matte", 512, 256, 0, 0, 0, 0,
   [
       (store_script_param, ":banner_mesh", 1),

       (set_fixed_point_multiplier, 100),

       (init_position, pos1),
       (position_set_x, pos1, -50),
       (position_set_y, pos1, 125),
       (cur_tableau_add_mesh, ":banner_mesh", pos1, 123, 0),
       (init_position, pos1),
       (position_set_z, pos1, 10),
       (cur_tableau_add_mesh, "mesh_tableau_mesh_shield_round_4", pos1, 0, 0),
       (cur_tableau_set_camera_parameters, 0, 200, 100, 0, 100000),
       ]),
  
  ("round_shield_5", 0, "sample_shield_matte", 512, 256, 0, 0, 0, 0,
   [
       (store_script_param, ":banner_mesh", 1),

       (set_fixed_point_multiplier, 100),

       (init_position, pos1),
       (position_set_x, pos1, -50),
       (position_set_y, pos1, 125),
       (cur_tableau_add_mesh, ":banner_mesh", pos1, 122, 0),
       (init_position, pos1),
       (position_set_z, pos1, 10),
       (cur_tableau_add_mesh, "mesh_tableau_mesh_shield_round_5", pos1, 0, 0),
       (cur_tableau_set_camera_parameters, 0, 200, 100, 0, 100000),
       ]),
  ("small_round_shield_1", 0, "sample_shield_small_round_1", 512, 256, 0, 0, 0, 0,
   [
       (store_script_param, ":banner_mesh", 1),

       (set_fixed_point_multiplier, 100),

       (init_position, pos1),
       (position_set_x, pos1, -50),
       (position_set_y, pos1, 130),
       (cur_tableau_add_mesh, ":banner_mesh", pos1, 127, 0),
       (init_position, pos1),
       (position_set_z, pos1, 10),
       (cur_tableau_add_mesh, "mesh_tableau_mesh_shield_small_round_1", pos1, 0, 0),
       (cur_tableau_set_camera_parameters, 0, 200, 100, 0, 100000),
       ]),
  
  ("small_round_shield_2", 0, "sample_shield_small_round_2", 512, 256, 0, 0, 0, 0,
   [
       (store_script_param, ":banner_mesh", 1),

       (set_fixed_point_multiplier, 100),

       (init_position, pos1),
       (position_set_x, pos1, -50),
       (position_set_y, pos1, 130),
       (cur_tableau_add_mesh, ":banner_mesh", pos1, 127, 0),
       (init_position, pos1),
       (position_set_z, pos1, 10),
       (cur_tableau_add_mesh, "mesh_tableau_mesh_shield_small_round_2", pos1, 0, 0),
       (cur_tableau_set_camera_parameters, 0, 200, 100, 0, 100000),
       ]),
  ("small_round_shield_3", 0, "sample_shield_matte", 512, 256, 0, 0, 0, 0,
   [
       (store_script_param, ":banner_mesh", 1),

       (set_fixed_point_multiplier, 100),

       (init_position, pos1),
       (position_set_x, pos1, -50),
       (position_set_y, pos1, 130),
       (cur_tableau_add_mesh, ":banner_mesh", pos1, 127, 0),
       (init_position, pos1),
       (position_set_z, pos1, 10),
       (cur_tableau_add_mesh, "mesh_tableau_mesh_shield_small_round_3", pos1, 0, 0),
       (cur_tableau_set_camera_parameters, 0, 200, 100, 0, 100000),
       ]),
  
  ("kite_shield_1", 0, "sample_shield_matte", 512, 512, 0, 0, 0, 0,
   [
       (store_script_param, ":banner_mesh", 1),

       (set_fixed_point_multiplier, 100),

       (init_position, pos1),
       (position_set_x, pos1, -60),
       (position_set_y, pos1, 140),
       (cur_tableau_add_mesh, ":banner_mesh", pos1, 116, 0),
       (init_position, pos1),
       (position_set_z, pos1, 10),
       (cur_tableau_add_mesh, "mesh_tableau_mesh_shield_kite_1", pos1, 0, 0),
       (cur_tableau_set_camera_parameters, 0, 200, 200, 0, 100000),
       ]),
  ("kite_shield_2", 0, "sample_shield_matte", 512, 512, 0, 0, 0, 0,
   [
       (store_script_param, ":banner_mesh", 1),

       (set_fixed_point_multiplier, 100),

       (init_position, pos1),
       (position_set_x, pos1, -57),
       (position_set_y, pos1, 140),
       (cur_tableau_add_mesh, ":banner_mesh", pos1, 116, 0),
       (init_position, pos1),
       (position_set_z, pos1, 10),
       (cur_tableau_add_mesh, "mesh_tableau_mesh_shield_kite_2", pos1, 0, 0),
       (cur_tableau_set_camera_parameters, 0, 200, 200, 0, 100000),
       ]),
  ("kite_shield_3", 0, "sample_shield_matte", 512, 512, 0, 0, 0, 0,
   [
       (store_script_param, ":banner_mesh", 1),

       (set_fixed_point_multiplier, 100),

       (init_position, pos1),
       (position_set_x, pos1, -57),
       (position_set_y, pos1, 140),
       (cur_tableau_add_mesh, ":banner_mesh", pos1, 116, 0),
       (init_position, pos1),
       (position_set_z, pos1, 10),
       (cur_tableau_add_mesh, "mesh_tableau_mesh_shield_kite_3", pos1, 0, 0),
       (cur_tableau_set_camera_parameters, 0, 200, 200, 0, 100000),
       ]),
  ("kite_shield_4", 0, "sample_shield_matte", 512, 512, 0, 0, 0, 0,
   [
       (store_script_param, ":banner_mesh", 1),

       (set_fixed_point_multiplier, 100),

       (init_position, pos1),
       (position_set_x, pos1, -50),
       (position_set_y, pos1, 160),
       (cur_tableau_add_mesh, ":banner_mesh", pos1, 120, 0),
       (init_position, pos1),
       (position_set_z, pos1, 10),
       (cur_tableau_add_mesh, "mesh_tableau_mesh_shield_kite_4", pos1, 0, 0),
       (cur_tableau_set_camera_parameters, 0, 200, 200, 0, 100000),
       ]),
  ("heater_shield_1", 0, "sample_shield_matte", 512, 512, 0, 0, 0, 0,
   [
       (store_script_param, ":banner_mesh", 1),

       (set_fixed_point_multiplier, 100),

       (init_position, pos1),
       (position_set_x, pos1, -60),
       (position_set_y, pos1, 151),
       (cur_tableau_add_mesh, ":banner_mesh", pos1, 116, 0),
       (init_position, pos1),
       (position_set_z, pos1, 10),
       (cur_tableau_add_mesh, "mesh_tableau_mesh_shield_heater_1", pos1, 0, 0),
       (cur_tableau_set_camera_parameters, 0, 200, 200, 0, 100000),
       ]),
  ("heater_shield_2", 0, "sample_shield_matte", 512, 512, 0, 0, 0, 0,
   [
       (store_script_param, ":banner_mesh", 1),

       (set_fixed_point_multiplier, 100),

       (init_position, pos1),
       (position_set_x, pos1, -50),
       (position_set_y, pos1, 150),
       (cur_tableau_add_mesh, ":banner_mesh", pos1, 116, 0),
       (init_position, pos1),
       (position_set_z, pos1, 10),
       (cur_tableau_add_mesh, "mesh_tableau_mesh_shield_heater_2", pos1, 0, 0),
       (cur_tableau_set_camera_parameters, 0, 200, 200, 0, 100000),
       ]),
  ("pavise_shield_1", 0, "sample_shield_matte", 512, 512, 0, 0, 0, 0,
   [
       (store_script_param, ":banner_mesh", 1),

       (set_fixed_point_multiplier, 100),

       (init_position, pos1),
       (position_set_x, pos1, -54),
       (position_set_y, pos1, 120),
       (cur_tableau_add_mesh, ":banner_mesh", pos1, 118, 0),
       (init_position, pos1),
       (position_set_z, pos1, 10),
       (cur_tableau_add_mesh, "mesh_tableau_mesh_shield_pavise_1", pos1, 0, 0),
       (cur_tableau_set_camera_parameters, 0, 200, 200, 0, 100000),
       ]),
  ("pavise_shield_2", 0, "sample_shield_matte", 512, 512, 0, 0, 0, 0,
   [
       (store_script_param, ":banner_mesh", 1),

       (set_fixed_point_multiplier, 100),

       (init_position, pos1),
       (position_set_x, pos1, -54),
       (position_set_y, pos1, 120),
       (cur_tableau_add_mesh, ":banner_mesh", pos1, 116, 0),
       (init_position, pos1),
       (position_set_z, pos1, 10),
       (cur_tableau_add_mesh, "mesh_tableau_mesh_shield_pavise_2", pos1, 0, 0),
       (cur_tableau_set_camera_parameters, 0, 200, 200, 0, 100000),
       ]),

  ("heraldic_armor_a", 0, "sample_heraldic_armor_a", 512, 512, 0, 0, 0, 0,
   [
       (store_script_param, ":banner_mesh", 1),

       (set_fixed_point_multiplier, 100),
       (store_sub, ":background_slot", ":banner_mesh", arms_meshes_begin),
       (troop_get_slot, ":background_color", "trp_banner_background_color_array", ":background_slot"),
       (cur_tableau_set_background_color, ":background_color"),

       (init_position, pos1),
       (cur_tableau_add_mesh_with_vertex_color, "mesh_heraldic_armor_bg", pos1, 200, 100, ":background_color"),
       (init_position, pos1),

       (position_set_z, pos1, 50),
       (position_set_x, pos1, -25),
       (position_set_y, pos1, 130),
       (cur_tableau_add_mesh, ":banner_mesh", pos1, 103, 0),
       (init_position, pos1),
       (position_set_z, pos1, 100),
       (cur_tableau_add_mesh, "mesh_tableau_mesh_heraldic_armor_a", pos1, 0, 0),
       (cur_tableau_set_camera_parameters, 0, 200, 200, 0, 100000),
       ]),
  
  ("heraldic_armor_b", 0, "sample_heraldic_armor_b", 512, 512, 0, 0, 0, 0,
   [
       (store_script_param, ":banner_mesh", 1),

       (set_fixed_point_multiplier, 100),
       (store_sub, ":background_slot", ":banner_mesh", arms_meshes_begin),
       (troop_get_slot, ":background_color", "trp_banner_background_color_array", ":background_slot"),
       (cur_tableau_set_background_color, ":background_color"),

       (init_position, pos1),
       (cur_tableau_add_mesh_with_vertex_color, "mesh_heraldic_armor_bg", pos1, 200, 100, ":background_color"),
       (init_position, pos1),
       (position_set_z, pos1, 10),
       (position_set_x, pos1, -5),
       (position_set_y, pos1, 130),
       (cur_tableau_add_mesh, ":banner_mesh", pos1, 113, 0),
       (init_position, pos1),
       (position_set_z, pos1, 100),
       (cur_tableau_add_mesh, "mesh_tableau_mesh_heraldic_armor_b", pos1, 0, 0),
       (cur_tableau_set_camera_parameters, 0, 200, 200, 0, 100000),
       ]),
  
  ("heraldic_armor_c", 0, "sample_heraldic_armor_c", 512, 512, 0, 0, 0, 0,
   [
       (store_script_param, ":banner_mesh", 1),

       (set_fixed_point_multiplier, 100),
       (store_sub, ":background_slot", ":banner_mesh", arms_meshes_begin), #banner_meshes_begin),
       (troop_get_slot, ":background_color", "trp_banner_background_color_array", ":background_slot"),
       (cur_tableau_set_background_color, ":background_color"),

       (init_position, pos1),
       (cur_tableau_add_mesh_with_vertex_color, "mesh_heraldic_armor_bg", pos1, 200, 100, ":background_color"),
       (init_position, pos1),
       (position_set_z, pos1, 10),
       (position_set_x, pos1, -0),
       (position_set_y, pos1, 130),
       (cur_tableau_add_mesh, ":banner_mesh", pos1, 115, 0),
       (init_position, pos1),
       (position_set_z, pos1, 100),
       (cur_tableau_add_mesh, "mesh_tableau_mesh_heraldic_armor_c", pos1, 0, 0),
       (cur_tableau_set_camera_parameters, 0, 200, 200, 0, 100000),
       ]),
  
  ("heraldic_armor_d", 0, "sample_heraldic_armor_d", 512, 512, 0, 0, 0, 0,
   [
       (store_script_param, ":banner_mesh", 1),

       (set_fixed_point_multiplier, 100),
        (store_sub, ":background_slot", ":banner_mesh", arms_meshes_begin), #banner_meshes_begin),
       (troop_get_slot, ":background_color", "trp_banner_background_color_array", ":background_slot"),
       (cur_tableau_set_background_color, ":background_color"),

       (init_position, pos1),
       (cur_tableau_add_mesh_with_vertex_color, "mesh_heraldic_armor_bg", pos1, 200, 100, ":background_color"),
       (init_position, pos1),
       (position_set_z, pos1, 10),
       (position_set_x, pos1, -0),
       (position_set_y, pos1, 130),
       (cur_tableau_add_mesh, ":banner_mesh", pos1, 113, 0),
       (init_position, pos1),
       (position_set_z, pos1, 100),
       (cur_tableau_add_mesh, "mesh_tableau_mesh_heraldic_armor_d", pos1, 0, 0),
       (cur_tableau_set_camera_parameters, 0, 200, 200, 0, 100000),
       ]),
	   
  ("troop_note_alpha_mask", 0, "mat_troop_portrait_mask", 1024, 1024, 0, 0, 400, 400,
   [
       (store_script_param, ":troop_no", 1),
       (cur_tableau_set_background_color, 0x00888888),
       (cur_tableau_set_ambient_light, 10,11,15),
       (cur_tableau_render_as_alpha_mask),
       (call_script, "script_add_troop_to_cur_tableau", ":troop_no"),
       ]),

  ("troop_note_color", 0, "mat_troop_portrait_color", 1024, 1024, 0, 0, 400, 400,
   [
       (store_script_param, ":troop_no", 1),
       (cur_tableau_set_background_color, 0xFFC6BB94),
       (cur_tableau_set_ambient_light, 10,11,15),
       (call_script, "script_add_troop_to_cur_tableau", ":troop_no"),
       ]),

  ("troop_character_alpha_mask", 0, "mat_troop_portrait_mask", 1024, 1024, 0, 0, 400, 400,
   [
       (store_script_param, ":troop_no", 1),
       (cur_tableau_set_background_color, 0x00888888),
       (cur_tableau_set_ambient_light, 10,11,15),
       (cur_tableau_render_as_alpha_mask),
       (call_script, "script_add_troop_to_cur_tableau_for_character", ":troop_no"),
       ]),

  ("troop_character_color", 0, "mat_troop_portrait_color", 1024, 1024, 0, 0, 400, 400,
   [
       (store_script_param, ":troop_no", 1),
       (cur_tableau_set_background_color, 0xFFE0CFB1),
       (cur_tableau_set_ambient_light, 10,11,15),
       (call_script, "script_add_troop_to_cur_tableau_for_character", ":troop_no"),
       ]),
  
  ("troop_inventory_alpha_mask", 0, "mat_troop_portrait_mask", 1024, 1024, 0, 0, 400, 400,
   [
       (store_script_param, ":troop_no", 1),
       (cur_tableau_set_background_color, 0x00888888),
       (cur_tableau_set_ambient_light, 10,11,15),
       (cur_tableau_render_as_alpha_mask),
       (call_script, "script_add_troop_to_cur_tableau_for_inventory", ":troop_no"),
       ]),

  ("troop_inventory_color", 0, "mat_troop_portrait_color", 1024, 1024, 0, 0, 400, 400,
   [
       (store_script_param, ":troop_no", 1),
       (cur_tableau_set_background_color, 0xFF6A583A),
       (cur_tableau_set_ambient_light, 10,11,15),
       (call_script, "script_add_troop_to_cur_tableau_for_inventory", ":troop_no"),
       ]),

  ("troop_profile_alpha_mask", 0, "mat_troop_portrait_mask", 1024, 1024, 0, 0, 400, 400,
   [
       (store_script_param, ":troop_no", 1),
       (cur_tableau_set_background_color, 0x00888888),
       (cur_tableau_set_ambient_light, 10,11,15),
       (cur_tableau_render_as_alpha_mask),
       (call_script, "script_add_troop_to_cur_tableau_for_profile", ":troop_no"),
       ]),

  ("troop_profile_color", 0, "mat_troop_portrait_color", 1024, 1024, 0, 0, 400, 400,
   [
       (store_script_param, ":troop_no", 1),
       (cur_tableau_set_background_color, 0xFFF9E7A8),
       (cur_tableau_set_ambient_light, 10,11,15),
       (call_script, "script_add_troop_to_cur_tableau_for_profile", ":troop_no"),
       ]),


  ("troop_party_alpha_mask", 0, "mat_troop_portrait_mask", 1024, 1024, 0, 0, 400, 400,
   [
       (store_script_param, ":troop_no", 1),
       (cur_tableau_set_background_color, 0x00888888),
       (cur_tableau_set_ambient_light, 10,11,15),
       (cur_tableau_render_as_alpha_mask),
       (call_script, "script_add_troop_to_cur_tableau_for_party", ":troop_no"),
       ]),

  ("troop_party_color", 0, "mat_troop_portrait_color", 1024, 1024, 0, 0, 400, 400,
   [
       (store_script_param, ":troop_no", 1),
       (cur_tableau_set_background_color, 0xFFBE9C72),
       (cur_tableau_set_ambient_light, 10,11,15),
       (call_script, "script_add_troop_to_cur_tableau_for_party", ":troop_no"),
       ]),

  ("troop_note_mesh", 0, "tableau_with_transparency", 1024, 1024, 0, 0, 350, 350,
   [
       (store_script_param, ":troop_no", 1),
       (cur_tableau_set_background_color, 0xFF888888),
       (cur_tableau_set_ambient_light, 10,11,15),
       (set_fixed_point_multiplier, 100),
       (cur_tableau_set_camera_parameters, 0, 40, 40, 0, 100000),

       (init_position, pos1),
       (position_set_z, pos1, 100),
       (position_set_x, pos1, -20),
       (position_set_y, pos1, -20),
       (cur_tableau_add_tableau_mesh, "tableau_troop_note_color", ":troop_no", pos1, 0, 0),
       (position_set_z, pos1, 200),
       (cur_tableau_add_tableau_mesh, "tableau_troop_note_alpha_mask", ":troop_no", pos1, 0, 0),
       (position_set_z, pos1, 300),
       (cur_tableau_add_mesh, "mesh_portrait_blend_out", pos1, 0, 0),
       ]),

  ("center_note_mesh", 0, "tableau_with_transparency", 1024, 1024, 0, 0, 200, 200,
   [
       (store_script_param, ":center_no", 1),
       (set_fixed_point_multiplier, 100),
       (cur_tableau_set_background_color, 0x00888888),
       (cur_tableau_set_ambient_light, 10,11,15),
       
       (init_position, pos8),
       (position_set_x, pos8, -210),
       (position_set_y, pos8, 200),
       (position_set_z, pos8, 300),
       (cur_tableau_add_point_light, pos8, 550,500,450),

       (cur_tableau_set_camera_parameters, 1, 10, 10, 10, 10000),

       (init_position, pos1),
       (position_set_z, pos1, 0),
       (position_set_z, pos1, -500),


       (init_position, pos1),
       (position_set_y, pos1, -100),
       (position_set_x, pos1, -100),
       (position_set_z, pos1, 100),
       (position_rotate_z, pos1, 200),

       (party_get_icon, ":map_icon", ":center_no"),
       (try_begin),
         (ge, ":map_icon", 0),
         (cur_tableau_add_map_icon, ":map_icon", pos1, 0),
       (try_end),

       (init_position, pos5),
       (position_set_x, pos5, -90),
       (position_set_z, pos5, 500),
       (position_set_y, pos5, 480),
       (position_rotate_x, pos5, -90),
       (position_rotate_z, pos5, 180),
       (position_rotate_x, pos5, -35),
       (cur_tableau_set_camera_position, pos5),
       ]),

  ("faction_note_mesh_for_menu", 0, "pic_arms_swadian", 1024, 512, 0, 0, 450, 225,
   [
     (store_script_param, ":faction_no", 1),
     (cur_tableau_set_background_color, 0xFFFFFFFF),
     (set_fixed_point_multiplier, 100),
     (try_begin),
       (is_between, ":faction_no", "fac_kingdom_1", kingdoms_end), #Excluding player kingdom
       (store_add, ":banner_mesh", "mesh_pic_arms_swadian", ":faction_no"),
       (val_sub, ":banner_mesh", "fac_kingdom_1"),
       (init_position, pos1),
       (position_set_y, pos1, -5),
       (position_set_x, pos1, -45),
       (cur_tableau_add_mesh, ":banner_mesh", pos1, 0, 0),
       (cur_tableau_set_camera_parameters, 0, 160, 80, 0, 100000),
     (try_end),
     ]),

  ("faction_note_mesh", 0, "pic_arms_swadian", 1024, 512, 0, 0, 500, 250,
   [
     (store_script_param, ":faction_no", 1),
     (cur_tableau_set_background_color, 0xFFFFFFFF),
     (set_fixed_point_multiplier, 100),
     (try_begin),
       (is_between, ":faction_no", "fac_kingdom_1", kingdoms_end), #Excluding player kingdom
       (store_add, ":banner_mesh", "mesh_pic_arms_swadian", ":faction_no"),
       (val_sub, ":banner_mesh", "fac_kingdom_1"),
       (init_position, pos1),
       (position_set_y, pos1, -5),
       (cur_tableau_add_mesh, ":banner_mesh", pos1, 0, 0),
       (cur_tableau_set_camera_parameters, 0, 100, 50, 0, 100000),
     (try_end),
     ]),

  ("faction_note_mesh_banner", 0, "tableau_with_transparency", 1024, 1024, 0, 0, 200, 200,
   [
     (store_script_param, ":faction_no", 1),
     (set_fixed_point_multiplier, 100),
     (try_begin),
       (faction_get_slot, ":leader_troop", ":faction_no", slot_faction_leader),
       (ge, ":leader_troop", 0),
       (troop_get_slot, ":banner_spr", ":leader_troop", slot_troop_banner_scene_prop),
       (store_add, ":banner_scene_props_end", banner_scene_props_end_minus_one, 1),
       (is_between, ":banner_spr", banner_scene_props_begin, ":banner_scene_props_end"),
       (val_sub, ":banner_spr", banner_scene_props_begin),
       (store_add, ":banner_mesh", ":banner_spr", banner_meshes_begin),
       (init_position, pos1),
       (position_set_y, pos1, 100),
       (cur_tableau_add_mesh, ":banner_mesh", pos1, 0, 0),
       (cur_tableau_set_camera_parameters, 0, 210, 210, 0, 100000),
     (try_end),
     ]),
  
  ("2_factions_mesh", 0, "tableau_with_transparency", 1024, 1024, 0, 0, 200, 200,
   [
     (store_script_param, ":faction_no", 1),
     (store_mod, ":faction_no_2", ":faction_no", 128),
     (val_div, ":faction_no", 128),
     (val_add, ":faction_no", kingdoms_begin),
     (val_add, ":faction_no_2", kingdoms_begin),
     (set_fixed_point_multiplier, 100),
     (try_begin),
       (faction_get_slot, ":leader_troop", ":faction_no", slot_faction_leader),
       (ge, ":leader_troop", 0),
       (troop_get_slot, ":banner_spr", ":leader_troop", slot_troop_banner_scene_prop),
       (store_add, ":banner_scene_props_end", banner_scene_props_end_minus_one, 1),
       (is_between, ":banner_spr", banner_scene_props_begin, ":banner_scene_props_end"),
       (val_sub, ":banner_spr", banner_scene_props_begin),
       (store_add, ":banner_mesh", ":banner_spr", banner_meshes_begin),
       (init_position, pos1),
       (position_set_x, pos1, -50),
       (position_set_y, pos1, 100),
       (cur_tableau_add_mesh, ":banner_mesh", pos1, 0, 0),
     (try_end),
     (try_begin),
       (faction_get_slot, ":leader_troop", ":faction_no_2", slot_faction_leader),
       (ge, ":leader_troop", 0),
       (troop_get_slot, ":banner_spr", ":leader_troop", slot_troop_banner_scene_prop),
       (store_add, ":banner_scene_props_end", banner_scene_props_end_minus_one, 1),
       (is_between, ":banner_spr", banner_scene_props_begin, ":banner_scene_props_end"),
       (val_sub, ":banner_spr", banner_scene_props_begin),
       (store_add, ":banner_mesh", ":banner_spr", banner_meshes_begin),
       (init_position, pos1),
       (position_set_x, pos1, 50),
       (position_set_y, pos1, 100),
       (cur_tableau_add_mesh, ":banner_mesh", pos1, 0, 0),
     (try_end),
     (cur_tableau_set_camera_parameters, 0, 210, 210, 0, 100000),
     ]),

  ("color_picker", 0, "missiles", 32, 32, 0, 0, 0, 0,
   [
     (store_script_param, ":color", 1),
     (set_fixed_point_multiplier, 100),
     (init_position, pos1),
     (cur_tableau_add_mesh, "mesh_color_picker", pos1, 0, 0),
     (position_move_z, pos1, 1),
     (position_move_x, pos1, -2),
     (position_move_y, pos1, -2),
     (cur_tableau_add_mesh_with_vertex_color, "mesh_white_plane", pos1, 200, 0, ":color"),
     (cur_tableau_set_camera_parameters, 0, 20, 20, 0, 100000),
     ]),

  ("retired_troop_alpha_mask", 0, "mat_troop_portrait_mask", 2048, 2048, 0, 0, 600, 600,
   [
       (store_script_param, ":type", 1),
       (cur_tableau_set_background_color, 0x00888888),
       (cur_tableau_set_ambient_light, 10,11,15),
       (cur_tableau_render_as_alpha_mask),
       (call_script, "script_add_troop_to_cur_tableau_for_retirement", ":type"),
       ]),

  ("retired_troop_color", 0, "mat_troop_portrait_color", 2048, 2048, 0, 0, 600, 600,
   [
       (store_script_param, ":type", 1),
       (cur_tableau_set_background_color, 0xFFe7d399),
       (cur_tableau_set_ambient_light, 10,11,15),
       (call_script, "script_add_troop_to_cur_tableau_for_retirement", ":type"),
       ]),

  ("retirement_troop", 0, "tableau_with_transparency", 2048, 2048, 0, 0, 600, 600,
   [
     (store_script_param, ":type", 1),
     (cur_tableau_set_background_color, 0xFF888888),
     (cur_tableau_set_ambient_light, 10,11,15),
     (set_fixed_point_multiplier, 100),
     (cur_tableau_set_camera_parameters, 0, 40, 40, 0, 100000),

     (init_position, pos1),
     (position_set_z, pos1, 100),
     (position_set_x, pos1, -20),
     (position_set_y, pos1, -20),
     (cur_tableau_add_tableau_mesh, "tableau_retired_troop_color", ":type", pos1, 0, 0),
     (position_set_z, pos1, 200),
     (cur_tableau_add_tableau_mesh, "tableau_retired_troop_alpha_mask", ":type", pos1, 0, 0),
     ]),
  
]
