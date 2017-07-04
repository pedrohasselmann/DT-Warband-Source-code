from ID_items import *
from ID_quests import *
from ID_factions import *
from compiler import *

##############################################################
# These constants are used in various files.
# If you need to define a value that will be used in those files,
# just define it here rather than copying it across each file, so
# that it will be easy to change it if you need to.
##############################################################

########################################################
##  ITEM SLOTS             #############################
########################################################

slot_item_is_checked               = 0
slot_item_food_bonus               = 1
slot_item_book_reading_progress    = 2
slot_item_book_read                = 3
slot_item_intelligence_requirement = 4
slot_item_weapon_switch_to         = 5

slot_item_amount_available         = 7

slot_item_urban_demand             = 11 #consumer demand for a good in town, measured in abstract units. The more essential the item (ie, like grain) the higher the price
slot_item_rural_demand             = 12 #consumer demand in villages, measured in abstract units
slot_item_desert_demand            = 13 #consumer demand in villages, measured in abstract units

slot_item_production_slot          = 14 
slot_item_production_string        = 15 

slot_item_tied_to_good_price       = 20 #ie, weapons and metal armor to tools, padded to cloth, leather to leatherwork, etc

slot_item_num_positions            = 22
slot_item_positions_begin          = 23 #reserve around 5 slots after this

slot_item_primary_raw_material    		= 50
slot_item_is_raw_material_only_for      = 51
slot_item_input_number                  = 52 #ie, how many items of inputs consumed per run
slot_item_base_price                    = 53 #taken from module_items

slot_item_output_per_run                = 55 #number of items produced per run
slot_item_overhead_per_run              = 56 #labor and overhead per run
slot_item_secondary_raw_material        = 57 #in this case, the amount used is only one
slot_item_enterprise_building_cost      = 58 #enterprise building cost

slot_item_multiplayer_faction_price_multipliers_begin = 30 #reserve around 10 slots after this#

slot_item_multiplayer_item_class   = 60 #temporary, can be moved to higher values
slot_item_multiplayer_availability_linked_list_begin = 61 #temporary, can be moved to higher values


########################################################
##  AGENT SLOTS            #############################
########################################################

slot_agent_target_entry_point     = 0
slot_agent_target_x_pos           = 1
slot_agent_target_y_pos           = 2
slot_agent_is_alive_before_retreat= 3
slot_agent_is_in_scripted_mode    = 4
slot_agent_is_not_reinforcement   = 5
slot_agent_tournament_point       = 6
slot_agent_arena_team_set         = 7
slot_agent_spawn_entry_point      = 8
slot_agent_target_prop_instance   = 9
slot_agent_map_overlay_id         = 10
slot_agent_target_entry_point     = 11
slot_agent_is_running_away        = 12

slot_agent_is_respawn_as_bot      = 17
slot_agent_cur_animation          = 18
slot_agent_next_action_time       = 19
slot_agent_state                  = 20
slot_agent_in_duel_with           = 21
slot_agent_duel_start_time        = 22

slot_agent_walker_occupation      = 25
slot_agent_bought_horse           = 26 # Equipment cost fix
    
########################################################
##  FACTION SLOTS          #############################
########################################################
slot_faction_ai_state                   = 4
slot_faction_ai_object                  = 5

slot_faction_marshall                   = 8
slot_faction_marshal = slot_faction_marshall
slot_faction_ai_offensive_max_followers = 9

slot_faction_leader                     = 11

slot_faction_temp_slot                  = 12

slot_faction_banner                     = 15

slot_faction_number_of_parties    = 20
slot_faction_state                = 21

slot_faction_adjective            = 22

slot_faction_player_alarm         		= 30
slot_faction_last_mercenary_offer_time 	= 31
slot_faction_recognized_player    		= 32

#overriding troop info for factions in quick start mode.
slot_faction_quick_battle_tier_1_infantry      = 41
slot_faction_quick_battle_tier_2_infantry      = 42
slot_faction_quick_battle_tier_1_archer        = 43
slot_faction_quick_battle_tier_2_archer        = 44
slot_faction_quick_battle_tier_1_cavalry       = 45
slot_faction_quick_battle_tier_2_cavalry       = 46

slot_faction_tier_1_troop         = 41
slot_faction_tier_2_troop         = 42
slot_faction_tier_3_troop         = 43
slot_faction_tier_4_troop         = 44
slot_faction_tier_5_troop         = 45

slot_faction_bandit_troop         = 48
slot_faction_guard_troop          = 49
slot_faction_messenger_troop      = 50
slot_faction_prison_guard_troop   = 51
slot_faction_castle_guard_troop   = 52

slot_faction_town_walker_male_troop      = 53
slot_faction_town_walker_female_troop    = 54
slot_faction_village_walker_male_troop   = 55
slot_faction_village_walker_female_troop = 56
slot_faction_town_spy_male_troop         = 57
slot_faction_town_spy_female_troop       = 58

slot_faction_has_rebellion_chance = 60
slot_faction_instability          = 61 #last time measured

slot_faction_political_issue 							 = 64 #Center or marshal appointment
slot_faction_political_issue_time 						 = 65 #Now is used

slot_faction_reinforcements_a        = 77
slot_faction_reinforcements_b        = 78
slot_faction_reinforcements_c        = 79

slot_faction_num_armies              = 80
slot_faction_num_castles             = 81
slot_faction_num_towns               = 82

slot_faction_last_attacked_center    = 85
slot_faction_last_attacked_hours     = 86
slot_faction_last_safe_hours         = 87

slot_faction_num_routed_agents       = 90

#useful for competitive consumption
slot_faction_biggest_feast_score      = 91
slot_faction_biggest_feast_time       = 92
slot_faction_biggest_feast_host       = 93


#Faction AI states
slot_faction_last_feast_concluded       = 94 #Set when a feast starts -- this needs to be deprecated
slot_faction_last_feast_start_time      = 94 #this is a bit confusing


slot_faction_ai_last_offensive_time 	= 95 #Set when an offensive concludes
slot_faction_last_offensive_concluded 	= 95 #Set when an offensive concludes

slot_faction_ai_last_rest_time      	= 96 #the last time that the faction has had default or feast AI -- this determines lords' dissatisfaction with the campaign. Set during faction_ai script
slot_faction_ai_current_state_started   = 97 #

slot_faction_ai_last_decisive_event     = 98 #capture a fortress or declaration of war

slot_faction_morale_of_player_troops    = 99

#diplomacy
slot_faction_truce_days_with_factions_begin 			= 120
slot_faction_provocation_days_with_factions_begin 		= 130
slot_faction_war_damage_inflicted_on_factions_begin 	= 140
slot_faction_sum_advice_about_factions_begin 			= 150

	
########################################################
##  PARTY SLOTS            #############################
########################################################
slot_party_type                = 0  #spt_caravan, spt_town, spt_castle

slot_party_retreat_flag        = 2
slot_party_ignore_player_until = 3
slot_party_ai_state            = 4
slot_party_ai_object           = 5

slot_ship_captain              = 7
slot_town_lord                 = 7
slot_party_ai_substate         = 8
slot_town_claimed_by_player    = 9

slot_cattle_driven_by_player = slot_town_lord #hack

slot_town_center        = 10
slot_town_castle        = 11
slot_town_prison        = 12
slot_town_tavern        = 13
slot_town_store         = 14
slot_town_arena         = 16
slot_town_alley         = 17
slot_town_walls         = 18

slot_castle_exterior    = slot_town_center
slot_castle_interior    = slot_town_castle
slot_castle_prison      = slot_town_prison

slot_village_center     = slot_town_center

slot_town_tavernkeeper  = 20
slot_town_weaponsmith   = 21
slot_town_armorer       = 22
slot_town_merchant      = 23
slot_town_horse_merchant= 24
slot_town_mayor         = 25

slot_village_elder      = slot_town_mayor

slot_center_player_relation = 26

slot_center_siege_with_belfry = 27
slot_center_last_taken_by_troop = 28
slot_center_chest_troop = 29

# party will follow this party if set:
slot_party_commander_party = 30 #default -1   #Deprecate
slot_party_following_player    = 31
slot_party_follow_player_until_time = 32
slot_party_dont_follow_player_until_time = 33

slot_village_raided_by        = 34
slot_village_state            = 35 #svs_normal, svs_being_raided, svs_looted, svs_recovering, svs_deserted
slot_village_raid_progress    = 36
slot_village_recover_progress = 37
slot_village_smoke_added      = 38

slot_village_infested_by_bandits   = 39

slot_center_last_visited_by_lord   = 41

slot_center_last_player_alarm_hour = 42

slot_village_player_can_not_steal_cattle = 46

slot_center_accumulated_rents      = 47 #collected automatically by NPC lords
slot_center_accumulated_tariffs    = 48 #collected automatically by NPC lords
slot_town_wealth        = 49 #total amount of accumulated wealth in the center, pays for the garrison
slot_town_prosperity    = 50 #affects the amount of wealth generated

slot_party_last_toll_paid_hours = 52
slot_party_food_store           = 53 #used for sieges
slot_center_is_besieged_by      = 54 #used for sieges
slot_center_last_spotted_enemy  = 55

slot_party_cached_strength        = 56
slot_party_nearby_friend_strength = 57
slot_party_nearby_enemy_strength  = 58
slot_party_follower_strength      = 59

slot_center_original_faction           = 61
slot_center_ex_faction                 = 62

slot_party_follow_me                   = 63
slot_center_siege_begin_hours          = 64 #used for sieges
slot_center_siege_hardness             = 65

slot_center_sortie_strength            = 66
slot_center_sortie_enemy_strength      = 67

