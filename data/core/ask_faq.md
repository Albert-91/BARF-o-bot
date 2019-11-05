## faq presentation
## *scenario*: user chose solve problems showcase
* ask_faq
  - utter_ask_faq_intro
  - action_inject_intent_start_faq

## faq presentation - happy path
## *scenario*: 1st faq intent after starting showcase "solve problems", then bot responds faq then listen to next user input
* start_faq
  - action_listen
* faq
  - action_default_fallback
  - slot{"out_of_scope_detected": false}
* faq
  - action_reset_out_of_scope_detected
  - slot{"out_of_scope_detected": null}
  - action_respond_faq
  - action_inject_intent_start_faq

## faq presentation - happy path
## *scenario*: 2nd and following faq intent after starting showcase "solve problems", then bot responds faq then listen to next user input
  - action_inject_intent_start_faq
* start_faq
  - action_listen
* faq
  - action_default_fallback
  - slot{"out_of_scope_detected": false}
* faq
  - action_reset_out_of_scope_detected
  - slot{"out_of_scope_detected": null}
  - action_respond_faq
  - action_inject_intent_start_faq

## faq presentation - chitchat instead of faq
## *scenario*: 1st chitchat intent after starting showcase "solve problems", then bot responds chitchat then listen to next user input
* start_faq
  - action_listen
* chitchat
  - action_default_fallback
  - slot{"out_of_scope_detected": false}
* chitchat
  - action_reset_out_of_scope_detected
  - slot{"out_of_scope_detected": null}
  - respond_chitchat
  - action_inject_intent_start_faq

## faq presentation - chitchat instead of faq
## *scenario*: 2nd and following chitchat intent after starting showcase "solve problems", then bot responds chitchat then listen to next user input
  - action_inject_intent_start_faq
* start_faq
  - action_listen
* chitchat
  - action_default_fallback
  - slot{"out_of_scope_detected": false}
* chitchat
  - action_reset_out_of_scope_detected
  - slot{"out_of_scope_detected": null}
  - respond_chitchat
  - action_inject_intent_start_faq

## faq presentation - affirm/deny/menu/out_of_scope/explain instead of faq
## *scenario*: 1st affirm/deny/menu/out_of_scope/explain intent after starting showcase "solve problems", then bot responds asking for rephrase then listen to next user input
* start_faq
  - action_listen
* affirm OR deny OR menu OR out_of_scope OR explain
  - action_default_fallback
  - slot{"out_of_scope_detected": false}
* affirm OR deny OR menu OR out_of_scope OR explain
  - action_reset_out_of_scope_detected
  - slot{"out_of_scope_detected": null}  
  - utter_ask_faq_rephrase
  - action_inject_intent_start_faq

## faq presentation - affirm/deny/menu/out_of_scope/explain instead of faq after some intent
## *scenario*: 2nd and following affirm/deny/menu/out_of_scope/explain intent after starting showcase "solve problems", then bot responds asking for rephrase then listen to next user input
  - action_inject_intent_start_faq
* start_faq
  - action_listen
* affirm OR deny OR menu OR out_of_scope OR explain
  - action_default_fallback
  - slot{"out_of_scope_detected": false}
* affirm OR deny OR menu OR out_of_scope OR explain
  - action_reset_out_of_scope_detected
  - slot{"out_of_scope_detected": null}  
  - utter_ask_faq_rephrase
  - action_inject_intent_start_faq
  
## faq presentation - stop instead of faq - quit? - deny
## *scenario*: 1st stop intent after starting showcase "solve problems", then bot responds asking about quit from this showcase and user denies
* start_faq
  - action_listen
* stop
  - action_default_fallback
  - slot{"out_of_scope_detected": false}
* stop
  - action_reset_out_of_scope_detected
  - slot{"out_of_scope_detected": null}    
  - utter_ask_stop_faq
* deny
  - utter_ask_for_more_faq_questions
  - action_inject_intent_start_faq

## faq presentation - stop instead of faq after some intent - quit? - deny
## *scenario*: 2nd and following stop intent after starting showcase "solve problems", then bot responds asking about quit from this showcase and user denies
  - action_inject_intent_start_faq
* start_faq
  - action_listen
* stop
  - action_default_fallback
  - slot{"out_of_scope_detected": false}
* stop
  - action_reset_out_of_scope_detected
  - slot{"out_of_scope_detected": null}    
  - utter_ask_stop_faq
* deny
  - utter_ask_for_more_faq_questions
  - action_inject_intent_start_faq
  
## faq presentation - stop instead of faq after some intent - quit? - affirm
## *scenario*: 1st stop intent after starting showcase "solve problems", then bot responds asking about quit from this showcase and user affirms, then bot asking for feedback
* start_faq
  - action_listen
* stop
  - action_default_fallback
  - slot{"out_of_scope_detected": false}
* stop
  - action_reset_out_of_scope_detected
  - slot{"out_of_scope_detected": null}    
  - utter_ask_stop_faq
* affirm
  <!-- collect feedback -->    
  - form_feedback
  - form{"name": "form_feedback"}
  - form{"name": "null"}
  - utter_anything_else

## faq presentation - stop instead of faq after some intent - quit? - affirm
## *scenario*: 2nd and following stop intent after starting showcase "solve problems", then bot responds asking about quit from this showcase and user affirms, then bot asking for feedback
  - action_inject_intent_start_faq
* start_faq
  - action_listen
* stop
  - action_default_fallback
  - slot{"out_of_scope_detected": false}
* stop
  - action_reset_out_of_scope_detected
  - slot{"out_of_scope_detected": null}    
  - utter_ask_stop_faq
* affirm
  <!-- collect feedback -->    
  - form_feedback
  - form{"name": "form_feedback"}
  - form{"name": "null"}
  - utter_anything_else

## faq presentation - generic out_of_scope instead of faq
## *scenario*: 1st intent is generic "out_of_scope" after starting showcase "solve problems" then, then bot responds asking for rephrase
* start_faq
  - action_listen
* chitchat OR faq OR affirm OR deny OR explain OR menu OR out_of_scope
  - action_default_fallback
  - slot{"out_of_scope_detected": true}
* out_of_scope
  - action_reset_out_of_scope_detected
  - slot{"out_of_scope_detected": null}  
  - utter_ask_faq_rephrase
  - action_inject_intent_start_faq

## faq presentation - generic out_of_scope instead of faq after some intent
## *scenario*: 2nd and following intent is generic "out_of_scope" after starting showcase "solve problems" then, then bot responds asking for rephrase
  - action_inject_intent_start_faq
* start_faq
  - action_listen
* chitchat OR faq OR affirm OR deny OR explain OR menu OR out_of_scope
  - action_default_fallback
  - slot{"out_of_scope_detected": true}
* out_of_scope
  - action_reset_out_of_scope_detected
  - slot{"out_of_scope_detected": null}  
  - utter_ask_faq_rephrase
  - action_inject_intent_start_faq