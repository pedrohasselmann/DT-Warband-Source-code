from module_constants import *
from ID_factions import *
#from header_items import  *
#from header_operations import *
#from header_triggers import *
from compiler import *

####################################################################################################################
#  Each item record contains the following fields:
#  1) Item id: used for referencing items in other files.
#     The prefix itm_ is automatically added before each item id.
#  2) Item name. Name of item as it'll appear in inventory window
#  3) List of meshes.  Each mesh record is a tuple containing the following fields:
#    3.1) Mesh name.
#    3.2) Modifier bits that this mesh matches.
#     Note that the first mesh record is the default.
#  4) Item flags. See header_items.py for a list of available flags.
#  5) Item capabilities. Used for which animations this item is used with. See header_items.py for a list of available flags.
#  6) Item value.
#  7) Item stats: Bitwise-or of various stats about the item such as:
#      weight, abundance, difficulty, head_armor, body_armor,leg_armor, etc...
#  8) Modifier bits: Modifiers that can be applied to this item.
#  9) [Optional] Triggers: List of simple triggers to be associated with the item.
#  10) [Optional] Factions: List of factions that item can be found as merchandise.
####################################################################################################################

# Some constants for ease of use.
imodbits_none = 0
imodbits_horse_basic = imodbit_swaybacked|imodbit_lame|imodbit_spirited|imodbit_heavy|imodbit_stubborn
imodbits_horse_simple = imodbit_swaybacked|imodbit_lame|imodbit_heavy|imodbit_stubborn
imodbits_cloth  = imodbit_tattered | imodbit_ragged | imodbit_sturdy | imodbit_thick | imodbit_hardened
imodbits_clothes = imodbit_tattered | imodbit_ragged | imodbit_sturdy | imodbit_thick
imodbits_armor  = imodbit_rusty | imodbit_battered | imodbit_crude | imodbit_thick | imodbit_reinforced |imodbit_lordly
imodbits_plate  = imodbit_cracked | imodbit_rusty | imodbit_battered | imodbit_crude | imodbit_thick | imodbit_reinforced |imodbit_lordly
imodbits_polearm = imodbit_cracked | imodbit_bent | imodbit_balanced
imodbits_shield  = imodbit_cracked | imodbit_battered |imodbit_thick | imodbit_reinforced
imodbits_sword   = imodbit_rusty | imodbit_chipped | imodbit_balanced |imodbit_tempered
imodbits_sword_high   = imodbit_rusty | imodbit_chipped | imodbit_balanced |imodbit_tempered|imodbit_masterwork
imodbits_axe   = imodbit_rusty | imodbit_chipped | imodbit_heavy
imodbits_axe_minus_heavy   = imodbit_rusty | imodbit_chipped
imodbits_mace   = imodbit_rusty | imodbit_chipped | imodbit_heavy
imodbits_pick   = imodbit_rusty | imodbit_chipped | imodbit_balanced | imodbit_heavy
imodbits_bow = imodbit_cracked | imodbit_bent | imodbit_strong |imodbit_masterwork
imodbits_crossbow = imodbit_cracked | imodbit_bent | imodbit_masterwork
imodbits_missile   = imodbit_bent | imodbit_large_bag
imodbits_thrown   = imodbit_bent | imodbit_heavy| imodbit_balanced| imodbit_large_bag
imodbits_thrown_minus_heavy = imodbit_bent | imodbit_balanced| imodbit_large_bag

imodbits_horse_good = imodbit_spirited|imodbit_heavy
imodbits_good   = imodbit_sturdy | imodbit_thick | imodbit_hardened | imodbit_reinforced
imodbits_bad    = imodbit_rusty | imodbit_chipped | imodbit_tattered | imodbit_ragged | imodbit_cracked | imodbit_bent