slot_party_last_in_combat              = 68 #used for AI
slot_party_last_in_home_center         = 69 #used for AI
slot_party_leader_last_courted         = 70 #used for AI
slot_party_last_in_any_center          = 71 #used for AI

argument_none         = 0
argument_legal        = 1
argument_commons      = 2
argument_reward       = 3 
argument_victory      = 4
argument_lords        = 5

slot_town_village_product = 76

slot_town_rebellion_readiness = 77
#(readiness can be a negative number if the rebellion has been defeated)

slot_town_has_tournament                    = 78
slot_town_tournament_max_teams              = 79
slot_town_tournament_max_team_size          = 80
slot_town_tournament_weapon_maybe_horse     = 81 # first slot for which a horse is optional
slot_town_tournament_weapon_no_horse        = 82 # first slot for which a horse is forbidden
slot_town_tournament_weapon_1               = 83
slot_town_tournament_weapon_2               = 84
slot_town_tournament_weapon_3               = 85
slot_town_tournament_weapon_4               = 86
slot_town_tournament_weapon_5               = 87
slot_town_tournament_weapon_6               = 88
slot_town_tournament_weapon_7               = 89
slot_town_tournament_weapon_end             = 90
tournament_weapon_horse_offset = 10 # must be greater than the max number of weapon sets

slot_center_npc_volunteer_troop_type   = 90
slot_center_npc_volunteer_troop_amount = 91
slot_center_mercenary_troop_type  = 90
slot_center_mercenary_troop_amount= 91
slot_center_volunteer_troop_type  = 92
slot_center_volunteer_troop_amount= 93

slot_center_ransom_broker         = 95
slot_center_tavern_traveler       = 96
slot_center_traveler_info_faction = 97
slot_center_tavern_bookseller     = 98
slot_center_tavern_minstrel       = 99

slot_port_bound_center            = 120
slot_village_bound_center         = 120
slot_village_market_town          = 121
slot_village_farmer_party         = 122
slot_party_home_center            = 123 #Only use with caravans and villagers

slot_center_current_improvement   = 124
slot_center_improvement_end_hour  = 125

slot_party_last_traded_center     = 126 



slot_center_has_manor            = 130 #village
slot_center_has_fish_pond        = 131 #village
slot_center_has_watch_tower      = 132 #village
slot_center_has_school           = 133 #village
slot_center_has_messenger_post   = 134 #town, castle, village
slot_center_has_prisoner_tower   = 135 #town, castle

village_improvements_begin = slot_center_has_manor
village_improvements_end          = 135

walled_center_improvements_begin = slot_center_has_messenger_post
walled_center_improvements_end               = 136

slot_center_player_enterprise     				  = 137 #noted with the item produced
slot_center_player_enterprise_production_order    = 138
slot_center_player_enterprise_days_until_complete = 139


slot_center_has_bandits                        = 158
slot_center_faction_when_oath_renounced        = 159

slot_center_walker_0_troop                   = 160
slot_center_walker_1_troop                   = 161
slot_center_walker_2_troop                   = 162
slot_center_walker_3_troop                   = 163
slot_center_walker_4_troop                   = 164
slot_center_walker_5_troop                   = 165
slot_center_walker_6_troop                   = 166
slot_center_walker_7_troop                   = 167
slot_center_walker_8_troop                   = 168
slot_center_walker_9_troop                   = 169

slot_center_walker_0_dna                     = 170
slot_center_walker_1_dna                     = 171
slot_center_walker_2_dna                     = 172
slot_center_walker_3_dna                     = 173
slot_center_walker_4_dna                     = 174
slot_center_walker_5_dna                     = 175
slot_center_walker_6_dna                     = 176
slot_center_walker_7_dna                     = 177
slot_center_walker_8_dna                     = 178
slot_center_walker_9_dna                     = 179

slot_center_walker_0_type                    = 180
slot_center_walker_1_type                    = 181
slot_center_walker_2_type                    = 182
slot_center_walker_3_type                    = 183
slot_center_walker_4_type                    = 184
slot_center_walker_5_type                    = 185
slot_center_walker_6_type                    = 186
slot_center_walker_7_type                    = 187
slot_center_walker_8_type                    = 188
slot_center_walker_9_type                    = 189

slot_town_trade_route_1           = 190
slot_town_trade_route_2           = 191
slot_town_trade_route_3           = 192
slot_town_trade_route_4           = 193
slot_town_trade_route_5           = 194
slot_town_trade_route_6           = 195
slot_town_trade_route_7           = 196
slot_town_trade_route_8           = 197
slot_town_trade_route_9           = 198
slot_town_trade_route_10          = 199
slot_town_trade_route_11          = 200
slot_town_trade_route_12          = 201
slot_town_trade_route_13          = 202
slot_town_trade_route_14          = 203
slot_town_trade_route_15          = 204
slot_town_trade_routes_begin = slot_town_trade_route_1
slot_town_trade_routes_end = slot_town_trade_route_15 + 1


num_trade_goods = itm_siege_supply - itm_spice

#These affect production but in some cases also demand, so it is perhaps easier to itemize them than to have separate 
slot_village_number_of_cattle   = 205
slot_center_head_cattle         = 205 #dried meat, cheese, hides, butter
slot_center_head_sheep			= 206 #sausages, wool
slot_center_head_horses		 	= 207 #horses can be a trade item used in tracking but which are never offered for sale

slot_center_acres_pasture       = 208 #pasture area for grazing of cattles and sheeps, if this value is high then number of cattles and sheeps increase faster

slot_production_sources_begin   = 209
slot_center_acres_grain			= 209 #grain
slot_center_acres_olives        = 210 #olives
slot_center_acres_vineyard		= 211 #fruit
slot_center_acres_flax          = 212 #flax
slot_center_acres_dates			= 213 #dates

slot_center_fishing_fleet		= 214 #smoked fish
slot_center_salt_pans		    = 215 #salt

slot_center_apiaries       		= 216 #honey
slot_center_silk_farms			= 217 #silk
slot_center_kirmiz_farms		= 218 #dyes

slot_center_iron_deposits       = 219 #iron
slot_center_fur_traps			= 220 #furs

slot_center_mills				= 221 #bread
slot_center_breweries			= 222 #ale
slot_center_wine_presses		= 223 #wine
slot_center_olive_presses		= 224 #oil

slot_center_linen_looms			= 225 #linen
slot_center_silk_looms          = 226 #velvet
slot_center_wool_looms          = 227 #wool cloth

slot_center_pottery_kilns		= 228 #pottery
slot_center_smithies			= 229 #tools
slot_center_tanneries			= 230 #leatherwork
slot_center_spice_farms			= 231 #spice

slot_center_household_gardens   = 232 #cabbages
slot_production_sources_end     = 233
#chicken and pork are perishable and non-tradeable, and based on grain production

slot_town_last_nearby_fire_time                         = 240

slot_party_following_orders_of_troop        = 244
slot_party_orders_type				        = 245
slot_party_orders_object				    = 246
slot_party_orders_time				    	= 247

slot_party_temp_slot_1			            = 248 #right now used only within a single script, merchant_road_info_to_s42, to denote closed roads. Now also used in comparative scripts
slot_party_under_player_suggestion			= 249 #move this up a bit
slot_town_trade_good_prices_begin 			= 250

slot_center_last_reconnoitered_by_faction_time 				= 350


#slot_party_type values
spt_castle             = 2
spt_town               = 3
spt_village            = 4
spt_bandit_lair        = 9

spt_kingdom_hero_party = 10
spt_kingdom_caravan    = 11
spt_village_farmer     = 12
spt_cattle_herd        = 13

spt_ship_land		   = 20
spt_port               = 21


#slot_faction_state values
sfs_active                     = 0
sfs_defeated                   = 1
sfs_inactive                   = 2
sfs_inactive_rebellion         = 3
sfs_beginning_rebellion        = 4


#slot_faction_ai_state values
sfai_default                   		 = 0 #also defending
sfai_gathering_army            		 = 1
sfai_attacking_center          		 = 2
sfai_raiding_village           		 = 3
sfai_attacking_enemy_army      		 = 4
sfai_attacking_enemies_around_center = 5
sfai_feast             		 		 = 6 #can be feast, wedding, or major tournament
#Social events are a generic aristocratic gathering. Tournaments take place if they are in a town, and hunts take place if they are at a castle.
#Weddings will take place at social events between betrothed couples if they have been engaged for at least a month, if the lady's guardian is the town lord, and if both bride and groom are present
sfai_nascent_rebellion          = 7


#slot_party_ai_state values
spai_undefined                  = -1
spai_besieging_center           = 1
spai_patrolling_around_center   = 4
spai_raiding_around_center      = 5

spai_holding_center             = 7

spai_engaging_army              = 10
spai_accompanying_army          = 11
spai_screening_army             = 12
spai_trading_with_town          = 13
spai_retreating_to_center       = 14

spai_visiting_village           = 16

#slot_village_state values
svs_normal                      = 0
svs_being_raided                = 1
svs_looted                      = 2
svs_recovering                  = 3
svs_deserted                    = 4
svs_under_siege                 = 5

#$g_player_icon_state values
pis_normal                      = 0
pis_camping                     = 1
pis_ship                        = 2

#$main_party_loot_policy values
mplp_dump  = -1
mplp_none  = 0 # identical to dump, but NPCs may warn about it
mplp_sell  = 1
mplp_share = 2

########################################################
##  SCENE SLOTS            #############################
########################################################
slot_scene_visited              = 0
slot_scene_belfry_props_begin   = 10



########################################################
##  HERO TROOP SLOTS            ########################
########################################################

