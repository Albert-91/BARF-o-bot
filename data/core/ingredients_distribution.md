## ingredient distribution button
## *scenario*: user chose ingredient distribution
* ingredient_distribution
  - utter_ingredients_distribution_intro
  - action_reset_form_slots
  - action_inject_intent_start_ingredient_distribution

## ingredient_distribution form processing - happy path
## *scenario*: form starts then user follows all parameters gathering as expected then feedback, then asks anything else
* start_ingredient_distribution
  - form_calculate_ingredients_distribution
  - form{"name": "form_calculate_ingredients_distribution"}
  - form{"name": "null"}
  - action_reset_form_slots
  <!-- collect feedback -->    
  - form_feedback
  - form{"name": "form_feedback"}
  - form{"name": null}
  - utter_anything_else

## ingredient_distribution form processing - finish after interruption
## *scenario*: form restarts after some intents occurred & processed during params gathering but then 
##             user follows rest parameters gathering as expected then feedback, then asks anything else
  - action_inject_intent_start_ingredient_distribution  
* start_ingredient_distribution
  - action_reset_requested_slot 
  - form_calculate_ingredients_distribution
  - form{"name": "form_calculate_ingredients_distribution"}
  - form{"name": "null"}
  - action_reset_form_slots
  <!-- collect feedback -->    
  - form_feedback
  - form{"name": "form_feedback"}
  - form{"name": null}
  - utter_anything_else

## ingredient_distribution form processing - 1st params gathering interruption by chitchat
## *scenario*: form starts then params gathering is interrupted by chitchat then bot responds chitchat and restart form
* start_ingredient_distribution
  - form_calculate_ingredients_distribution
  - form{"name": "form_calculate_ingredients_distribution"}
* chitchat
  - action_default_fallback
  - slot{"out_of_scope_detected": false}
  - form{"name": null}
* chitchat
  - action_reset_out_of_scope_detected
  - slot{"out_of_scope_detected": null}
  - respond_chitchat    
  - action_inject_intent_start_ingredient_distribution  

## ingredient_distribution form processing - 2nd and following params gathering interruption by chitchat
## *scenario*: form restarts then params gathering is interrupted by chitchat then bot responds chitchat and restart form
  - action_inject_intent_start_ingredient_distribution  
* start_ingredient_distribution
  - action_reset_requested_slot 
  - form_calculate_ingredients_distribution
  - form{"name": "form_calculate_ingredients_distribution"}
* chitchat
  - action_default_fallback
  - slot{"out_of_scope_detected": false}
  - form{"name": null}
* chitchat
  - action_reset_out_of_scope_detected
  - slot{"out_of_scope_detected": null}
  - respond_chitchat    
  - action_inject_intent_start_ingredient_distribution 

## ingredient_distribution form processing - 1st params gathering interruption by faq
## *scenario*: form starts then params gathering is interrupted by faq then bot responds faq and restart form
* start_ingredient_distribution
  - form_calculate_ingredients_distribution
  - form{"name": "form_calculate_ingredients_distribution"}
* faq
  - action_default_fallback
  - slot{"out_of_scope_detected": false}
  - form{"name": null}
* faq
  - action_reset_out_of_scope_detected
  - slot{"out_of_scope_detected": null}
  - action_respond_faq
  - action_inject_intent_start_ingredient_distribution  

## ingredient_distribution form processing - 2nd and following params gathering interruption by faq
## *scenario*: form restarts then params gathering is interrupted by faq then bot responds faq and restart form
  - action_inject_intent_start_ingredient_distribution  
* start_ingredient_distribution
  - action_reset_requested_slot 
  - form_calculate_ingredients_distribution
  - form{"name": "form_calculate_ingredients_distribution"}
* faq
  - action_default_fallback
  - slot{"out_of_scope_detected": false}
  - form{"name": null}
* faq
  - action_reset_out_of_scope_detected
  - slot{"out_of_scope_detected": null}
  - action_respond_faq    
  - action_inject_intent_start_ingredient_distribution  

