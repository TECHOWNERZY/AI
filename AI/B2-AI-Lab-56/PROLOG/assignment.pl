symptom(ramesh, fever).
symptom(ramesh, fatigue).
symptom(ramesh, sore_throat).
symptom(ramesh, runny_nose).

symptom(sita, fever).
symptom(sita, cough).
symptom(sita, shortness_of_breath).
symptom(sita, fatigue).

symptom(steve, headache).
symptom(steve, body_ache).
symptom(steve, chills).
symptom(steve, fever).

symptom(john, rash).
symptom(john, itching).
symptom(john, swollen_lymph_nodes).
symptom(john, fatigue).

% Hypotheses
hypothesis(Patient, flu) :-
                          symptom(Patient, fever),
                          symptom(Patient, fatigue),
                          symptom(Patient, sore_throat),
                          symptom(Patient, runny_nose).

hypothesis(Patient, covid19) :-
                               symptom(Patient, fever),
                               symptom(Patient, cough),
                               symptom(Patient, shortness_of_breath),
                               symptom(Patient, fatigue).

hypothesis(Patient, common_cold) :-
                                 symptom(Patient, sore_throat),
                                 symptom(Patient, runny_nose).

hypothesis(Patient, allergies) :-
                                symptom(Patient, headache),
                                symptom(Patient, body_ache),
                                symptom(Patient, chills).

hypothesis(Patient, chickenpox) :-
                                 symptom(Patient, rash),
                                 symptom(Patient, itching),
                                 symptom(Patient, swollen_lymph_nodes).