slot_troop_occupation          = 2
slot_troop_state               = 3  
slot_troop_last_talk_time      = 4
slot_troop_met                 = 5 # 0 = not met, 1 = met
slot_troop_courtship_state     = 5 # 2 = professed admiration, 3 = agreed to seek a marriage, 4 = ended relationship
slot_troop_party_template      = 6
slot_troop_renown              = 7
slot_troop_prisoner_of_party   = 8  # important for heroes only
slot_troop_present_at_event    = 9
slot_troop_leaded_party         = 10 # important for kingdom heroes only
slot_troop_wealth               = 11 # important for kingdom heroes only
slot_troop_cur_center           = 12 # important for royal family members only (non-kingdom heroes)
slot_troop_banner_scene_prop    = 13 # important for kingdom heroes and player only
slot_troop_original_faction     = 14 # for pretenders
slot_troop_home_port            = 14 # for boat captains

slot_troop_age                 =  18
slot_troop_age_appearance      =  19

slot_troop_does_not_give_quest = 20
slot_troop_player_debt         = 21
slot_troop_player_relation     = 22

slot_troop_last_quest          = 24
slot_troop_last_quest_betrayed = 25
slot_troop_last_persuasion_time= 26
slot_troop_last_comment_time   = 27
slot_troop_spawned_before      = 28
slot_troop_last_comment_slot   = 29

slot_troop_spouse              = 30
slot_troop_father              = 31
slot_troop_mother              = 32
slot_troop_guardian            = 33 #Usually siblings are identified by a common parent.This is used for brothers if the father is not an active npc. At some point we might introduce geneologies
slot_troop_betrothed           = 34 #Obviously superseded once slot_troop_spouse is filled
#other relations are derived from one's parents 
slot_troop_love_interest_1     = 35 #each unmarried lord has three love interests
slot_troop_love_interest_2     = 36
slot_troop_love_interest_3     = 37
slot_troop_love_interests_end  = 38

slot_lady_no_messages          				= 37
slot_lady_last_suitor          				= 38
slot_lord_granted_courtship_permission      = 38
slot_troop_betrothal_time                   = 39 #used in scheduling the wedding
slot_lady_used_tournament					= 40

slot_troop_trainer_met                       = 30
slot_troop_trainer_waiting_for_result        = 31
slot_troop_trainer_training_fight_won        = 32
slot_troop_trainer_num_opponents_to_beat     = 33
slot_troop_trainer_training_system_explained = 34
slot_troop_trainer_opponent_troop            = 35
slot_troop_trainer_training_difficulty       = 36
slot_troop_trainer_training_fight_won        = 37

slot_troop_merchant_repairs_item             = 30
slot_troop_merchant_repairs_done             = 31

slot_troop_current_rumor       = 45
slot_troop_temp_slot           = 46
slot_troop_promised_fief       = 47

slot_troop_temp_decision_seed      = 49 #Resets at recalculate_ai
slot_troop_recruitment_random      = 50 #used in a number of different places in the intrigue procedures to overcome intermediate hurdles, although not for the final calculation, might be replaced at some point by the global decision seed
#Decision seeds can be used so that some randomness can be added to NPC decisions, without allowing the player to spam the NPC with suggestions
#The temp decision seed is reset 24 to 48 hours after the NPC last spoke to the player, while the set seed only changes in special occasions
#The single seed is used with varying modula to give high/low outcomes on different issues, without using a separate slot for each issue
slot_troop_intrigue_impatience        = 51
slot_lord_reputation_type     		  = 52
slot_lord_recruitment_argument        = 53 #the last argument proposed by the player to the lord
slot_lord_recruitment_candidate       = 54 #the last candidate proposed by the player to the lord
slot_troop_change_to_faction          = 55

# Companion-related constants
slot_troop_first_encountered          = 59
slot_troop_home                       = 60

slot_troop_morality_state       = 61
tms_no_problem         = 0
tms_acknowledged       = 1
tms_dismissed          = 2

slot_troop_morality_type = 62
tmt_aristocratic = 1
tmt_egalitarian = 2
tmt_humanitarian = 3
tmt_honest = 4
tmt_pious = 5

slot_troop_morality_value = 63

slot_troop_2ary_morality_type  = 64
slot_troop_2ary_morality_state = 65
slot_troop_2ary_morality_value = 66

slot_troop_town_with_contacts  = 67
slot_troop_town_contact_type   = 68 # 1 are nobles, 2 are commons
slot_troop_morality_penalties =  69 # accumulated grievances from morality conflicts

slot_troop_personalityclash_object   = 71 # 0 = they have no problem, 1 = they have a problem
slot_troop_personalityclash_state    = 72 # 1 = pclash_penalty_to_self, 2 = pclash_penalty_to_other, 3 = pclash_penalty_to_other,
pclash_penalty_to_self  = 1
pclash_penalty_to_other = 2
pclash_penalty_to_both  = 3

slot_troop_personalityclash2_object   = 73
slot_troop_personalityclash2_state    = 74

slot_troop_personalitymatch_object    = 75
slot_troop_personalitymatch_state     = 76
slot_troop_personalityclash_penalties = 77 ### accumulated grievances from personality clash

slot_troop_home_speech_delivered = 78 #only for companions
slot_troop_discussed_rebellion   = 78 #only for pretenders

slot_troop_fights_in_tournaments = 79 #only in player party

#courtship slots
slot_lady_courtship_heroic_recited 	    = 74
slot_lady_courtship_allegoric_recited 	= 75
slot_lady_courtship_comic_recited 		= 76
slot_lady_courtship_mystic_recited 		= 77
slot_lady_courtship_tragic_recited 		= 78

#NPC history slots
slot_troop_met_previously        = 80
slot_troop_turned_down_twice     = 81
slot_troop_playerparty_history   = 82

pp_history_scattered         = 1
pp_history_dismissed         = 2
pp_history_quit              = 3
pp_history_indeterminate     = 4

slot_troop_playerparty_history_string   = 83
slot_troop_return_renown        = 84

#conversation strings -- must be in this order!
slot_troop_intro 						= 101
slot_troop_intro_response_1 			= 102
slot_troop_intro_response_2 			= 103
slot_troop_backstory_a 					= 104
slot_troop_backstory_b 					= 105
slot_troop_backstory_c 					= 106
slot_troop_backstory_delayed 			= 107
slot_troop_backstory_response_1 		= 108
slot_troop_backstory_response_2 		= 109
slot_troop_signup   					= 110
slot_troop_signup_2 					= 111
slot_troop_signup_response_1 			= 112
slot_troop_signup_response_2 			= 113
slot_troop_mentions_payment 			= 114 #Not used, but written
slot_troop_payment_response 			= 115 #Not used, but written
slot_troop_morality_speech   			= 116
slot_troop_2ary_morality_speech 		= 117
slot_troop_personalityclash_speech 		= 118
slot_troop_personalityclash_speech_b 	= 119
slot_troop_personalityclash2_speech 	= 120
slot_troop_personalityclash2_speech_b 	= 121
slot_troop_personalitymatch_speech 		= 122
slot_troop_personalitymatch_speech_b 	= 123
slot_troop_retirement_speech 			= 124
slot_troop_rehire_speech 				= 125
slot_troop_home_intro           		= 126
slot_troop_home_description    			= 127
slot_troop_home_description_2 			= 128
slot_troop_home_recap         			= 129
slot_troop_honorific   					= 130
slot_troop_kingsupport_string_1			= 131
slot_troop_kingsupport_string_2			= 132
slot_troop_kingsupport_string_2a		= 133
slot_troop_kingsupport_string_2b		= 134
slot_troop_kingsupport_string_3			= 135
slot_troop_kingsupport_objection_string	= 136
slot_troop_intel_gathering_string	    = 137
slot_troop_fief_acceptance_string	    = 138
slot_troop_woman_to_woman_string	    = 139
slot_troop_turn_against_string	        = 140

slot_troop_strings_end 					= 141

slot_troop_payment_request 				= 141
slot_troop_kingsupport_state			= 142
slot_troop_kingsupport_argument			= 143
slot_troop_kingsupport_opponent			= 144
slot_troop_kingsupport_objection_state  = 145 # 0 = default, 1 = needs to voice, 2 = has voiced

slot_troop_is_in_bounty_hunter_guild    = 146 #RAMARAUNT BOUNTY CAMP -1 = no, 1 = yes

slot_troop_days_on_mission		        = 150
slot_troop_current_mission			    = 151
slot_troop_mission_object               = 152
npc_mission_kingsupport					= 1
npc_mission_gather_intel                = 2
npc_mission_peace_request               = 3
npc_mission_pledge_vassal               = 4
npc_mission_seek_recognition            = 5
npc_mission_test_waters                 = 6
npc_mission_non_aggression              = 7
npc_mission_rejoin_when_possible        = 8

#Number of routed agents after battle ends.
slot_troop_player_routed_agents                 = 146
slot_troop_ally_routed_agents                   = 147
slot_troop_enemy_routed_agents                  = 148

#Special quest slots
slot_troop_mission_participation        = 149
mp_unaware                              = 0 
mp_stay_out                             = 1 
mp_prison_break_fight                   = 2 
mp_prison_break_stand_back              = 3 
mp_prison_break_escaped                 = 4 
mp_prison_break_caught                  = 5 

#Below are some constants to expand the political system a bit. The idea is to make quarrels less random, but instead make them serve a rational purpose -- as a disincentive to lords to seek 

slot_troop_controversy                     = 150 #Determines whether or not a troop is likely to receive fief or marshalship
slot_troop_recent_offense_type 	           = 151 #failure to join army, failure to support colleague
slot_troop_recent_offense_object           = 152 #to whom it happened
slot_troop_recent_offense_time             = 153
slot_troop_stance_on_faction_issue         = 154 #when it happened