## ingredient_distribution form processing - 1st params gathering interruption by explain
## *scenario*: form starts then params gathering is interrupted by explain then bot utters wrong param 
##             value and restart form
* start_ingredient_distribution  
  - form_calculate_ingredients_distribution
  - form{"name": "form_calculate_ingredients_distribution"}
* explain 
  - action_default_fallback
  - slot{"out_of_scope_detected": false}
  - form{"name": null}
* explain
  - action_reset_out_of_scope_detected
  - slot{"out_of_scope_detected": null}    
  - action_utter_explain_requested_slot_value
  - action_inject_intent_start_ingredient_distribution

## ingredient_distribution form processing - 2nd and following params gathering interruption by explain
## *scenario*: form restarts then params gathering is interrupted by explain then bot utters wrong param 
##             value and restart form
  - action_inject_intent_start_ingredient_distribution
* start_ingredient_distribution
  - action_reset_requested_slot 
  - form_calculate_ingredients_distribution
  - form{"name": "form_calculate_ingredients_distribution"}
* explain
  - action_default_fallback
  - slot{"out_of_scope_detected": false}
  - form{"name": null}
* explain  
  - action_reset_out_of_scope_detected
  - slot{"out_of_scope_detected": null}    
  - action_utter_explain_requested_slot_value
  - action_inject_intent_start_ingredient_distribution    
  
## ingredient_distribution form processing - 1st params gathering interruption by stop then deny
## *scenario*: form starts then params gathering is interrupted by stop then bot ask to stop showcase then user 
##             deny and bot continue showcase
* start_ingredient_distribution  
  - form_calculate_ingredients_distribution
  - form{"name": "form_calculate_ingredients_distribution"}
* stop OR menu OR weather
  - action_default_fallback
  - slot{"out_of_scope_detected": false}
  - form{"name": null}
* stop OR menu OR weather
  - action_reset_out_of_scope_detected
  - slot{"out_of_scope_detected": null}    
  - utter_ask_stop_ingredients_distribution
* deny
  - utter_continue_ingredients_distribution
  - action_inject_intent_start_ingredient_distribution    

## ingredient_distribution form processing - 2nd and following params gathering interruption by stop then deny
## *scenario*: form restarts then params gathering is interrupted by stop then bot ask to stop showcase then user 
##             deny and bot continue showcase
  - action_inject_intent_start_ingredient_distribution
* start_ingredient_distribution
  - action_reset_requested_slot   
  - form_calculate_ingredients_distribution
  - form{"name": "form_calculate_ingredients_distribution"}
* stop OR menu OR weather
  - action_default_fallback
  - slot{"out_of_scope_detected": false}
  - form{"name": null}
* stop OR menu OR weather
  - action_reset_out_of_scope_detected
  - slot{"out_of_scope_detected": null}    
  - utter_ask_stop_ingredients_distribution
* deny
  - utter_continue_ingredients_distribution
  - action_inject_intent_start_ingredient_distribution   

## ingredient_distribution form processing - 1st params gathering interruption by stop then affirm
## *scenario*: form starts then params gathering is interrupted by stop then bot ask to stop showcase then user 
##             affirm then feedback then asks anything else
* start_ingredient_distribution  
  - form_calculate_ingredients_distribution
  - form{"name": "form_calculate_ingredients_distribution"}
* stop OR menu OR weather
  - action_default_fallback
  - slot{"out_of_scope_detected": false}
  - form{"name": null}
* stop OR menu OR weather
  - action_reset_out_of_scope_detected
  - slot{"out_of_scope_detected": null}    
  - utter_ask_stop_ingredients_distribution
* affirm
  - action_deactivate_form
  - form{"name": null}
  - action_reset_form_slots
  <!-- collect feedback -->    
  - form_feedback
  - form{"name": "form_feedback"}
  - form{"name": "null"}
  - utter_anything_else