items = [
#************************************************************************************************
# ITEMS in this range are hardcoded into item_codes.h and their order should not be changed!
#************************************************************************************************
 ["no_item","INVALID ITEM", [("invalid_item",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary, itc_longsword, 3,weight(1.5)|spd_rtng(103)|weapon_length(90)|swing_damage(16,blunt)|thrust_damage(10,blunt),imodbits_none],
 ["tutorial_spear", "Spear", [("spear",0)], itp_type_polearm| itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_no_blur, itc_spear, 0 , weight(4.5)|difficulty(0)|spd_rtng(80) | weapon_length(158)|swing_damage(0 , cut) | thrust_damage(19 ,  pierce),imodbits_polearm ],
 ["tutorial_club", "Club", [("club",0)], itp_type_one_handed_wpn| itp_primary|itp_wooden_parry|itp_wooden_attack, itc_scimitar, 0 , weight(2.5)|difficulty(0)|spd_rtng(95) | weapon_length(95)|swing_damage(11 , blunt) | thrust_damage(0 ,  pierce),imodbits_none ],
 ["tutorial_battle_axe", "Battle Axe", [("battle_ax",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 0 , weight(5)|difficulty(0)|spd_rtng(88) | weapon_length(108)|swing_damage(27 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
 ["tutorial_arrows","Arrows", [("arrow",0),("flying_missile",ixmesh_flying_ammo),("quiver", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back, 0,weight(3)|abundance(160)|weapon_length(95)|thrust_damage(0,pierce)|max_ammo(20),imodbits_missile],
 ["tutorial_bolts","Bolts", [("bolt",0),("flying_missile",ixmesh_flying_ammo),("bolt_bag", ixmesh_carry),("bolt_bag_b", ixmesh_carry|imodbit_large_bag)], itp_type_bolts, itcf_carry_quiver_right_vertical, 0,weight(2.25)|abundance(90)|weapon_length(55)|thrust_damage(0,pierce)|max_ammo(18),imodbits_missile],
 ["tutorial_short_bow", "Short Bow", [("short_bow",0),("short_bow_carry",ixmesh_carry)], itp_type_bow |itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bow_back, 0 , weight(1)|difficulty(0)|spd_rtng(98) | shoot_speed(49) | thrust_damage(12 ,  pierce  ),imodbits_bow ],
 ["tutorial_crossbow", "Crossbow", [("crossbow",0)], itp_type_crossbow |itp_primary|itp_two_handed|itp_cant_reload_on_horseback ,itcf_shoot_crossbow|itcf_carry_crossbow_back, 0 , weight(3)|difficulty(0)|spd_rtng(42)|  shoot_speed(68) | thrust_damage(32,pierce)|max_ammo(1),imodbits_crossbow ],
 ["tutorial_throwing_daggers", "Throwing Daggers", [("throwing_dagger",0)], itp_type_thrown |itp_primary ,itcf_throw_knife, 0 , weight(3.5)|difficulty(0)|spd_rtng(102) | shoot_speed(25) | thrust_damage(16 ,  cut)|max_ammo(14)|weapon_length(0),imodbits_missile ],
 ["tutorial_saddle_horse", "Saddle Horse", [("saddle_horse",0)], itp_type_horse, 0, 0,abundance(90)|body_armor(3)|difficulty(0)|horse_speed(40)|horse_maneuver(38)|horse_charge(8),imodbits_horse_basic],
 ["tutorial_shield", "Kite Shield", [("shield_kite_a",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|weapon_length(150),imodbits_shield ],
 ["tutorial_staff_no_attack","Staff", [("wooden_staff",0)],itp_type_polearm|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack,itc_parry_polearm|itcf_carry_sword_back,9, weight(3.5)|spd_rtng(120) | weapon_length(115)|swing_damage(0,blunt) | thrust_damage(0,blunt),imodbits_none],
 ["tutorial_staff","Staff", [("wooden_staff",0)],itp_type_polearm|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack,itc_staff|itcf_carry_sword_back,9, weight(3.5)|spd_rtng(120) | weapon_length(115)|swing_damage(16,blunt) | thrust_damage(16,blunt),imodbits_none],
 ["tutorial_sword", "Sword", [("long_sword",0),("scab_longsw_a", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 0 , weight(1.5)|difficulty(0)|spd_rtng(100) | weapon_length(102)|swing_damage(18 , cut) | thrust_damage(15 ,  pierce),imodbits_sword ],
 ["tutorial_axe", "Axe", [("iron_ax",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 0 , weight(4)|difficulty(0)|spd_rtng(91) | weapon_length(108)|swing_damage(19 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
 ["tutorial_dagger","Dagger", [("practice_dagger",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary, itc_longsword, 3,weight(1.5)|spd_rtng(103)|weapon_length(40)|swing_damage(16,blunt)|thrust_damage(10,blunt),imodbits_none],

 ["horse_meat","Horse Meat", [("raw_meat",0)], itp_type_goods|itp_consumable|itp_food, 0, 12,weight(40)|food_quality(30)|max_ammo(40),imodbits_none],
 ["practice_sword","Practice Sword", [("practice_sword",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_wooden_parry|itp_wooden_attack, itc_longsword, 3,weight(1.5)|spd_rtng(103)|weapon_length(90)|swing_damage(22,blunt)|thrust_damage(20,blunt),imodbits_none],
 ["heavy_practice_sword","Heavy Practice Sword", [("heavy_practicesword",0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_wooden_parry|itp_wooden_attack, itc_greatsword,    21, weight(6.25)|spd_rtng(94)|weapon_length(128)|swing_damage(30,blunt)|thrust_damage(24,blunt),imodbits_none],
 ["practice_dagger","Practice Dagger", [("practice_dagger",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_no_parry|itp_wooden_attack, itc_dagger|itcf_carry_dagger_front_left, 2,weight(0.5)|spd_rtng(110)|weapon_length(47)|swing_damage(16,blunt)|thrust_damage(14,blunt),imodbits_none],
 ["practice_axe","Practice Axe", [("hatchet",0)], itp_type_one_handed_wpn| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 24 , weight(2) | spd_rtng(95) | weapon_length(75) | swing_damage(24, blunt) | thrust_damage(0, pierce), imodbits_axe],
 ["arena_axe","Axe",[("arena_axe",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 137 , weight(1.5)|spd_rtng(100) | weapon_length(69)|swing_damage(24 , blunt) | thrust_damage(0 ,  pierce),imodbits_axe ],
 ["arena_sword","Sword",[("arena_sword_one_handed",0),("sword_medieval_b_scabbard", ixmesh_carry),], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 243 , weight(1.5)|spd_rtng(99) | weapon_length(95)|swing_damage(22 , blunt) | thrust_damage(20 ,  blunt),imodbits_sword_high ],
 ["arena_sword_two_handed","Two Handed Sword", [("arena_sword_two_handed",0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back, 670 , weight(2.75)|spd_rtng(93) | weapon_length(110)|swing_damage(30 , blunt) | thrust_damage(24 ,  blunt),imodbits_sword_high ],
 ["arena_lance","Lance",[("arena_lance",0)], itp_couchable|itp_type_polearm|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_staff|itcf_carry_spear, 90 , weight(2.5)|spd_rtng(96) | weapon_length(150)|swing_damage(20 , blunt) | thrust_damage(25 ,  blunt),imodbits_polearm ],

 ["practice_staff","Practice Staff", [("wooden_staff",0)],itp_type_polearm|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack,itc_staff|itcf_carry_sword_back,9, weight(2.5)|spd_rtng(103) | weapon_length(118)|swing_damage(18,blunt) | thrust_damage(18,blunt),imodbits_none],
 ["practice_lance","Practice Lance", [("joust_of_peace",0)], itp_couchable|itp_type_polearm|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack, itc_greatlance, 18,weight(4.25)|spd_rtng(58)|weapon_length(240)|swing_damage(0,blunt)|thrust_damage(15,blunt),imodbits_none],
 ["practice_shield","Practice Shield", [("shield_round_a",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 20,weight(3.5)|body_armor(1)|hit_points(200)|spd_rtng(100)|shield_width(50),imodbits_none],
 ["practice_bow","Practice Bow", [("hunting_bow",0), ("hunting_bow_carry",ixmesh_carry)], itp_type_bow |itp_primary|itp_two_handed,itcf_shoot_bow|itcf_carry_bow_back, 0, weight(1.5)|spd_rtng(90) | shoot_speed(40) | thrust_damage(21, blunt),imodbits_bow ],
 ["practice_crossbow", "Practice Crossbow", [("crossbow_a",0)], itp_type_crossbow |itp_primary|itp_two_handed ,itcf_shoot_crossbow|itcf_carry_crossbow_back, 0, weight(3)|spd_rtng(42)| shoot_speed(68) | thrust_damage(32,blunt)|max_ammo(1),imodbits_crossbow],
 ["practice_javelin", "Practice Javelins", [("javelin",0),("javelins_quiver_new", ixmesh_carry)], itp_type_thrown |itp_primary|itp_next_item_as_melee,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn, 0, weight(5) | spd_rtng(91) | shoot_speed(28) | thrust_damage(27, blunt) | max_ammo(50) | weapon_length(75), imodbits_thrown],
 ["practice_javelin_melee", "practice_javelin_melee", [("javelin",0)], itp_type_polearm|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_no_blur , itc_spear, 0, weight(1)|difficulty(0)|spd_rtng(91) |swing_damage(12, blunt)| thrust_damage(14,  blunt)|weapon_length(75),imodbits_polearm ],
 ["practice_throwing_daggers", "Throwing Daggers", [("throwing_dagger",0)], itp_type_thrown |itp_primary ,itcf_throw_knife, 0 , weight(3.5)|spd_rtng(102) | shoot_speed(25) | thrust_damage(16, blunt)|max_ammo(10)|weapon_length(0),imodbits_thrown ],
 ["practice_throwing_daggers_100_amount", "Throwing Daggers", [("throwing_dagger",0)], itp_type_thrown |itp_primary ,itcf_throw_knife, 0 , weight(3.5)|spd_rtng(102) | shoot_speed(25) | thrust_damage(16, blunt)|max_ammo(100)|weapon_length(0),imodbits_thrown ],
 ["practice_horse","Practice Horse", [("saddle_horse",0)], itp_type_horse, 0, 37,body_armor(10)|horse_speed(40)|horse_maneuver(37)|horse_charge(14),imodbits_none],
 ["practice_arrows","Practice Arrows", [("arena_arrow",0),("flying_missile",ixmesh_flying_ammo),("quiver", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back, 0,weight(1.5)|weapon_length(95)|max_ammo(80),imodbits_missile],
 ["practice_bolts","Practice Bolts", [("bolt",0),("flying_missile",ixmesh_flying_ammo),("bolt_bag", ixmesh_carry),("bolt_bag_b", ixmesh_carry|imodbit_large_bag)], itp_type_bolts, itcf_carry_quiver_right_vertical, 0,weight(2.25)|weapon_length(55)|max_ammo(49),imodbits_missile],
 ["practice_arrows_10_amount","Practice Arrows", [("arrow",0),("flying_missile",ixmesh_flying_ammo),("quiver", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back, 0,weight(1.5)|weapon_length(95)|max_ammo(10),imodbits_missile],
 ["practice_arrows_100_amount","Practice Arrows", [("arrow",0),("flying_missile",ixmesh_flying_ammo),("quiver", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back, 0,weight(1.5)|weapon_length(95)|max_ammo(100),imodbits_missile],
 ["practice_bolts_9_amount","Practice Bolts", [("bolt",0),("flying_missile",ixmesh_flying_ammo),("bolt_bag", ixmesh_carry),("bolt_bag_b", ixmesh_carry|imodbit_large_bag)], itp_type_bolts, itcf_carry_quiver_right_vertical, 0,weight(2.25)|weapon_length(55)|max_ammo(9),imodbits_missile],
 ["practice_boots", "Practice Boots", [("boot_nomad_a",0)], itp_type_foot_armor |itp_civilian  | itp_attach_armature,0, 11 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(10), imodbits_cloth ],

 ["red_tourney_armor","Red Tourney Armor", [("tourn_armor_a",0)], itp_type_body_armor|itp_covers_legs, 0, 152,weight(15.0)|body_armor(20)|leg_armor(6),imodbits_none],
 ["blue_tourney_armor","Blue Tourney Armor", [("mail_shirt",0)], itp_type_body_armor|itp_covers_legs, 0, 152,weight(15.0)|body_armor(20)|leg_armor(6),imodbits_none],
 ["green_tourney_armor","Green Tourney Armor", [("leather_vest",0)], itp_type_body_armor|itp_covers_legs, 0, 152,weight(15.0)|body_armor(20)|leg_armor(6),imodbits_none],
 ["gold_tourney_armor","Gold Tourney Armor", [("padded_armor",0)], itp_type_body_armor|itp_covers_legs, 0, 152,weight(15.0)|body_armor(20)|leg_armor(6),imodbits_none],
 ["red_tourney_helmet","Red Tourney Helmet",[("flattop_helmet",0)],itp_type_head_armor,0,126, weight(2)|head_armor(16),imodbits_none],
 ["blue_tourney_helmet","Blue Tourney Helmet",[("segmented_helm",0)],itp_type_head_armor,0,126, weight(2)|head_armor(16),imodbits_none],
 ["green_tourney_helmet","Green Tourney Helmet",[("hood_c",0)],itp_type_head_armor,0,126, weight(2)|head_armor(16),imodbits_none],
 ["gold_tourney_helmet","Gold Tourney Helmet",[("hood_a",0)],itp_type_head_armor,0,126, weight(2)|head_armor(16),imodbits_none],

["arena_shield_red", "Arena Shield", [("arena_shield_red",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  42 , weight(2)|hit_points(360)|body_armor(1)|spd_rtng(100)|weapon_length(60),imodbits_shield ],
["arena_shield_blue", "Arena Shield", [("arena_shield_blue",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  42 , weight(2)|hit_points(360)|body_armor(1)|spd_rtng(100)|weapon_length(60),imodbits_shield ],
["arena_shield_green", "Arena Shield", [("arena_shield_green",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  42 , weight(2)|hit_points(360)|body_armor(1)|spd_rtng(100)|weapon_length(60),imodbits_shield ],
["arena_shield_yellow", "Arena Shield", [("arena_shield_yellow",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  42 , weight(2)|hit_points(360)|body_armor(1)|spd_rtng(100)|weapon_length(60),imodbits_shield ],
["arena_armor_white", "Tunic over Mail", [("arena_armorW_new",0)], itp_type_body_armor  |itp_covers_legs ,0, 650 , weight(16)|abundance(100)|head_armor(0)|body_armor(29)|leg_armor(13), imodbits_armor ],
["arena_armor_red", "Tunic over Mail", [("arena_armorR_new",0)], itp_type_body_armor  |itp_covers_legs ,0, 650 , weight(16)|abundance(100)|head_armor(0)|body_armor(29)|leg_armor(13), imodbits_armor ],
["arena_armor_blue", "Tunic over Mail", [("arena_armorB_new",0)], itp_type_body_armor  |itp_covers_legs ,0, 650 , weight(16)|abundance(100)|head_armor(0)|body_armor(29)|leg_armor(13), imodbits_armor ],
["arena_armor_green", "Tunic over Mail", [("arena_armorG_new",0)], itp_type_body_armor  |itp_covers_legs ,0, 650 , weight(16)|abundance(100)|head_armor(0)|body_armor(29)|leg_armor(13), imodbits_armor ],
["arena_armor_yellow", "Tunic over Mail", [("arena_armorY_new",0)], itp_type_body_armor  |itp_covers_legs ,0, 650 , weight(16)|abundance(100)|head_armor(0)|body_armor(29)|leg_armor(13), imodbits_armor ],
["arena_tunic_white", "Padded Tunic", [("arena_tunicW_new",0)], itp_type_body_armor |itp_covers_legs ,0, 27 , weight(2)|abundance(100)|head_armor(0)|body_armor(16)|leg_armor(6), imodbits_cloth ],
["arena_tunic_red", "Padded Tunic", [("arena_tunicR_new",0)], itp_type_body_armor |itp_covers_legs ,0, 27 , weight(2)|abundance(100)|head_armor(0)|body_armor(16)|leg_armor(6), imodbits_cloth ], 
["arena_tunic_blue", "Padded Tunic", [("arena_tunicB_new",0)], itp_type_body_armor |itp_covers_legs ,0, 27 , weight(2)|abundance(100)|head_armor(0)|body_armor(16)|leg_armor(6), imodbits_cloth ], 
["arena_tunic_green", "Padded Tunic", [("arena_tunicG_new",0)], itp_type_body_armor |itp_covers_legs ,0, 27 , weight(2)|abundance(100)|head_armor(0)|body_armor(16)|leg_armor(6), imodbits_cloth ],
["arena_tunic_yellow", "Padded Tunic", [("arena_tunicY_new",0)], itp_type_body_armor |itp_covers_legs ,0, 27 , weight(2)|abundance(100)|head_armor(0)|body_armor(16)|leg_armor(6), imodbits_cloth ],
["arena_helmet_red", "Arena Helmet", [("arena_helmetR",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_plate ],
["arena_helmet_blue", "Arena Helmet", [("arena_helmetB",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_plate ],
["arena_helmet_green", "Arena Helmet", [("arena_helmetG",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_plate ],
["arena_helmet_yellow", "Arena Helmet", [("arena_helmetY",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_plate ],
["steppe_helmet_white", "Steppe Helmet", [("steppe_helmetW",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0), imodbits_plate ], 
["steppe_helmet_red", "Steppe Helmet", [("steppe_helmetR",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0), imodbits_plate ], 
["steppe_helmet_blue", "Steppe Helmet", [("steppe_helmetB",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0), imodbits_plate ], 
["steppe_helmet_green", "Steppe Helmet", [("steppe_helmetG",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0), imodbits_plate ], 
["steppe_helmet_yellow", "Steppe Helmet", [("steppe_helmetY",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0), imodbits_plate ], 
["tourney_helm_white", "Tourney Helm", [("tourney_helmR",0)], itp_type_head_armor|itp_covers_head,0, 760 , weight(2.75)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_plate ],
["tourney_helm_red", "Tourney Helm", [("tourney_helmR",0)], itp_type_head_armor|itp_covers_head,0, 760 , weight(2.75)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_plate ],
["tourney_helm_blue", "Tourney Helm", [("tourney_helmB",0)], itp_type_head_armor|itp_covers_head,0, 760 , weight(2.75)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_plate ],
["tourney_helm_green", "Tourney Helm", [("tourney_helmG",0)], itp_type_head_armor|itp_covers_head,0, 760 , weight(2.75)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_plate ],
["tourney_helm_yellow", "Tourney Helm", [("tourney_helmY",0)], itp_type_head_armor|itp_covers_head,0, 760 , weight(2.75)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_plate ],
["arena_turban_red", "Arena Turban", [("tuareg_open",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_plate ],
["arena_turban_blue", "Arena Turban", [("tuareg_open",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_plate ],
["arena_turban_green", "Arena Turban", [("tuareg_open",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_plate ],
["arena_turban_yellow", "Arena Turban", [("tuareg_open",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_plate ],

##
## BOOKS
##

 ["book_tactics","De Re Militari", [("book_a",0)], itp_type_book, 0, 4000,weight(2)|abundance(100),imodbits_none],
 ["book_persuasion","Rhetorica ad Herennium", [("book_b",0)], itp_type_book, 0, 5000,weight(2)|abundance(100),imodbits_none],
 ["book_leadership","The Life of Arthur Eld", [("book_d",0)], itp_type_book, 0, 4200,weight(2)|abundance(100),imodbits_none], # Editado
 ["book_intelligence","Essays on Logic", [("book_e",0)], itp_type_book, 0, 2900,weight(2)|abundance(100),imodbits_none],
 ["book_trade","A Treatise on the Value of Things", [("book_f",0)], itp_type_book, 0, 3100,weight(2)|abundance(100),imodbits_none],
 ["book_weapon_mastery", "On the Art of Fighting with Swords", [("book_d",0)], itp_type_book, 0, 4200,weight(2)|abundance(100),imodbits_none],
 ["book_engineering","Methods of Mechanical Theorems", [("book_open",0)], itp_type_book, 0, 4000,weight(2)|abundance(100),imodbits_none],
 ["book_wound_treatment_reference","The Book of Healing", [("book_c",0)], itp_type_book, 0, 3500,weight(2)|abundance(100),imodbits_none],
 ["book_training_reference","Manual of Arms", [("book_open",0)], itp_type_book, 0, 3500,weight(2)|abundance(100),imodbits_none],
 ["book_surgery_reference","The Great Book of Surgery", [("book_c",0)], itp_type_book, 0, 3500,weight(2)|abundance(100),imodbits_none],

##
## COMMODITIES
##

 ["spice","Spice", [("spice_sack",0)], itp_merchandise|itp_type_goods|itp_consumable, 0, 880,weight(40)|abundance(25)|max_ammo(50),imodbits_none],
 ["salt","Salt", [("salt_sack",0)], itp_merchandise|itp_type_goods, 0, 255,weight(50)|abundance(120),imodbits_none],
 ["oil","Oil", [("oil",0)], itp_merchandise|itp_type_goods|itp_consumable, 0, 450,weight(50)|abundance(60)|max_ammo(50),imodbits_none],
 ["pottery","Pottery", [("jug",0)], itp_merchandise|itp_type_goods, 0, 100,weight(50)|abundance(90),imodbits_none],
 ["raw_flax","Flax Bundle", [("raw_flax",0)], itp_merchandise|itp_type_goods, 0, 150,weight(40)|abundance(90),imodbits_none],
 ["linen","Linen", [("linen",0)], itp_merchandise|itp_type_goods, 0, 250,weight(40)|abundance(90),imodbits_none],
 ["wool","Wool", [("wool_sack",0)], itp_merchandise|itp_type_goods, 0, 130,weight(40)|abundance(90),imodbits_none],
 ["wool_cloth","Wool Cloth", [("wool_cloth",0)], itp_merchandise|itp_type_goods, 0, 250,weight(40)|abundance(90),imodbits_none],
 ["raw_silk","Raw Silk", [("raw_silk_bundle",0)], itp_merchandise|itp_type_goods, 0, 600,weight(30)|abundance(90),imodbits_none],
 ["raw_dyes","Dyes", [("dyes",0)], itp_merchandise|itp_type_goods, 0, 200,weight(10)|abundance(90),imodbits_none],
 ["velvet","Velvet", [("velvet",0)], itp_merchandise|itp_type_goods, 0, 1025,weight(40)|abundance(30),imodbits_none],
 ["iron","Iron", [("iron",0)], itp_merchandise|itp_type_goods, 0,264,weight(60)|abundance(60),imodbits_none],
 ["tools","Tools", [("iron_hammer",0)], itp_merchandise|itp_type_goods, 0, 410,weight(50)|abundance(90),imodbits_none],
 ["raw_leather","Hides", [("leatherwork_inventory",0)], itp_merchandise|itp_type_goods, 0, 120,weight(40)|abundance(90),imodbits_none],
 ["leatherwork","Leatherwork", [("leatherwork_frame",0)], itp_merchandise|itp_type_goods, 0, 220,weight(40)|abundance(90),imodbits_none],
 ["raw_date_fruit","Date Fruit", [("date_inventory",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 120,weight(40)|food_quality(10)|max_ammo(10),imodbits_none],
 ["furs","Furs", [("fur_pack",0)], itp_merchandise|itp_type_goods, 0, 391,weight(40)|abundance(90),imodbits_none],
 ["wine","Wine", [("amphora_slim",0)], itp_merchandise|itp_type_goods|itp_consumable, 0, 220,weight(30)|abundance(60)|max_ammo(50),imodbits_none],
 ["ale","Ale", [("ale_barrel",0)], itp_merchandise|itp_type_goods|itp_consumable, 0, 120,weight(30)|abundance(70)|max_ammo(50),imodbits_none],
 ["smoked_fish","Smoked Fish", [("smoked_fish",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 65,weight(15)|abundance(110)|food_quality(50)|max_ammo(50),imodbits_none],
 ["cheese","Cheese", [("cheese_b",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 75,weight(6)|abundance(110)|food_quality(40)|max_ammo(30),imodbits_none],
 ["honey","Honey", [("honey_pot",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 220,weight(5)|abundance(110)|food_quality(40)|max_ammo(30),imodbits_none],
 ["sausages","Sausages", [("sausages",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 85,weight(10)|abundance(110)|food_quality(40)|max_ammo(40),imodbits_none],
 ["cabbages","Cabbages", [("cabbage",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 30,weight(15)|abundance(110)|food_quality(40)|max_ammo(50),imodbits_none],
 ["dried_meat","Dried Meat", [("smoked_meat",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 85,weight(15)|abundance(100)|food_quality(70)|max_ammo(50),imodbits_none],
 ["apples","Fruit", [("apple_basket",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 44,weight(20)|abundance(110)|food_quality(40)|max_ammo(50),imodbits_none],
 ["raw_grapes","Grapes", [("grapes_inventory",0)], itp_merchandise|itp_consumable|itp_type_goods, 0, 75,weight(40)|abundance(90)|food_quality(10)|max_ammo(10),imodbits_none], #x2 for wine
 ["raw_olives","Olives", [("olive_inventory",0)], itp_merchandise|itp_consumable|itp_type_goods, 0, 100,weight(40)|abundance(90)|food_quality(10)|max_ammo(10),imodbits_none], #x3 for oil
 ["grain","Grain", [("wheat_sack",0)], itp_merchandise|itp_type_goods|itp_consumable, 0, 30,weight(30)|abundance(110)|food_quality(40)|max_ammo(50),imodbits_none],
 ["cattle_meat","Beef", [("raw_meat",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 80,weight(20)|abundance(100)|food_quality(80)|max_ammo(50),imodbits_none],
 ["bread","Bread", [("bread_a",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 50,weight(30)|abundance(110)|food_quality(40)|max_ammo(50),imodbits_none],
 ["chicken","Chicken", [("chicken",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 95,weight(10)|abundance(110)|food_quality(40)|max_ammo(50),imodbits_none],
 ["pork","Pork", [("pork",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 75,weight(15)|abundance(100)|food_quality(70)|max_ammo(50),imodbits_none],
 ["butter","Butter", [("butter_pot",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 150,weight(6)|abundance(110)|food_quality(40)|max_ammo(30),imodbits_none],
#************************************************************************************************
# ITEMS before this point are hardcoded into item_codes.h and their order should not be changed!
#************************************************************************************************

# Quest Items
 ["siege_supply","Supplies", [("ale_barrel",0)], itp_type_goods, 0, 96,weight(40)|abundance(70),imodbits_none],
 ["quest_wine","Wine", [("amphora_slim",0)], itp_type_goods, 0, 46,weight(40)|abundance(60)|max_ammo(50),imodbits_none],
 ["quest_ale","Ale", [("ale_barrel",0)], itp_type_goods, 0, 31,weight(40)|abundance(70)|max_ammo(50),imodbits_none],

# Tutorial Items
 ["tutorial_sword", "Sword", [("long_sword",0),("scab_longsw_a", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 0 , weight(1.5)|difficulty(0)|spd_rtng(100) | weapon_length(102)|swing_damage(18 , cut) | thrust_damage(15 ,  pierce),imodbits_sword ],
 ["tutorial_axe", "Axe", [("iron_ax",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 0 , weight(4)|difficulty(0)|spd_rtng(91) | weapon_length(108)|swing_damage(19 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
 ["tutorial_spear", "Spear", [("spear",0)], itp_type_polearm| itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_no_blur, itc_spear, 0 , weight(4.5)|difficulty(0)|spd_rtng(80) | weapon_length(158)|swing_damage(0 , cut) | thrust_damage(19 ,  pierce),imodbits_polearm ],
 ["tutorial_club", "Club", [("club",0)], itp_type_one_handed_wpn| itp_primary|itp_wooden_parry|itp_wooden_attack, itc_scimitar, 0 , weight(2.5)|difficulty(0)|spd_rtng(95) | weapon_length(95)|swing_damage(11 , blunt) | thrust_damage(0 ,  pierce),imodbits_none ],
 ["tutorial_battle_axe", "Battle Axe", [("battle_ax",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 0 , weight(5)|difficulty(0)|spd_rtng(88) | weapon_length(108)|swing_damage(27 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
 ["tutorial_arrows","Arrows", [("arrow",0),("flying_missile",ixmesh_flying_ammo),("quiver", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back, 0,weight(3)|abundance(160)|weapon_length(95)|thrust_damage(0,pierce)|max_ammo(20),imodbits_missile],
 ["tutorial_bolts","Bolts", [("bolt",0),("flying_missile",ixmesh_flying_ammo),("bolt_bag", ixmesh_carry),("bolt_bag_b", ixmesh_carry|imodbit_large_bag)], itp_type_bolts, itcf_carry_quiver_right_vertical, 0,weight(2.25)|abundance(90)|weapon_length(63)|thrust_damage(0,pierce)|max_ammo(18),imodbits_missile],
 ["tutorial_short_bow", "Short Bow", [("short_bow",0),("short_bow_carry",ixmesh_carry)], itp_type_bow |itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bow_back, 0 , weight(1)|difficulty(0)|spd_rtng(98) | shoot_speed(49) | thrust_damage(12 ,  pierce  ),imodbits_bow ],
 ["tutorial_crossbow", "Crossbow", [("crossbow_a",0)], itp_type_crossbow |itp_primary|itp_two_handed|itp_cant_reload_on_horseback ,itcf_shoot_crossbow|itcf_carry_crossbow_back, 0 , weight(3)|difficulty(0)|spd_rtng(42)|  shoot_speed(68) | thrust_damage(32,pierce)|max_ammo(1),imodbits_crossbow ],
 ["tutorial_throwing_daggers", "Throwing Daggers", [("throwing_dagger",0)], itp_type_thrown |itp_primary ,itcf_throw_knife, 0 , weight(3.5)|difficulty(0)|spd_rtng(102) | shoot_speed(25) | thrust_damage(16 ,  cut)|max_ammo(14)|weapon_length(0),imodbits_missile ],
 ["tutorial_saddle_horse", "Saddle Horse", [("saddle_horse",0)], itp_type_horse, 0, 0,abundance(90)|body_armor(3)|difficulty(0)|horse_speed(40)|horse_maneuver(38)|horse_charge(8),imodbits_horse_basic],
 ["tutorial_shield", "Kite Shield", [("shield_kite_a",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|weapon_length(150),imodbits_shield ],
 ["tutorial_staff_no_attack","Staff", [("wooden_staff",0)],itp_type_polearm|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack,itc_parry_polearm|itcf_carry_sword_back,9, weight(3.5)|spd_rtng(120) | weapon_length(115)|swing_damage(0,blunt) | thrust_damage(0,blunt),imodbits_none],
 ["tutorial_staff","Staff", [("wooden_staff",0)],itp_type_polearm|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack,itc_staff|itcf_carry_sword_back,9, weight(3.5)|spd_rtng(120) | weapon_length(115)|swing_damage(16,blunt) | thrust_damage(16,blunt),imodbits_none],
 ["practice_spear","Practice Spear",[("arena_lance",0)], itp_type_polearm|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_no_blur, itc_spear|itcf_carry_spear, 90 , weight(2.5)|spd_rtng(96) | weapon_length(150)|swing_damage(20 , blunt) | thrust_damage(25 ,  blunt),imodbits_polearm ],

###################
# MOUNTS - Slot 8 #
###################
# Keep sumpter_horse in front!

# Unarmored
# Editado os nomes
 ["sumpter_horse","Dappled Beige Horse", [("sumpter_horse",0)], itp_merchandise|itp_type_horse, 0, 134,abundance(90)|hit_points(100)|body_armor(14)|difficulty(1)|horse_speed(37)|horse_maneuver(39)|horse_charge(9)|horse_scale(100),imodbits_horse_simple],
 ["saddle_horse","Palamino Horse", [("saddle_horse",0)], itp_merchandise|itp_type_horse, 0, 240,abundance(90)|hit_points(100)|body_armor(8)|difficulty(1)|horse_speed(45)|horse_maneuver(44)|horse_charge(10)|horse_scale(104),imodbits_horse_basic],
 ["nord_pony","Nord Pony", [("horse_c",0)], itp_merchandise|itp_type_horse, 0, 172,abundance(80)|hit_points(120)|body_armor(10)|difficulty(1)|horse_speed(42)|horse_maneuver(44)|horse_charge(12)|horse_scale(98),imodbits_horse_basic, [], [fac_kingdom_4]],
 ["steppe_horse","Steppe Horse", [("steppe_horse",0)], itp_merchandise|itp_type_horse, 0, 192,abundance(80)|hit_points(120)|body_armor(10)|difficulty(2)|horse_speed(40)|horse_maneuver(51)|horse_charge(8)|horse_scale(98),imodbits_horse_basic, [], [fac_kingdom_2, fac_kingdom_3]],
 ["arabian_horse_a","Desert Horse", [("arabian_horse_a",0)], itp_merchandise|itp_type_horse, 0, 550,abundance(80)|hit_points(110)|body_armor(10)|difficulty(2)|horse_speed(42)|horse_maneuver(50)|horse_charge(12)|horse_scale(100),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_3, fac_kingdom_6]],
 ["courser","Courser", [("courser",0)], itp_merchandise|itp_type_horse, 0, 600,abundance(70)|body_armor(12)|hit_points(110)|difficulty(2)|horse_speed(50)|horse_maneuver(44)|horse_charge(12)|horse_scale(106),imodbits_horse_basic|imodbit_champion],
 ["arabian_horse_b","Mohaine Horse", [("arabian_horse_b",0)], itp_merchandise|itp_type_horse, 0, 700,abundance(80)|hit_points(120)|body_armor(10)|difficulty(3)|horse_speed(43)|horse_maneuver(54)|horse_charge(16)|horse_scale(100),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_6]],
 ["hunter","Hunter Horse", [("hunting_horse",0)], itp_merchandise|itp_type_horse, 0, 810,abundance(60)|hit_points(160)|body_armor(18)|difficulty(3)|horse_speed(43)|horse_maneuver(44)|horse_charge(24)|horse_scale(108),imodbits_horse_basic|imodbit_champion],
# Armored
 ["warhorse","War Horse", [("warhorse_chain",0),("warhorse_heavy",imodbit_heavy)], itp_merchandise|itp_type_horse, 0, 1224,abundance(50)|hit_points(165)|body_armor(40)|difficulty(4)|horse_speed(40)|horse_maneuver(41)|horse_charge(28)|horse_scale(110),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_4, fac_kingdom_5, fac_kingdom_6]],
 ["warhorse_steppe","Steppe War Horse", [("warhorse_steppe",0)], itp_merchandise|itp_type_horse, 0, 1400,abundance(45)|hit_points(150)|body_armor(40)|difficulty(4)|horse_speed(40)|horse_maneuver(50)|horse_charge(28)|horse_scale(112),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_2, fac_kingdom_3] ],
 ["warhorse_sarranid","Mohaine Charger", [("warhorse_sarranid",0)], itp_merchandise|itp_type_horse, 0, 1811,abundance(40)|hit_points(165)|body_armor(58)|difficulty(4)|horse_speed(40)|horse_maneuver(44)|horse_charge(32)|horse_scale(112),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_6]],
 ["charger","Gilead Charger", [("charger_new",0)], itp_merchandise|itp_type_horse, 0, 1811,abundance(40)|hit_points(165)|body_armor(58)|difficulty(4)|horse_speed(40)|horse_maneuver(44)|horse_charge(32)|horse_scale(112),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_1]],
 ["charger_black","Black Charger", [("charger_black",0)], itp_merchandise|itp_type_horse, 0, 1811,abundance(20)|hit_points(165)|body_armor(58)|difficulty(4)|horse_speed(40)|horse_maneuver(44)|horse_charge(32)|horse_scale(112),imodbits_horse_basic, [], [fac_kingdom_5]],
 ["charger_plate","Northern Charger", [("charger_plate",0)], itp_merchandise|itp_type_horse, 0, 1811,abundance(20)|hit_points(165)|body_armor(58)|difficulty(4)|horse_speed(40)|horse_maneuver(44)|horse_charge(32)|horse_scale(112),imodbits_horse_simple, [], [fac_kingdom_4]],

##########################
# AMMUNITION - Slots 0-3 #
##########################
# Keep arrows in front!

# Arrows
 ["arrows","Arrows", [("arrow",0),("flying_missile",ixmesh_flying_ammo),("quiver", ixmesh_carry)], itp_type_arrows|itp_merchandise|itp_default_ammo, itcf_carry_quiver_back, 
 72,weight(3)|abundance(160)|weapon_length(95)|thrust_damage(1,pierce)|max_ammo(30),imodbits_missile, [], [fac_kingdom_1, fac_kingdom_4, fac_kingdom_5]],
 ["arrows_cav","Arrows", [("arrow",0),("flying_missile",ixmesh_flying_ammo),("quiver", ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_back_right, 
 72,weight(3)|abundance(160)|weapon_length(95)|thrust_damage(1,pierce)|max_ammo(30),imodbits_missile, [], [fac_kingdom_2, fac_kingdom_3, fac_kingdom_6]],
 ["barbed_arrows","Barbed Arrows", [("barbed_arrow",0),("flying_missile",ixmesh_flying_ammo),("quiver_d", ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_back_right, 
 124,weight(3)|abundance(70)|weapon_length(95)|thrust_damage(2,cut)|max_ammo(30),imodbits_missile, [], [fac_kingdom_2, fac_kingdom_3, fac_kingdom_6]],
 ["khergit_arrows","Khergit Arrows", [("arrow_b",0),("flying_missile",ixmesh_flying_ammo),("quiver_b", ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_back_right, 
 410,weight(3.5)|abundance(30)|weapon_length(95)|thrust_damage(3,cut)|max_ammo(30),imodbits_missile, [], [fac_kingdom_3]],
 ["steel_arrows","Steel Arrows", [("arrow_b",0),("flying_missile",ixmesh_flying_ammo),("arena_quiver", ixmesh_carry)], itp_type_arrows|itp_merchandise|itp_default_ammo, itcf_carry_quiver_back, 
 240,weight(3)|abundance(160)|weapon_length(95)|thrust_damage(2,pierce)|max_ammo(30),imodbits_missile, [], [fac_kingdom_1, fac_kingdom_5]],
 ["bodkin_arrows","Bodkin Arrows", [("piercing_arrow",0),("flying_missile",ixmesh_flying_ammo),("quiver_c", ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_back, 
 350,weight(3)|abundance(50)|weapon_length(91)|thrust_damage(3,pierce)|max_ammo(30),imodbits_missile, [], [fac_kingdom_1, fac_kingdom_4]],
 ["bodkin_arrows_cav","Bodkin Arrows", [("piercing_arrow",0),("flying_missile",ixmesh_flying_ammo),("quiver_c", ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_back_right, 
 350,weight(3)|abundance(50)|weapon_length(91)|thrust_damage(3,pierce)|max_ammo(30),imodbits_missile, [], [fac_kingdom_2]],
# Bolts
 ["bolts","Bolts", [("bolt",0),("flying_missile",ixmesh_flying_ammo),("bolt_bag", ixmesh_carry)], itp_type_bolts|itp_merchandise|itp_default_ammo|itp_can_penetrate_shield, itcf_carry_quiver_right_vertical, 
 64,weight(2.25)|abundance(90)|weapon_length(63)|thrust_damage(1,pierce)|max_ammo(30),imodbits_missile],
 ["hunting_bolts","Hunting Bolts", [("bolt",0),("flying_missile",ixmesh_flying_ammo),("bolt_bag_c", ixmesh_carry)], itp_type_bolts|itp_merchandise|itp_can_penetrate_shield, itcf_carry_quiver_right_vertical, 
 120,weight(2.5)|abundance(20)|weapon_length(63)|thrust_damage(2,cut)|max_ammo(30),imodbits_missile, [], [fac_kingdom_5]],
 ["steel_bolts","Steel Bolts", [("bolt",0),("flying_missile",ixmesh_flying_ammo),("bolt_bag_b", ixmesh_carry)], itp_type_bolts|itp_merchandise|itp_can_penetrate_shield, itcf_carry_quiver_right_vertical, 
 210,weight(2.5)|abundance(20)|weapon_length(63)|thrust_damage(2,pierce)|max_ammo(30),imodbits_missile, [], [fac_kingdom_5]],
# Bullets
 ["cartridges","Cartridges", [("cartridge_a",0)], itp_type_bullets|itp_merchandise|itp_can_penetrate_shield|itp_default_ammo, 0, 
 41,weight(2.25)|abundance(90)|weapon_length(3)|thrust_damage(1,pierce)|max_ammo(50),imodbit_large_bag, [], [fac_no_faction]],

#####################
# ARMOR - Slots 4-7 #
#####################
# Keep leather_gloves in front!

###################
# Gloves - Slot 7 #
###################
["leather_gloves","Leather Gloves", [("leather_gloves_L",0)], itp_merchandise|itp_type_hand_armor,0,
 90, weight(0.25)|abundance(120)|body_armor(2)|difficulty(0),imodbits_cloth],
["mail_mittens","Mail Mittens", [("mail_mittens_L",0)], itp_merchandise|itp_type_hand_armor,0,
 350, weight(0.5)|abundance(100)|body_armor(4)|difficulty(0),imodbits_armor],
["scale_gauntlets","Scale Gauntlets", [("scale_gauntlets_b_L",0)], itp_merchandise|itp_type_hand_armor,0,
 710, weight(0.75)|abundance(100)|body_armor(5)|difficulty(0),imodbits_armor, [], [fac_kingdom_4, fac_kingdom_6]],
["lamellar_gauntlets","Lamellar Gauntlets", [("scale_gauntlets_a_L",0)], itp_merchandise|itp_type_hand_armor,0,
 910, weight(0.9)|abundance(100)|body_armor(6)|difficulty(0),imodbits_armor, [], [fac_kingdom_2, fac_kingdom_3]],
["gauntlets","Gauntlets", [("gauntlets_L",0),("gauntlets_L",imodbit_reinforced)], itp_merchandise|itp_type_hand_armor,0,
 1040, weight(1.0)|abundance(100)|body_armor(7)|difficulty(0),imodbits_armor, [], [fac_kingdom_1, fac_kingdom_5]],

#####################
# Footwear - Slot 6 #
#####################

# Civilian Shoes & Boots
["wrapping_boots", "Wrapping Boots", [("wrapping_boots_a",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
 3 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(3)|difficulty(0) ,imodbits_clothes ],
["woolen_hose", "Woolen Hose", [("woolen_hose_a",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
 6 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(4)|difficulty(0) ,imodbits_clothes, [], [fac_kingdom_1, fac_kingdom_4, fac_kingdom_5] ],
["blue_hose", "Blue Hose", [("blue_hose_a",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
 11 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(5)|difficulty(0) ,imodbits_clothes, [], [fac_kingdom_1, fac_kingdom_4, fac_kingdom_5] ],
["sarranid_boots_a", "Sarranid Shoes", [("sarranid_shoes",0)], itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
 30 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(8)|difficulty(0) ,imodbits_clothes, [], [fac_kingdom_6] ],
["hunter_boots", "Hunter Boots", [("hunter_boots_a",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature,0,
 19 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(9)|difficulty(0) ,imodbits_clothes, [], [fac_kingdom_1, fac_kingdom_4, fac_kingdom_2] ],
["hide_boots", "Hide Boots", [("hide_boots_a",0)], itp_merchandise| itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 34 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["ankle_boots", "Ankle Boots", [("ankle_boots_a_new",0)], itp_merchandise| itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 75 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(12)|difficulty(0) ,imodbits_clothes, [], [fac_kingdom_1] ],
["nomad_boots", "Nomad Boots", [("nomad_boots_a",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 90 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(14)|difficulty(0) ,imodbits_clothes, [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5] ],
["light_leather_boots",  "Light Leather Boots", [("light_leather_boots",0)], itp_type_foot_armor |itp_merchandise| itp_attach_armature,0,
 91 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(15)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_1, fac_kingdom_5, fac_kingdom_6] ],
["sarranid_boots_b", "Sarranid Leather Boots", [("sarranid_boots",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
 120 , weight(2)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(16)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_6] ],
["leather_boots", "Leather Boots", [("leather_boots_a",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 174 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(16)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_1, fac_kingdom_4, fac_kingdom_5] ],
["khergit_leather_boots", "Khergit Leather Boots", [("khergit_leather_boots",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
 120 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(18)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_3] ],
# Armored Boots
["khergit_guard_boots",  "Khergit Guard Boots", [("lamellar_boots_a",0)], itp_type_foot_armor | itp_merchandise | itp_attach_armature,0,
 254 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(20)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_3] ],
["sarranid_boots_c", "Sarranid Mail Boots", [("sarranid_mail_chausses",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
 280 , weight(3)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(20)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_6] ],
["splinted_leather_greaves", "Splinted Leather Greaves", [("leather_greaves_a",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature,0,
 310 , weight(2)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(21)|difficulty(0) ,imodbits_armor ],
["mail_chausses", "Mail Chausses", [("mail_chausses_a",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature  ,0,
 530 , weight(3)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(24)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_4, fac_kingdom_5] ],
["splinted_greaves", "Splinted Greaves", [("splinted_greaves_a",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature,0,
 853 , weight(2.75)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(28)|difficulty(7) ,imodbits_armor, [], [fac_kingdom_3, fac_kingdom_6] ],
["sarranid_boots_d", "Sarranid Plated Boots", [("sarranid_camel_boots",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
 920 , weight(3)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_6] ],
["mail_boots", "Mail Boots", [("mail_boots_a",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature  ,0,
 1250 , weight(3)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(31)|difficulty(8) ,imodbits_armor, [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_4, fac_kingdom_5, fac_kingdom_6] ],
["iron_greaves", "Iron Greaves", [("iron_greaves_a",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature,0,
 1770 , weight(3.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(33)|difficulty(9) ,imodbits_armor ],
["plate_boots", "Plate Boots", [("plate_boots",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature,0,
 1770 , weight(3.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(33)|difficulty(9) ,imodbits_plate, [], [fac_kingdom_1, fac_kingdom_5] ], 

#####################
# Bodywear - Slot 5 #
#####################

# Womens' Clothes
["dress", "Dress", [("dress",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 6 , weight(1)|abundance(50)|head_armor(0)|body_armor(6)|leg_armor(2)|difficulty(0) ,imodbits_clothes, [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5] ],
["blue_dress", "Blue Dress", [("blue_dress_new",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 6 , weight(1)|abundance(50)|head_armor(0)|body_armor(6)|leg_armor(2)|difficulty(0) ,imodbits_clothes, [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5] ],
["peasant_dress", "Peasant Dress", [("peasant_dress_b_new",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 6 , weight(1)|abundance(50)|head_armor(0)|body_armor(6)|leg_armor(2)|difficulty(0) ,imodbits_clothes, [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5] ], 
["woolen_dress", "Woolen Dress", [("woolen_dress",0)], itp_merchandise| itp_type_body_armor|itp_civilian  |itp_covers_legs ,0, 10 , weight(1.75)|abundance(50)|head_armor(0)|body_armor(8)|leg_armor(2)|difficulty(0) ,imodbits_clothes, [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5] ],
["sarranid_common_dress", "Sarranid Dress", [("sarranid_common_dress",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 33 , weight(3)|abundance(50)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_clothes, [], [fac_kingdom_6]],
["sarranid_common_dress_b", "Sarranid Dress", [("sarranid_common_dress_b",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 33 , weight(3)|abundance(50)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_clothes, [], [fac_kingdom_6]],

# Noble Ladies' Dresses
["court_dress", "Court Dress", [("court_dress",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 348 , weight(4)|abundance(10)|head_armor(0)|body_armor(14)|leg_armor(4)|difficulty(0) ,imodbits_none, [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_4, fac_kingdom_5] ],
["lady_dress_ruby", "Lady Dress", [("lady_dress_r",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(10)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_none, [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_4, fac_kingdom_5]],
["lady_dress_green", "Lady Dress", [("lady_dress_g",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(10)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_none, [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_4, fac_kingdom_5]],
["lady_dress_blue", "Lady Dress", [("lady_dress_b",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(10)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_none, [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_4, fac_kingdom_5]],
["red_dress", "Red Dress", [("red_dress",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(10)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_none, [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_4, fac_kingdom_5]],
["brown_dress", "Brown Dress", [("brown_dress",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(10)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_none, [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_4, fac_kingdom_5]],
["green_dress", "Green Dress", [("green_dress",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(10)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_none, [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_4, fac_kingdom_5]],
["khergit_lady_dress", "Khergit Lady Dress", [("khergit_lady_dress",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(20)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_none, [], [fac_kingdom_3]],
["khergit_lady_dress_b", "Khergit Leather Lady Dress", [("khergit_lady_dress_b",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(20)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_none, [], [fac_kingdom_3]],
["sarranid_lady_dress", "Sarranid Lady Dress", [("sarranid_lady_dress",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(20)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_none, [], [fac_kingdom_6]],
["sarranid_lady_dress_b", "Sarranid Lady Dress", [("sarranid_lady_dress_b",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(20)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_none, [], [fac_kingdom_6]],

# Common Clothes
["shirt", "Shirt", [("shirt",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 3 , weight(1)|abundance(50)|head_armor(0)|body_armor(5)|leg_armor(0)|difficulty(0) ,imodbits_clothes ],
["tunic_with_green_cape", "Tunic with Green Cape", [("peasant_man_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 6 , weight(1)|abundance(50)|head_armor(0)|body_armor(6)|leg_armor(2)|difficulty(0) ,imodbits_clothes ], 
["linen_tunic", "Linen Tunic", [("shirt_a",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 6 , weight(1)|abundance(50)|head_armor(0)|body_armor(6)|leg_armor(1)|difficulty(0) ,imodbits_clothes ],
["short_tunic", "Red Tunic", [("rich_tunic_a",0)], itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 10 , weight(1)|abundance(50)|head_armor(0)|body_armor(7)|leg_armor(1)|difficulty(0) ,imodbits_clothes ],
["red_shirt", "Red Shirt", [("rich_tunic_a",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 10 , weight(1)|abundance(50)|head_armor(0)|body_armor(7)|leg_armor(1)|difficulty(0) ,imodbits_clothes ],
["red_tunic", "Red Tunic", [("arena_tunicR_new",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 10 , weight(1)|abundance(50)|head_armor(0)|body_armor(7)|leg_armor(1)|difficulty(0) ,imodbits_clothes ],
["green_tunic", "Green Tunic", [("arena_tunicG_new",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 10 , weight(1)|abundance(50)|head_armor(0)|body_armor(7)|leg_armor(1)|difficulty(0) ,imodbits_clothes ],
["blue_tunic", "Blue Tunic", [("arena_tunicB_new",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 10 , weight(1)|abundance(50)|head_armor(0)|body_armor(7)|leg_armor(1)|difficulty(0) ,imodbits_clothes ],
["pelt_coat", "Pelt Coat", [("thick_coat_a",0)],  itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0, 14, weight(2)|abundance(50)|head_armor(0)|body_armor(9)|leg_armor(1)|difficulty(0) ,imodbits_clothes ],
["robe", "Robe", [("robe",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0, 31 , weight(1.5)|abundance(50)|head_armor(0)|body_armor(8)|leg_armor(6)|difficulty(0) ,imodbits_clothes ],
["sarranid_cloth_robe", "Worn Robe", [("sar_robe",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 33 , weight(1)|abundance(50)|head_armor(0)|body_armor(9)|leg_armor(9)|difficulty(0) ,imodbits_clothes, [], [fac_kingdom_6] ],
["sarranid_cloth_robe_b", "Worn Robe", [("sar_robe_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 33 , weight(1)|abundance(50)|head_armor(0)|body_armor(9)|leg_armor(9)|difficulty(0) ,imodbits_clothes, [], [fac_kingdom_6] ],
["coarse_tunic", "Tunic with vest", [("coarse_tunic_a",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 47 , weight(2)|abundance(50)|head_armor(0)|body_armor(11)|leg_armor(6)|difficulty(0) ,imodbits_clothes ],
["leather_apron", "Leather Apron", [("leather_apron",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 61 , weight(3)|abundance(50)|head_armor(0)|body_armor(12)|leg_armor(7)|difficulty(0) ,imodbits_clothes ],

# Fancy Clothes
["leather_jacket", "Leather Jacket", [("leather_jacket_new",0)], itp_merchandise| itp_type_body_armor | itp_covers_legs  |itp_civilian ,0, 50 , weight(3)|abundance(50)|head_armor(0)|body_armor(20)|leg_armor(0)|difficulty(0) ,imodbits_clothes ],
["fur_coat", "Fur Coat", [("fur_coat",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0, 117 , weight(6)|abundance(50)|head_armor(0)|body_armor(13)|leg_armor(6)|difficulty(0) ,imodbits_clothes ],
["tabard", "Tabard", [("tabard_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0, 107 , weight(3)|abundance(50)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_clothes ],
["courtly_outfit", "Courtly Outfit", [("nobleman_outf",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 248 , weight(4)|abundance(20)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_none ],
["nobleman_outfit", "Nobleman Outfit", [("nobleman_outfit_b_new",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 288 , weight(4)|abundance(20)|head_armor(0)|body_armor(15)|leg_armor(12)|difficulty(0) ,imodbits_none ], 
["rich_outfit", "Rich Outfit", [("merchant_outf",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 348 , weight(4)|abundance(20)|head_armor(0)|body_armor(16)|leg_armor(4)|difficulty(0) ,imodbits_none ],

# Cheap Armor
["nomad_armor", "Nomad Armor", [("nomad_armor_new",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs   ,0, 25 , weight(2)|abundance(50)|head_armor(0)|body_armor(24)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["khergit_armor", "Khergit Armor", [("khergit_armor_new",0)], itp_merchandise| itp_type_body_armor | itp_covers_legs ,0, 38 , weight(2)|abundance(50)|head_armor(0)|body_armor(24)|leg_armor(0)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_3] ],
["rawhide_coat", "Rawhide Coat", [("coat_of_plates_b",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 12 , weight(5)|abundance(50)|head_armor(0)|body_armor(10)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

# Light Armor
["leather_armor", "Leather Armor", [("tattered_leather_armor_a",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs  ,0,
 65 , weight(7)|abundance(100)|head_armor(0)|body_armor(18)|leg_armor(0)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_1, fac_kingdom_5] ],
["skirmisher_armor", "Skirmisher Armor", [("skirmisher_armor",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 74 , weight(3)|abundance(200)|head_armor(0)|body_armor(15)|leg_armor(9)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_6] ],
["leather_vest", "Leather Vest", [("leather_vest_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 146 , weight(4)|abundance(100)|head_armor(0)|body_armor(15)|leg_armor(7)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_2, fac_kingdom_3, fac_kingdom_4] ],
["steppe_armor", "Steppe Armor", [("lamellar_leather",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 195 , weight(5)|abundance(100)|head_armor(0)|body_armor(16)|leg_armor(8)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_2, fac_kingdom_3, fac_kingdom_6] ],
["archers_vest", "Archer's Padded Vest", [("archers_vest",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0,
 260 , weight(6)|abundance(200)|head_armor(0)|body_armor(23)|leg_armor(12)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_6] ],
["gambeson", "Gambeson", [("white_gambeson",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 260 , weight(5)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(5)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_1, fac_kingdom_4] ],
["blue_gambeson", "Blue Gambeson", [("blue_gambeson",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 270 , weight(5)|abundance(100)|head_armor(0)|body_armor(21)|leg_armor(5)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_4, fac_kingdom_5] ],
["red_gambeson", "Red Gambeson", [("red_gambeson_a",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 275 , weight(5)|abundance(100)|head_armor(0)|body_armor(21)|leg_armor(5)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_1, fac_kingdom_5] ],
["padded_cloth", "Aketon", [("padded_cloth_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 297 , weight(11)|abundance(100)|head_armor(0)|body_armor(22)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_1, fac_kingdom_4] ],
["aketon_green", "Padded Cloth", [("padded_cloth_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 297 , weight(11)|abundance(100)|head_armor(0)|body_armor(22)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_1, fac_kingdom_5] ],
["leather_jerkin", "Leather Jerkin", [("ragged_leather_jerkin",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 321 , weight(6)|abundance(100)|head_armor(0)|body_armor(23)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["light_leather", "Light Leather", [("light_leather",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0,
 352 , weight(5)|abundance(100)|head_armor(0)|body_armor(26)|leg_armor(7)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_1, fac_kingdom_4, fac_kingdom_5, fac_kingdom_6] ],
["nomad_vest", "Nomad Vest", [("nomad_vest_new",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 360 , weight(7)|abundance(50)|head_armor(0)|body_armor(22)|leg_armor(8)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_2, fac_kingdom_3, fac_kingdom_4] ],
["ragged_outfit", "Ragged Outfit", [("ragged_outfit_a_new",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 390 , weight(7)|abundance(100)|head_armor(0)|body_armor(23)|leg_armor(9)|difficulty(0) ,imodbit_tattered | imodbit_sturdy | imodbit_thick | imodbit_hardened ],
["padded_leather", "Padded Leather", [("leather_armor_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian,0,
 454 , weight(12)|abundance(100)|head_armor(0)|body_armor(27)|leg_armor(10)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_1, fac_kingdom_4, fac_kingdom_5] ],
["tribal_warrior_outfit", "Tribal Warrior Outfit", [("tribal_warrior_outfit_a_new",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 520 , weight(14)|abundance(100)|head_armor(0)|body_armor(30)|leg_armor(10)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_2, fac_kingdom_3, fac_kingdom_4] ],
["nomad_robe", "Nomad Robe", [("nomad_robe_a",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs |itp_civilian,0,
 610 , weight(15)|abundance(100)|head_armor(0)|body_armor(32)|leg_armor(10)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_2, fac_kingdom_3, fac_kingdom_6] ],
["sarranid_leather_armor", "Sarranid Leather Armor", [("sarranid_leather_armor",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 650 , weight(9)|abundance(200)|head_armor(0)|body_armor(32)|leg_armor(12)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_6] ],

# Medium Armor
["mail_with_tunic_red", "Mail with Tunic", [("arena_armorR_new",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 650 , weight(16)|abundance(100)|head_armor(0)|body_armor(39)|leg_armor(8), imodbits_armor, [], [fac_kingdom_1, fac_kingdom_4, fac_kingdom_5] ],
["mail_with_tunic_green", "Mail with Tunic", [("arena_armorG_new",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 650 , weight(16)|abundance(100)|head_armor(0)|body_armor(39)|leg_armor(8), imodbits_armor, [], [fac_kingdom_1, fac_kingdom_4, fac_kingdom_5] ],
["mail_with_tunic_blue", "Mail with Tunic", [("arena_armorB_new",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 650 , weight(16)|abundance(100)|head_armor(0)|body_armor(39)|leg_armor(8), imodbits_armor, [], [fac_kingdom_1, fac_kingdom_4, fac_kingdom_5] ],
["studded_leather_coat", "Studded Leather Coat", [("leather_armor_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 690 , weight(14)|abundance(100)|head_armor(0)|body_armor(36)|leg_armor(10)|difficulty(7) ,imodbits_armor ],
["byrnie", "Byrnie", [("byrnie_a_new",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 795 , weight(17)|abundance(100)|head_armor(0)|body_armor(39)|leg_armor(6)|difficulty(7) ,imodbits_armor, [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_4] ],
["haubergeon", "Haubergeon", [("haubergeon_c",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 863 , weight(18)|abundance(100)|head_armor(0)|body_armor(41)|leg_armor(6)|difficulty(6) ,imodbits_armor, [], [fac_kingdom_1, fac_kingdom_4, fac_kingdom_5] ],
["lamellar_vest", "Lamellar Vest", [("lamellar_vest_a",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 970 , weight(18)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_cloth, [], [fac_kingdom_2] ],
["lamellar_vest_khergit", "Lamellar Vest", [("lamellar_vest_b",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 970 , weight(18)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_cloth, [], [fac_kingdom_3] ],
["sarranid_cavalry_robe", "Cavalry Robe", [("arabian_armor_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 990 , weight(15)|abundance(150)|head_armor(0)|body_armor(36)|leg_armor(8)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_6] ],
["mail_shirt", "Mail Shirt", [("mail_shirt_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 1040 , weight(19)|abundance(100)|head_armor(0)|body_armor(37)|leg_armor(12)|difficulty(7) ,imodbits_armor, [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_4, fac_kingdom_5] ],
["arabian_armor_b", "Sarranid Guard Armor", [("arabian_armor_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 1200 , weight(19)|abundance(100)|head_armor(0)|body_armor(38)|leg_armor(8)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_6] ],
["mail_hauberk", "Mail Hauberk", [("hauberk_a_new",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(12)|difficulty(7) ,imodbits_armor ],
["sarranid_mail_shirt", "Sarranid Mail Shirt", [("sarranian_mail_shirt",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 1400 , weight(19)|abundance(150)|head_armor(0)|body_armor(40)|leg_armor(14)|difficulty(7) ,imodbits_armor, [], [fac_kingdom_6] ],
 
["scale_armor", "Nord Scale Armor", [("lamellar_armor_e",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 1200 , weight(18)|abundance(100)|head_armor(0)|body_armor(42)|leg_armor(8)|difficulty(8) ,imodbits_armor, [], [fac_kingdom_4] ],
["light_mail_and_plate", "Light Mail and Plate", [("light_mail_and_plate",0)], itp_type_body_armor|itp_covers_legs,0,
 1532 , weight(16)|abundance(100)|head_armor(0)|body_armor(42)|leg_armor(14)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_1, fac_kingdom_4] ],
["brigandine_red", "Brigandine", [("brigandine_b",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs,0,
 1830 , weight(19)|abundance(100)|head_armor(0)|body_armor(46)|leg_armor(12)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_1, fac_kingdom_4, fac_kingdom_5] ],
["mail_and_plate", "Mail and Plate", [("mail_and_plate",0)], itp_type_body_armor|itp_covers_legs,0,
 2593 , weight(20)|abundance(100)|head_armor(0)|body_armor(50)|leg_armor(12)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_4] ],
 
# Medium-Heavy Armor
["mail_with_surcoat", "Mail with Surcoat", [("mail_long_surcoat_new",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 1544 , weight(22)|abundance(100)|head_armor(0)|body_armor(42)|leg_armor(14)|difficulty(7) ,imodbits_armor, [], [fac_kingdom_1] ],
["surcoat_over_mail", "Surcoat over Mail", [("surcoat_over_mail_new",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 1720 , weight(22)|abundance(100)|head_armor(0)|body_armor(43)|leg_armor(14)|difficulty(7) ,imodbits_armor , [], [fac_kingdom_5]],
 
# Heraldic Armor
["heraldic_mail_with_surcoat", "Heraldic Mail with Surcoat", [("heraldic_armor_new_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 3454 , weight(22)|abundance(100)|head_armor(0)|body_armor(49)|leg_armor(17)|difficulty(7) ,imodbits_armor,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_armor_a", ":agent_no", ":troop_no")])]],
["heraldic_mail_with_tunic", "Heraldic Mail with Tunic", [("heraldic_armor_new_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 3520 , weight(22)|abundance(100)|head_armor(0)|body_armor(50)|leg_armor(16)|difficulty(7) ,imodbits_armor,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_armor_b", ":agent_no", ":troop_no")])]],
["heraldic_mail_with_tunic_b", "Heraldic Mail with Tunic", [("heraldic_armor_new_c",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 3610 , weight(22)|abundance(100)|head_armor(0)|body_armor(50)|leg_armor(16)|difficulty(7) ,imodbits_armor,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_armor_c", ":agent_no", ":troop_no")])]],
["heraldic_mail_with_tabard", "Heraldic Mail with Tabard", [("heraldic_armor_new_d",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 3654 , weight(21)|abundance(100)|head_armor(0)|body_armor(51)|leg_armor(15)|difficulty(7) ,imodbits_armor,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_armor_d", ":agent_no", ":troop_no")])]],

# Heavy Armor 
["lamellar_armor", "Lamellar Armor", [("lamellar_armor_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 2410 , weight(23)|abundance(100)|head_armor(0)|body_armor(48)|leg_armor(13)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_2, fac_kingdom_3] ],
["banded_armor", "Banded Armor", [("banded_armor_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 2710 , weight(23)|abundance(100)|head_armor(0)|body_armor(49)|leg_armor(14)|difficulty(8) ,imodbits_armor, [], [fac_kingdom_2, fac_kingdom_4] ],
["mamluke_mail", "Mamluke Mail", [("sarranid_elite_cavalary",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0, 
 2900 , weight(24)|abundance(100)|head_armor(0)|body_armor(48)|leg_armor(16)|difficulty(8) ,imodbits_armor, [], [fac_kingdom_6] ],
["khergit_guard_armor", "Khergit Guard Armor", [("lamellar_armor_a",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0,
 3048 , weight(25)|abundance(100)|head_armor(0)|body_armor(50)|leg_armor(18)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_3] ],
["cuir_bouilli", "Cuir Bouilli", [("cuir_bouilli_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 3100 , weight(24)|abundance(100)|head_armor(0)|body_armor(50)|leg_armor(15)|difficulty(8) ,imodbits_armor, [], [fac_kingdom_2, fac_kingdom_4] ],

["khergit_elite_armor", "Khergit Elite Armor", [("lamellar_armor_d",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 3828 , weight(25)|abundance(100)|head_armor(0)|body_armor(52)|leg_armor(16)|difficulty(8) ,imodbits_armor, [], [fac_kingdom_3] ],
["vaegir_elite_armor", "Vaegir Elite Armor", [("lamellar_armor_c",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 3828 , weight(25)|abundance(100)|head_armor(0)|body_armor(52)|leg_armor(16)|difficulty(8) ,imodbits_armor, [], [fac_kingdom_2] ],
["sarranid_elite_armor", "Sarranid Elite Armor", [("tunic_armor_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian ,0,
 3828 , weight(25)|abundance(100)|head_armor(0)|body_armor(52)|leg_armor(16)|difficulty(8) ,imodbits_armor, [], [fac_kingdom_6] ],
["coat_of_plates", "Coat of Plates", [("coat_of_plates_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 3828 , weight(25)|abundance(100)|head_armor(0)|body_armor(52)|leg_armor(16)|difficulty(8) ,imodbits_armor, [], [fac_kingdom_5] ],
["coat_of_plates_red", "Coat of Plates", [("coat_of_plates_red",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 3828 , weight(25)|abundance(100)|head_armor(0)|body_armor(52)|leg_armor(16)|difficulty(8) ,imodbits_armor, [], [fac_kingdom_1] ],

["plate_armor", "Plate Armor", [("full_plate_armor",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 6553 , weight(27)|abundance(30)|head_armor(0)|body_armor(55)|leg_armor(17)|difficulty(9) ,imodbits_plate, [], [fac_kingdom_1, fac_kingdom_5] ],
 
#####################
# Headwear - Slot 4 #
#####################

# Womens' Headwear
["wimple_a", "Wimple", [("wimple_a_new",0)],itp_merchandise|itp_type_head_armor|itp_civilian|itp_fit_to_head,0,10, weight(0.5)|abundance(50)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_clothes],
["wimple_with_veil", "Wimple with Veil", [("wimple_b_new",0)],itp_merchandise|itp_type_head_armor|itp_civilian|itp_fit_to_head,0,10, weight(0.5)|abundance(50)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_clothes],
["sarranid_felt_head_cloth", "Head Cloth", [("common_tulbent",0)],  itp_type_head_armor  |itp_civilian |itp_attach_armature,0, 4 , weight(0.5)|abundance(50)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_clothes, [], [fac_kingdom_6] ],
["sarranid_felt_head_cloth_b", "Head Cloth", [("common_tulbent_b",0)],  itp_type_head_armor  |itp_civilian |itp_attach_armature,0, 4 , weight(0.5)|abundance(50)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_clothes, [], [fac_kingdom_6] ],
["woolen_hood", "Woolen Hood", [("woolen_hood",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 4 , weight(1)|abundance(50)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_clothes, [], [fac_kingdom_1, fac_kingdom_4, fac_kingdom_5] ],
["female_hood", "Lady's Hood", [("ladys_hood_new",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 9 , weight(1)|abundance(50)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_clothes, [], [fac_kingdom_1, fac_kingdom_4, fac_kingdom_5] ],

# Noble Ladies' Headwear
["turret_hat_ruby", "Turret Hat", [("turret_hat_r",0)], itp_merchandise|itp_type_head_armor  |itp_civilian|itp_fit_to_head ,0, 70 , weight(0.5)|abundance(20)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_none, [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_4, fac_kingdom_5] ], 
["turret_hat_blue", "Turret Hat", [("turret_hat_b",0)], itp_merchandise|itp_type_head_armor  |itp_civilian|itp_fit_to_head ,0, 80 , weight(0.5)|abundance(20)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_none, [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_4, fac_kingdom_5] ], 
["turret_hat_green", "Barbette", [("barbette_new",0)],itp_merchandise|itp_type_head_armor|itp_civilian|itp_fit_to_head,0,70, weight(0.5)|abundance(20)|head_armor(6)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_none, [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_4, fac_kingdom_5] ],
["court_hat", "Turret Hat", [("court_hat",0)], itp_merchandise|itp_type_head_armor  |itp_civilian|itp_fit_to_head ,0, 80 , weight(0.5)|abundance(20)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_none, [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_4, fac_kingdom_5] ], 
["sarranid_head_cloth", "Lady Head Cloth", [("tulbent",0)],  itp_merchandise|itp_type_head_armor | itp_doesnt_cover_hair |itp_civilian |itp_attach_armature,0, 10 , weight(0.5)|abundance(20)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_none, [], [fac_kingdom_6] ],
["sarranid_head_cloth_b", "Lady Head Cloth", [("tulbent_b",0)],  itp_merchandise|itp_type_head_armor | itp_doesnt_cover_hair |itp_civilian |itp_attach_armature,0, 10 , weight(0.5)|abundance(20)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_none, [], [fac_kingdom_6] ],
["khergit_lady_hat", "Khergit Lady Hat", [("khergit_lady_hat",0)],  itp_merchandise|itp_type_head_armor   |itp_civilian |itp_doesnt_cover_hair | itp_fit_to_head,0, 10 , weight(0.5)|abundance(20)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_none, [], [fac_kingdom_3] ],
["khergit_lady_hat_b", "Khergit Lady Leather Hat", [("khergit_lady_hat_b",0)], itp_merchandise|itp_type_head_armor  | itp_doesnt_cover_hair | itp_fit_to_head  |itp_civilian ,0, 10 , weight(0.5)|abundance(20)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_none, [], [fac_kingdom_3] ],

# Common Hats
["head_wrappings","Head Wrapping",[("head_wrapping",0)],itp_type_head_armor|itp_fit_to_head,0,16, weight(0.25)|abundance(0)|head_armor(3),imodbits_clothes, [], [fac_no_faction]],
["straw_hat", "Straw Hat", [("straw_hat_new",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,9, weight(1)|abundance(50)|head_armor(2)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_clothes],
["woolen_cap", "Woolen Cap", [("woolen_cap_new",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 2 , weight(1)|abundance(50)|head_armor(6)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_clothes ],
["felt_hat", "Felt Hat", [("felt_hat_a_new",0)], itp_merchandise| itp_type_head_armor |itp_civilian,0, 4 , weight(1)|abundance(50)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_clothes ],
["common_hood", "Hood", [("hood_new",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,9, weight(1)|abundance(50)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_clothes],
["hood_b", "Hood", [("hood_b",0)],itp_type_head_armor|itp_civilian,0,9, weight(1)|abundance(0)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_clothes, [], [fac_no_faction]],
["hood_c", "Hood", [("hood_c",0)],itp_type_head_armor|itp_civilian,0,9, weight(1)|abundance(0)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_clothes, [], [fac_no_faction]],
["hood_d", "Hood", [("hood_d",0)],itp_type_head_armor|itp_civilian,0,9, weight(1)|abundance(0)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_clothes, [], [fac_no_faction]],
["black_hood", "Black Hood", [("hood_black",0)], itp_type_head_armor|itp_merchandise   ,0, 193 , weight(2)|abundance(100)|head_armor(18)|body_armor(0)|leg_armor(0) ,imodbits_clothes ],

# Fancy Hats
["headcloth", "Headcloth", [("headcloth_a_new",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 1 , weight(0.5)|abundance(50)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_clothes, [], [fac_kingdom_3, fac_kingdom_6] ],
["fur_hat", "Fur Hat", [("fur_hat_a_new",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 4 , weight(0.5)|abundance(50)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_clothes, [], [fac_kingdom_2, fac_kingdom_4] ],
["felt_hat_b", "Felt Hat", [("felt_hat_b_new",0)], itp_merchandise| itp_type_head_armor |itp_civilian,0, 4 , weight(1)|abundance(50)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_clothes, [], [fac_kingdom_1, fac_kingdom_5] ],
["sarranid_felt_hat", "Sarranid Felt Hat", [("sar_helmet3",0)], itp_merchandise| itp_type_head_armor   ,0, 16 , weight(2)|abundance(50)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_clothes, [], [fac_kingdom_6] ],

# Cheap Western Helmets
["arming_cap", "Arming Cap", [("arming_cap_a_new",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0,
 5 , weight(1)|abundance(100)|head_armor(7)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_1] ],
["padded_coif", "Padded Coif", [("padded_coif_a_new",0)], itp_merchandise| itp_type_head_armor   ,0,
 6 , weight(1)|abundance(100)|head_armor(11)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_1, fac_kingdom_4, fac_kingdom_5] ],
["leather_cap", "Leather Cap", [("leather_cap_a_new",0)], itp_merchandise| itp_type_head_armor|itp_civilian ,0,
 8, weight(1)|abundance(100)|head_armor(18)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_4] ],
["skullcap", "Skullcap", [("skull_cap_new_a",0)], itp_merchandise| itp_type_head_armor   ,0,
 60 , weight(1.0)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate ],

# Cheap Eastern Helmets
["nomad_cap", "Nomad Skullcap", [("nomad_cap_a_new",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0,
 6 , weight(0.75)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_2, fac_kingdom_3] ],
["nomad_cap_b", "Nomad Leather Cap", [("nomad_cap_b_new",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0,
 6 , weight(0.75)|abundance(100)|head_armor(13)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_2, fac_kingdom_3]  ],
["steppe_cap", "Nomad Warrior Cap", [("steppe_cap_a_new",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0,
 14 , weight(1)|abundance(100)|head_armor(14)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_2, fac_kingdom_3]  ],
["leather_steppe_cap_a", "Fur Steppe Cap", [("leather_steppe_cap_a_new",0)], itp_merchandise|itp_type_head_armor,0, 
24 , weight(1)|abundance(100)|head_armor(15)|body_armor(0)|leg_armor(0) ,imodbits_cloth, [], [fac_kingdom_2, fac_kingdom_3] ],
["leather_steppe_cap_b", "Steppe Skullcap", [("tattered_steppe_cap_b_new",0)], itp_merchandise|itp_type_head_armor,0, 
36 , weight(1)|abundance(100)|head_armor(16)|body_armor(0)|leg_armor(0) ,imodbits_cloth, [], [fac_kingdom_2, fac_kingdom_3] ],
["leather_steppe_cap_c", "Steppe Warrior Cap", [("steppe_cap_a_new",0)], itp_merchandise|itp_type_head_armor,0,
 51 , weight(1)|abundance(100)|head_armor(16)|body_armor(0)|leg_armor(0) ,imodbits_cloth, [], [fac_kingdom_2, fac_kingdom_3] ],
["leather_warrior_cap", "Khergit Leather Helmet", [("skull_cap_new_b",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0,
 14 , weight(1)|abundance(100)|head_armor(18)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_3] ],
 
# Swadian and Rhodok Helmets
["mail_coif", "Mail Coif", [("mail_coif_new",0)], itp_merchandise| itp_type_head_armor   ,0,
 71 , weight(1.25)|abundance(100)|head_armor(22)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_armor, [], [fac_kingdom_1, fac_kingdom_4, fac_kingdom_5] ],
["footman_helmet", "Footman's Helmet", [("skull_cap_new",0)], itp_merchandise| itp_type_head_armor   ,0,
 95 , weight(1.5)|abundance(100)|head_armor(24)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_4, fac_kingdom_5] ],
["nasal_helmet", "Nasal Helmet", [("nasal_helmet_b",0)], itp_merchandise| itp_type_head_armor   ,0,
 121 , weight(1.25)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_4, fac_kingdom_5] ],
["norman_helmet", "Helmet with Cap", [("norman_helmet_a",0)], itp_merchandise| itp_type_head_armor|itp_fit_to_head ,0,
 147 , weight(1.25)|abundance(100)|head_armor(28)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], [fac_kingdom_1, fac_kingdom_4, fac_kingdom_5] ],
["segmented_helmet", "Segmented Helmet", [("segmented_helm_new",0)], itp_merchandise| itp_type_head_armor   ,0,
 174 , weight(1.25)|abundance(100)|head_armor(31)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], [fac_kingdom_1, fac_kingdom_4, fac_kingdom_5] ],
["helmet_with_neckguard", "Helmet with Neckguard", [("neckguard_helm_new",0)], itp_merchandise| itp_type_head_armor   ,0,
 190 , weight(1.5)|abundance(100)|head_armor(32)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], [fac_kingdom_1, fac_kingdom_4, fac_kingdom_5] ],
["flat_topped_helmet", "Flat Topped Helmet", [("flattop_helmet_new",0)], itp_merchandise| itp_type_head_armor   ,0,
 203 , weight(1.75)|abundance(100)|head_armor(33)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], [fac_kingdom_1] ],
["kettle_hat", "Kettle Hat", [("kettle_hat_new",0)], itp_merchandise| itp_type_head_armor,0,
 240 , weight(1.75)|abundance(100)|head_armor(35)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], [fac_kingdom_1, fac_kingdom_5] ],
["bascinet", "Bascinet", [("bascinet_avt_new",0)], itp_merchandise|itp_type_head_armor   ,0,
 479 , weight(2.25)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate, [], [fac_kingdom_1, fac_kingdom_5] ],
["bascinet_2", "Bascinet with Aventail", [("bascinet_new_a",0)], itp_merchandise|itp_type_head_armor   ,0,
 479 , weight(2.25)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate, [], [fac_kingdom_1, fac_kingdom_4, fac_kingdom_5] ],
["bascinet_3", "Bascinet with Nose Guard", [("bascinet_new_b",0)], itp_merchandise|itp_type_head_armor   ,0,
 479 , weight(2.25)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate, [], [fac_kingdom_1, fac_kingdom_4, fac_kingdom_5] ],
["guard_helmet", "Guard Helmet", [("reinf_helmet_new",0)], itp_merchandise| itp_type_head_armor   ,0,
 555 , weight(2.5)|abundance(100)|head_armor(47)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ],
["full_helm", "Full Helm", [("great_helmet_new_b",0)], itp_merchandise| itp_type_head_armor |itp_covers_head ,0,
 811 , weight(2.5)|abundance(100)|head_armor(51)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate, [], [fac_kingdom_1, fac_kingdom_5] ],
["great_helmet", "Great Helmet", [("great_helmet_new",0)], itp_merchandise| itp_type_head_armor|itp_covers_head,0,
 980 , weight(2.75)|abundance(100)|head_armor(53)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate, [], [fac_kingdom_1, fac_kingdom_4] ],
["winged_great_helmet", "Winged Great Helmet", [("maciejowski_helmet_new",0)], itp_merchandise|itp_type_head_armor|itp_covers_head,0,
 1240 , weight(2.75)|abundance(100)|head_armor(55)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate, [], [fac_kingdom_1, fac_kingdom_4] ],

# Vaegir Helmets
["vaegir_fur_cap", "Vaegir Skullcap", [("vaeg_helmet3",0)], itp_merchandise| itp_type_head_armor   ,0,
 50 , weight(1)|abundance(100)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], [fac_kingdom_2, fac_kingdom_3] ],
["vaegir_fur_helmet", "Vaegir Helmet", [("vaeg_helmet2",0)], itp_merchandise| itp_type_head_armor   ,0,
 110 , weight(2)|abundance(100)|head_armor(21)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], [fac_kingdom_2] ],
["vaegir_spiked_helmet", "Vaegir Spiked Helmet", [("vaeg_helmet1",0)], itp_merchandise| itp_type_head_armor   ,0,
 230 , weight(2.50)|abundance(100)|head_armor(32)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], [fac_kingdom_2] ],
["vaegir_lamellar_helmet", "Vaegir Lamellar Helmet", [("vaeg_helmet4",0)], itp_merchandise| itp_type_head_armor   ,0,
 360 , weight(2.75)|abundance(100)|head_armor(38)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], [fac_kingdom_2] ],
["vaegir_guard_helmet", "Vaegir Guard Helmet", [("vaeg_helmet5",0)], itp_merchandise| itp_type_head_armor   ,0,
 650, weight(2.75)|abundance(100)|head_armor(42)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], [fac_kingdom_2] ],
["vaegir_noble_helmet", "Vaegir Nobleman Helmet", [("vaeg_helmet7",0)], itp_merchandise| itp_type_head_armor   ,0,
 710, weight(2.75)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], [fac_kingdom_2] ],
["vaegir_half_mask", "Vaegir Nobleman Mask", [("vaeg_helmet8",0)], itp_merchandise| itp_type_head_armor |itp_covers_beard ,0,
 750 , weight(3)|abundance(100)|head_armor(46)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], [fac_kingdom_2] ],
["vaegir_war_helmet", "Vaegir War Helmet", [("vaeg_helmet6",0)], itp_merchandise| itp_type_head_armor   ,0,
 820 , weight(3)|abundance(100)|head_armor(47)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], [fac_kingdom_2] ],
["vaegir_war_mask", "Vaegir War Mask", [("vaeg_helmet9",0)], itp_merchandise| itp_type_head_armor |itp_covers_beard ,0,
 950 , weight(3.50)|abundance(100)|head_armor(52)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], [fac_kingdom_2] ],

# Khergit Helmets
["khergit_war_helmet", "Khergit War Helmet", [("tattered_steppe_cap_a_new",0)], itp_type_head_armor | itp_merchandise,0,
 200 , weight(2)|abundance(100)|head_armor(31)|body_armor(0)|leg_armor(0) ,imodbits_cloth, [], [fac_kingdom_2] ],
["spiked_helmet", "Spiked Helmet", [("spiked_helmet_new",0)], itp_merchandise| itp_type_head_armor,0,
 278 , weight(2)|abundance(100)|head_armor(38)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], [fac_kingdom_2, fac_kingdom_3] ],
["khergit_guard_helmet", "Khergit Guard Helmet", [("lamellar_helmet_a",0)], itp_type_head_armor |itp_merchandise,0,
 433 , weight(2)|abundance(100)|head_armor(40)|body_armor(0)|leg_armor(0) ,imodbits_cloth, [], [fac_kingdom_2] ],
["khergit_cavalry_helmet", "Khergit Cavalry Helmet", [("lamellar_helmet_b",0)], itp_type_head_armor | itp_merchandise,0,
 333 , weight(2)|abundance(100)|head_armor(36)|body_armor(0)|leg_armor(0) ,imodbits_cloth, [], [fac_kingdom_2] ],

# Nord Helmets
["nordic_archer_helmet", "Nordic Leather Helmet", [("Helmet_A_vs2",0)], itp_merchandise| itp_type_head_armor    ,0,
 40 , weight(1.25)|abundance(100)|head_armor(14)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], [fac_kingdom_4] ],
["nordic_veteran_archer_helmet", "Nordic Leather Helmet", [("Helmet_A",0)], itp_merchandise| itp_type_head_armor,0,
 70 , weight(1.5)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], [fac_kingdom_4] ],
["nordic_footman_helmet", "Nordic Footman Helmet", [("Helmet_B_vs2",0)], itp_merchandise| itp_type_head_armor |itp_fit_to_head ,0,
 150 , weight(1.75)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], [fac_kingdom_4] ],
["nordic_fighter_helmet", "Nordic Fighter Helmet", [("Helmet_B",0)], itp_merchandise| itp_type_head_armor|itp_fit_to_head ,0,
 240 , weight(2)|abundance(100)|head_armor(34)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], [fac_kingdom_4] ],
["nordic_helmet", "Nordic Helmet", [("helmet_w_eyeguard_new",0)], itp_merchandise| itp_type_head_armor   ,0,
 340 , weight(2)|abundance(100)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], [fac_kingdom_1, fac_kingdom_4] ],
["nordic_huscarl_helmet", "Nordic Huscarl's Helmet", [("Helmet_C_vs2",0)], itp_merchandise| itp_type_head_armor   ,0,
 390 , weight(2)|abundance(100)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], [fac_kingdom_4] ],
["nordic_warlord_helmet", "Nordic Warlord Helmet", [("Helmet_C",0)], itp_merchandise| itp_type_head_armor ,0,
 880 , weight(2.25)|abundance(100)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], [fac_kingdom_4] ],

# Sarranid Helmets
["turban", "Turban", [("tuareg_open",0)], itp_merchandise| itp_type_head_armor   ,0,
 28 , weight(1)|abundance(150)|head_armor(11)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_cloth, [], [fac_kingdom_6] ],
["desert_turban", "Desert Turban", [("tuareg",0)], itp_merchandise| itp_type_head_armor | itp_covers_beard ,0,
 38 , weight(1.50)|abundance(150)|head_armor(14)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_cloth, [], [fac_kingdom_6]  ],
["sarranid_warrior_cap", "Sarranid Warrior Cap", [("tuareg_helmet",0)], itp_merchandise| itp_type_head_armor | itp_covers_beard  ,0,
 90 , weight(2)|abundance(150)|head_armor(19)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], [fac_kingdom_6]  ],
["sarranid_horseman_helmet", "Horseman Helmet", [("sar_helmet2",0)], itp_merchandise| itp_type_head_armor   ,0,
 180 , weight(2.75)|abundance(150)|head_armor(25)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], [fac_kingdom_6]  ],
["sarranid_helmet1", "Sarranid Keffiyeh Helmet", [("sar_helmet1",0)], itp_merchandise| itp_type_head_armor   ,0,
 290 , weight(2.50)|abundance(150)|head_armor(35)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], [fac_kingdom_6]  ],
["sarranid_mail_coif", "Sarranid Mail Coif", [("tuareg_helmet2",0)], itp_merchandise| itp_type_head_armor ,0,
 430 , weight(3)|abundance(150)|head_armor(41)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], [fac_kingdom_6]  ],
["sarranid_veiled_helmet", "Sarranid Veiled Helmet", [("sar_helmet4",0)], itp_merchandise| itp_type_head_armor | itp_covers_beard  ,0,
 810 , weight(3.50)|abundance(150)|head_armor(47)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], [fac_kingdom_6]  ],

# Previously store decoration only (ugly and obsolete)
# ["felt_steppe_cap", "Felt Steppe Cap", [("felt_steppe_cap",0)], itp_type_head_armor   ,0, 237 , weight(2)|abundance(0)|head_armor(16)|body_armor(0)|leg_armor(0) ,imodbits_cloth, [], [fac_no_faction] ],
# ["khergit_helmet", "Khergit Helmet", [("khergit_guard_helmet",0)], itp_type_head_armor   ,0, 361 , weight(2)|abundance(0)|head_armor(33)|body_armor(0)|leg_armor(0) ,imodbits_cloth, [], [fac_no_faction] ],
# ["byzantion_helmet_a", "Byzantion Helmet", [("byzantion_helmet_a",0)], itp_type_head_armor   ,0, 278 , weight(2)|abundance(0)|head_armor(20)|body_armor(0)|leg_armor(0) ,imodbits_cloth, [], [fac_no_faction] ],
# ["magyar_helmet_a", "Magyar Helmet", [("magyar_helmet_a",0)], itp_type_head_armor   ,0, 278 , weight(2)|abundance(0)|head_armor(20)|body_armor(0)|leg_armor(0) ,imodbits_cloth, [], [fac_no_faction] ],
# ["rus_helmet_a", "Rus Helmet", [("rus_helmet_a",0)], itp_type_head_armor   ,0, 278 , weight(2)|abundance(0)|head_armor(20)|body_armor(0)|leg_armor(0) ,imodbits_cloth, [], [fac_no_faction] ],
# ["sipahi_helmet_a", "Sipahi Helmet", [("sipahi_helmet_a",0)], itp_type_head_armor   ,0, 278 , weight(2)|abundance(0)|head_armor(20)|body_armor(0)|leg_armor(0) ,imodbits_cloth, [], [fac_no_faction] ],
# ["shahi", "Shahi", [("shahi",0)], itp_type_head_armor   ,0, 278 , weight(2)|abundance(0)|head_armor(20)|body_armor(0)|leg_armor(0) ,imodbits_cloth, [], [fac_no_faction] ],
# ["rabati", "Rabati", [("rabati",0)], itp_type_head_armor   ,0, 278 , weight(2)|abundance(0)|head_armor(20)|body_armor(0)|leg_armor(0) ,imodbits_cloth, [], [fac_no_faction] ],

################
# Special Sets #
################
["burlap_tunic", "Burlap Tunic", [("shirt",0)], itp_type_body_armor  |itp_covers_legs ,0,
 5 , weight(1)|abundance(0)|head_armor(0)|body_armor(3)|leg_armor(1)|difficulty(0) ,imodbits_armor, [], [fac_no_faction] ],
["pilgrim_disguise", "Pilgrim Disguise", [("pilgrim_outfit",0)], 0| itp_type_body_armor |itp_covers_legs |itp_civilian ,0,
 25 , weight(2)|abundance(0)|head_armor(0)|body_armor(19)|leg_armor(8)|difficulty(0) ,imodbits_cloth, [], [fac_no_faction] ],
["pilgrim_hood", "Pilgrim Hood", [("pilgrim_hood",0)], 0| itp_type_head_armor |itp_civilian  ,0,
 35 , weight(1.25)|abundance(0)|head_armor(14)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth, [], [fac_no_faction] ],

["bride_dress", "Bride Dress", [("bride_dress",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 500 , weight(3)|abundance(0)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth, [], [fac_no_faction]],
["bride_crown", "Crown of Flowers", [("bride_crown",0)],  itp_type_head_armor | itp_doesnt_cover_hair |itp_civilian |itp_attach_armature,0,
 1 , weight(0.5)|abundance(0)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth, [], [fac_no_faction] ],
["bride_shoes", "Bride Shoes", [("bride_shoes",0)], itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
 30 , weight(1)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(8)|difficulty(0) ,imodbits_cloth, [], [fac_no_faction] ],

["strange_boots",  "Strange Boots", [("samurai_boots",0)], itp_type_foot_armor | itp_attach_armature,0,
 465 , weight(1)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(21)|difficulty(0) ,imodbits_cloth, [], [fac_no_faction] ],
["strange_armor",  "Strange Armor", [("samurai_armor",0)], itp_type_body_armor  |itp_covers_legs ,0,
 1259 , weight(18)|abundance(0)|head_armor(0)|body_armor(38)|leg_armor(19)|difficulty(7) ,imodbits_armor, [], [fac_no_faction] ],
["strange_helmet", "Strange Helmet", [("samurai_helmet",0)], itp_type_head_armor   ,0,
 824 , weight(2)|abundance(0)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], [fac_no_faction] ],

["black_greaves", "Black Greaves", [("black_greaves",0)], itp_type_foot_armor  | itp_attach_armature,0,
 2361 , weight(3.5)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(35)|difficulty(0) ,imodbits_armor, [], [fac_no_faction] ],
["black_armor", "Black Armor", [("black_armor",0)], itp_type_body_armor  |itp_covers_legs ,0,
 9496 , weight(28)|abundance(0)|head_armor(0)|body_armor(57)|leg_armor(18)|difficulty(10) ,imodbits_plate, [], [fac_no_faction] ],
["black_helmet", "Black Helmet", [("black_helm",0)], itp_type_head_armor,0,
 638 , weight(2.75)|abundance(0)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate, [], [fac_no_faction] ],
 
# Like Heraldic Mail, but takes the Faction's banner, not the Lord's banner
["mail_with_faction_surcoat", "Soldier's Mail with Surcoat", [("heraldic_armor_new_a",0)], itp_type_body_armor  |itp_covers_legs ,0,
 3454 , weight(22)|abundance(0)|head_armor(0)|body_armor(49)|leg_armor(17)|difficulty(7) ,imodbits_armor,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_tableau_item_set_troop_faction", "tableau_heraldic_armor_a", ":agent_no", ":troop_no")])], [fac_no_faction]],

# Possible, er, "Easteregg"
["santa_cap", "Red Cap", [("noel_helmet",0)], itp_type_head_armor|itp_civilian,0,
 9, weight(1)|abundance(50)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_clothes, [], [fac_no_faction]],
 
# Outcommented armor (ugly and obsolete, but technically functional):
#["heraldric_armor", "Heraldric Armor", [("tourn_armor_a",0)], itp_type_body_armor  |itp_covers_legs ,0, 442 , weight(17)|abundance(100)|head_armor(0)|body_armor(35)|leg_armor(8)|difficulty(7) ,imodbits_armor ],
#["leather_steppe_cap_c", "Leather Steppe Cap", [("leather_steppe_cap_c",0)], itp_type_head_armor   ,0, 51 , weight(2)|abundance(100)|head_armor(18)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],

# Obsolete meshes (now replaced):
# lthr_armor_a, linen_tunic, cvl_costume_a, coarse_tunic, tabard_a, leather_vest, red_gambeson, aketon_a, leather_jerkin,
# padded_leather, mail_shirt, haubergeon_a, haubergeon_b, brigandine_a, reinf_jerkin, std_lthr_coat, hard_lthr_a

#############################
# MELEE WEAPONS - Slots 0-3 #
#############################
# Keep wooden_stick in front!

# One-Handed Weapons
####################

# Clubs and Maces
["wooden_stick",  "Wooden Stick", [("wooden_stick",0)], itp_type_one_handed_wpn| itp_primary|itp_wooden_parry|itp_wooden_attack, itc_scimitar, 
4 , weight(2.5)|abundance(0)|difficulty(0)|spd_rtng(99) | weapon_length(63)|swing_damage(13 , blunt) | thrust_damage(0 ,  pierce),imodbits_none, [], [fac_no_faction] ],
["cudgel",         "Cudgel", [("club",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_wooden_parry|itp_wooden_attack, itc_scimitar, 
4 , weight(2.5)|abundance(100)|difficulty(0)|spd_rtng(99) | weapon_length(70)|swing_damage(13 , blunt) | thrust_damage(0 ,  pierce),imodbits_none ],
["club",         "Club", [("club",0)], itp_type_one_handed_wpn|itp_merchandise| itp_can_knock_down|itp_primary|itp_wooden_parry|itp_wooden_attack, itc_scimitar, 
11 , weight(2.5)|abundance(100)|difficulty(0)|spd_rtng(98) | weapon_length(70)|swing_damage(20 , blunt) | thrust_damage(0 ,  pierce),imodbits_none ],
["spiked_club",   "Spiked Club", [("spiked_club",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 
83 , weight(3)|abundance(100)|difficulty(0)|spd_rtng(97) | weapon_length(70)|swing_damage(21 , pierce) | thrust_damage(0 ,  pierce),imodbits_mace, [], [fac_kingdom_1, fac_kingdom_5] ],
["sarranid_mace_1", "Iron Mace", [("mace_small_d",0)], itp_type_one_handed_wpn|itp_merchandise|itp_can_knock_down |itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
 45 , weight(2.0)|abundance(100)|difficulty(0)|spd_rtng(99) | weapon_length(73)|swing_damage(22 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace, [], [fac_kingdom_6] ],
["mace_1",         "Spiked Club", [("mace_d",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
 45 , weight(1.5)|abundance(100)|difficulty(0)|spd_rtng(99) | weapon_length(70)|swing_damage(19 , pierce) | thrust_damage(0 ,  pierce),imodbits_mace, [], [fac_kingdom_2, fac_kingdom_3, fac_kingdom_4] ],
["mace_2",         "Knobbed Mace", [("mace_a",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
 98 , weight(2.5)|abundance(100)|difficulty(0)|spd_rtng(98) | weapon_length(70)|swing_damage(21 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["mace_3",         "Spiked Mace", [("mace_c",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
 152 , weight(2.75)|abundance(100)|difficulty(0)|spd_rtng(98) | weapon_length(70)|swing_damage(23 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["mace_4",         "Winged Mace", [("mace_b",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
 212 , weight(2.75)|abundance(100)|difficulty(0)|spd_rtng(98) | weapon_length(70)|swing_damage(24 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["winged_mace",         "Flanged Mace", [("flanged_mace",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 
122 , weight(3.5)|abundance(100)|difficulty(0)|spd_rtng(103) | weapon_length(70)|swing_damage(24 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["spiked_mace",         "Spiked Mace", [("spiked_mace_new",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 
180 , weight(3.5)|abundance(100)|difficulty(0)|spd_rtng(98) | weapon_length(70)|swing_damage(28 , blunt) | thrust_damage(0 ,  pierce),imodbits_pick ],
["mace_bronze",         "Bronze Mace", [("mace_pear",0)], itp_type_one_handed_wpn|itp_merchandise|itp_can_knock_down |itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
145 , weight(3.0)|abundance(100)|difficulty(0)|spd_rtng(97) | weapon_length(73)|swing_damage(26 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace, [], [fac_kingdom_6] ],
["morningstar_short",   "Short Morningstar", [("mace_morningstar",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 
280 , weight(3.5)|abundance(100)|difficulty(0)|spd_rtng(98) | weapon_length(70)|swing_damage(28 , pierce) | thrust_damage(0 ,  pierce),imodbits_pick ],

# Hammers and Picks
["hammer",    "Hammer", [("iron_hammer_new",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar, 
7 , weight(2)|abundance(100)|difficulty(0)|spd_rtng(100) | weapon_length(55)|swing_damage(24 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["hammer_alt", "Hammer", [("iron_hammer_alt",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_wooden_parry, itc_scimitar,
7 , weight(2)|spd_rtng(100) | weapon_length(55)|swing_damage(20 , pierce) | thrust_damage(0 ,  pierce),imodbits_mace, [], [fac_no_faction] ],
["pickaxe", "Pickaxe", [("rusty_pick_a",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 
27 , weight(3)|abundance(100)|difficulty(0)|spd_rtng(99) | weapon_length(70)|swing_damage(19 , pierce) | thrust_damage(0 ,  pierce),imodbits_pick ],
["pickaxe_alt", "Pickaxe", [("rusty_pick_alt",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
27 , weight(3)|spd_rtng(99) | weapon_length(70)|swing_damage(18 , blunt) | thrust_damage(0 ,  pierce),imodbits_pick, [], [fac_no_faction] ],
["fighting_pick", "Fighting Pick", [("fighting_pick_new",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 
108 , weight(1.0)|abundance(100)|difficulty(0)|spd_rtng(98) | weapon_length(70)|swing_damage(22 , pierce) | thrust_damage(0 ,  pierce),imodbits_pick, [], [fac_kingdom_1, fac_kingdom_5] ],
["fighting_pick_alt", "Fighting Pick", [("fighting_pick_alt",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
108 , weight(1.0)|spd_rtng(98) | weapon_length(70)|swing_damage(22 , blunt) | thrust_damage(0 ,  pierce),imodbits_pick, [], [fac_no_faction] ],
["military_pick", "Military Pick", [("steel_pick_new",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 
280 , weight(1.5)|abundance(100)|difficulty(0)|spd_rtng(97) | weapon_length(70)|swing_damage(31 , pierce) | thrust_damage(0 ,  pierce),imodbits_pick, [], [fac_kingdom_1, fac_kingdom_5] ],
["military_pick_alt", "Military Pick", [("steel_pick_alt",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_axe_left_hip,
280 , weight(1.5)|spd_rtng(97) | weapon_length(70)|swing_damage(29 , blunt) | thrust_damage(0 ,  pierce),imodbits_pick, [], [fac_no_faction] ],
["military_hammer", "Military Hammer", [("military_hammer",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 
317 , weight(2)|abundance(100)|difficulty(0)|spd_rtng(95) | weapon_length(70)|swing_damage(31 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace, [], [fac_kingdom_1, fac_kingdom_5] ],
["military_hammer_alt", "Military Hammer", [("military_hammer_alt",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_axe_left_hip,
317 , weight(2)| spd_rtng(95) | weapon_length(70)|swing_damage(25 , pierce) | thrust_damage(0 ,  pierce),imodbits_mace, [], [fac_no_faction] ],

# Blades
["sickle",         "Sickle", [("sickle",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry|itp_wooden_parry, itc_cleaver, 
9 , weight(1.5)|abundance(100)|difficulty(0)|spd_rtng(99) | weapon_length(40)|swing_damage(20 , cut) | thrust_damage(0 ,  pierce),imodbits_none ],
["cleaver",         "Cleaver", [("cleaver_new",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry|itp_wooden_parry, itc_cleaver, 
14 , weight(1.5)|abundance(100)|difficulty(0)|spd_rtng(103) | weapon_length(35)|swing_damage(24 , cut) | thrust_damage(0 ,  pierce),imodbits_none ],
["cleaver_throw", "Cleaver", [("cleaver_new",0)], itp_type_thrown|itp_primary,itcf_throw_axe,
14, weight(1.5)|difficulty(0)|spd_rtng(103) | shoot_speed(18) | thrust_damage(32,cut)|max_ammo(1)|weapon_length(30),imodbits_none, [], [fac_no_faction] ],
["knife",         "Knife", [("peasant_knife_new",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_left, 
18 , weight(0.5)|abundance(100)|difficulty(0)|spd_rtng(110) | weapon_length(40)|swing_damage(21 , cut) | thrust_damage(13 ,  pierce),imodbits_sword ],
["knife_throw", "Knife", [("peasant_knife_throw",0)], itp_type_thrown|itp_primary ,itcf_throw_knife,
18 , weight(0.5)|difficulty(0)|spd_rtng(114) | shoot_speed(24) | thrust_damage(19 ,  cut)|max_ammo(1)|weapon_length(0),imodbits_thrown, [], [fac_no_faction] ],
["butchering_knife", "Butchering Knife", [("khyber_knife_new",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_right, 
23 , weight(0.75)|abundance(100)|difficulty(0)|spd_rtng(108) | weapon_length(60)|swing_damage(24 , cut) | thrust_damage(17 ,  pierce),imodbits_sword ],
["dagger",         "Dagger", [("dagger_b",0),("dagger_b_scabbard",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_left|itcf_show_holster_when_drawn, 
37 , weight(0.75)|abundance(100)|difficulty(0)|spd_rtng(109) | weapon_length(47)|swing_damage(22 , cut) | thrust_damage(19 ,  pierce),imodbits_sword_high ],
["dagger_throw", "Dagger", [("dagger_throw",0)], itp_type_thrown|itp_primary ,itcf_throw_knife,
37 , weight(0.75)|difficulty(0)|spd_rtng(113) | shoot_speed(23) | thrust_damage(21 ,  cut)|max_ammo(1)|weapon_length(0),imodbits_thrown, [], [fac_no_faction] ],
["falchion",         "Falchion", [("falchion_new",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip, 
105 , weight(2.5)|abundance(100)|difficulty(8)|spd_rtng(98) | weapon_length(73)|swing_damage(30 , cut) | thrust_damage(0 ,  pierce),imodbits_sword ],
["military_sickle", "Military Sickle", [("military_sickle_a",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 220 , weight(1.0)|abundance(100)|difficulty(9)|spd_rtng(100) | weapon_length(75)|swing_damage(26 , pierce) | thrust_damage(0 ,  pierce),imodbits_axe ],

# Swadian Swords
["sword_medieval_a", "Sword", [("sword_medieval_a",0),("sword_medieval_a_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 163 , weight(1.5)|abundance(100)|difficulty(0)|spd_rtng(99) | weapon_length(95)|swing_damage(27 , cut) | thrust_damage(22 ,  pierce),imodbits_sword_high, [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_4, fac_kingdom_5] ],
["sword_medieval_a_small", "Short Sword",[("sword_norman",0),("sword_norman_scabbard", ixmesh_carry),("sword_norman_rusty",imodbit_rusty),("sword_norman_rusty_scabbard", ixmesh_carry|imodbit_rusty)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 104 , weight(1)|abundance(100)|difficulty(0)|spd_rtng(103) | weapon_length(75)|swing_damage(25 , cut) | thrust_damage(23 ,  pierce),imodbits_sword_high, [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_4, fac_kingdom_5] ],
["sword_medieval_a_long", "Long Sword", [("sword_medieval_a_long",0),("sword_medieval_a_long_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 243 , weight(1.5)|abundance(100)|difficulty(0)|spd_rtng(97) | weapon_length(105)|swing_damage(27 , cut) | thrust_damage(24 ,  pierce),imodbits_sword_high, [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_4, fac_kingdom_5] ],
["sword_medieval_b", "Sword", [("sword_medieval_b",0),("sword_medieval_b_scabbard", ixmesh_carry),("sword_rusty_a",imodbit_rusty),("sword_rusty_a_scabbard", ixmesh_carry|imodbit_rusty)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 243 , weight(1.5)|abundance(100)|difficulty(0)|spd_rtng(99) | weapon_length(95)|swing_damage(28 , cut) | thrust_damage(23 ,  pierce),imodbits_sword_high, [], [fac_kingdom_1, fac_kingdom_4, fac_kingdom_5] ],
["sword_medieval_b_small", "Short Sword", [("sword_medieval_b_small",0),("sword_medieval_b_small_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 152 , weight(1)|abundance(100)|difficulty(0)|spd_rtng(102) | weapon_length(85)|swing_damage(26, cut) | thrust_damage(24, pierce),imodbits_sword_high, [], [fac_kingdom_1, fac_kingdom_4, fac_kingdom_5] ],
["sword_medieval_b_long", "Long Sword", [("long_sword",0),("scab_longsw_a", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 312 , weight(1.7)|abundance(100)|difficulty(0)|spd_rtng(98) | weapon_length(102)|swing_damage(28 , cut) | thrust_damage(27 ,  pierce),imodbits_sword_high, [], [fac_kingdom_1, fac_kingdom_4, fac_kingdom_5] ],
["sword_medieval_c", "Arming Sword", [("sword_medieval_c",0),("sword_medieval_c_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 410 , weight(1.5)|abundance(100)|difficulty(0)|spd_rtng(99) | weapon_length(95)|swing_damage(29 , cut) | thrust_damage(24 ,  pierce),imodbits_sword_high, [], [fac_kingdom_1, fac_kingdom_5] ],
["sword_medieval_c_small", "Short Arming Sword", [("sword_medieval_c_small",0),("sword_medieval_c_small_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 243 , weight(1)|abundance(100)|difficulty(0)|spd_rtng(103) | weapon_length(86)|swing_damage(26, cut) | thrust_damage(24 ,  pierce),imodbits_sword_high, [], [fac_kingdom_1, fac_kingdom_5] ],
["sword_medieval_c_long", "Long Arming Sword", [("sword_medieval_c_long",0),("sword_medieval_c_long_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 480 , weight(1.7)|abundance(100)|difficulty(0)|spd_rtng(99) | weapon_length(100)|swing_damage(29 , cut) | thrust_damage(28 ,  pierce),imodbits_sword_high, [], [fac_kingdom_1, fac_kingdom_5] ],
["sword_medieval_d", "Arming Sword", [("sword_medieval_d",0),("sword_medieval_d_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 480 , weight(1.5)|abundance(100)|difficulty(0)|spd_rtng(99) | weapon_length(95)|swing_damage(33 , cut) | thrust_damage(24 ,  pierce),imodbits_sword, [], [fac_kingdom_1, fac_kingdom_5] ],
["sword_medieval_d_mid", "Long Arming Sword", [("b_long_sword",0),("scab_longsw_b", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 520 , weight(1.7)|abundance(100)|difficulty(0)|spd_rtng(101) | weapon_length(100)|swing_damage(33 , cut) | thrust_damage(26 ,  pierce),imodbits_sword, [], [fac_kingdom_1, fac_kingdom_5] ],
["sword_medieval_d_long", "Long Arming Sword", [("sword_medieval_d_long",0),("sword_medieval_d_long_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 550 , weight(1.8)|abundance(100)|difficulty(0)|spd_rtng(99) | weapon_length(105)|swing_damage(33 , cut) | thrust_damage(28 ,  pierce),imodbits_sword, [], [fac_kingdom_1, fac_kingdom_5] ],
 
# Khergit Swords
["sword_khergit_1", "Nomad Sabre", [("khergit_sword_b",0),("khergit_sword_b_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 105 , weight(1.25)|abundance(100)|difficulty(0)|spd_rtng(100) | weapon_length(97)|swing_damage(29 , cut),imodbits_sword_high, [], [fac_kingdom_2, fac_kingdom_3] ],
["sword_khergit_2", "Sabre", [("khergit_sword_c",0),("khergit_sword_c_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 191 , weight(1.5)|abundance(100)|difficulty(0)|spd_rtng(99) | weapon_length(97)|swing_damage(30 , cut),imodbits_sword_high, [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3] ],
["sword_khergit_2b", "Khergit Cavalry Sword", [("shashqa",0),("scab_shashqa", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 215 , weight(1.5)|abundance(100)|difficulty(0)|spd_rtng(101) | weapon_length(100)|swing_damage(30 , cut) | thrust_damage(0 ,  pierce),imodbits_sword, [], [fac_kingdom_2, fac_kingdom_3] ],
["sword_khergit_3", "Sabre", [("khergit_sword_a",0),("khergit_sword_a_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 294 , weight(1.5)|abundance(100)|difficulty(0)|spd_rtng(99) | weapon_length(98)|swing_damage(31 , cut),imodbits_sword_high, [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3] ],
["sword_khergit_3b", "Khergit Arming Sword", [("sword_medieval_e",0),("sword_medieval_e_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 331 , weight(1.6)|abundance(100)|difficulty(0)|spd_rtng(99) | weapon_length(95)|swing_damage(30 , cut) | thrust_damage(18 ,  pierce),imodbits_sword, [], [fac_kingdom_3] ],
["sword_khergit_4", "Heavy Sabre", [("khergit_sword_d",0),("khergit_sword_d_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 384 , weight(1.75)|abundance(100)|difficulty(0)|spd_rtng(98) | weapon_length(96)|swing_damage(33 , cut),imodbits_sword_high, [], [fac_kingdom_3] ],
["sword_khergit_4b", "Khergit Guard Sword", [("khergit_sword",0),("khergit_sword_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 383 , weight(1.7)|abundance(100)|difficulty(0)|spd_rtng(100) | weapon_length(97)|swing_damage(32 , cut) | thrust_damage(19 ,  pierce),imodbits_sword, [], [fac_kingdom_3] ],
 
# Nord Swords
["sword_viking_0", "Nordic Sword", [("viking_sword",0),("scab_vikingsw", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 142 , weight(1.5)|abundance(100)|difficulty(0)|spd_rtng(99) | weapon_length(98)|swing_damage(27 , cut) | thrust_damage(19 ,  pierce),imodbits_sword, [], [fac_kingdom_2, fac_kingdom_4] ],
["sword_viking_1", "Nordic Sword", [("sword_viking_c",0),("sword_viking_c_scabbard ", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 147 , weight(1.5)|abundance(100)|difficulty(0)|spd_rtng(99) | weapon_length(94)|swing_damage(28 , cut) | thrust_damage(20 ,  pierce),imodbits_sword_high, [], [fac_kingdom_2, fac_kingdom_4] ] ,
["sword_viking_1_long", "Nordic Long Sword", [("sword_viking_c_long",0),("sword_viking_c_long_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 247 , weight(1.7)|abundance(100)|difficulty(0)|spd_rtng(95) | weapon_length(105)|swing_damage(30 , cut) | thrust_damage(22 ,  pierce),imodbits_sword, [], [fac_kingdom_2, fac_kingdom_4] ],
["sword_viking_2", "Nordic Sword", [("sword_viking_b",0),("sword_viking_b_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 276 , weight(1.5)|abundance(100)|difficulty(0)|spd_rtng(99) | weapon_length(95)|swing_damage(29 , cut) | thrust_damage(21 ,  pierce),imodbits_sword_high, [], [fac_kingdom_2, fac_kingdom_4] ],
["sword_viking_2_small", "Nordic Short Sword", [("sword_viking_b_small",0),("sword_viking_b_small_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 162 , weight(1.25)|abundance(100)|difficulty(0)|spd_rtng(103) | weapon_length(85)|swing_damage(28 , cut) | thrust_damage(21 ,  pierce),imodbits_sword_high, [], [fac_kingdom_2, fac_kingdom_4] ],
["sword_viking_3", "Nordic War Sword", [("sword_viking_a",0),("sword_viking_a_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 394 , weight(1.5)|abundance(100)|difficulty(0)|spd_rtng(99) | weapon_length(95)|swing_damage(30 , cut) | thrust_damage(21 ,  pierce),imodbits_sword_high, [], [fac_kingdom_4] ],
["sword_viking_3_small", "Nordic Short War Sword", [("sword_viking_a_small",0),("sword_viking_a_small_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 280 , weight(1.25)|abundance(100)|difficulty(0)|spd_rtng(103) | weapon_length(86)|swing_damage(29 , cut) | thrust_damage(21 ,  pierce),imodbits_sword_high, [], [fac_kingdom_4] ],
["sword_viking_3_long", "Nordic Long War Sword", [("sword_viking_a_long",0),("sword_viking_a_long_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 464 , weight(1.7)|abundance(100)|difficulty(0)|spd_rtng(97) | weapon_length(105)|swing_damage(32 , cut) | thrust_damage(23 ,  pierce),imodbits_sword, [], [fac_kingdom_4] ] ,

# Rhodok Swords
["military_cleaver_b", "Soldier's Cleaver", [("military_cleaver_b",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip,
 193 , weight(1.5)|abundance(100)|difficulty(0)|spd_rtng(96) | weapon_length(95)|swing_damage(31 , cut) | thrust_damage(0 ,  pierce),imodbits_sword_high, [], [fac_kingdom_5] ],
["military_cleaver_c", "Military Cleaver", [("military_cleaver_c",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip,
 263 , weight(1.5)|abundance(100)|difficulty(0)|spd_rtng(96) | weapon_length(95)|swing_damage(35 , cut) | thrust_damage(0 ,  pierce),imodbits_sword_high, [], [fac_kingdom_5] ],

# Sarranid Swords
["scimitar_a", "Scimitar", [("scimeter",0),("scab_scimeter", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
208 , weight(1.5)|abundance(100)|difficulty(0)|spd_rtng(100) | weapon_length(99)|swing_damage(29 , cut) | thrust_damage(0 ,  pierce),imodbits_sword_high, [], [fac_kingdom_3, fac_kingdom_6] ],
["scimitar", "Scimitar", [("scimitar_a",0),("scab_scimeter_a", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
210 , weight(1.5)|abundance(100)|difficulty(0)|spd_rtng(101) | weapon_length(97)|swing_damage(30 , cut) | thrust_damage(0 ,  pierce),imodbits_sword_high, [], [fac_kingdom_3, fac_kingdom_6] ],
["scimitar_b", "Elite Scimitar", [("scimitar_b",0),("scab_scimeter_b", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
290 , weight(1.5)|abundance(100)|difficulty(0)|spd_rtng(100) | weapon_length(103)|swing_damage(32 , cut) | thrust_damage(0 ,  pierce),imodbits_sword_high, [], [fac_kingdom_6] ],

["arabian_sword_a",         "Sarranid Sword", [("arabian_sword_a",0),("scab_arabian_sword_a", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
108 , weight(1.5)|abundance(100)|difficulty(0)|spd_rtng(99) | weapon_length(97)|swing_damage(26 , cut) | thrust_damage(19 ,  pierce),imodbits_sword_high, [], [fac_kingdom_6] ],
["arabian_sword_b",         "Sarranid Arming Sword", [("arabian_sword_b",0),("scab_arabian_sword_b", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
218 , weight(1.7)|abundance(100)|difficulty(0)|spd_rtng(99) | weapon_length(97)|swing_damage(28 , cut) | thrust_damage(19 ,  pierce),imodbits_sword_high, [], [fac_kingdom_6] ],
["arabian_sword_c",         "Sarranid Cavalry Sword", [("arabian_sword_c",0),("scab_arabian_sword_c", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
310 , weight(1.5)|abundance(100)|difficulty(0)|spd_rtng(98) | weapon_length(105)|swing_damage(28 , cut) | thrust_damage(19 ,  pierce),imodbits_sword_high, [], [fac_kingdom_6] ],
["arabian_sword_d",         "Sarranid Guard Sword", [("arabian_sword_d",0),("scab_arabian_sword_d", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
420 , weight(1.7)|abundance(100)|difficulty(0)|spd_rtng(99) | weapon_length(97)|swing_damage(30 , cut) | thrust_damage(20 ,  pierce),imodbits_sword_high, [], [fac_kingdom_6] ],

# Exotic Swords
["strange_short_sword", "Strange Short Sword", [("wakizashi",0),("wakizashi_scabbard",ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_wakizashi|itcf_show_holster_when_drawn, 321 , weight(1.25)|abundance(0)|difficulty(0)|spd_rtng(108) | weapon_length(65)|swing_damage(25 , cut) | thrust_damage(19 ,  pierce),imodbits_sword, [], [fac_no_faction] ],
["strange_sword", "Strange Sword", [("katana",0),("katana_scabbard",ixmesh_carry)], itp_type_two_handed_wpn| itp_primary, itc_bastardsword|itcf_carry_katana|itcf_show_holster_when_drawn, 679 , weight(2.0)|abundance(0)|difficulty(9)|spd_rtng(108) | weapon_length(95)|swing_damage(32 , cut) | thrust_damage(18 ,  pierce),imodbits_sword, [], [fac_no_faction] ],
["strange_great_sword",  "Strange Great Sword", [("no_dachi",0),("no_dachi_scabbard",ixmesh_carry)], itp_type_two_handed_wpn|itp_two_handed|itp_primary, itc_nodachi|itcf_carry_sword_back|itcf_show_holster_when_drawn, 920 , weight(3.5)|abundance(0)|difficulty(11)|spd_rtng(92) | weapon_length(125)|swing_damage(38 , cut) | thrust_damage(0 ,  pierce),imodbits_axe, [], [fac_no_faction] ],
  
# Axes
["hatchet",         "Hatchet", [("hatchet",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 
13 , weight(2)|abundance(100)|difficulty(0)|spd_rtng(97) | weapon_length(60)|swing_damage(23 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["hatchet_throw", "Hatchet", [("hatchet",0)], itp_type_thrown|itp_primary,itcf_throw_axe,
13, weight(2)|difficulty(0)|spd_rtng(97) | shoot_speed(18) | thrust_damage(21,cut)|max_ammo(1)|weapon_length(50),imodbits_axe, [], [fac_no_faction] ],
["hand_axe",         "Hand Axe", [("hatchet",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 
24 , weight(2)|abundance(100)|difficulty(7)|spd_rtng(95) | weapon_length(75)|swing_damage(27 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["fighting_axe", "Fighting Axe", [("fighting_ax",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 
77 , weight(2.5)|abundance(100)|difficulty(9)|spd_rtng(92) | weapon_length(90)|swing_damage(31 , cut) | thrust_damage(0 ,  pierce),imodbits_axe_minus_heavy ],
["one_handed_war_axe_a", "One Handed Axe", [("one_handed_war_axe_a",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 87 , weight(1.5)|abundance(100)|difficulty(9)|spd_rtng(98) | weapon_length(71)|swing_damage(32 , cut) | thrust_damage(0 ,  pierce),imodbits_axe, [], [fac_kingdom_2, fac_kingdom_3, fac_kingdom_4] ],
["one_handed_battle_axe_a", "One Handed Battle Axe", [("one_handed_battle_axe_a",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 142 , weight(1.5)|abundance(100)|difficulty(9)|spd_rtng(98) | weapon_length(73)|swing_damage(34 , cut) | thrust_damage(0 ,  pierce),imodbits_axe, [], [fac_kingdom_2, fac_kingdom_3, fac_kingdom_4] ],
["one_handed_war_axe_b", "One Handed War Axe", [("one_handed_war_axe_b",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 190 , weight(1.5)|abundance(100)|difficulty(9)|spd_rtng(98) | weapon_length(76)|swing_damage(34 , cut) | thrust_damage(0 ,  pierce),imodbits_axe, [], [fac_kingdom_4] ],
["one_handed_battle_axe_b", "One Handed Battle Axe", [("one_handed_battle_axe_b",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 230 , weight(1.75)|abundance(100)|difficulty(9)|spd_rtng(98) | weapon_length(72)|swing_damage(36 , cut) | thrust_damage(0 ,  pierce),imodbits_axe, [], [fac_kingdom_4] ],
["one_handed_battle_axe_c", "One Handed War Axe", [("one_handed_battle_axe_c",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 550 , weight(2.0)|abundance(100)|difficulty(9)|spd_rtng(98) | weapon_length(76)|swing_damage(37 , cut) | thrust_damage(0 ,  pierce),imodbits_axe, [], [fac_kingdom_4] ],
["one_handed_battle_axe_c_alt", "One Handed War Axe", [("one_handed_battle_axe_c_alt",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 550 , weight(2.0)|spd_rtng(98) | weapon_length(76)|swing_damage(25 , pierce) | thrust_damage(0 ,  pierce),imodbits_axe, [], [fac_no_faction] ],
["sarranid_axe_a", "Iron Battle Axe", [("one_handed_battle_axe_g",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 250 , weight(1.65)|abundance(100)|difficulty(9)|spd_rtng(97) | weapon_length(71)|swing_damage(35 , cut) | thrust_damage(0 ,  pierce),imodbits_axe, [], [fac_kingdom_6] ],
["sarranid_axe_a_alt", "Iron Battle Axe", [("one_handed_battle_axe_g_alt",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 250 , weight(1.65)|spd_rtng(97) | weapon_length(71)|swing_damage(22 , blunt) | thrust_damage(0 ,  pierce),imodbits_axe, [], [fac_no_faction] ],
["sarranid_axe_b", "Iron War Axe", [("one_handed_battle_axe_h",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 360 , weight(1.75)|abundance(100)|difficulty(9)|spd_rtng(97) | weapon_length(71)|swing_damage(38 , cut) | thrust_damage(0 ,  pierce),imodbits_axe, [], [fac_kingdom_6] ],
["sarranid_axe_b_alt", "Iron War Axe", [("one_handed_battle_axe_h_alt",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 360 , weight(1.75)|spd_rtng(97) | weapon_length(71)|swing_damage(31 , pierce) | thrust_damage(0 ,  pierce),imodbits_axe, [], [fac_no_faction] ],

# One/Two-Handed Weapons
########################

["stone_hammer",         "Stone Hammer", [("sledgehammer",0)], itp_type_two_handed_wpn|itp_can_knock_down|itp_unbalanced|itp_crush_through|itp_primary|itp_wooden_parry|itp_wooden_attack, itc_scimitar|itcf_carry_mace_left_hip,
125 , weight(5.0)|abundance(0)|difficulty(10)|spd_rtng(85) | weapon_length(70)|swing_damage(36 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace, [], [fac_no_faction] ],
["fighting_axe_heavy", "Heavy Fighting Axe", [("fighting_ax",0)], itp_type_two_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_morningstar|itcf_carry_axe_left_hip, 
146 , weight(2.5)|abundance(100)|difficulty(10)|spd_rtng(106) | weapon_length(90)|swing_damage(48 , cut) | thrust_damage(0 ,  pierce),imodbits_axe_minus_heavy ], # Stats raised to counter 1h-penalty of -15% speed, -35% dmg; was 92, 31c (90, 33c for "heavy")
["club_with_spike_head",  "Spiked Staff", [("mace_e",0)],  itp_type_two_handed_wpn|itp_merchandise|itp_can_knock_down|itp_primary|itp_wooden_parry, itc_bastardsword|itcf_carry_axe_back,
 200 , weight(2.80)|abundance(100)|difficulty(9)|spd_rtng(95) | weapon_length(117)|swing_damage(24 , blunt) | thrust_damage(20 ,  pierce),imodbits_mace ],
["morningstar",         "Morningstar", [("mace_morningstar_new",0)], itp_crush_through|itp_type_two_handed_wpn|itp_merchandise|itp_primary|itp_wooden_parry|itp_unbalanced, itc_morningstar|itcf_carry_mace_left_hip, 
305 , weight(4.5)|abundance(100)|difficulty(13)|spd_rtng(95) | weapon_length(85)|swing_damage(38 , pierce) | thrust_damage(0 ,  pierce),imodbits_mace, [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5] ],
["bastard_sword_a", "Bastard Sword", [("bastard_sword_a",0),("bastard_sword_a_scabbard", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 294 , weight(2.0)|abundance(100)|difficulty(9)|spd_rtng(98) | weapon_length(101)|swing_damage(35 , cut) | thrust_damage(26 ,  pierce),imodbits_sword_high, [], [fac_kingdom_1, fac_kingdom_4, fac_kingdom_5] ],
["bastard_sword_b", "Heavy Bastard Sword", [("bastard_sword_b",0),("bastard_sword_b_scabbard", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 526 , weight(2.25)|abundance(100)|difficulty(9)|spd_rtng(97) | weapon_length(105)|swing_damage(37 , cut) | thrust_damage(27 ,  pierce),imodbits_sword_high, [], [fac_kingdom_1, fac_kingdom_4] ],
["bastard_sword_c", "Long Bastard Sword", [("bastard_sword",0),("scab_bastardsw", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 724 , weight(2.5)|abundance(100)|difficulty(10)|spd_rtng(96) | weapon_length(120)|swing_damage(39 , cut) | thrust_damage(28 ,  pierce),imodbits_sword_high, [], [fac_kingdom_1, fac_kingdom_5] ],
 
# Two-Handed Weapons
####################

# Blunts
["maul",         "Maul", [("maul_b",0)], itp_crush_through|itp_type_two_handed_wpn|itp_merchandise|itp_can_knock_down |itp_primary|itp_two_handed|itp_wooden_parry|itp_wooden_attack|itp_unbalanced, itc_nodachi|itcf_carry_spear, 
97 , weight(6)|abundance(100)|difficulty(11)|spd_rtng(83) | weapon_length(79)|swing_damage(36 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["sledgehammer", "Sledgehammer", [("maul_c",0)], itp_crush_through|itp_type_two_handed_wpn|itp_merchandise|itp_can_knock_down|itp_primary|itp_two_handed|itp_wooden_parry|itp_wooden_attack|itp_unbalanced, itc_nodachi|itcf_carry_spear, 
101 , weight(7)|abundance(100)|difficulty(12)|spd_rtng(81) | weapon_length(82)|swing_damage(39, blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["warhammer",    "Great Hammer", [("maul_d",0)], itp_crush_through|itp_type_two_handed_wpn|itp_merchandise|itp_can_knock_down|itp_primary|itp_two_handed|itp_wooden_parry|itp_wooden_attack|itp_unbalanced, itc_nodachi|itcf_carry_spear, 
290 , weight(9)|abundance(100)|difficulty(14)|spd_rtng(79) | weapon_length(75)|swing_damage(45 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace, [], [fac_kingdom_1, fac_kingdom_4, fac_kingdom_5] ],
["sarranid_two_handed_mace_1", "Iron Mace", [("mace_long_d",0)], itp_type_two_handed_wpn|itp_can_knock_down|itp_two_handed|itp_merchandise| itp_primary|itp_crush_through|itp_unbalanced, itc_greatsword|itcf_carry_axe_back,
470 , weight(4.5)|abundance(100)|difficulty(0)|spd_rtng(90) | weapon_length(95)|swing_damage(35 , blunt) | thrust_damage(22 ,  blunt),imodbits_mace, [], [fac_kingdom_6] ],

# Swords
["broadsword",  "Executioner's Sword", [("broadsword",0),("scab_broadsword", ixmesh_carry)], itp_type_two_handed_wpn| itp_two_handed|itp_primary, itc_nodachi|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 322 , weight(2.5)|abundance(0)|difficulty(8)|spd_rtng(91) | weapon_length(101)|swing_damage(38 , cut) | thrust_damage(0 ,  pierce),imodbits_sword, [], [fac_no_faction] ],
["great_sword",  "Great Sword", [("b_bastard_sword",0),("scab_bastardsw_b", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back|itcf_show_holster_when_drawn,
 423 , weight(2.75)|abundance(100)|difficulty(10)|spd_rtng(95) | weapon_length(125)|swing_damage(39 , cut) | thrust_damage(31 ,  pierce),imodbits_sword_high, [], [fac_kingdom_4] ],
["sword_of_war", "Sword of War", [("b_bastard_sword",0),("scab_bastardsw_b", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back|itcf_show_holster_when_drawn,
 524 , weight(3)|abundance(100)|difficulty(11)|spd_rtng(94) | weapon_length(130)|swing_damage(40 , cut) | thrust_damage(31 ,  pierce),imodbits_sword_high, [], [fac_kingdom_4] ],
["sword_two_handed_b", "Two Handed Sword", [("sword_two_handed_b",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back,
 670 , weight(2.75)|abundance(100)|difficulty(10)|spd_rtng(97) | weapon_length(110)|swing_damage(40 , cut) | thrust_damage(28 ,  pierce),imodbits_sword_high, [], [fac_kingdom_1, fac_kingdom_5] ],
["sword_two_handed_a", "Great Sword", [("sword_two_handed_a",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back,
 1123 , weight(2.75)|abundance(100)|difficulty(10)|spd_rtng(96) | weapon_length(120)|swing_damage(42 , cut) | thrust_damage(29 ,  pierce),imodbits_sword_high, [], [fac_kingdom_1, fac_kingdom_5] ],

["khergit_sword_two_handed_a", "Two Handed Sabre", [("khergit_sword_two_handed_a",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary, itc_nodachi|itcf_carry_sword_back,
 523 , weight(2.75)|abundance(100)|difficulty(10)|spd_rtng(96) | weapon_length(120)|swing_damage(40 , cut) | thrust_damage(0 ,  pierce),imodbits_sword_high, [], [fac_kingdom_3] ],
["khergit_sword_two_handed_b", "Two Handed Sabre", [("khergit_sword_two_handed_b",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary, itc_nodachi|itcf_carry_sword_back,
 920 , weight(2.75)|abundance(100)|difficulty(10)|spd_rtng(96) | weapon_length(120)|swing_damage(44 , cut) | thrust_damage(0 ,  pierce),imodbits_sword_high, [], [fac_kingdom_3] ],

["two_handed_cleaver", "War Cleaver", [("military_cleaver_a",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary, itc_nodachi|itcf_carry_sword_back,
 640 , weight(2.75)|abundance(100)|difficulty(10)|spd_rtng(93) | weapon_length(120)|swing_damage(45 , cut) | thrust_damage(0 ,  cut),imodbits_sword_high, [], [fac_kingdom_5] ],

# Axes
["axe",                 "Axe", [("iron_ax",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 
65 , weight(4)|abundance(100)|difficulty(8)|spd_rtng(91) | weapon_length(108)|swing_damage(32 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["voulge",         "Voulge", [("voulge",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 
129 , weight(4.5)|abundance(100)|difficulty(8)|spd_rtng(87) | weapon_length(119)|swing_damage(35 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["battle_axe",         "Battle Axe", [("battle_ax",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 
240 , weight(5)|abundance(100)|difficulty(9)|spd_rtng(88) | weapon_length(108)|swing_damage(41 , cut) | thrust_damage(0 ,  pierce),imodbits_axe, [], [fac_kingdom_2] ],
["war_axe",         "War Axe", [("war_ax",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 
264 , weight(5)|abundance(100)|difficulty(10)|spd_rtng(86) | weapon_length(110)|swing_damage(43 , cut) | thrust_damage(0 ,  pierce),imodbits_axe, [], [fac_kingdom_2] ],
["double_axe",     "Headsman's Axe", [("dblhead_ax",0)], itp_type_two_handed_wpn|itp_crush_through|itp_unbalanced|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back,
 359 , weight(6.5)|abundance(0)|difficulty(12)|spd_rtng(85) | weapon_length(95)|swing_damage(50 , cut) | thrust_damage(0 ,  pierce),imodbits_axe, [], [fac_no_faction] ],
["great_axe", "Great Axe", [("great_ax",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
 415 , weight(7)|abundance(100)|difficulty(13)|spd_rtng(82) | weapon_length(120)|swing_damage(45 , cut) | thrust_damage(0 ,  pierce),imodbits_axe, [], [fac_kingdom_4] ],
["two_handed_axe",         "Two Handed Axe", [("two_handed_battle_axe_a",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
 90 , weight(4.5)|abundance(100)|difficulty(10)|spd_rtng(96) | weapon_length(90)|swing_damage(38 , cut) | thrust_damage(0 ,  pierce),imodbits_axe, [], [fac_kingdom_4] ],
["two_handed_battle_axe_2",         "Two Handed War Axe", [("two_handed_battle_axe_b",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
 152 , weight(4.5)|abundance(100)|difficulty(10)|spd_rtng(96) | weapon_length(92)|swing_damage(44 , cut) | thrust_damage(0 ,  pierce),imodbits_axe, [], [fac_kingdom_4] ],
["great_axe_2",         "Great Axe", [("two_handed_battle_axe_e",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
 316 , weight(4.5)|abundance(100)|difficulty(10)|spd_rtng(94) | weapon_length(96)|swing_damage(47 , cut) | thrust_damage(0 ,  pierce),imodbits_axe, [], [fac_kingdom_4] ],
["sarranid_two_handed_axe_a",         "Sarranid Battle Axe", [("two_handed_battle_axe_g",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
 350 , weight(3.0)|abundance(100)|difficulty(10)|spd_rtng(89) | weapon_length(95)|swing_damage(49 , cut) | thrust_damage(0 ,  pierce),imodbits_axe, [], [fac_kingdom_6] ],
["sarranid_two_handed_axe_a_alt",     "Sarranid Battle Axe", [("two_handed_battle_axe_g_alt",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
 350 , weight(3.0)|spd_rtng(89) | weapon_length(95)|swing_damage(40 , blunt) | thrust_damage(0 ,  pierce),imodbits_axe, [], [fac_no_faction] ],
["sarranid_two_handed_axe_b",         "Sarranid War Axe", [("two_handed_battle_axe_h",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
 280 , weight(2.50)|abundance(100)|difficulty(10)|spd_rtng(90) | weapon_length(90)|swing_damage(46 , cut) | thrust_damage(0 ,  pierce),imodbits_axe, [], [fac_kingdom_6] ],
["sarranid_two_handed_axe_b_alt",     "Sarranid War Axe", [("two_handed_battle_axe_h_alt",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
 280 , weight(2.50)|spd_rtng(90) | weapon_length(90)|swing_damage(40 , pierce) | thrust_damage(0 ,  pierce),imodbits_axe, [], [fac_no_faction] ],

# Long Axes
["long_axe",         "Long Axe", [("long_axe_a",0)], itp_type_polearm|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_next_item_as_melee|itp_unbalanced|itp_merchandise,itc_staff|itcf_carry_axe_back,
 390 , weight(4.75)|abundance(100)|difficulty(10)|spd_rtng(93) | weapon_length(120)|swing_damage(46 , cut) | thrust_damage(19 ,  blunt),imodbits_axe, [], [fac_kingdom_4] ],
["long_axe_alt",         "Long Axe", [("long_axe_a",0)],itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
 390 , weight(4.75)|abundance(0)|difficulty(10)|spd_rtng(88) | weapon_length(120)|swing_damage(46 , cut) | thrust_damage(0 ,  pierce),imodbits_axe, [], [fac_no_faction] ],
["long_axe_b",         "Long War Axe", [("long_axe_b",0)], itp_type_polearm| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_next_item_as_melee|itp_unbalanced|itp_merchandise, itc_staff|itcf_carry_axe_back,
 510 , weight(5.0)|abundance(100)|difficulty(10)|spd_rtng(92) | weapon_length(125)|swing_damage(50 , cut) | thrust_damage(18 ,  blunt),imodbits_axe, [], [fac_kingdom_4] ],
["long_axe_b_alt",         "Long War Axe", [("long_axe_b",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
 510 , weight(5.0)|abundance(0)|difficulty(10)|spd_rtng(87) | weapon_length(125)|swing_damage(50 , cut) | thrust_damage(0 ,  pierce),imodbits_axe, [], [fac_no_faction] ],
["long_axe_c",         "Great Long Axe", [("long_axe_c",0)], itp_type_polearm| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_next_item_as_melee|itp_unbalanced|itp_merchandise, itc_staff|itcf_carry_axe_back,
 660 , weight(5.5)|abundance(100)|difficulty(10)|spd_rtng(91) | weapon_length(127)|swing_damage(54 , cut) | thrust_damage(19 ,  blunt),imodbits_axe, [], [fac_kingdom_4] ],
["long_axe_c_alt",      "Great Long Axe", [("long_axe_c",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
 660 , weight(5.5)|abundance(0)|difficulty(10)|spd_rtng(85) | weapon_length(127)|swing_damage(54 , cut) | thrust_damage(0 ,  pierce),imodbits_axe, [], [fac_no_faction] ],

# Shortened Polearms
["shortened_voulge",         "Shortened Voulge", [("two_handed_battle_axe_c",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
 228 , weight(4.5)|abundance(100)|difficulty(10)|spd_rtng(92) | weapon_length(100)|swing_damage(45 , cut) | thrust_damage(0 ,  pierce),imodbits_axe, [], [fac_kingdom_1, fac_kingdom_5] ],
["shortened_military_scythe",         "Shortened Military Scythe", [("two_handed_battle_scythe_a",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary, itc_nodachi|itcf_carry_sword_back,
 264 , weight(3.0)|abundance(100)|difficulty(10)|spd_rtng(90) | weapon_length(112)|swing_damage(45 , cut) | thrust_damage(0 ,  pierce),imodbits_sword_high, [], [fac_kingdom_2, fac_kingdom_4] ],
["bardiche",         "Bardiche", [("two_handed_battle_axe_d",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
 291 , weight(4.75)|abundance(100)|difficulty(10)|spd_rtng(91) | weapon_length(102)|swing_damage(47 , cut) | thrust_damage(0 ,  pierce),imodbits_axe, [], [fac_kingdom_2] ],
["great_bardiche",         "Great Bardiche", [("two_handed_battle_axe_f",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
 617 , weight(5.0)|abundance(100)|difficulty(10)|spd_rtng(89) | weapon_length(116)|swing_damage(50 , cut) | thrust_damage(0 ,  pierce),imodbits_axe, [], [fac_kingdom_2] ],

# Polearms
##########

# Staff
["staff",         "Staff", [("wooden_staff",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack, itc_staff|itcf_carry_sword_back,
 36 , weight(1.5)|abundance(100)|difficulty(0)|spd_rtng(100) | weapon_length(130)|swing_damage(18 , blunt) | thrust_damage(19 ,  blunt),imodbits_polearm ],
["quarter_staff", "Quarter Staff", [("quarter_staff",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry|itp_wooden_attack, itc_staff|itcf_carry_sword_back,
 60 , weight(2)|abundance(100)|difficulty(0)|spd_rtng(104) | weapon_length(140)|swing_damage(20 , blunt) | thrust_damage(20 ,  blunt),imodbits_polearm ],
["iron_staff",         "Iron Staff", [("iron_staff",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary, itc_staff|itcf_carry_sword_back,
 202 , weight(2)|abundance(100)|difficulty(0)|spd_rtng(97) | weapon_length(140)|swing_damage(25 , blunt) | thrust_damage(26 ,  blunt),imodbits_polearm, [], [fac_kingdom_6] ],

# Spear 
["shortened_spear",         "Shortened Spear", [("spear_g_1-9m",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry|itp_no_blur, itc_spear|itcf_carry_spear,
 53 , weight(2.0)|abundance(100)|difficulty(0)|spd_rtng(102) | weapon_length(120)|swing_damage(0 , blunt) | thrust_damage(25 ,  pierce),imodbits_polearm ],
["shortened_spear_throw",         "Shortened Spear", [("spear_g_1-9m",0)], itp_type_thrown|itp_primary ,itcf_throw_javelin, 
 53 , weight(2.0)|difficulty(0)|spd_rtng(98) | shoot_speed(20) | thrust_damage(48, pierce)|max_ammo(1)|weapon_length(110),imodbits_thrown, [], [fac_no_faction] ],
["spear",         "Spear", [("spear_h_2-15m",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry|itp_no_blur, itc_spear|itcf_carry_spear,
 85 , weight(2.25)|abundance(100)|difficulty(0)|spd_rtng(98) | weapon_length(135)|swing_damage(0 , blunt) | thrust_damage(26 ,  pierce),imodbits_polearm ],
["boar_spear",         "Boar Spear", [("spear",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry,itc_cutting_spear|itcf_carry_spear, 
 76 , weight(1.5)|abundance(100)|difficulty(0)|spd_rtng(90) | weapon_length(157)|swing_damage(26 , cut) | thrust_damage(23 ,  pierce),imodbits_polearm, [], [fac_kingdom_2, fac_kingdom_4] ],
["bamboo_spear",         "Bamboo Spear", [("arabian_spear_a_3m",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_no_blur, itc_spear|itcf_carry_spear,
 80 , weight(2.0)|abundance(100)|difficulty(0)|spd_rtng(88) | weapon_length(200)|swing_damage(0 , blunt) | thrust_damage(20 ,  pierce),imodbits_polearm, [], [fac_kingdom_3, fac_kingdom_6] ],
["war_spear",         "War Spear", [("spear_i_2-3m",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry|itp_no_blur, itc_spear|itcf_carry_spear,
 140 , weight(2.5)|abundance(100)|difficulty(0)|spd_rtng(95) | weapon_length(150)|swing_damage(0 , blunt) | thrust_damage(27 ,  pierce),imodbits_polearm ],

# Lance
["double_sided_lance", "Double Sided Lance", [("lance_dblhead",0)], itp_couchable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff,
 261 , weight(4.0)|abundance(100)|difficulty(0)|spd_rtng(95) | weapon_length(128)|swing_damage(25, cut) | thrust_damage(27 ,  pierce),imodbits_polearm ],
["light_lance",         "Light Lance", [("spear_b_2-75m",0)], itp_couchable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_no_blur, itc_spear,
 180 , weight(2.5)|abundance(100)|difficulty(0)|spd_rtng(85) | weapon_length(175)|swing_damage(0 , blunt) | thrust_damage(27 ,  pierce),imodbits_polearm ],
["lance",         "Lance", [("spear_d_2-8m",0)], itp_couchable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_no_blur, itc_spear,
 270 , weight(2.5)|abundance(100)|difficulty(0)|spd_rtng(80) | weapon_length(180)|swing_damage(0 , blunt) | thrust_damage(26 ,  pierce),imodbits_polearm ],
["heavy_lance",         "Heavy Lance", [("spear_f_2-9m",0)], itp_couchable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_no_blur, itc_spear,
 360 , weight(2.75)|abundance(100)|difficulty(10)|spd_rtng(75) | weapon_length(190)|swing_damage(0 , blunt) | thrust_damage(26 ,  pierce),imodbits_polearm ],
["great_lance",         "Great Lance", [("heavy_lance",0)], itp_couchable|itp_type_polearm|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_greatlance, 
 410 , weight(5)|abundance(100)|difficulty(11)|spd_rtng(55) | weapon_length(240)|swing_damage(0 , cut) | thrust_damage(21 ,  pierce),imodbits_polearm, [], [fac_kingdom_1] ],
["jousting_lance", "Jousting Lance", [("joust_of_peace",0)], itp_couchable|itp_type_polearm|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_greatlance,
 158 , weight(5)|abundance(100)|difficulty(0)|spd_rtng(61) | weapon_length(240)|swing_damage(0 , cut) | thrust_damage(17 ,  blunt),imodbits_polearm, [], [fac_kingdom_1] ],

# Pike
["pike",         "Long Pike", [("spear_a_3m",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed|itp_is_pike|itp_no_blur, itc_pike,
 125 , weight(3.0)|abundance(100)|difficulty(0)|spd_rtng(81) | weapon_length(245)|swing_damage(0 , blunt) | thrust_damage(26 ,  pierce),imodbits_polearm, [], [fac_kingdom_1, fac_kingdom_4, fac_kingdom_5] ],
["ashwood_pike", "Heavy Pike", [("pike",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_two_handed|itp_wooden_parry|itp_is_pike|itp_no_blur, itc_pike,
 205 , weight(3.5)|abundance(100)|difficulty(9)|spd_rtng(90) | weapon_length(170)|swing_damage(0 , blunt) | thrust_damage(29,  pierce),imodbits_polearm ],
["awlpike",    "Awlpike", [("awl_pike_b",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_no_blur, itc_spear|itcf_carry_spear,
 345 , weight(2.25)|abundance(100)|difficulty(0)|spd_rtng(92) | weapon_length(165)|swing_damage(0 , blunt) | thrust_damage(33 ,  pierce),imodbits_polearm, [], [fac_kingdom_1, fac_kingdom_5] ],
["awlpike_long",  "Long Awlpike", [("awl_pike_a",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_no_blur, itc_spear|itcf_carry_spear,
 385 , weight(2.25)|abundance(100)|difficulty(0)|spd_rtng(89) | weapon_length(185)|swing_damage(0 , blunt) | thrust_damage(32 ,  pierce),imodbits_polearm, [], [fac_kingdom_1, fac_kingdom_5] ],

# Hammer
["bec_de_corbin_a",  "Footman's Hammer", [("bec_de_corbin_alt",0)], itp_type_polearm|itp_merchandise|itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed, itc_staff|itcf_carry_spear,
 225 , weight(3.0)|abundance(100)|difficulty(0)|spd_rtng(81) | weapon_length(120)|swing_damage(38, blunt) | thrust_damage(38 ,  pierce),imodbits_polearm, [], [fac_kingdom_1, fac_kingdom_5] ],
["bec_de_corbin_b",  "Footman's Hammer", [("bec_de_corbin_a",0)], itp_type_polearm|itp_merchandise|itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed, itc_staff|itcf_carry_spear,
 225 , weight(3.0)|spd_rtng(81) | weapon_length(120)|swing_damage(38, pierce) | thrust_damage(38 ,  pierce),imodbits_polearm, [], [fac_no_faction] ],
["polehammer",         "Polehammer", [("pole_hammer",0)], itp_type_polearm|itp_offset_lance|itp_primary|itp_two_handed|itp_can_knock_down|itp_unbalanced|itp_wooden_parry, itc_guandao,
 169 , weight(7)|abundance(0)|difficulty(18)|spd_rtng(70) | weapon_length(126)|swing_damage(50 , blunt) | thrust_damage(35 ,  blunt),imodbits_polearm, [], [fac_no_faction] ],

# Mace
["long_spiked_club",         "Long Spiked Club", [("mace_long_c",0)], itp_type_polearm|itp_can_knock_down|itp_merchandise|itp_next_item_as_melee|itp_primary|itp_wooden_parry, itc_staff|itcf_carry_axe_back,
 264 , weight(3)|abundance(100)|difficulty(0)|spd_rtng(96) | weapon_length(126)|swing_damage(23 , pierce) | thrust_damage(20 ,  blunt),imodbits_mace ],
["long_spiked_club_alt",     "Long Spiked Club", [("mace_long_c",0)], itp_type_two_handed_wpn|itp_can_knock_down|itp_primary|itp_two_handed|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back,
 264 , weight(3)|abundance(0)|difficulty(0)|spd_rtng(91) | weapon_length(126)|swing_damage(23 , pierce) | thrust_damage(0 ,  blunt),imodbits_mace, [], [fac_no_faction] ],
["long_hafted_knobbed_mace",        "Long Hafted Knobbed Mace", [("mace_long_a",0)], itp_type_polearm| itp_can_knock_down|itp_merchandise|itp_next_item_as_melee|itp_primary|itp_wooden_parry, itc_staff|itcf_carry_axe_back,
 324 , weight(3)|abundance(100)|difficulty(0)|spd_rtng(95) | weapon_length(133)|swing_damage(26 , blunt) | thrust_damage(23 ,  blunt),imodbits_mace ],
["long_hafted_knobbed_mace_alt",    "Long Hafted Knobbed Mace", [("mace_long_a",0)], itp_type_two_handed_wpn| itp_can_knock_down|itp_primary|itp_two_handed|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back,
 324 , weight(3)|abundance(0)|difficulty(0)|spd_rtng(90) | weapon_length(133)|swing_damage(26 , blunt) | thrust_damage(0 ,  blunt),imodbits_mace, [], [fac_no_faction] ],
["long_hafted_spiked_mace",         "Long Hafted Spiked Mace", [("mace_long_b",0)], itp_type_polearm|itp_can_knock_down|itp_merchandise|itp_next_item_as_melee|itp_primary|itp_wooden_parry, itc_staff|itcf_carry_axe_back,
 310 , weight(3)|abundance(100)|difficulty(0)|spd_rtng(94) | weapon_length(140)|swing_damage(28 , blunt) | thrust_damage(26 ,  blunt),imodbits_mace ],
["long_hafted_spiked_mace_alt",     "Long Hafted Spiked Mace", [("mace_long_b",0)], itp_type_two_handed_wpn|itp_can_knock_down|itp_primary|itp_two_handed|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back,
 310 , weight(3)|abundance(0)|difficulty(0)|spd_rtng(89) | weapon_length(140)|swing_damage(28 , blunt) | thrust_damage(0 ,  blunt),imodbits_mace, [], [fac_no_faction] ],

# Axe
["long_voulge",         "Voulge", [("two_handed_battle_long_axe_a",0)], itp_type_polearm|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_staff,
 120 , weight(3.0)|abundance(100)|difficulty(10)|spd_rtng(88) | weapon_length(175)|swing_damage(40 , cut) | thrust_damage(18 ,  pierce),imodbits_axe, [], [fac_kingdom_1, fac_kingdom_5] ],
["long_bardiche",         "Long Bardiche", [("two_handed_battle_long_axe_b",0)], itp_type_polearm|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_staff,
390 , weight(4.75)|abundance(100)|difficulty(11)|spd_rtng(89) | weapon_length(140)|swing_damage(48 , cut) | thrust_damage(17 ,  pierce),imodbits_axe, [], [fac_kingdom_2] ],
["great_long_bardiche",         "Great Long Bardiche", [("two_handed_battle_long_axe_c",0)], itp_type_polearm|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_staff,
 660 , weight(5.0)|abundance(100)|difficulty(12)|spd_rtng(88) | weapon_length(155)|swing_damage(50 , cut) | thrust_damage(17 ,  pierce),imodbits_axe, [], [fac_kingdom_2] ],
["poleaxe",         "Poleaxe", [("pole_ax",0)], itp_type_polearm|itp_offset_lance|itp_merchandise|itp_cant_use_on_horseback|itp_primary|itp_two_handed|itp_wooden_parry, itc_staff,
 384 , weight(4.5)|abundance(100)|difficulty(13)|spd_rtng(77) | weapon_length(180)|swing_damage(50 , cut) | thrust_damage(15 ,  blunt),imodbits_polearm, [], [fac_kingdom_2, fac_kingdom_4] ],

# Blade
["scythe",         "Scythe", [("scythe",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_staff|itcf_carry_spear,
 43 , weight(2)|abundance(100)|difficulty(0)|spd_rtng(97) | weapon_length(182)|swing_damage(30 , cut) | thrust_damage(14 ,  pierce),imodbits_polearm ],
["military_scythe",         "Military Scythe", [("spear_e_2-5m",0),("spear_c_2-5m",imodbits_bad)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_staff|itcf_carry_spear,
 155 , weight(2.5)|abundance(100)|difficulty(0)|spd_rtng(90) | weapon_length(155)|swing_damage(36 , cut) | thrust_damage(25 ,  pierce),imodbits_polearm, [], [fac_kingdom_2, fac_kingdom_4] ],
["long_military_scythe", "Long Military Scythe", [("spear_e_3-25m",0)], itp_couchable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear,
 315 , weight(3.5)|abundance(100)|difficulty(0)|spd_rtng(78) | weapon_length(230)|swing_damage(36 , cut) | thrust_damage(24 ,  pierce),imodbits_polearm, [], [fac_kingdom_2, fac_kingdom_4] ],
["hafted_blade_b",         "Hafted Blade", [("khergit_pike_b",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_two_handed|itp_penalty_with_shield|itp_wooden_parry, itcf_carry_spear|itc_guandao,
 185 , weight(2.75)|abundance(100)|difficulty(0)|spd_rtng(95) | weapon_length(135)|swing_damage(37 , cut) | thrust_damage(20 ,  pierce),imodbits_polearm, [], [fac_kingdom_3] ],
["hafted_blade_a",         "Hafted Blade", [("khergit_pike_a",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_two_handed|itp_penalty_with_shield|itp_wooden_parry, itcf_carry_spear|itc_guandao,
 350 , weight(3.25)|abundance(100)|difficulty(0)|spd_rtng(93) | weapon_length(153)|swing_damage(39 , cut) | thrust_damage(19 ,  pierce),imodbits_polearm, [], [fac_kingdom_3] ],
["glaive",         "Glaive", [("glaive_b",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_two_handed|itp_wooden_parry, itc_staff|itcf_carry_spear,
 352 , weight(4.5)|abundance(100)|difficulty(0)|spd_rtng(90) | weapon_length(157)|swing_damage(39 , cut) | thrust_damage(21 ,  pierce),imodbits_polearm, [], [fac_kingdom_1, fac_kingdom_5] ],

# Fork
["pitch_fork",         "Pitch Fork", [("pitch_fork",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_no_blur,itc_spear,
 19 , weight(1.5)|abundance(100)|difficulty(0)|spd_rtng(87) | weapon_length(154)|swing_damage(0 , blunt) | thrust_damage(22 ,  pierce),imodbits_polearm ],
["military_fork", "Military Fork", [("military_fork",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry|itp_no_blur,itc_spear,
 153 , weight(2)|abundance(100)|difficulty(0)|spd_rtng(95) | weapon_length(135)|swing_damage(0 , blunt) | thrust_damage(30 ,  pierce),imodbits_polearm, [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_4, fac_kingdom_5] ],
["battle_fork",         "Battle Fork", [("battle_fork",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry|itp_no_blur,itc_spear,
 282 , weight(2.2)|abundance(100)|difficulty(0)|spd_rtng(90) | weapon_length(144)|swing_damage(0, blunt) | thrust_damage(35 ,  pierce),imodbits_polearm, [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_4, fac_kingdom_5] ],
["trident",         "Trident", [("trident",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_no_blur,itc_spear,
 190 , weight(2.5)|abundance(100)|difficulty(0)|spd_rtng(85) | weapon_length(157)|swing_damage(0 , blunt) | thrust_damage(33 ,  pierce),imodbits_polearm, [], [fac_kingdom_1, fac_kingdom_4, fac_kingdom_5] ],

#######################
# SHIELDS - Slots 0-3 #
#######################
# Keep wooden_shield in front!

# Large Round Shields
["wooden_shield", "Wooden Shield", [("shield_round_a",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  42 , weight(2)|abundance(40)|hit_points(360)|body_armor(1)|spd_rtng(100)|shield_width(50),imodbits_shield ],
["nordic_shield", "Nordic Shield", [("shield_round_b",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  95 , weight(2)|abundance(40)|hit_points(440)|body_armor(1)|spd_rtng(100)|shield_width(50),imodbits_shield, [], [fac_kingdom_2, fac_kingdom_4] ],

# Small Round Shields
["wooden_round_shield", "Wooden Round Shield", [("shield_round_g",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  60 , weight(2)|abundance(40)|hit_points(240)|body_armor(6)|spd_rtng(102)|shield_width(40),imodbits_shield ],
["hide_covered_round_shield", "Hide Covered Round Shield", [("shield_round_f",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  40 , weight(2)|abundance(40)|hit_points(260)|body_armor(3)|spd_rtng(100)|shield_width(40),imodbits_shield, [], [fac_kingdom_2, fac_kingdom_3] ],
["leather_covered_round_shield", "Leather Covered Round Shield", [("shield_round_d",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  80 , weight(2.5)|abundance(40)|hit_points(310)|body_armor(8)|spd_rtng(96)|shield_width(40),imodbits_shield ],
["plate_covered_round_shield", "Plate Covered Round Shield", [("shield_round_e",0)], itp_merchandise|itp_type_shield, itcf_carry_round_shield,  140 , weight(4)|abundance(20)|hit_points(330)|body_armor(16)|spd_rtng(90)|shield_width(40),imodbits_shield, [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_5] ],
["steel_shield", "Steel Shield", [("shield_dragon",0)], itp_merchandise|itp_type_shield, itcf_carry_round_shield,  697 , weight(4)|abundance(10)|hit_points(700)|body_armor(17)|spd_rtng(61)|shield_width(40),imodbits_shield, [], [fac_kingdom_1, fac_kingdom_5] ],

# Generic Heater Shields
["fur_covered_shield",  "Fur Covered Shield", [("shield_kite_m",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  227 , weight(3.5)|abundance(10)|hit_points(600)|body_armor(1)|spd_rtng(76)|shield_width(41)|shield_height(81),imodbits_shield, [], [fac_kingdom_2, fac_kingdom_3] ],
["shield_heater_c", "Heater Shield", [("shield_heater_c",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  277 , weight(3.5)|abundance(10)|hit_points(410)|body_armor(2)|spd_rtng(80)|shield_width(32)|shield_height(60),imodbits_shield, [], [fac_kingdom_1] ],
["shield_heater_d", "Heater Shield", [("shield_heater_d",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  477 , weight(3.5)|abundance(10)|hit_points(710)|body_armor(4)|spd_rtng(80)|shield_width(30)|shield_height(50),imodbits_shield, [], [fac_kingdom_6] ],

# Nord Round Shields
["tab_shield_round_a", "Old Round Shield", [("tableau_shield_round_5",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  
26 , weight(2.5)|abundance(80)|hit_points(195)|body_armor(4)|spd_rtng(93)|shield_width(40),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_round_shield_5", ":agent_no", ":troop_no")])], [fac_kingdom_3, fac_kingdom_4, fac_kingdom_6]],
["tab_shield_round_b", "Plain Round Shield", [("tableau_shield_round_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  
65 , weight(3)|abundance(100)|hit_points(260)|body_armor(8)|spd_rtng(90)|shield_width(50),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_round_shield_3", ":agent_no", ":troop_no")])], [fac_kingdom_4]],
["tab_shield_round_c", "Round Shield", [("tableau_shield_round_2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  
105 , weight(3.5)|abundance(100)|hit_points(310)|body_armor(12)|spd_rtng(87)|shield_width(50),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner","tableau_round_shield_2", ":agent_no", ":troop_no")])], [fac_kingdom_4]],
["tab_shield_round_d", "Heavy Round Shield", [("tableau_shield_round_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  
210 , weight(4)|abundance(50)|hit_points(350)|body_armor(15)|spd_rtng(84)|shield_width(50),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_round_shield_1", ":agent_no", ":troop_no")])], [fac_kingdom_4]],
["tab_shield_round_e", "Huscarl's Round Shield", [("tableau_shield_round_4",0)], itp_merchandise|itp_type_shield, itcf_carry_round_shield,  
430 , weight(4.5)|abundance(25)|hit_points(410)|body_armor(19)|spd_rtng(81)|shield_width(50),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_round_shield_4", ":agent_no", ":troop_no")])], [fac_kingdom_4]],

# Vaegir Kite Shields (also Sarranid Infantry)
["tab_shield_kite_a", "Old Kite Shield",   [("tableau_shield_kite_1" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  
33 , weight(2)|abundance(80)|hit_points(165)|body_armor(5)|spd_rtng(96)|shield_width(36)|shield_height(70),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_kite_shield_1", ":agent_no", ":troop_no")])], [fac_kingdom_2, fac_kingdom_6]],
["tab_shield_kite_b", "Plain Kite Shield",   [("tableau_shield_kite_3" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  
70 , weight(2.5)|abundance(100)|hit_points(215)|body_armor(10)|spd_rtng(93)|shield_width(36)|shield_height(70),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_kite_shield_3", ":agent_no", ":troop_no")])], [fac_kingdom_2, fac_kingdom_6]],
["tab_shield_kite_c", "Kite Shield",   [("tableau_shield_kite_2" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  
156 , weight(3)|abundance(100)|hit_points(265)|body_armor(13)|spd_rtng(90)|shield_width(36)|shield_height(70),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_kite_shield_2", ":agent_no", ":troop_no")])], [fac_kingdom_2, fac_kingdom_6]],
["tab_shield_kite_d", "Heavy Kite Shield",   [("tableau_shield_kite_2" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  
320 , weight(3.5)|abundance(50)|hit_points(310)|body_armor(18)|spd_rtng(87)|shield_width(36)|shield_height(70),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_kite_shield_2", ":agent_no", ":troop_no")])], [fac_kingdom_2, fac_kingdom_6]],
["tab_shield_kite_cav_a", "Horseman's Kite Shield",   [("tableau_shield_kite_4" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  
205 , weight(2)|abundance(40)|hit_points(165)|body_armor(14)|spd_rtng(103)|shield_width(30)|shield_height(50),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_kite_shield_4", ":agent_no", ":troop_no")])], [fac_kingdom_2, fac_kingdom_4]],
["tab_shield_kite_cav_b", "Knightly Kite Shield",   [("tableau_shield_kite_4" ,0)], itp_merchandise|itp_type_shield, itcf_carry_kite_shield,  
360 , weight(2.5)|abundance(20)|hit_points(225)|body_armor(23)|spd_rtng(100)|shield_width(30)|shield_height(50),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_kite_shield_4", ":agent_no", ":troop_no")])], [fac_kingdom_2, fac_kingdom_4]],

# Swadian Heater Shields
["tab_shield_heater_a", "Old Heater Shield",   [("tableau_shield_heater_1" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  
36 , weight(2)|abundance(80)|hit_points(160)|body_armor(6)|spd_rtng(96)|shield_width(36)|shield_height(70),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heater_shield_1", ":agent_no", ":troop_no")])], [fac_kingdom_1]],
["tab_shield_heater_b", "Plain Heater Shield",   [("tableau_shield_heater_1" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  
74 , weight(2.5)|abundance(100)|hit_points(210)|body_armor(11)|spd_rtng(93)|shield_width(36)|shield_height(70),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heater_shield_1", ":agent_no", ":troop_no")])], [fac_kingdom_1]],
["tab_shield_heater_c", "Heater Shield",   [("tableau_shield_heater_1" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  
160 , weight(3)|abundance(100)|hit_points(260)|body_armor(14)|spd_rtng(90)|shield_width(36)|shield_height(70),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heater_shield_1", ":agent_no", ":troop_no")])], [fac_kingdom_1]],
["tab_shield_heater_d", "Heavy Heater Shield",   [("tableau_shield_heater_1" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  
332 , weight(3.5)|abundance(50)|hit_points(305)|body_armor(19)|spd_rtng(87)|shield_width(36)|shield_height(70),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heater_shield_1", ":agent_no", ":troop_no")])], [fac_kingdom_1]],
["tab_shield_heater_cav_a", "Horseman's Heater Shield",   [("tableau_shield_heater_2" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  
229 , weight(2)|abundance(40)|hit_points(160)|body_armor(16)|spd_rtng(103)|shield_width(30)|shield_height(50),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heater_shield_2", ":agent_no", ":troop_no")])], [fac_kingdom_1]],
["tab_shield_heater_cav_b", "Knightly Heater Shield",   [("tableau_shield_heater_2" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  
390 , weight(2.5)|abundance(20)|hit_points(220)|body_armor(23)|spd_rtng(100)|shield_width(30)|shield_height(50),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heater_shield_2", ":agent_no", ":troop_no")])], [fac_kingdom_1]],

# Rhodok Board Shields
["tab_shield_pavise_a", "Old Board Shield",   [("tableau_shield_pavise_2" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,  
60 , weight(3.5)|abundance(100)|hit_points(280)|body_armor(4)|spd_rtng(89)|shield_width(43)|shield_height(100),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_pavise_shield_2", ":agent_no", ":troop_no")])], [fac_kingdom_5]],
["tab_shield_pavise_b", "Plain Board Shield",   [("tableau_shield_pavise_2" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,  
114 , weight(4)|abundance(100)|hit_points(360)|body_armor(8)|spd_rtng(85)|shield_width(43)|shield_height(100),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_pavise_shield_2", ":agent_no", ":troop_no")])], [fac_kingdom_5]],
["tab_shield_pavise_c", "Board Shield",   [("tableau_shield_pavise_1" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,  
210 , weight(4.5)|abundance(100)|hit_points(430)|body_armor(10)|spd_rtng(81)|shield_width(43)|shield_height(100),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_pavise_shield_1", ":agent_no", ":troop_no")])], [fac_kingdom_5]],
["tab_shield_pavise_d", "Heavy Board Shield",   [("tableau_shield_pavise_1" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,  
370 , weight(5)|abundance(50)|hit_points(550)|body_armor(14)|spd_rtng(78)|shield_width(43)|shield_height(100),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_pavise_shield_1", ":agent_no", ":troop_no")])], [fac_kingdom_5]],

# Khergit Cavalry Shields (also Sarranid Cavalry)
["tab_shield_small_round_a", "Plain Cavalry Shield", [("tableau_shield_small_round_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  
96 , weight(2)|abundance(100)|hit_points(160)|body_armor(8)|spd_rtng(105)|shield_width(40),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_small_round_shield_3", ":agent_no", ":troop_no")])], [fac_kingdom_3, fac_kingdom_6]],
["tab_shield_small_round_b", "Round Cavalry Shield", [("tableau_shield_small_round_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  
195 , weight(2.5)|abundance(100)|hit_points(200)|body_armor(14)|spd_rtng(103)|shield_width(40),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_small_round_shield_1", ":agent_no", ":troop_no")])], [fac_kingdom_3, fac_kingdom_6]],
["tab_shield_small_round_c", "Elite Cavalry Shield", [("tableau_shield_small_round_2",0)], itp_merchandise|itp_type_shield, itcf_carry_round_shield,  
370 , weight(3)|abundance(40)|hit_points(250)|body_armor(22)|spd_rtng(100)|shield_width(40),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_small_round_shield_2", ":agent_no", ":troop_no")])], [fac_kingdom_3, fac_kingdom_6]],

# Obsolete Shields, kinda ugly
#["round_shield", "Round Shield", [("shield_round_c",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  64 , weight(2)|hit_points(400)|body_armor(1)|spd_rtng(100)|shield_width(50),imodbits_shield ],
#["kite_shield",  "Kite Shield", [("shield_kite_a",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|shield_width(90),imodbits_shield ],
#["kite_shield_", "Kite Shield", [("shield_kite_b",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|shield_width(90),imodbits_shield ],
#["large_shield", "Large Shield", [("shield_kite_c",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  165 , weight(2.5)|hit_points(520)|body_armor(1)|spd_rtng(80)|shield_width(92),imodbits_shield ],
#["battle_shield", "Battle Shield", [("shield_kite_d",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  196 , weight(3)|hit_points(560)|body_armor(1)|spd_rtng(78)|shield_width(94),imodbits_shield ],
#["heraldric_shield", "Heraldric Shield", [("shield_heraldic",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  301 , weight(3.5)|hit_points(640)|body_armor(1)|spd_rtng(83)|shield_width(65),imodbits_shield ],
#["heater_shield", "Heater Shield", [("shield_heater_a",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  477 , weight(3.5)|hit_points(710)|body_armor(4)|spd_rtng(80)|shield_width(60),imodbits_shield ],
#["nomad_shield", "Nomad Shield", [("shield_wood_b",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  12 , weight(2)|hit_points(260)|body_armor(6)|spd_rtng(110)|shield_width(30),imodbits_shield ],

# This shield uses the Faction's banner, not the Lord's banner
["shield_heater_faction", "Soldier's Heater Shield",   [("tableau_shield_heater_2" ,0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  
229 , weight(2)|abundance(0)|hit_points(160)|body_armor(16)|spd_rtng(103)|shield_width(30)|shield_height(50),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_tableau_item_set_troop_faction", "tableau_heater_shield_2", ":agent_no", ":troop_no")])], [fac_no_faction]],

# Decoration Kite Shields
["shield_kite_g", "Kite Shield", [("shield_kite_g",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|abundance(0)|hit_points(480)|body_armor(1)|spd_rtng(90)|shield_width(36)|shield_height(70),imodbits_shield, [], [fac_no_faction] ],
["shield_kite_h", "Kite Shield", [("shield_kite_h",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|abundance(0)|hit_points(480)|body_armor(1)|spd_rtng(90)|shield_width(36)|shield_height(70),imodbits_shield, [], [fac_no_faction] ],
["shield_kite_i", "Kite Shield", [("shield_kite_i",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|abundance(0)|hit_points(480)|body_armor(1)|spd_rtng(90)|shield_width(36)|shield_height(70),imodbits_shield, [], [fac_no_faction] ],
["shield_kite_k", "Kite Shield", [("shield_kite_k",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|abundance(0)|hit_points(480)|body_armor(1)|spd_rtng(90)|shield_width(36)|shield_height(70),imodbits_shield, [], [fac_no_faction] ],
["norman_shield_1", "Kite Shield", [("norman_shield_1",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|abundance(0)|hit_points(480)|body_armor(1)|spd_rtng(90)|shield_width(36)|shield_height(70),imodbits_shield, [], [fac_no_faction] ],
["norman_shield_2", "Kite Shield", [("norman_shield_2",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|abundance(0)|hit_points(480)|body_armor(1)|spd_rtng(90)|shield_width(36)|shield_height(70),imodbits_shield, [], [fac_no_faction] ],
["norman_shield_3", "Kite Shield", [("norman_shield_3",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|abundance(0)|hit_points(480)|body_armor(1)|spd_rtng(90)|shield_width(36)|shield_height(70),imodbits_shield, [], [fac_no_faction] ],
["norman_shield_4", "Kite Shield", [("norman_shield_4",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|abundance(0)|hit_points(480)|body_armor(1)|spd_rtng(90)|shield_width(36)|shield_height(70),imodbits_shield, [], [fac_no_faction] ],
["norman_shield_5", "Kite Shield", [("norman_shield_5",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|abundance(0)|hit_points(480)|body_armor(1)|spd_rtng(90)|shield_width(36)|shield_height(70),imodbits_shield, [], [fac_no_faction] ],
["norman_shield_6", "Kite Shield", [("norman_shield_6",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|abundance(0)|hit_points(480)|body_armor(1)|spd_rtng(90)|shield_width(36)|shield_height(70),imodbits_shield, [], [fac_no_faction] ],
["norman_shield_7", "Kite Shield", [("norman_shield_7",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|abundance(0)|hit_points(480)|body_armor(1)|spd_rtng(90)|shield_width(36)|shield_height(70),imodbits_shield, [], [fac_no_faction] ],
["norman_shield_8", "Kite Shield", [("norman_shield_8",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|abundance(0)|hit_points(480)|body_armor(1)|spd_rtng(90)|shield_width(36)|shield_height(70),imodbits_shield, [], [fac_no_faction] ],

["test_shield", "Mesh-Based Shield", [("mesh_ui_kingdom_shield_7",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|abundance(0)|hit_points(480)|body_armor(1)|spd_rtng(90)|shield_width(36)|shield_height(70),imodbits_shield, [], [fac_no_faction] ],

##############################
# RANGED WEAPONS - Slots 0-3 #
##############################
# Keep darts in front!

# Throwing Spears
["darts",         "Darts", [("dart_b",0),("dart_b_bag", ixmesh_carry)], itp_type_thrown |itp_merchandise|itp_primary ,itcf_throw_javelin|itcf_carry_quiver_right_vertical|itcf_show_holster_when_drawn, 
155 , weight(4)|abundance(100)|difficulty(1)|spd_rtng(95) | shoot_speed(28) | thrust_damage(22 ,  pierce)|max_ammo(7)|weapon_length(32),imodbits_thrown ],
["war_darts",         "War Darts", [("dart_a",0),("dart_a_bag", ixmesh_carry)], itp_type_thrown |itp_merchandise|itp_primary ,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn, 
285 , weight(5)|abundance(100)|difficulty(1)|spd_rtng(93) | shoot_speed(27) | thrust_damage(25 ,  pierce)|max_ammo(7)|weapon_length(45),imodbits_thrown ],
["javelin",         "Javelins", [("javelin",0),("javelins_quiver_new", ixmesh_carry)], itp_type_thrown |itp_merchandise|itp_primary|itp_next_item_as_melee ,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn, 
300, weight(4)|abundance(100)|difficulty(1)|spd_rtng(91) | shoot_speed(25) | thrust_damage(34 ,  pierce)|max_ammo(5)|weapon_length(75),imodbits_thrown ],
["javelin_melee",         "Javelin", [("javelin",0)], itp_type_polearm|itp_primary|itp_wooden_parry|itp_no_blur , itc_spear, 
300, weight(1)|abundance(0)|difficulty(0)|spd_rtng(95) |swing_damage(0, cut)| thrust_damage(14,  pierce)|weapon_length(75),imodbits_polearm, [], [fac_no_faction] ],
["throwing_spears",         "Throwing Spears", [("jarid_new_b",0),("jarid_new_b_bag", ixmesh_carry)], itp_type_thrown |itp_merchandise|itp_primary|itp_next_item_as_melee ,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn, 
525 , weight(3)|abundance(100)|difficulty(2)|spd_rtng(87) | shoot_speed(22) | thrust_damage(44 ,  pierce)|max_ammo(4)|weapon_length(65),imodbits_thrown, [], [fac_kingdom_3, fac_kingdom_4] ],
["throwing_spear_melee",         "Throwing Spear", [("jarid_new_b",0),("javelins_quiver", ixmesh_carry)],itp_type_polearm|itp_primary|itp_wooden_parry|itp_no_blur , itc_spear, 
525 , weight(1)|abundance(0)|difficulty(1)|spd_rtng(91) | swing_damage(0, cut) | thrust_damage(23 ,  pierce)|weapon_length(75),imodbits_thrown, [], [fac_no_faction] ],
["jarid",         "Jarids", [("jarid_new",0),("jarid_quiver", ixmesh_carry)], itp_type_thrown |itp_merchandise|itp_primary|itp_next_item_as_melee ,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn, 
560 , weight(2.75)|abundance(100)|difficulty(2)|spd_rtng(89) | shoot_speed(24) | thrust_damage(45 ,  pierce)|max_ammo(4)|weapon_length(65),imodbits_thrown, [], [fac_kingdom_2, fac_kingdom_3, fac_kingdom_6] ],
["jarid_melee",         "Jarid", [("jarid_new",0),("jarid_quiver", ixmesh_carry)], itp_type_polearm|itp_primary|itp_wooden_parry|itp_no_blur , itc_spear,
560 , weight(1)|abundance(0)|difficulty(2)|spd_rtng(93) | swing_damage(0, cut) | thrust_damage(20 ,  pierce)|weapon_length(65),imodbits_thrown, [], [fac_no_faction] ],

# Other Throwing Weapons
["stones",         "Stones", [("throwing_stone",0)], itp_type_thrown|itp_primary ,itcf_throw_stone,
 1 , weight(4)|abundance(0)|difficulty(0)|spd_rtng(97) | shoot_speed(30) | thrust_damage(11 ,  blunt)|max_ammo(18)|weapon_length(8),imodbit_large_bag, [], [fac_no_faction] ],
["throwing_knives", "Throwing Knives", [("throwing_knife",0)], itp_type_thrown |itp_merchandise|itp_primary ,itcf_throw_knife,
 76 , weight(2.5)|abundance(100)|difficulty(0)|spd_rtng(121) | shoot_speed(25) | thrust_damage(19 ,  cut)|max_ammo(14)|weapon_length(0),imodbits_thrown ],
["throwing_daggers", "Throwing Daggers", [("throwing_dagger",0)], itp_type_thrown |itp_merchandise|itp_primary ,itcf_throw_knife,
 193 , weight(2.5)|abundance(100)|difficulty(0)|spd_rtng(110) | shoot_speed(24) | thrust_damage(25 ,  cut)|max_ammo(13)|weapon_length(0),imodbits_thrown ],
["light_throwing_axes", "Light Throwing Axes", [("francisca",0)], itp_type_thrown |itp_merchandise|itp_primary|itp_next_item_as_melee,itcf_throw_axe,
360, weight(5)|abundance(100)|difficulty(2)|spd_rtng(99) | shoot_speed(18) | thrust_damage(35,cut)|max_ammo(4)|weapon_length(53),imodbits_thrown_minus_heavy, [], [fac_kingdom_4, fac_kingdom_6] ],
["light_throwing_axes_melee", "Light Throwing Axe", [("francisca",0)], itp_type_one_handed_wpn |itp_primary|itp_bonus_against_shield,itc_scimitar,
360, weight(1)|abundance(0)|difficulty(2)|spd_rtng(99)|weapon_length(53)| swing_damage(26,cut),imodbits_thrown_minus_heavy, [], [fac_no_faction] ],
["throwing_axes", "Throwing Axes", [("throwing_axe_a",0)], itp_type_thrown |itp_merchandise|itp_primary|itp_next_item_as_melee,itcf_throw_axe,
490, weight(5)|abundance(100)|difficulty(3)|spd_rtng(98) | shoot_speed(18) | thrust_damage(39,cut)|max_ammo(4)|weapon_length(53),imodbits_thrown_minus_heavy, [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_4] ],
["throwing_axes_melee", "Throwing Axe", [("throwing_axe_a",0)], itp_type_one_handed_wpn |itp_primary|itp_bonus_against_shield,itc_scimitar,
490, weight(1)|abundance(0)|difficulty(3)|spd_rtng(98) | swing_damage(29,cut)|weapon_length(53),imodbits_thrown_minus_heavy, [], [fac_no_faction] ],
["heavy_throwing_axes", "Heavy Throwing Axes", [("throwing_axe_b",0)], itp_type_thrown |itp_merchandise|itp_primary|itp_next_item_as_melee,itcf_throw_axe,
620, weight(5)|abundance(100)|difficulty(4)|spd_rtng(97) | shoot_speed(18) | thrust_damage(44,cut)|max_ammo(4)|weapon_length(53),imodbits_thrown_minus_heavy, [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_4] ],
["heavy_throwing_axes_melee", "Heavy Throwing Axe", [("throwing_axe_b",0)], itp_type_one_handed_wpn |itp_primary|itp_bonus_against_shield,itc_scimitar,
620, weight(1)|abundance(0)|difficulty(4)|spd_rtng(97) | swing_damage(32,cut)|weapon_length(53),imodbits_thrown_minus_heavy, [], [fac_no_faction] ],

# Bows
["hunting_bow",         "Hunting Bow", [("hunting_bow",0),("hunting_bow_carry",ixmesh_carry)],itp_type_bow |itp_merchandise|itp_primary|itp_two_handed,itcf_shoot_bow|itcf_carry_bow_back, 
17 , weight(1)|abundance(100)|difficulty(0)|spd_rtng(100) | shoot_speed(52) | thrust_damage(15 ,  pierce),imodbits_bow ],
["short_bow",         "Short Bow", [("short_bow",0),("short_bow_carry",ixmesh_carry)], itp_type_bow |itp_merchandise|itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bow_back, 
58 , weight(1)|abundance(100)|difficulty(1)|spd_rtng(97) | shoot_speed(55) | thrust_damage(18 ,  pierce  ),imodbits_bow ],
["nomad_bow",         "Nomad Bow", [("nomad_bow",0),("nomad_bow_case", ixmesh_carry)], itp_type_bow |itp_merchandise|itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn, 
164 , weight(1.25)|abundance(100)|difficulty(2)|spd_rtng(94) | shoot_speed(56) | thrust_damage(20 ,  pierce),imodbits_bow, [], [fac_kingdom_2, fac_kingdom_3, fac_kingdom_6] ],
["long_bow",         "Long Bow", [("long_bow",0),("long_bow_carry",ixmesh_carry)], itp_type_bow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_use_on_horseback ,itcf_shoot_bow|itcf_carry_bow_back, 
145 , weight(1.75)|abundance(80)|difficulty(3)|spd_rtng(79) | shoot_speed(56) | thrust_damage(22 ,  pierce),imodbits_bow, [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_4] ],
["khergit_bow",         "Khergit Bow", [("khergit_bow",0),("khergit_bow_case", ixmesh_carry)], itp_type_bow |itp_merchandise|itp_primary|itp_two_handed,itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn, 
269 , weight(1.25)|abundance(80)|difficulty(3)|spd_rtng(90) | shoot_speed(57) | thrust_damage(21 ,pierce),imodbits_bow, [], [fac_kingdom_3] ],
["strong_bow",         "Strong Bow", [("strong_bow",0),("strong_bow_case", ixmesh_carry)], itp_type_bow |itp_merchandise|itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn, 
437 , weight(1.25)|abundance(80)|difficulty(3)|spd_rtng(88) | shoot_speed(58) | thrust_damage(23 ,pierce),imodbit_cracked | imodbit_bent | imodbit_masterwork, [], [fac_kingdom_2, fac_kingdom_3, fac_kingdom_6] ],
["war_bow",         "War Bow", [("war_bow",0),("war_bow_carry",ixmesh_carry)],itp_type_bow|itp_merchandise|itp_primary|itp_two_handed|itp_cant_use_on_horseback ,itcf_shoot_bow|itcf_carry_bow_back, 
728 , weight(1.5)|abundance(60)|difficulty(4)|spd_rtng(84) | shoot_speed(59) | thrust_damage(25 ,pierce),imodbits_bow, [], [fac_kingdom_2] ],

# Crossbows
["hunting_crossbow", "Hunting Crossbow", [("crossbow_a",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed ,itcf_shoot_crossbow|itcf_carry_crossbow_back, 
22 , weight(2.25)|abundance(100)|difficulty(0)|spd_rtng(47) | shoot_speed(50) | thrust_damage(37 ,  pierce)|max_ammo(1),imodbits_crossbow ],
["light_crossbow", "Light Crossbow", [("crossbow_b",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed ,itcf_shoot_crossbow|itcf_carry_crossbow_back, 
67 , weight(2.5)|abundance(100)|difficulty(8)|spd_rtng(45) | shoot_speed(59) | thrust_damage(44 ,  pierce)|max_ammo(1),imodbits_crossbow ],
["crossbow",         "Crossbow",         [("crossbow_a",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_on_horseback ,itcf_shoot_crossbow|itcf_carry_crossbow_back, 
182 , weight(3)|abundance(100)|difficulty(8)|spd_rtng(43) | shoot_speed(66) | thrust_damage(49,pierce)|max_ammo(1),imodbits_crossbow, [], [fac_kingdom_1, fac_kingdom_2, fac_kingdom_4, fac_kingdom_5] ],
["heavy_crossbow", "Heavy Crossbow", [("crossbow_c",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_on_horseback ,itcf_shoot_crossbow|itcf_carry_crossbow_back, 
349 , weight(3.5)|abundance(50)|difficulty(9)|spd_rtng(41) | shoot_speed(68) | thrust_damage(58 ,pierce)|max_ammo(1),imodbits_crossbow, [], [fac_kingdom_1, fac_kingdom_5] ],
["sniper_crossbow", "Siege Crossbow", [("crossbow_c",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_on_horseback ,itcf_shoot_crossbow|itcf_carry_crossbow_back, 
683 , weight(3.75)|abundance(20)|difficulty(10)|spd_rtng(37) | shoot_speed(70) | thrust_damage(63 ,pierce)|max_ammo(1)|abundance(40),imodbits_crossbow, [], [fac_kingdom_5] ],

["quick_crossbow", "Quick Crossbow", [("light_crossbow",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed ,itcf_shoot_crossbow|itcf_carry_crossbow_back, 
235 , weight(2.5)|abundance(0)|difficulty(8)|spd_rtng(48) | shoot_speed(62) | thrust_damage(47,pierce)|max_ammo(1)|accuracy(95),imodbits_crossbow, [], [fac_no_faction] ],
["rpt_crossbow", "Repeating Crossbow", [("crossbow",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_on_horseback ,itcf_shoot_crossbow|itcf_carry_crossbow_back, 
346 , weight(4)|abundance(0)|difficulty(9)|spd_rtng(41) | shoot_speed(59) | thrust_damage(44,pierce)|max_ammo(5)|accuracy(85),imodbits_crossbow, [], [fac_no_faction] ],
["strong_crossbow", "Strong Crossbow", [("heavy_crossbow",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_on_horseback ,itcf_shoot_crossbow|itcf_carry_crossbow_back, 
1605 , weight(3.75)|abundance(0)|difficulty(12)|spd_rtng(34) | shoot_speed(72) | thrust_damage(66,pierce)|max_ammo(1)|accuracy(99),imodbits_crossbow, [], [fac_no_faction] ],

# Firearms Llew Textures
["flintlock_pistol", "Flintlock Pistol", [("flintlock_pistol",0)], itp_type_pistol|itp_merchandise|itp_primary,itcf_shoot_pistol|itcf_reload_pistol,
 230, weight(1.5)|abundance(10)|difficulty(0)|spd_rtng(38) | shoot_speed(140) | thrust_damage(45,pierce)|max_ammo(1)|accuracy(65),imodbits_none,
 [(ti_on_weapon_attack, [(play_sound,"snd_pistol_shot"),(position_move_x, pos1,27),(position_move_y, pos1,36),(particle_system_burst, "psys_pistol_smoke", pos1, 15)])], [fac_no_faction]],
["arquebus", "Matchlock Arquebus",[("arquebus",0)],itp_type_musket|itp_merchandise|itp_cant_reload_on_horseback|itp_primary|itp_two_handed, itcf_reload_musket|itcf_carry_spear|itcf_shoot_musket,
 190, weight(5.5)|abundance(10)|difficulty(0)|spd_rtng(42) | shoot_speed(140) | thrust_damage(60,pierce)|max_ammo(1)|accuracy(75),imodbits_none,
 [(ti_on_weapon_attack, [(play_sound,"snd_pistol_shot"),(position_move_x, pos1,0),(position_move_y, pos1,100),(particle_system_burst, "psys_pistol_smoke", pos1, 15)])], [fac_no_faction]],
["blunderbus", "Blunderbus",[("blunderbus",0)],itp_type_musket|itp_merchandise|itp_primary|itp_two_handed, itcf_reload_musket|itcf_carry_spear|itcf_shoot_musket,
 210, weight(4.0)|abundance(10)|difficulty(0)|spd_rtng(45) | shoot_speed(120) | thrust_damage(55,pierce)|max_ammo(1)|accuracy(75),imodbits_none,
 [(ti_on_weapon_attack, [(play_sound,"snd_pistol_shot"),(position_move_x, pos1,0),(position_move_y, pos1,72),(particle_system_burst, "psys_pistol_smoke", pos1, 15)])], [fac_no_faction]],
["matchlock_1", "Matchlock Musket",[("matchlock_1",0)],itp_type_musket|itp_merchandise|itp_cant_use_on_horseback|itp_primary|itp_two_handed, itcf_reload_musket|itcf_carry_spear|itcf_shoot_musket,
 360, weight(8.5)|abundance(10)|difficulty(0)|spd_rtng(38) | shoot_speed(160) | thrust_damage(85,pierce)|max_ammo(1)|accuracy(85),imodbits_none,
 [(ti_on_weapon_attack, [(play_sound,"snd_pistol_shot"),(position_move_x, pos1,0),(position_move_y, pos1,107),(particle_system_burst, "psys_pistol_smoke", pos1, 15)])], [fac_no_faction]],
["matchlock_2", "Matchlock Musket",[("matchlock_2",0)],itp_type_musket|itp_merchandise|itp_cant_use_on_horseback|itp_primary|itp_two_handed, itcf_reload_musket|itcf_carry_spear|itcf_shoot_musket,
 380, weight(9.0)|abundance(10)|difficulty(0)|spd_rtng(38) | shoot_speed(160) | thrust_damage(85,pierce)|max_ammo(1)|accuracy(85),imodbits_none,
 [(ti_on_weapon_attack, [(play_sound,"snd_pistol_shot"),(position_move_x, pos1,0),(position_move_y, pos1,112),(particle_system_burst, "psys_pistol_smoke", pos1, 15)])], [fac_no_faction]],
["flintlock_rifle", "Flintlock Rifle",[("flintlock_rifle",0)],itp_type_musket|itp_merchandise|itp_cant_use_on_horseback|itp_primary|itp_two_handed, itcf_reload_musket|itcf_carry_spear|itcf_shoot_musket,
 1240, weight(9.0)|abundance(20)|difficulty(0)|spd_rtng(28) | shoot_speed(160) | thrust_damage(95,pierce)|max_ammo(1)|accuracy(85),imodbits_none,
 [(ti_on_weapon_attack, [(play_sound,"snd_pistol_shot"),(position_move_x, pos1,0),(position_move_y, pos1,139),(particle_system_burst, "psys_pistol_smoke", pos1, 15)])], [fac_no_faction]],

################
# RANDOM STUFF #
################
# Keep torch in front!

["torch", "Torch", [("club",0)], itp_type_one_handed_wpn|itp_primary, itc_scimitar, 11 , weight(2.5)|difficulty(0)|spd_rtng(95) | weapon_length(95)|swing_damage(11 , blunt) | thrust_damage(0 ,  pierce),imodbits_none,
 [(ti_on_init_item, [(set_position_delta,0,60,0),(particle_system_add_new, "psys_torch_fire"),(particle_system_add_new, "psys_torch_smoke"),(set_current_color,150, 130, 70),(add_point_light, 10, 30),])], [fac_no_faction]],
["lyre", "Lyre", [("lyre",0)], itp_type_shield|itp_wooden_parry|itp_civilian, itcf_carry_bow_back,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|weapon_length(90),0, [], [fac_no_faction] ],
["lute", "Lute", [("lute",0)], itp_type_shield|itp_wooden_parry|itp_civilian, itcf_carry_bow_back,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|weapon_length(90),0, [], [fac_no_faction] ],
["keys", "Ring of Keys", [("throwing_axe_a",0)], itp_type_one_handed_wpn |itp_primary|itp_bonus_against_shield,itc_scimitar, 240, weight(5)|spd_rtng(98) | swing_damage(29,cut)|max_ammo(5)|weapon_length(53),imodbits_thrown, [], [fac_no_faction] ], 
["practice_bow_2","Practice Bow", [("hunting_bow",0), ("hunting_bow_carry",ixmesh_carry)], itp_type_bow |itp_primary|itp_two_handed,itcf_shoot_bow|itcf_carry_bow_back, 0, weight(1.5)|spd_rtng(90) | shoot_speed(40) | thrust_damage(21, blunt),imodbits_bow, [], [fac_no_faction] ],
["practice_arrows_2","Practice Arrows", [("arena_arrow",0),("flying_missile",ixmesh_flying_ammo),("quiver", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back, 0,weight(1.5)|weapon_length(95)|max_ammo(80),imodbits_missile, [], [fac_no_faction]],
["heraldic_mail_with_surcoat_for_tableau", "{!}Heraldic Mail with Surcoat", [("heraldic_armor_new_a",0)], itp_type_body_armor |itp_covers_legs ,0, 1, weight(22)|abundance(0)|head_armor(0)|body_armor(1)|leg_armor(1),imodbits_armor,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_armor_a", ":agent_no", ":troop_no")])], [fac_no_faction]],
["mail_boots_for_tableau", "Mail Boots", [("mail_boots_a",0)], itp_type_foot_armor | itp_attach_armature  ,0, 1, weight(3)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor, [], [fac_no_faction] ],
["book_of_the_dead","Strange Book", [("book_b",0)], itp_type_book, 0, 5000,weight(2)|abundance(0),imodbits_none, [], [fac_no_faction]],
["human_meat","Human Flesh", [("raw_meat",0)], itp_type_goods|itp_consumable|itp_food, 0, 80,weight(20)|abundance(0)|food_quality(120)|max_ammo(30),imodbits_none], # Adicionado


#Ramaraunt Combat OSP BEGIN
["untitled", "invishead", [("invisihead",0)], itp_type_head_armor|itp_fit_to_head|itp_covers_head|itp_covers_beard, 0, 187, weight(1.25)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0), imodbits_plate ],
#Ramaraunt Combat OSP END

#TAVERN OSP BEGIN
["dedal_kufel","Kufel",[("dedal_kufelL",0)],	itp_type_hand_armor,0,0,weight(1),0],
["dedal_lutnia","Lutnia",[("dedal_lutniaL",0)],	itp_type_hand_armor,0,0,weight(1),0],
["dedal_lira","Lira",[("dedal_liraL",0)],		itp_type_hand_armor,0,0,weight(1),0],
#TAVERN OSP END

#head of wanted man RAMARAUNT ADD
["criminals_head","Wanted Criminal's Head", [("bloodystumps",0)], itp_always_loot, 0, 1,weight(40),imodbits_none],
["old_rotten_head","Old Rotten Head", [("bloodystumps",0)], 0, 0, 1,weight(40),imodbits_none],
#head end

##########################
### Dark Tower Weapons ###
##########################
# Editado e Adicionado
["sandalwood_gun", "Sandalwood Gun", [("colt",0)], itp_type_pistol|itp_primary,itcf_shoot_pistol|itcf_reload_pistol,
 2000, weight(1.5)|abundance(0)|difficulty(0)|spd_rtng(80)|shoot_speed(140)|thrust_damage(60,pierce)|max_ammo(8)|accuracy(90),imodbits_none,
 [(ti_on_weapon_attack, [(play_sound,"snd_pistol_shot"),(position_move_x, pos1,27),(position_move_y, pos1,36),(particle_system_burst, "psys_pistol_smoke", pos1, 15)])], [fac_no_faction]],

################
### GRENADES ###
################
# Editado e Adicionado
["german_grenade1", "WW2 Grenade", [("Stickgrenade",0)], itp_type_thrown|itp_primary|itp_next_item_as_melee|itp_can_penetrate_shield, itcf_throw_javelin|itcf_carry_axe_left_hip, 
27, weight(0.5) | spd_rtng(91) | shoot_speed(28) | thrust_damage(27, blunt) | max_ammo(20) | weapon_length(1),imodbits_none],  # Editado
["british_grenade1", "Grenade", [("grenade2",0)], itp_type_thrown|itp_primary|itp_next_item_as_melee|itp_can_penetrate_shield, itcf_throw_javelin|itcf_carry_axe_left_hip, 
27, weight(0.5) | spd_rtng(91) | shoot_speed(28) | thrust_damage(27, blunt) | max_ammo(20) | weapon_length(1),imodbits_none,
[(ti_on_missile_hit, [(particle_system_burst, "psys_mod_blast", pos1, 10),(particle_system_burst, "psys_explosive_explosion_sparks_a", pos1, 40),(particle_system_burst, "psys_explosive_explosion_sparks_b", pos1, 40),
                      (particle_system_burst, "psys_explosion_dirt", pos1, 400),(particle_system_burst, "psys_explosive_explosion_smoke", pos1, 10),
                      (store_trigger_param_1, ":shooter_agent"),
                      (try_for_agents,":victim_agent"),
                            (agent_is_alive,":victim_agent"),
                            (agent_get_position,pos2,":victim_agent"),
                            (get_distance_between_positions,":dist",pos1,pos2),
                             (try_begin),
                                 (le,":dist",500),
                                 (agent_deliver_damage_to_agent, ":shooter_agent",":victim_agent" , 20),
                                 (store_random_in_range, ":random", 1, 3),
                                 (try_begin),
                                     (eq, ":random", 1),
                                     (agent_set_animation, ":victim_agent", "anim_fall_far_back"),
                                 (else_try),
                                     (eq, ":random", 2),
                                     (agent_set_animation, ":victim_agent", "anim_fall_far_back2"),
                                 (try_end),
                              (try_end),
                        (try_end)],
  )],
],  # Editado
["dynamite", "Dynamite", [("dynamite",0)], itp_type_thrown|itp_primary|itp_next_item_as_melee|itp_can_penetrate_shield, itcf_throw_javelin|itcf_carry_axe_left_hip, 
27, weight(0.5) | spd_rtng(91) | shoot_speed(28) | thrust_damage(27, blunt) | max_ammo(20) | weapon_length(1),imodbits_none],  # Editado

["grenade_fragments","Grenade Fragments",[("invisi",0),("xenoargh_grenade_fragment",ixmesh_flying_ammo),("bolt_bag_c",ixmesh_carry),("xeno_bolts_and_bullets",ixmesh_inventory)],itp_type_bolts|itp_can_penetrate_shield|itp_no_pick_up_from_ground,itcf_carry_quiver_right_vertical,2000,weight(2.25)|abundance(90)|weapon_length(150)|thrust_damage(1,pierce)|max_ammo(30),imodbits_none,
 [
 (ti_on_missile_hit,
      [
         #pos1 - Missile hit position
         #param_1 - Shooter agent
         #pos1 - Missile hit position
         #param_1 - Shooter agent
		(copy_position, pos63, pos1),     
		(position_get_z, ":z_pos", pos63),
		(set_fixed_point_multiplier, 100),
		(try_begin),
			(gt, ":z_pos", -50),
			(particle_system_burst,"psys_bullet_dust",pos63,1),
		(else_try),
			(gt, ":z_pos", -300),
			(position_set_z, pos63, -50),
			(particle_system_burst, "psys_water_hit_a", pos63, 8),
			(particle_system_burst, "psys_water_hit_b", pos63, 4),
		(try_end),
]),
]],

##########################
### Special Cartridges ###
##########################
# Editado e Adicionado
["cartridgesFAIL","Ammunition", [("ammo_belt",0),("Projectile",ixmesh_flying_ammo),("bolt_bag_c", ixmesh_carry)], itp_type_bullets|itp_can_penetrate_shield, itcf_carry_quiver_right_vertical, 210,weight(2.5)|abundance(0)|weapon_length(63)|thrust_damage(2,pierce)|max_ammo(29),imodbits_missile],
["cartridges","Crappy Ammunition", [("ammo_belt",0),("Projectile",ixmesh_flying_ammo),("ammobelt", ixmesh_carry)], itp_type_bullets|itp_can_penetrate_shield|itp_default_ammo,0, 0,weight(2.25)|abundance(0)|weapon_length(3)|thrust_damage(1,pierce)|max_ammo(50),imodbits_missile],
["cartridges2","Ammunition", [("ammo_belt",0),("Projectile",ixmesh_flying_ammo),("ammobelt", ixmesh_carry)], itp_type_bullets|itp_can_penetrate_shield|itp_default_ammo,0, 250,weight(2.25)|abundance(0)|weapon_length(3)|thrust_damage(4,pierce)|max_ammo(50),imodbits_missile],
["cartridges3","Good Ammunition", [("ammo_belt",0),("Projectile",ixmesh_flying_ammo),("ammobelt", ixmesh_carry)], itp_type_bullets|itp_can_penetrate_shield|itp_default_ammo,0, 250,weight(2.25)|abundance(0)|weapon_length(3)|thrust_damage(8,pierce)|max_ammo(50),imodbits_missile],

["cartridges4","Explosive Rounds", [("ammo_belt",0),("Projectile",ixmesh_flying_ammo),("ammobelt", ixmesh_carry)], itp_type_bullets|itp_can_penetrate_shield|itp_default_ammo, 0, 600,weight(2.25)|abundance(0)|weapon_length(3)|thrust_damage(8,pierce)|max_ammo(50),imodbits_missile,
[(ti_on_missile_hit, [(particle_system_burst, "psys_mod_blast", pos1, 10),(particle_system_burst, "psys_explosive_explosion_sparks_a", pos1, 40),(particle_system_burst, "psys_explosive_explosion_sparks_b", pos1, 40),
                      (particle_system_burst, "psys_explosion_dirt", pos1, 400),(particle_system_burst, "psys_explosive_explosion_smoke", pos1, 10),
                      (store_trigger_param_1, ":shooter_agent"),
                      (try_for_agents,":victim_agent"),
                            (agent_is_alive,":victim_agent"),
                            (agent_get_position,pos2,":victim_agent"),
                            (get_distance_between_positions,":dist",pos1,pos2),
                             (try_begin),
                                 (le,":dist",500),
                                 (agent_deliver_damage_to_agent, ":shooter_agent",":victim_agent" , 20),
                                 (store_random_in_range, ":random", 1, 3),
                                 (try_begin),
                                     (eq, ":random", 1),
                                     (agent_set_animation, ":victim_agent", "anim_fall_far_back"),
                                 (else_try),
                                     (eq, ":random", 2),
                                     (agent_set_animation, ":victim_agent", "anim_fall_far_back2"),
                                 (try_end),
                              (try_end),
                        (try_end)],
  )],
 ],

# Editado: Ammo Commodity

["rounds_45",".45 Magnum Round", [("ammo_1",0)], itp_merchandise|itp_type_goods|itp_consumable, 100, 391,weight(25)|abundance(40)|max_ammo(12),imodbits_none], # ammo_1
["rounds_556",".577mm Rounds", [("ammo_3",0)], itp_merchandise|itp_type_goods|itp_consumable, 0, 70,weight(25)|abundance(40)|max_ammo(20),imodbits_none],            # ammo_3
["rounds_308",".58mm Rounds", [("ammo_4",0)], itp_merchandise|itp_type_goods|itp_consumable, 0, 125,weight(25)|abundance(40)|max_ammo(12),imodbits_none],            # ammo_4


["ammo_carry_1","Cheap Ammo Pouch", [("ammo_belt",0),("Projectile",ixmesh_flying_ammo),("ammobelt", ixmesh_carry)], itp_type_bullets|itp_merchandise|itp_can_penetrate_shield|itp_default_ammo,0, 30,weight(2.25)|abundance(90)|weapon_length(3)|thrust_damage(1,pierce)|max_ammo(8),imodbits_missile],
["ammo_carry_2","Cheap Ammo Belt", [("ammo_belt",0),("Projectile",ixmesh_flying_ammo),("ammobelt", ixmesh_carry)], itp_type_bullets|itp_merchandise|itp_can_penetrate_shield|itp_default_ammo,0, 50,weight(2.25)|abundance(90)|weapon_length(3)|thrust_damage(2,pierce)|max_ammo(8),imodbits_missile],
["ammo_carry_3","Ammo Pouch", [("ammo_belt",0),("Projectile",ixmesh_flying_ammo),("ammobelt", ixmesh_carry)], itp_type_bullets|itp_merchandise|itp_can_penetrate_shield|itp_default_ammo,0, 100,weight(2.25)|abundance(90)|weapon_length(3)|thrust_damage(3,pierce)|max_ammo(14),imodbits_missile],
["ammo_carry_4","Ammo Belt", [("ammo_belt",0),("Projectile",ixmesh_flying_ammo),("ammobelt", ixmesh_carry)], itp_type_bullets|itp_merchandise|itp_can_penetrate_shield|itp_default_ammo,0, 150,weight(2.25)|abundance(90)|weapon_length(3)|thrust_damage(4,pierce)|max_ammo(14),imodbits_missile],
["ammo_carry_5","Large Ammo Bag", [("ammo_belt",0),("Projectile",ixmesh_flying_ammo),("ammobelt", ixmesh_carry)], itp_type_bullets|itp_merchandise|itp_can_penetrate_shield|itp_default_ammo,0, 500,weight(2.25)|abundance(90)|weapon_length(3)|thrust_damage(3,pierce)|max_ammo(50),imodbits_missile],
["ammo_carry_6","Ammo Bandolier", [("ammo_belt",0),("Projectile",ixmesh_flying_ammo),("ammobelt", ixmesh_carry)], itp_type_bullets|itp_merchandise|itp_can_penetrate_shield|itp_default_ammo,0, 1000,weight(2.25)|abundance(90)|weapon_length(3)|thrust_damage(4,pierce)|max_ammo(25),imodbits_missile,
  [(ti_on_missile_hit, [(copy_position, pos30,pos1)],
     )],
  ],
["ammo_end","Ammo end", [("ammo_belt",0),("Projectile",ixmesh_flying_ammo),("ammobelt", ixmesh_carry)], itp_type_bullets|itp_merchandise|itp_can_penetrate_shield|itp_default_ammo,0, 1000,weight(2.25)|abundance(90)|weapon_length(3)|thrust_damage(4,pierce)|max_ammo(25),imodbits_missile],


###############
### TANK!!! ###
###############
#Aleph's cannon; has a bunch of special kludges to adjust for fact...
#... that AI doesn't use missile weapons correctly on large-scale Agents.
["tank_cannon","Tank Cannon",[("invisi",0)],itp_type_crossbow|itp_primary|itp_two_handed|itp_cant_use_on_horseback|itp_no_pick_up_from_ground,itcf_shoot_musket|itcf_reload_musket|itcf_carry_spear,12000,weight(255.0)|spd_rtng(100)|shoot_speed(110)|thrust_damage(100,pierce)|max_ammo(1)|accuracy(105),imodbits_none,[(ti_on_weapon_attack,[ 
(store_trigger_param_1,reg4),#Get the attacker Agent for add_missile
(copy_position, pos63, pos1),
(agent_get_position, pos61, reg4),
(position_move_z,pos61,100,0),#Move up along Z
(position_move_y,pos61,50,0),#Move out along Y
(position_move_x,pos61,10,0),#Move right along X
(position_copy_rotation, pos61, pos63),
(particle_system_burst,"psys_pistol_smoke",pos61,45),#Smoke
(particle_system_burst,"psys_gun_sparks",pos61,45),#Flare
(play_sound,"snd_gunshot_heavy"),
(get_player_agent_no,":player_agent"),
(try_begin),
	(neq, ":player_agent", reg4),
	(agent_ai_get_behavior_target, reg5, reg4),
	(neq, reg5, reg4),
	(agent_is_alive, reg5),
	(agent_is_active, reg5),
	(agent_get_position, pos62, reg5),
	(store_random_in_range, ":x_move", -1000, 1000),
	(position_move_x, pos62, ":x_move", 0),
	(store_random_in_range, ":y_move", -1000, 1000),
	(position_move_y, pos62, ":y_move",0),
	(store_random_in_range, ":z_move", -1000, 1000),
	(position_move_z, pos62, ":z_move",0),

	(position_get_distance_to_ground_level, ":distance", pos62),
	(try_begin),
		(lt, ":distance", 0),
		(position_set_z_to_ground_level, pos62),
		(position_move_z, pos62, 200),
	(try_end),		
	(play_sound_at_position, "snd_explosive_ammo_explode", pos62),
	
	(try_for_range, ":unused", 1, 34),
		(copy_position, pos3, pos62),
		(store_random_in_range, ":x_move", -500, 500),
		(position_move_x, pos3, ":x_move", 0),
		(store_random_in_range, ":y_move", -500, 500),
		(position_move_y, pos3, ":y_move",0),
		(store_random_in_range, ":z_move", -500, 500),
		(position_move_z, pos3, ":z_move",0),
		
		(position_get_distance_to_ground_level, ":distance", pos3),
		(try_begin),
			(lt, ":distance", 0),
			(position_set_z_to_ground_level, pos3),
			(position_move_z, pos3, 200),
		(try_end),	

		(try_for_range, ":unused", 1, 20),
			(store_random_in_range, ":x_offset", 1, 361),#Random Rotation of X
			(position_rotate_x, pos3, ":x_offset"),	
			(store_random_in_range, ":y_offset", 1, 361),#Random Rotation of Y
			(position_rotate_y, pos3, ":y_offset"),	
			(store_random_in_range, ":z_offset", 1, 361),#Random Rotation of Z
			(position_rotate_z, pos3, ":z_offset"),		
			(store_random_in_range, ":speed", 1500, 2500),
			(add_missile, reg4, pos3, ":speed", "itm_matchlock_1", 0, "itm_grenade_fragments", 0),
		(try_end),	
		(particle_system_burst,"psys_explosion_dirt",pos3,200),			
		(particle_system_burst,"psys_explosive_explosion_sparks_a",pos3,35),
		(particle_system_burst,"psys_explosive_explosion_sparks_b",pos3,35),
	(try_end),	
	
(else_try),
	(copy_position, pos2, pos61),
	(add_missile, reg4, pos2, 11000, "itm_flintlock_rifle", 0,"itm_explosive_cannon_rounds", 0),
(try_end),
  ])]],

["universal_cannon_ammo","Cannon Ammunition",[("xeno_bullet",0),("xeno_cannonball_solid",ixmesh_inventory)],itp_type_bolts|itp_can_penetrate_shield|itp_no_pick_up_from_ground,0,3500,weight(3)|abundance(200)|weapon_length(150)|thrust_damage(500,pierce)|max_ammo(1000),imodbits_none],

["tank_body", "tank_body", [("mark4_unit",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(40)|abundance(100)|head_armor(0)|body_armor(85)|leg_armor(85)|difficulty(0) ,imodbits_cloth ],

 ["explosive_cannon_rounds","Explosive Cannon Round",[("xeno_bullet",0),("xenoargh_explosive_cannon_flying",ixmesh_flying_ammo),("xeno_cannonball_explosive",ixmesh_inventory)],itp_type_bolts|itp_can_penetrate_shield|itp_no_pick_up_from_ground,itcf_carry_quiver_right_vertical,3000,weight(3)|abundance(0)|weapon_length(150)|thrust_damage(100,pierce)|max_ammo(200),imodbits_none,
   [   
 (ti_on_missile_hit,
      [
  	(store_trigger_param_1,reg1),
	(copy_position, pos62, pos1),#Need to store it in a safe-ish place here.
	(position_get_distance_to_ground_level, ":distance", pos62),
	(try_begin),
		(lt, ":distance", 0),
		(position_set_z_to_ground_level, pos62),
		(position_move_z, pos62, 200),
	(try_end),		
	(play_sound_at_position, "snd_explosive_ammo_explode", pos62),
	
	(try_for_range, ":unused", 1, 34),
		(copy_position, pos3, pos62),
		(store_random_in_range, ":x_move", -500, 500),
		(position_move_x, pos3, ":x_move", 0),
		(store_random_in_range, ":y_move", -500, 500),
		(position_move_y, pos3, ":y_move",0),
		(store_random_in_range, ":z_move", -500, 500),
		(position_move_z, pos3, ":z_move",0),
		
		(position_get_distance_to_ground_level, ":distance", pos3),
		(try_begin),
			(lt, ":distance", 0),
			(position_set_z_to_ground_level, pos3),
			(position_move_z, pos3, 200),
		(try_end),	

		(try_for_range, ":unused", 1, 20),
			(store_random_in_range, ":x_offset", 1, 361),#Random Rotation of X
			(position_rotate_x, pos3, ":x_offset"),	
			(store_random_in_range, ":y_offset", 1, 361),#Random Rotation of Y
			(position_rotate_y, pos3, ":y_offset"),	
			(store_random_in_range, ":z_offset", 1, 361),#Random Rotation of Z
			(position_rotate_z, pos3, ":z_offset"),		
			(store_random_in_range, ":speed", 1500, 2500),
			(add_missile, reg1, pos3, ":speed", "itm_matchlock_1", 0, "itm_grenade_fragments", 0),
		(try_end),	
		(particle_system_burst,"psys_explosion_dirt",pos3,200),			
		(particle_system_burst,"psys_explosive_explosion_sparks_a",pos3,35),
		(particle_system_burst,"psys_explosive_explosion_sparks_b",pos3,35),
	(try_end),	

			
]),
]],

###############
### ANIMALS ###
###############
# Editado e Adicionado

["doberman","Doberman", [("doberman",0)], itp_merchandise|itp_type_horse, 0, 1811,abundance(40)|hit_points(10)|body_armor(15)|difficulty(0)|horse_speed(40)|horse_maneuver(44)|horse_charge(32)|horse_scale(60),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_1, fac_kingdom_5]],
["dobermanb","Infected Doberman", [("dobermanb",0)], itp_merchandise|itp_type_horse, 0, 1811,abundance(40)|hit_points(10)|body_armor(15)|difficulty(0)|horse_speed(40)|horse_maneuver(44)|horse_charge(32)|horse_scale(60),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_1, fac_kingdom_5]],
["dobermanc","Infected Doberman", [("dobermanc",0)], itp_merchandise|itp_type_horse, 0, 1811,abundance(40)|hit_points(10)|body_armor(15)|difficulty(0)|horse_speed(40)|horse_maneuver(44)|horse_charge(32)|horse_scale(60),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_1, fac_kingdom_5]],
["dog_2","Mongrel", [("dog_2",0)], itp_merchandise|itp_type_horse, 0, 1811,abundance(40)|hit_points(10)|body_armor(15)|difficulty(0)|horse_speed(40)|horse_maneuver(44)|horse_charge(32)|horse_scale(60),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_1, fac_kingdom_5]],
["dog_2b","Infected Mongrel", [("dog_2b",0)], itp_merchandise|itp_type_horse, 0, 1811,abundance(40)|hit_points(10)|body_armor(15)|difficulty(0)|horse_speed(40)|horse_maneuver(44)|horse_charge(32)|horse_scale(60),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_1, fac_kingdom_5]],
["dog_2c","Infected Mongrel", [("dog_2c",0)], itp_merchandise|itp_type_horse, 0, 1811,abundance(40)|hit_points(10)|body_armor(15)|difficulty(0)|horse_speed(40)|horse_maneuver(44)|horse_charge(32)|horse_scale(60),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_1, fac_kingdom_5]],
["elephant","Elephant", [("elephant",0)], itp_merchandise|itp_type_horse, 0, 1811,abundance(40)|hit_points(50)|body_armor(15)|difficulty(0)|horse_speed(30)|horse_maneuver(44)|horse_charge(32)|horse_scale(140),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_1, fac_kingdom_5]],
["elephantb","Infected Elephant", [("elephant_z",0)], itp_merchandise|itp_type_horse, 0, 1811,abundance(40)|hit_points(50)|body_armor(15)|difficulty(0)|horse_speed(30)|horse_maneuver(44)|horse_charge(32)|horse_scale(140),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_1, fac_kingdom_5]],
["elephantc","Infected Elephant", [("elephant_z2",0)], itp_merchandise|itp_type_horse, 0, 1811,abundance(40)|hit_points(50)|body_armor(15)|difficulty(0)|horse_speed(30)|horse_maneuver(44)|horse_charge(32)|horse_scale(140),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_1, fac_kingdom_5]],
["boar","Boar", [("animal_boar",0)], itp_merchandise|itp_type_horse, 0, 1811,abundance(40)|hit_points(20)|body_armor(15)|difficulty(0)|horse_speed(40)|horse_maneuver(44)|horse_charge(32)|horse_scale(80),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_1, fac_kingdom_5]],
["donkey","Donkey", [("animal_donkeywild",0)], itp_merchandise|itp_type_horse, 0, 1811,abundance(40)|hit_points(10)|body_armor(0)|difficulty(0)|horse_speed(50)|horse_maneuver(44)|horse_charge(32)|horse_scale(85),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_1, fac_kingdom_5]],
["cow","Cow", [("animal_cowblackwhite",0)], itp_merchandise|itp_type_horse, 0, 1811,abundance(40)|hit_points(10)|body_armor(0)|difficulty(0)|horse_speed(30)|horse_maneuver(44)|horse_charge(32)|horse_scale(95),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_1, fac_kingdom_5]],
["cowb","Cow", [("animal_cowbrown",0)], itp_merchandise|itp_type_horse, 0, 1811,abundance(40)|hit_points(10)|body_armor(0)|difficulty(0)|horse_speed(30)|horse_maneuver(44)|horse_charge(32)|horse_scale(100),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_1, fac_kingdom_5]],
["cowc","Cow", [("animal_cowbrownwhite",0)], itp_merchandise|itp_type_horse, 0, 1811,abundance(40)|hit_points(10)|body_armor(0)|difficulty(0)|horse_speed(30)|horse_maneuver(44)|horse_charge(32)|horse_scale(90),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_1, fac_kingdom_5]],
["cowd","Cow", [("animal_cowwhite",0)], itp_merchandise|itp_type_horse, 0, 1811,abundance(40)|hit_points(10)|body_armor(0)|difficulty(0)|horse_speed(30)|horse_maneuver(44)|horse_charge(32)|horse_scale(105),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_1, fac_kingdom_5]],
["deer_f","Deer (Doe)", [("animal_deerfemale",0)], itp_merchandise|itp_type_horse, 0, 1811,abundance(40)|hit_points(10)|body_armor(0)|difficulty(0)|horse_speed(30)|horse_maneuver(44)|horse_charge(32)|horse_scale(80),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_1, fac_kingdom_5]],
["deer_m","Deer (Buck)", [("animal_deermale",0)], itp_merchandise|itp_type_horse, 0, 1811,abundance(40)|hit_points(20)|body_armor(0)|difficulty(0)|horse_speed(30)|horse_maneuver(44)|horse_charge(32)|horse_scale(85),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_1, fac_kingdom_5]],
["deer_y","Deer (Fawn)", [("animal_deeryoung",0)], itp_merchandise|itp_type_horse, 0, 1811,abundance(40)|hit_points(5)|body_armor(0)|difficulty(0)|horse_speed(30)|horse_maneuver(44)|horse_charge(32)|horse_scale(70),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_1, fac_kingdom_5]],
["goat","Goat", [("animal_goatbrown",0)], itp_merchandise|itp_type_horse, 0, 1811,abundance(40)|hit_points(10)|body_armor(0)|difficulty(0)|horse_speed(30)|horse_maneuver(44)|horse_charge(32)|horse_scale(70),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_1, fac_kingdom_5]],
["goatb","Goat", [("animal_goatwhite",0)], itp_merchandise|itp_type_horse, 0, 1811,abundance(40)|hit_points(10)|body_armor(0)|difficulty(0)|horse_speed(30)|horse_maneuver(44)|horse_charge(32)|horse_scale(70),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_1, fac_kingdom_5]],

["items_end", "Items End", [("shield_round_a",0)], 0, 0, 1, 0, 0],
]