tro_failed_to_join_army                    = 1
tro_failed_to_support_colleague            = 2

#CONTROVERSY
#This is used to create a more "rational choice" model of faction politics, in which lords pick fights with other lords for gain, rather than simply because of clashing personalities
#It is intended to be a limiting factor for players and lords in their ability to intrigue against each other. It represents the embroilment of a lord in internal factional disputes. In contemporary media English, a lord with high "controversy" would be described as "embattled."
#The main effect of high controversy is that it disqualifies a lord from receiving a fief or an appointment
#It is a key political concept because it provides incentive for much of the political activity. For example, Lord Red Senior is worried that his rival, Lord Blue Senior, is going to get a fied which Lord Red wants. So, Lord Red turns to his protege, Lord Orange Junior, to attack Lord Blue in public. The fief goes to Lord Red instead of Lord Blue, and Lord Red helps Lord Orange at a later date.


slot_troop_will_join_prison_break      = 161

troop_slots_reserved_for_relations_start        = 165 #this is based on id_troops, and might change

slot_troop_relations_begin				= 0 #this creates an array for relations between troops; use this to specify an offset
											#Right now, lords start at 165 and run to around 290, including pretenders
											
### Troop occupations slot_troop_occupation
slto_inactive           = 0 #for companions at the beginning of the game

slto_kingdom_hero       = 2
slto_inactive_pretender = 3
slto_retirement         = 4
slto_player_companion   = 5 #This is specifically for companions in the employ of the player -- ie, in the party, or on a mission
slto_kingdom_lady       = 6 #Usually inactive (Calradia is a traditional place). However, can be made potentially active if active_npcs are expanded to include ladies

stl_unassigned          = -1
stl_reserved_for_player = -2
stl_rejected_by_player  = -3

########################################################
##  REGULAR TROOP SLOTS            #####################
########################################################

# Using items to upgrade (or sidegrade) troops
slot_soldier_elite_upgrade_to		= 10
slot_soldier_elite_upgrade_with		= 11

											
########################################################
##  PLAYER SLOTS           #############################
########################################################

slot_player_spawned_this_round                 = 0
slot_player_last_rounds_used_item_earnings     = 1
slot_player_selected_item_indices_begin        = 2
slot_player_selected_item_indices_end          = 11
slot_player_cur_selected_item_indices_begin    = slot_player_selected_item_indices_end
slot_player_cur_selected_item_indices_end      = slot_player_selected_item_indices_end + 9
slot_player_join_time                          = 21
slot_player_button_index                       = 22 #used for presentations
slot_player_can_answer_poll                    = 23
slot_player_first_spawn                        = 24
slot_player_spawned_at_siege_round             = 25
slot_player_poll_disabled_until_time           = 26
slot_player_total_equipment_value              = 27
slot_player_last_team_select_time              = 28
slot_player_death_pos_x                        = 29
slot_player_death_pos_y                        = 30
slot_player_death_pos_z                        = 31
slot_player_damage_given_to_target_1           = 32 #used only in destroy mod
slot_player_damage_given_to_target_2           = 33 #used only in destroy mod
slot_player_last_bot_count                     = 34
slot_player_bot_type_1_wanted                  = 35
slot_player_bot_type_2_wanted                  = 36
slot_player_bot_type_3_wanted                  = 37
slot_player_bot_type_4_wanted                  = 38
slot_player_spawn_count                        = 39

# character backgrounds
cb_noble = 1
cb_merchant = 2
cb_guard = 3
cb_forester = 4
cb_nomad = 5
cb_thief = 6
cb_priest = 7

cb2_page = 0
cb2_apprentice = 1
cb2_urchin  = 2
cb2_steppe_child = 3
cb2_merchants_helper = 4
cb2_mummer = 5
cb2_courtier = 6
cb2_noble = 7
cb2_acolyte = 8

cb3_bravo = 1
cb3_merc = 2
cb3_poacher = 3
cb3_craftsman = 4
cb3_peddler = 5
cb3_preacher = 6
cb3_troubadour = 7
cb3_squire = 8
cb3_lady_in_waiting = 9
cb3_student = 10

cb4_revenge = 1
cb4_loss    = 2
cb4_wanderlust =  3
cb4_fervor =  4
cb4_disown  = 5
cb4_greed  = 6

########################################################
##  TEAM SLOTS             #############################
########################################################

# Multiplayer
slot_team_flag_situation                       = 0

# Singleplayer
# For the simplifed morale system:
slot_team_relation_to_player			= 0
slot_team_fighting_strength				= 1
slot_team_routing_strength				= 2
slot_team_defeated_strength				= 3

########################################################
##  QUEST SLOTS            #############################
########################################################

slot_quest_target_center            = 1
slot_quest_target_troop             = 2
slot_quest_target_faction           = 3
slot_quest_object_troop             = 4

slot_quest_giver_troop              = 6
slot_quest_object_center            = 7
slot_quest_target_party             = 8
slot_quest_target_party_template    = 9
slot_quest_target_amount            = 10
slot_quest_current_state            = 11
slot_quest_giver_center             = 12
slot_quest_target_dna               = 13
slot_quest_target_item              = 14
slot_quest_object_faction           = 15

slot_quest_target_state             = 16
slot_quest_object_state             = 17

slot_quest_convince_value           = 19
slot_quest_importance               = 20
slot_quest_xp_reward                = 21
slot_quest_gold_reward              = 22
slot_quest_expiration_days          = 23
slot_quest_dont_give_again_period   = 24
slot_quest_dont_give_again_remaining_days = 25

slot_quest_failure_consequence      = 26
slot_quest_temp_slot      			= 27

########################################################
##  PARTY TEMPLATE SLOTS   #############################
########################################################

slot_party_template_num_killed             = 1

slot_party_template_lair_type    	 	   = 3
slot_party_template_lair_party    		   = 4
slot_party_template_lair_spawnpoint_begin  = 5
slot_party_template_lair_spawnpoint_end    = 6


########################################################
##  SCENE PROP SLOTS       #############################
########################################################

scene_prop_open_or_close_slot       = 1
scene_prop_smoke_effect_done        = 2
scene_prop_number_of_agents_pushing = 3 #for belfries only
scene_prop_next_entry_point_id      = 4 #for belfries only
scene_prop_belfry_platform_moved    = 5 #for belfries only
scene_prop_slots_end                = 6

########################################################

# Team Relations
rel_enemy   = 0
rel_neutral = 1
rel_ally    = 2

#Encounter types
enctype_fighting_against_village_raid = 1
enctype_catched_during_village_raid   = 2

#Talk contexts
tc_town_talk                  = 0
tc_court_talk   	      	  = 1
tc_party_encounter            = 2
tc_castle_gate                = 3
tc_siege_commander            = 4
tc_join_battle_ally           = 5
tc_join_battle_enemy          = 6
tc_castle_commander           = 7
tc_hero_freed                 = 8
tc_hero_defeated              = 9
tc_entering_center_quest_talk = 10
tc_back_alley                 = 11
tc_siege_won_seneschal        = 12
tc_ally_thanks                = 13
tc_tavern_talk                = 14
tc_rebel_thanks               = 15
tc_garden            		  = 16
tc_courtship            	  = 16
tc_after_duel            	  = 17
tc_prison_break               = 18
tc_escape               	  = 19
tc_give_center_to_fief        = 20
tc_merchants_house            = 21

#Log entry types
logent_village_raided            = 1
logent_village_extorted          = 2
logent_caravan_accosted          = 3 #in caravan accosted, center and troop object are -1, and the defender's faction is the object
logent_traveller_attacked        = 3 #in traveller attacked, origin and destination are center and troop object, and the attacker's faction is the object
logent_helped_peasants           = 4 
logent_party_traded              = 5

logent_castle_captured_by_player              = 10
logent_lord_defeated_by_player                = 11
logent_lord_captured_by_player                = 12
logent_lord_defeated_but_let_go_by_player     = 13
logent_player_defeated_by_lord                = 14
logent_player_retreated_from_lord             = 15
logent_player_retreated_from_lord_cowardly    = 16
logent_lord_helped_by_player                  = 17
logent_player_participated_in_siege           = 18
logent_player_participated_in_major_battle    = 19
logent_castle_given_to_lord_by_player         = 20
logent_pledged_allegiance                     = 21
logent_liege_grants_fief_to_vassal            = 22
logent_renounced_allegiance                   = 23 
logent_player_claims_throne_1    		      = 24
logent_player_claims_throne_2    		      = 25
logent_troop_feels_cheated_by_troop_over_land		   = 26
logent_ruler_intervenes_in_quarrel                     = 27
logent_lords_quarrel_over_land                         = 28
logent_lords_quarrel_over_insult                       = 29
logent_marshal_vs_lord_quarrel                  	   = 30
logent_lords_quarrel_over_woman                        = 31
logent_lord_protests_marshall_appointment			   = 32
logent_lord_blames_defeat						   	   = 33
logent_player_suggestion_succeeded					   = 35
logent_player_suggestion_failed					       = 36
logent_liege_promises_fief_to_vassal				   = 37
logent_lord_insults_lord_for_cowardice                 = 38
logent_lord_insults_lord_for_rashness                  = 39
logent_lord_insults_lord_for_abandonment               = 40
logent_lord_insults_lord_for_indecision                = 41
logent_lord_insults_lord_for_cruelty                   = 42
logent_lord_insults_lord_for_dishonor                  = 43
logent_game_start                           = 45 
logent_poem_composed                        = 46 ##Not added
logent_tournament_distinguished             = 47 ##Not added
logent_tournament_won                       = 48 ##Not added