## ingredient_distribution form processing - 2nd and following params gathering interruption by stop then affirm
## *scenario*: form restarts then params gathering is interrupted by stop then bot ask to stop showcase then user 
##             affirm then feedback then asks anything else
  - action_inject_intent_start_ingredient_distribution
* start_ingredient_distribution
  - action_reset_requested_slot
  - form_calculate_ingredients_distribution
  - form{"name": "form_calculate_ingredients_distribution"}
* stop OR menu OR weather
  - action_default_fallback
  - slot{"out_of_scope_detected": false}
  - form{"name": null}
* stop OR menu OR weather
  - action_reset_out_of_scope_detected
  - slot{"out_of_scope_detected": null}    
  - utter_ask_stop_ingredients_distribution
* affirm
  - action_deactivate_form
  - form{"name": null}
  - action_reset_form_slots
  <!-- collect feedback -->    
  - form_feedback
  - form{"name": "form_feedback"}
  - form{"name": "null"}
  - utter_anything_else  

## ingredient_distribution form processing - 1st params gathering interruption by other (not supported in scenario) intent
## *scenario*: form starts then params gathering is interrupted by not supported intent then bot utters wrong param
##             value and restart form
* start_ingredient_distribution  
  - form_calculate_ingredients_distribution
  - form{"name": "form_calculate_ingredients_distribution"}
* affirm OR deny OR out_of_scope
  - action_default_fallback
  - slot{"out_of_scope_detected": false}
  - form{"name": null}
* affirm OR deny OR out_of_scope
  - action_reset_out_of_scope_detected
  - slot{"out_of_scope_detected": null}  
  - action_utter_wrong_requested_slot_value
  - action_inject_intent_start_ingredient_distribution

## ingredient_distribution form processing - 2nd and following params gathering interruption by other (not supported in scenario) intent
## *scenario*: form restarts then params gathering is interrupted by not supported intent then bot utters wrong param
##             value and restart form
  - action_inject_intent_start_ingredient_distribution  
* start_ingredient_distribution
  - action_reset_requested_slot
  - form_calculate_ingredients_distribution
  - form{"name": "form_calculate_ingredients_distribution"}
* affirm OR deny OR out_of_scope
  - action_default_fallback
  - slot{"out_of_scope_detected": false}
  - form{"name": null}
* affirm OR deny OR out_of_scope
  - action_reset_out_of_scope_detected
  - slot{"out_of_scope_detected": null}  
  - action_utter_wrong_requested_slot_value
  - action_inject_intent_start_ingredient_distribution

## ingredient_distribution form processing - 1st params gathering interruption by generic "out of scope"
## *scenario*: form starts then params gathering is interrupted generic "out of scope" then bot utters wrong param
##             value and restart form
* start_ingredient_distribution  
  - form_calculate_ingredients_distribution
  - form{"name": "form_calculate_ingredients_distribution"}
* chitchat OR affirm OR deny OR explain OR menu OR out_of_scope OR faq
  - action_default_fallback
  - slot{"out_of_scope_detected": true}
  - form{"name": null}
* out_of_scope
  - action_reset_out_of_scope_detected
  - slot{"out_of_scope_detected": null}  
  - action_utter_wrong_requested_slot_value
  - action_inject_intent_start_ingredient_distribution

## ingredient_distribution form processing - 2nd and following params gathering interruption by generic "out of scope"
## *scenario*: form restarts then params gathering is interrupted generic "out of scope" then bot utters wrong param
##             value and restart form
  - action_inject_intent_start_ingredient_distribution  
* start_ingredient_distribution
  - action_reset_requested_slot
  - form_calculate_ingredients_distribution
  - form{"name": "form_calculate_ingredients_distribution"}
* chitchat OR affirm OR deny OR explain OR menu OR out_of_scope OR faq
  - action_default_fallback
  - slot{"out_of_scope_detected": true}
  - form{"name": null}
* out_of_scope
  - action_reset_out_of_scope_detected
  - slot{"out_of_scope_detected": null}  
  - action_utter_wrong_requested_slot_value
  - action_inject_intent_start_ingredient_distribution