#logent courtship - lady is always actor, suitor is always troop object
logent_lady_favors_suitor                   = 51 #basically for gossip
logent_lady_betrothed_to_suitor_by_choice   = 52
logent_lady_betrothed_to_suitor_by_family   = 53
logent_lady_rejects_suitor                  = 54
logent_lady_father_rejects_suitor           = 55
logent_lady_marries_lord                    = 56
logent_lady_elopes_with_lord                = 57
logent_lady_rejected_by_suitor              = 58
logent_lady_betrothed_to_suitor_by_pressure = 59 #mostly for gossip
logent_lady_and_suitor_break_engagement		= 60
logent_lady_marries_suitor				    = 61
logent_lord_holds_lady_hostages             = 62
logent_challenger_defeats_lord_in_duel      = 63
logent_challenger_loses_to_lord_in_duel     = 64

logent_player_stole_cattles_from_village    = 66

logent_party_spots_wanted_bandits           = 70

logent_border_incident_cattle_stolen          = 72 #possibly add this to rumors for non-player faction
logent_border_incident_bride_abducted         = 73 #possibly add this to rumors for non-player faction
logent_border_incident_villagers_killed       = 74 #possibly add this to rumors for non-player faction
logent_border_incident_subjects_mistreated    = 75 #possibly add this to rumors for non-player faction

#These supplement caravans accosted and villages burnt, in that they create a provocation. So far, they only refer to the player
logent_border_incident_troop_attacks_neutral  = 76
logent_border_incident_troop_breaks_truce     = 77
logent_border_incident_troop_suborns_lord     = 78

logent_policy_ruler_attacks_without_provocation 			= 80
logent_policy_ruler_ignores_provocation         			= 81 #possibly add this to rumors for non-player factions
logent_policy_ruler_makes_peace_too_soon        			= 82
logent_policy_ruler_declares_war_with_justification         = 83
logent_policy_ruler_breaks_truce                            = 84
logent_policy_ruler_issues_indictment_just                  = 85 #possibly add this to rumors for non-player faction
logent_policy_ruler_issues_indictment_questionable          = 86 #possibly add this to rumors for non-player faction

logent_player_faction_declares_war						    = 90 #this doubles for declare war to extend power
logent_faction_declares_war_out_of_personal_enmity		    = 91
logent_faction_declares_war_to_regain_territory 		    = 92
logent_faction_declares_war_to_curb_power					= 93
logent_faction_declares_war_to_respond_to_provocation	    = 94
logent_war_declaration_types_end							= 95

#lord reputation type, for commentaries
#"Martial" will be twice as common as the other types
lrep_none           = 0 
lrep_martial        = 1 #chivalrous but not terribly empathetic or introspective, - eg Richard Lionheart, your average 14th century French baron
lrep_quarrelsome    = 2 #spiteful, cynical, a bit paranoid, possibly hotheaded - eg Robert Graves' Tiberius, some of Charles VI's uncles
lrep_selfrighteous  = 3 #coldblooded, moralizing, often cruel - eg William the Conqueror, Timur, Octavian, Aurangzeb (although he is arguably upstanding instead, particularly after his accession)
lrep_cunning        = 4 #coldblooded, pragmatic, amoral - eg Louis XI, Guiscard, Akbar Khan, Abd al-Aziz Ibn Saud
lrep_debauched      = 5 #spiteful, amoral, sadistic - eg Caligula, Tuchman's Charles of Navarre
lrep_goodnatured    = 6 #chivalrous, benevolent, perhaps a little too decent to be a good warlord - eg Hussein ibn Ali. Few well-known historical examples maybe. because many lack the drive to rise to faction leadership. Ranjit Singh has aspects
lrep_upstanding     = 7 #moralizing, benevolent, pragmatic, - eg Bernard Cornwell's Alfred, Charlemagne, Salah al-Din, Sher Shah Suri

#commoner reputation type, for some (ex-)companions
lrep_roguish        = 8 #Tries to live life as a lord to the full
lrep_benefactor     = 9 #Tries to improve lot of folks on land
lrep_custodian      = 10 #Tries to maximize fief's earning potential

#lreps specific to dependent noblewomen
lrep_conventional    = 21 #Charlotte York in SATC seasons 1-2, probably most medieval aristocrats
lrep_adventurous     = 22 #Tomboyish. However, this basically means that she likes to travel and hunt, and perhaps yearn for wider adventures. However, medieval noblewomen who fight are rare, and those that attempt to live independently of a man are rarer still, and best represented by pre-scripted individuals like companions
lrep_otherworldly    = 23 #Prone to mysticism, romantic. 
lrep_ambitious       = 24 #Lady Macbeth
lrep_moralist        = 25 #Equivalent of upstanding or benefactor -- takes nobless oblige, and her traditional role as repository of morality, very seriously. Based loosely on Christine de Pisa 

courtship_poem_tragic      = 1 #Emphasizes longing, Laila and Majnoon
courtship_poem_heroic      = 2 #Norse sagas with female heroines
courtship_poem_comic       = 3 #Emphasis on witty repartee -- Contrasto (Sicilian school satire) 
courtship_poem_mystic      = 4 #Sufi poetry. Song of Songs
courtship_poem_allegoric   = 5 #Idealizes woman as a civilizing force -- the Romance of the Rose, Siege of the Castle of Love


tutorial_fighters_begin = "trp_tutorial_fighter_1"
tutorial_fighters_end   = "trp_tutorial_archer_1"

#Walker types: 
walkert_default            = 0
walkert_needs_money        = 1
walkert_needs_money_helped = 2
walkert_spy                = 3
num_town_walkers = 8
town_walker_entries_start = 32

reinforcement_cost_easy     = 600
reinforcement_cost_moderate = 450
reinforcement_cost_hard     = 300

max_bandit_parties_easy     = 16 # Was 14 at mount&blade, 18 in warband, 16 last decision
max_bandit_parties_moderate = 24 # Bandits are more spread out now, so we might need a few more
max_bandit_parties_hard     = 32 # If you play on hard, I assume you like a challenge...
max_looter_parties = 42 # Was 33 at mount&blade, 50 in warband, 42 last decision; does not scale with difficulty, looters are basically XP on legs

bandit_spawn_radius = 25
deserter_spawn_radius = 4
merchant_toll_duration = 72 #Tolls are valid for 72 hours
hero_escape_after_defeat_chance = 70
raid_distance = 4
fire_duration = 4 #fires takes 4 hours
num_tournament_rounds = 6 # -> 64 participants
ship_charter_cost = 100 # per day

surnames_begin = "str_surname_1"
surnames_end = "str_surnames_end"
names_begin = "str_name_1"
names_end = surnames_begin
countersigns_begin = "str_countersign_1"
countersigns_end = names_begin
secret_signs_begin = "str_secret_sign_1"
secret_signs_end = countersigns_begin

kingdom_titles_male_begin = "str_faction_title_male_player"
kingdom_titles_female_begin = "str_faction_title_female_player"

kingdoms_begin = "fac_player_supporters_faction"
kingdoms_end = "fac_kingdoms_end"

npc_kingdoms_begin = "fac_kingdom_1"
npc_kingdoms_end = kingdoms_end

bandits_begin = "trp_bandit"
bandits_end = "trp_manhunter"

kingdom_ladies_begin = "trp_kingdom_1_lady_1"
kingdom_ladies_end = "trp_heroes_end"

#active NPCs in order: companions, kings, lords, pretenders
pretenders_begin = "trp_kingdom_1_pretender"
pretenders_end = kingdom_ladies_begin

lords_begin = "trp_knight_1_1"
lords_end = pretenders_begin

kings_begin = "trp_kingdom_1_lord"
kings_end = lords_begin

companions_begin = "trp_npc1"
companions_end = kings_begin

active_npcs_begin = "trp_npc1"
active_npcs_end = kingdom_ladies_begin
# "active_npcs_begin replaces kingdom_heroes_begin to allow for companions to become lords. Includes anyone who may at some point lead their own party: the original kingdom heroes, companions who may become kingdom heroes, and pretenders. (slto_kingdom_hero as an occupation means that you lead a party on the map. Pretenders have the occupation "slto_inactive_pretender", even if they are part of a player's party, until they have their own independent party)
# If you're a modder and you don't want to go through and switch every kingdom_heroes to active_npcs, simply define a constant: kingdom_heroes_begin = active_npcs_begin., and kingdom_heroes_end = active_npcs_end. I haven't tested for that, but I think it should work.
# Hint: It does not work. Fix, maybe?

active_npcs_including_player_begin = "trp_kingdom_heroes_including_player_begin"
original_kingdom_heroes_begin = "trp_kingdom_1_lord"

heroes_begin = active_npcs_begin
heroes_end = kingdom_ladies_end

#Ramaraunt ADD FOR BOUNTY QUESTS
chests_begin = "trp_household_possessions"
chests_end = "trp_temp_array_a"
#Ramaraunt END FOR BOUNTY QUESTS

#Ramaraunt ADD FOR BOUNTY QUESTS
bandit_fugitives_begin = "trp_desert_bandit_fugitive"
bandit_fugitives_end = "trp_black_khergit_horseman"
#Ramaraunt END FOR BOUNTY QUESTS

soldiers_begin = "trp_farmer"
soldiers_end = "trp_kidnapped_girl"

pretenders_begin = "trp_kingdom_1_pretender"
pretenders_end = active_npcs_end

tavern_minstrels_begin = "trp_tavern_minstrel_1"
tavern_minstrels_end   = "trp_kingdom_heroes_including_player_begin"

tavern_booksellers_begin = "trp_tavern_bookseller_1"
tavern_booksellers_end   = tavern_minstrels_begin

tavern_captains_begin = "trp_tavern_captain_1"
tavern_captains_end   = tavern_booksellers_begin

tavern_travelers_begin = "trp_tavern_traveler_1"
tavern_travelers_end   = tavern_captains_begin

ransom_brokers_begin = "trp_ransom_broker_1"
ransom_brokers_end   = tavern_travelers_begin

mercenary_troops_begin = "trp_watchman"
mercenary_troops_end = "trp_mercenary_musketeer"

outlaws_begin = "trp_looter"
outlaws_end = "trp_manhunter"

arena_champions_begin = "trp_xerina"
arena_champions_end = "trp_fight_promoter"

arena_fighters_begin = "trp_arena_training_fighter_1"
arena_fighters_end = "trp_cattle"

multiplayer_troops_begin = "trp_swadian_crossbowman_multiplayer"
multiplayer_troops_end = "trp_multiplayer_end"

multiplayer_ai_troops_begin = "trp_swadian_crossbowman_multiplayer_ai"
multiplayer_ai_troops_end = multiplayer_troops_begin

multiplayer_scenes_begin = "scn_multi_scene_1"
multiplayer_scenes_end = "scn_multiplayer_maps_end"

multiplayer_scene_names_begin = "str_multi_scene_1"
multiplayer_scene_names_end = "str_multi_scene_end"

multiplayer_flag_projections_begin = "mesh_flag_project_sw"
multiplayer_flag_projections_end = "mesh_flag_projects_end"

multiplayer_flag_taken_projections_begin = "mesh_flag_project_sw_miss"
multiplayer_flag_taken_projections_end = "mesh_flag_project_misses_end"

multiplayer_game_type_names_begin = "str_multi_game_type_1"
multiplayer_game_type_names_end = "str_multi_game_types_end"

quick_battle_troops_begin = "trp_quick_battle_troop_1"
quick_battle_troops_end = "trp_quick_battle_troops_end"

quick_battle_troop_texts_begin = "str_quick_battle_troop_1"
quick_battle_troop_texts_end = "str_quick_battle_troops_end"

quick_battle_scenes_begin = "scn_quick_battle_scene_1"
quick_battle_scenes_end = "scn_quick_battle_maps_end"

quick_battle_scene_images_begin = "mesh_cb_ui_maps_scene_01"

quick_battle_battle_scenes_begin = quick_battle_scenes_begin
quick_battle_battle_scenes_end = "scn_quick_siege_scene_1"

quick_battle_siege_scenes_begin = quick_battle_battle_scenes_end
quick_battle_siege_scenes_end = quick_battle_scenes_end

quick_battle_scene_names_begin = "str_quick_battle_scene_1"

#Ramaraunt ADD Bounty Quests
bounty_quests_begin = "qst_dead_or_alive_party"
bounty_quests_end = "qst_quests_end"

bounty_quests_begin_2 = "qst_blank_quest_27"
bounty_quests_end_2 = "qst_blank_quest_27"
#Ramaraunt END

lord_quests_begin = "qst_deliver_message"
lord_quests_end   = "qst_follow_army"

lord_quests_begin_2 = "qst_destroy_bandit_lair"
lord_quests_end_2   = "qst_blank_quest_2"

enemy_lord_quests_begin = "qst_lend_surgeon"
enemy_lord_quests_end   = lord_quests_end

village_elder_quests_begin = "qst_deliver_grain"
village_elder_quests_end = "qst_eliminate_bandits_infesting_village"

village_elder_quests_begin_2 = "qst_blank_quest_6"
village_elder_quests_end_2   = "qst_blank_quest_6"

mayor_quests_begin  = "qst_move_cattle_herd"
mayor_quests_end    = village_elder_quests_begin

mayor_quests_begin_2 = "qst_blank_quest_11"
mayor_quests_end_2   = "qst_blank_quest_11"

lady_quests_begin = "qst_rescue_lord_by_replace"
lady_quests_end   = mayor_quests_begin

lady_quests_begin_2 = "qst_blank_quest_16"
lady_quests_end_2   = "qst_blank_quest_16"

army_quests_begin = "qst_deliver_cattle_to_army"
army_quests_end   = lady_quests_begin

army_quests_begin_2 = "qst_blank_quest_21"
army_quests_end_2   = "qst_blank_quest_21"

player_realm_quests_begin = "qst_resolve_dispute"
player_realm_quests_end = "qst_blank_quest_1"

player_realm_quests_begin_2 = "qst_blank_quest_26"
player_realm_quests_end_2 = "qst_blank_quest_26"

all_items_begin = 0
all_items_end = "itm_items_end"

all_quests_begin = 0
all_quests_end = "qst_quests_end"

locations_begin = "p_zendar"
locations_end   = "p_training_ground_1"

training_grounds_begin   = "p_training_ground_1"
training_grounds_end     = "p_tutorial_ground"

towns_begin = "p_town_1"
castles_begin = "p_castle_1"
villages_begin = "p_village_1"

towns_end = castles_begin
castles_end = villages_begin
villages_end = locations_begin

walled_centers_begin = towns_begin
walled_centers_end   = castles_end

centers_begin = towns_begin
centers_end   = villages_end

ports_begin   = "p_port_1"
ports_end     = "p_landed_ship"

#RAMARAUNT ADD ZENDAR PORT
zendar_port = "p_Port_of_Zendar"
zendar_tavern_cap = "trp_tavern_captain_zendar"
zendar_town = "p_zendar"
#RAMARAUNT END

scenes_begin = "scn_town_1_center"
scenes_end = "scn_castle_1_exterior"

regular_troops_begin       = "trp_novice_fighter"
regular_troops_end         = "trp_tournament_master"

arena_masters_begin    = "trp_town_1_arena_master"
arena_masters_end      = "trp_town_1_armorer"

training_gound_trainers_begin    = "trp_trainer_1"
training_gound_trainers_end      = "trp_ransom_broker_1"

town_walkers_begin = "trp_town_walker_m"
town_walkers_end = "trp_village_walker_m"

village_walkers_begin = "trp_village_walker_m"
village_walkers_end   = "trp_spy_walker_m"

spy_walkers_begin = "trp_spy_walker_m"
spy_walkers_end = "trp_tournament_master"

walkers_begin = town_walkers_begin
walkers_end   = spy_walkers_end

armor_merchants_begin  = "trp_town_1_armorer"
armor_merchants_end    = "trp_town_1_weaponsmith"

weapon_merchants_begin = "trp_town_1_weaponsmith"
weapon_merchants_end   = "trp_town_1_tavernkeeper"

tavernkeepers_begin    = "trp_town_1_tavernkeeper"
tavernkeepers_end      = "trp_town_1_merchant"

goods_merchants_begin  = "trp_town_1_merchant"
goods_merchants_end    = "trp_town_1_horse_merchant"

horse_merchants_begin  = "trp_town_1_horse_merchant"
horse_merchants_end    = "trp_town_1_mayor"

mayors_begin           = "trp_town_1_mayor"
mayors_end             = "trp_village_1_elder"

village_elders_begin   = "trp_village_1_elder"
village_elders_end     = "trp_merchants_end"

#Ramaraunt Add
bandit_spawns_begin = "p_plains_bandit_spawn_point_1"
bandit_spawns_end = "p_spawn_points_end"

fugitives_begin = "trp_desert_bandit_fugitive"
fugitives_end = "trp_fugitives_end"
#ramaraunt end


startup_merchants_begin = "trp_swadian_merchant"
startup_merchants_default = "trp_default_merchant"
startup_merchants_end = "trp_relative_of_merchant"

num_max_items = 10000 #used for multiplayer mode

average_price_factor = 1000
minimum_price_factor = 100
maximum_price_factor = 10000

village_prod_min = 0 #was -5
village_prod_max = 20 #was 20

trade_goods_begin = "itm_spice"
trade_goods_end = "itm_siege_supply"
food_begin = "itm_smoked_fish"
food_end = "itm_siege_supply"
reference_books_begin = "itm_book_wound_treatment_reference"
reference_books_end   = trade_goods_begin
readable_books_begin = "itm_book_tactics"
readable_books_end   = reference_books_begin
books_begin = readable_books_begin
books_end = reference_books_end
horses_begin = "itm_sumpter_horse"
horses_end = "itm_arrows"
ammo_begin = "itm_arrows"
ammo_end = "itm_leather_gloves"
armors_begin = "itm_leather_gloves"
armors_end = "itm_wooden_stick"
weapons_begin = "itm_wooden_stick"
weapons_end = "itm_wooden_shield"
shields_begin = "itm_wooden_shield"
shields_end = "itm_darts"
ranged_weapons_begin = "itm_darts"
ranged_weapons_end = "itm_torch"
equipment_begin = horses_begin
equipment_end = ranged_weapons_end

# Banner constants
banner_meshes_begin = "mesh_banner_a01"
banner_meshes_end_minus_one = "mesh_banner_f21"

arms_meshes_begin = "mesh_arms_a01"
arms_meshes_end_minus_one = "mesh_arms_f21"

banner_map_icons_begin = "icon_banner_01"
banner_map_icons_end_minus_one = "icon_banner_136"

banner_scene_props_begin = "spr_banner_a"
banner_scene_props_end_minus_one = "spr_banner_f21"

khergit_banners_begin_offset = 63
khergit_banners_end_offset = 84

sarranid_banners_begin_offset = 105
sarranid_banners_end_offset = 125

banners_end_offset = 144
banner_pages       = 9 # 16 per page

# Some constants for merchant inventories
merchant_inventory_space = 30
num_merchandise_goods = 40

# Note positions
note_troop_location = 3

#battle tactics
btactic_hold = 1
btactic_follow_leader = 2
btactic_charge = 3
btactic_stand_ground = 4

#default right mouse menu orders
cmenu_move = -7
cmenu_follow = -6

# Town center modes - resets in game menus during the options
tcm_default 		= 0
tcm_disguised 		= 1
tcm_prison_break 	= 2
tcm_escape      	= 3

# Arena battle modes
#abm_fight = 0
abm_training = 1
abm_visit = 2
abm_tournament = 3

# Camp training modes
ctm_melee    = 1
ctm_ranged   = 2
ctm_mounted  = 3
ctm_training = 4

# Village bandits attack modes
vba_normal          = 1
vba_after_training  = 2

arena_tier1_opponents_to_beat = 3
arena_tier1_prize = 5
arena_tier2_opponents_to_beat = 6
arena_tier2_prize = 10
arena_tier3_opponents_to_beat = 10
arena_tier3_prize = 25
arena_tier4_opponents_to_beat = 20
arena_tier4_prize = 60
arena_grand_prize = 250

color_msg_enemy_routed = 0x44CCAA # Should be same color as killed or wounded
color_msg_ally_routed  = 0xCCCC33 # yellow = routed, orange = wounded, red = killed
color_msg_ally_rallied = 0x33CC33 # green = rallied

#NORMAL ACHIEVEMENTS
ACHIEVEMENT_NONE_SHALL_PASS = 1,
ACHIEVEMENT_MAN_EATER = 2,
ACHIEVEMENT_THE_HOLY_HAND_GRENADE = 3,
ACHIEVEMENT_LOOK_AT_THE_BONES = 4,
ACHIEVEMENT_KHAAAN = 5,
ACHIEVEMENT_GET_UP_STAND_UP = 6,
ACHIEVEMENT_BARON_GOT_BACK = 7,
ACHIEVEMENT_BEST_SERVED_COLD = 8,
ACHIEVEMENT_TRICK_SHOT = 9,
ACHIEVEMENT_GAMBIT = 10,
ACHIEVEMENT_OLD_SCHOOL_SNIPER = 11,
ACHIEVEMENT_CALRADIAN_ARMY_KNIFE = 12,
ACHIEVEMENT_MOUNTAIN_BLADE = 13,
ACHIEVEMENT_HOLY_DIVER = 14,
ACHIEVEMENT_FORCE_OF_NATURE = 15,

#SKILL RELATED ACHIEVEMENTS:
ACHIEVEMENT_BRING_OUT_YOUR_DEAD = 16,
ACHIEVEMENT_MIGHT_MAKES_RIGHT = 17,
ACHIEVEMENT_COMMUNITY_SERVICE = 18,
ACHIEVEMENT_AGILE_WARRIOR = 19,
ACHIEVEMENT_MELEE_MASTER = 20,
ACHIEVEMENT_DEXTEROUS_DASTARD = 21,
ACHIEVEMENT_MIND_ON_THE_MONEY = 22,
ACHIEVEMENT_ART_OF_WAR = 23,
ACHIEVEMENT_THE_RANGER = 24,
ACHIEVEMENT_TROJAN_BUNNY_MAKER = 25,

#MAP RELATED ACHIEVEMENTS:
ACHIEVEMENT_MIGRATING_COCONUTS = 26,
ACHIEVEMENT_HELP_HELP_IM_BEING_REPRESSED = 27,
ACHIEVEMENT_SARRANIDIAN_NIGHTS = 28,
ACHIEVEMENT_OLD_DIRTY_SCOUNDREL = 29,
ACHIEVEMENT_THE_BANDIT = 30,
ACHIEVEMENT_GOT_MILK = 31,
ACHIEVEMENT_SOLD_INTO_SLAVERY = 32,
ACHIEVEMENT_MEDIEVAL_TIMES = 33,
ACHIEVEMENT_GOOD_SAMARITAN = 34,
ACHIEVEMENT_MORALE_LEADER = 35,
ACHIEVEMENT_ABUNDANT_FEAST = 36,
ACHIEVEMENT_BOOK_WORM = 37,
ACHIEVEMENT_ROMANTIC_WARRIOR = 38,

#POLITICALLY ORIENTED ACHIEVEMENTS:
ACHIEVEMENT_HAPPILY_EVER_AFTER = 39,
ACHIEVEMENT_HEART_BREAKER = 40,
ACHIEVEMENT_AUTONOMOUS_COLLECTIVE = 41,
ACHIEVEMENT_I_DUB_THEE = 42,
ACHIEVEMENT_SASSY = 43,
ACHIEVEMENT_THE_GOLDEN_THRONE = 44,
ACHIEVEMENT_KNIGHTS_OF_THE_ROUND = 45,
ACHIEVEMENT_TALKING_HELPS = 46,
ACHIEVEMENT_KINGMAKER = 47,
ACHIEVEMENT_PUGNACIOUS_D = 48,
ACHIEVEMENT_GOLD_FARMER = 49,
ACHIEVEMENT_ROYALITY_PAYMENT = 50,
ACHIEVEMENT_MEDIEVAL_EMLAK = 51,
ACHIEVEMENT_CALRADIAN_TEA_PARTY = 52,
ACHIEVEMENT_MANIFEST_DESTINY = 53,
ACHIEVEMENT_CONCILIO_CALRADI = 54,
ACHIEVEMENT_VICTUM_SEQUENS = 55,

#MULTIPLAYER ACHIEVEMENTS:
ACHIEVEMENT_THIS_IS_OUR_LAND = 56,
ACHIEVEMENT_SPOIL_THE_CHARGE = 57,
ACHIEVEMENT_HARASSING_HORSEMAN = 58,
ACHIEVEMENT_THROWING_STAR = 59,
ACHIEVEMENT_SHISH_KEBAB = 60,
ACHIEVEMENT_RUIN_THE_RAID = 61,
ACHIEVEMENT_LAST_MAN_STANDING = 62,
ACHIEVEMENT_EVERY_BREATH_YOU_TAKE = 63,
ACHIEVEMENT_CHOPPY_CHOP_CHOP = 64,
ACHIEVEMENT_MACE_IN_YER_FACE = 65,
ACHIEVEMENT_THE_HUSCARL = 66,
ACHIEVEMENT_GLORIOUS_MOTHER_FACTION = 67,
ACHIEVEMENT_ELITE_WARRIOR = 68,

#COMBINED ACHIEVEMENTS
ACHIEVEMENT_SON_OF_ODIN = 69,
ACHIEVEMENT_KING_ARTHUR = 70,
ACHIEVEMENT_KASSAI_MASTER = 71,
ACHIEVEMENT_IRON_BEAR = 72,
ACHIEVEMENT_LEGENDARY_RASTAM = 73,
ACHIEVEMENT_SVAROG_THE_MIGHTY = 74,

ACHIEVEMENT_MAN_HANDLER = 75,
ACHIEVEMENT_GIRL_POWER = 76,
ACHIEVEMENT_QUEEN = 77,
ACHIEVEMENT_EMPRESS = 78,
ACHIEVEMENT_TALK_OF_THE_TOWN = 79,
ACHIEVEMENT_LADY_OF_THE_LAKE = 80,


# Character Creation Presentation (1.0.2)
# Created by Windyplains.  Inspired by Dunde's character creation presentation in Custom Commander.

###########################################################################################################################
#####                                                MODULE SETTINGS                                                  #####
###########################################################################################################################

# script_mcc_generate_skill_set modes
limit_to_stats                         = 0
equip_the_player                       = 1

###########################################################################################################################
#####                                              CHARACTER BACKGROUNDS                                              #####
###########################################################################################################################

# character backgrounds
cb_noble = 7
cb_merchant = 6
cb_guard = 5
cb_forester = 4
cb_nomad = 3
cb_thief = 2
cb_doctor = 1
cb_priest = 0

cb2_courtier = 5
cb2_page = 5
cb2_steppe_child = 5
cb2_apprentice = 4
cb2_acolyte  = 3
cb2_merchants_helper = 2
cb2_mummer = 1
cb2_urchin = 0
cb2_noble = 0

cb3_slaver = 9
cb3_bandit = 8
cb3_merc = 7
cb3_poacher = 6
cb3_craftsman = 5
cb3_peddler = 4
cb3_preacher = 3
cb3_troubadour = 2
cb3_student = 1
cb3_bravo = 0
cb3_squire = 0
cb3_lady_in_waiting = 0

cb4_duty = 6
cb4_revenge = 5
cb4_loss    = 4
cb4_wanderlust =  3
cb4_fervor = 2
cb4_disown  = 1
cb4_greed  = 0

kingdom_1 = 5
kingdom_2 = 4
kingdom_3 = 3
kingdom_4 = 2
kingdom_5 = 1
kingdom_6 = 0

###########################################################################################################################
#####                                            PRESENTATION DEFINITIONS                                             #####
###########################################################################################################################
# mcc_objects                            = "trp_tpe_presobj"
# mcc_data                               = "trp_tpe_xp_table"

# Slots of mcc_OBJECTS
mcc_obj_button_done                    = 1
mcc_obj_button_default                 = 2
mcc_obj_button_random                  = 3
mcc_obj_label_menus                    = 4
mcc_obj_label_story                    = 5
mcc_obj_label_gender                   = 6
mcc_obj_label_father                   = 7
mcc_obj_label_earlylife                = 8
mcc_obj_label_later                    = 9
mcc_obj_label_reason                   = 10
mcc_obj_menu_gender                    = 11
mcc_obj_menu_father                    = 12
mcc_obj_menu_earlylife                 = 13
mcc_obj_menu_later                     = 14
mcc_obj_menu_reason                    = 15
mcc_obj_label_options                  = 16
# mcc_obj_menu_trooptrees                = 17
# mcc_val_menu_trooptrees                = 18
# mcc_obj_checkbox_fogofwar              = 19
# mcc_val_checkbox_fogofwar              = 20
# mcc_obj_label_mtt                      = 21
# mcc_obj_checkbox_gather_npcs           = 22
# mcc_val_checkbox_gather_npcs           = 23
mcc_obj_menu_initial_region            = 24
mcc_val_menu_initial_region            = 25
mcc_obj_label_region                   = 26
mcc_obj_label_strength                 = 27
mcc_obj_stat_strength                  = 28
mcc_obj_label_agility                  = 29
mcc_obj_stat_agility                   = 30
mcc_obj_label_intelligence             = 31
mcc_obj_stat_intelligence              = 32
mcc_obj_label_charisma                 = 33
mcc_obj_stat_charisma                  = 34
mcc_obj_stat_gold                      = 35
mcc_obj_stat_renown                    = 36
mcc_obj_stat_weapon_onehand            = 37
mcc_obj_stat_weapon_twohand            = 38
mcc_obj_stat_weapon_polearm            = 39
mcc_obj_stat_weapon_archery            = 40
mcc_obj_stat_weapon_crossbow           = 41
mcc_obj_stat_weapon_throwing           = 42
mcc_obj_stat_weapon_firearm            = 43
mcc_obj_stat_container                 = 44
mcc_obj_button_back                    = 45

# Slots of mcc_DATA
# Slots 0-99 reserved.
mcc_item_storage_begin                 = 100
# Slots 101-120 reserved.
mcc_item_storage_end                   = 121
# Swadian items begin.
mcc_swadia_items_begin                 = 130
mcc_swadia_item_trade1                 = 130
mcc_swadia_item_trade2                 = 131
mcc_swadia_item_horse                  = 132
# mcc_swadia_item_richhorse              = 133
mcc_swadia_item_shield                 = 134
mcc_swadia_item_instrument             = 135
# mcc_swadia_item_poorboots              = 136
mcc_swadia_item_boots                  = 137
# mcc_swadia_item_richboots              = 138
# mcc_swadia_item_cloth                  = 139
# mcc_swadia_item_dress                  = 140
mcc_swadia_item_armor                  = 141
# mcc_swadia_item_gauntlets              = 142
# mcc_swadia_item_hood                   = 143
mcc_swadia_item_helmet                 = 144
# mcc_swadia_item_ladyhelmet             = 145
# mcc_swadia_item_axe                    = 146
# mcc_swadia_item_blunt                  = 147
mcc_swadia_item_dagger                 = 148
mcc_swadia_item_spear                  = 149
mcc_swadia_item_sword                  = 150
mcc_swadia_item_bow                    = 151
mcc_swadia_item_arrow                  = 152
mcc_swadia_item_throwing               = 153
mcc_swadia_items_end                   = 154
# slots 155-159 reserved for Swadia.
# Swadian items end.  Vaegir items begin.
mcc_vaegir_items_begin                 = 160
mcc_vaegir_item_trade1                 = 160
mcc_vaegir_item_trade2                 = 161
mcc_vaegir_item_horse                  = 162
# mcc_vaegir_item_richhorse              = 163
mcc_vaegir_item_shield                 = 164
mcc_vaegir_item_instrument             = 165
# mcc_vaegir_item_poorboots              = 166
mcc_vaegir_item_boots                  = 167
# mcc_vaegir_item_richboots              = 168
# mcc_vaegir_item_cloth                  = 169
# mcc_vaegir_item_dress                  = 170
mcc_vaegir_item_armor                  = 171
# mcc_vaegir_item_gauntlets              = 172
# mcc_vaegir_item_hood                   = 173
mcc_vaegir_item_helmet                 = 174
# mcc_vaegir_item_ladyhelmet             = 175
# mcc_vaegir_item_axe                    = 176
# mcc_vaegir_item_blunt                  = 177
mcc_vaegir_item_dagger                 = 178
mcc_vaegir_item_spear                  = 179
mcc_vaegir_item_sword                  = 180
mcc_vaegir_item_bow                    = 181
mcc_vaegir_item_arrow                  = 182
mcc_vaegir_item_throwing               = 183
mcc_vaegir_items_end                   = 184
# slots 185-189 reserved for Vaegir.
# Vaegir items end.  Khergit items begin.
mcc_khergit_items_begin                = 190
mcc_khergit_item_trade1                = 190
mcc_khergit_item_trade2                = 191
mcc_khergit_item_horse                 = 192
# mcc_khergit_item_richhorse             = 193
mcc_khergit_item_shield                = 194
mcc_khergit_item_instrument            = 195
# mcc_khergit_item_poorboots             = 196
mcc_khergit_item_boots                 = 197
# mcc_khergit_item_richboots             = 198
# mcc_khergit_item_cloth                 = 199
# mcc_khergit_item_dress                 = 200
mcc_khergit_item_armor                 = 201
# mcc_khergit_item_gauntlets             = 202
# mcc_khergit_item_hood                  = 203
mcc_khergit_item_helmet                = 204
# mcc_khergit_item_ladyhelmet            = 205
# mcc_khergit_item_axe                   = 206
# mcc_khergit_item_blunt                 = 207
mcc_khergit_item_dagger                = 208
mcc_khergit_item_spear                 = 209
mcc_khergit_item_sword                 = 210
mcc_khergit_item_bow                   = 211
mcc_khergit_item_arrow                 = 212
mcc_khergit_item_throwing              = 213
mcc_khergit_items_end                  = 214
# slots 215-219 reserved for Khergit.
# Khergit items end.  Nord items begin.
mcc_nord_items_begin                   = 220
mcc_nord_item_trade1                   = 220
mcc_nord_item_trade2                   = 221
mcc_nord_item_horse                    = 222
# mcc_nord_item_richhorse                = 223
mcc_nord_item_shield                   = 224
mcc_nord_item_instrument               = 225
# mcc_nord_item_poorboots                = 226
mcc_nord_item_boots                    = 227
# mcc_nord_item_richboots                = 228
# mcc_nord_item_cloth                    = 229
# mcc_nord_item_dress                    = 230
mcc_nord_item_armor                    = 231
mcc_nord_item_gauntlets                = 232
mcc_nord_item_hood                     = 233
mcc_nord_item_helmet                   = 234
# mcc_nord_item_ladyhelmet               = 235
# mcc_nord_item_axe                      = 236
# mcc_nord_item_blunt                    = 237
mcc_nord_item_dagger                   = 238
mcc_nord_item_spear                    = 239
mcc_nord_item_sword                    = 240
mcc_nord_item_bow                      = 241
mcc_nord_item_arrow                    = 242
mcc_nord_item_throwing                 = 243
mcc_nord_items_end                     = 244
# slots 245-249 reserved for Nord.
# Nord items end.  Rhodok items begin.
mcc_rhodok_items_begin                 = 250
mcc_rhodok_item_trade1                 = 250
mcc_rhodok_item_trade2                 = 251
mcc_rhodok_item_horse                  = 252
# mcc_rhodok_item_richhorse              = 253
mcc_rhodok_item_shield                 = 254
mcc_rhodok_item_instrument             = 255
# mcc_rhodok_item_poorboots              = 256
mcc_rhodok_item_boots                  = 257
# mcc_rhodok_item_richboots              = 258
# mcc_rhodok_item_cloth                  = 259
# mcc_rhodok_item_dress                  = 260
mcc_rhodok_item_armor                  = 261
# mcc_rhodok_item_gauntlets              = 262
# mcc_rhodok_item_hood                   = 263
mcc_rhodok_item_helmet                 = 264
# mcc_rhodok_item_ladyhelmet             = 265
# mcc_rhodok_item_axe                    = 266
# mcc_rhodok_item_blunt                  = 267
mcc_rhodok_item_dagger                 = 268
mcc_rhodok_item_spear                  = 269
mcc_rhodok_item_sword                  = 270
mcc_rhodok_item_bow                    = 271
mcc_rhodok_item_arrow                  = 272
mcc_rhodok_item_throwing               = 273
mcc_rhodok_items_end                   = 274
# slots 275-279 reserved for Rhodok.
# Rhodok items end.  Sarrand items begin.
mcc_sarrand_items_begin                = 280
mcc_sarrand_item_trade1                = 280
mcc_sarrand_item_trade2                = 281
mcc_sarrand_item_horse                 = 282
# mcc_sarrand_item_richhorse             = 283
mcc_sarrand_item_shield                = 284
mcc_sarrand_item_instrument            = 285
# mcc_sarrand_item_poorboots             = 286
mcc_sarrand_item_boots                 = 287
# mcc_sarrand_item_richboots             = 288
# mcc_sarrand_item_cloth                 = 289
# mcc_sarrand_item_dress                 = 290
mcc_sarrand_item_armor                 = 291
# mcc_sarrand_item_gauntlets             = 292
# mcc_sarrand_item_hood                  = 293
mcc_sarrand_item_helmet                = 294
# mcc_sarrand_item_ladyhelmet            = 295
# mcc_sarrand_item_axe                   = 296
# mcc_sarrand_item_blunt                 = 297
mcc_sarrand_item_dagger                = 298
mcc_sarrand_item_spear                 = 299
mcc_sarrand_item_sword                 = 300
mcc_sarrand_item_bow                   = 301
mcc_sarrand_item_arrow                 = 302
mcc_sarrand_item_throwing              = 303
mcc_sarrand_items_end                  = 304
# slots 305-309 reserved for Sarrand.
# Sarrand items end.

# END
