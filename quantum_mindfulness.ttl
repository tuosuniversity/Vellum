@prefix : <http://tuos.org/qm#> .
@prefix dc: <http://purl.org/dc/elements/1.1/> .
@prefix qm: <https://tuos.org/qm#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@base <http://tuos.org/qm#> .

: rdf:type owl:Ontology ;
                       dc:creator "The University of Ontological Science" ;
                       dc:title "Quantum Mindfulness - Power of Perception and Psychodynamic Dimensions Ontology" ;
                       rdfs:comment "A formal ontology of the Quantum Mindfulness framework's Prime Modality. This version uses OWL restrictions to define relationships at the class level, ensuring a robust and machine-readable structure."@en ,
                                    "A formal ontology of the psychodynamic architecture of consciousness as detailed in the Quantum Mindfulness source material. This model defines the sequential process from Observation to the emergence of a final Mental State, and the mechanism of Belief Formation."@en ,
                                    "An ontology of the Quantum Mindfulness framework. Note: While some source texts refer to eleven dimensions, the detailed enumeration consistently lists ten (Pd1–Pd10). The concept of 'eleven' may allude to a foundational 'Psycho-Volitional core' that underpins the ten enumerable dimensions."@en .

#################################################################
#    Annotation properties
#################################################################

###  http://purl.org/dc/elements/1.1/creator
dc:creator rdf:type owl:AnnotationProperty ;
           rdfs:comment "An entity primarily responsible for making the resource."@en .


###  http://purl.org/dc/elements/1.1/title
dc:title rdf:type owl:AnnotationProperty ;
         rdfs:comment "A name given to the resource."@en .


###  http://www.w3.org/2000/01/rdf-schema#subClassOf
rdfs:subClassOf rdf:type owl:AnnotationProperty ;
                rdfs:comment "The subject is a class of the object."@en .


###  http://www.w3.org/2004/02/skos/core#altLabel
skos:altLabel rdf:type owl:AnnotationProperty ;
              rdfs:comment "An alternative lexical label for a resource."@en .


###  http://www.w3.org/2004/02/skos/core#definition
skos:definition rdf:type owl:AnnotationProperty .


###  https://tuos.org/qm#hasDefinition
qm:hasDefinition rdf:type owl:AnnotationProperty ;
                 rdfs:label "has definition"@en .


#################################################################
#    Object Properties
#################################################################

###  https://tuos.org/qm#actsAsChannelFor
qm:actsAsChannelFor rdf:type owl:ObjectProperty ;
                    rdfs:domain qm:PsychoMotivationalDimension ;
                    rdfs:comment "Indicates a function that enables refined influences and insights from higher dimensions to flow downward and inform concrete actions."@en ;
                    rdfs:label "acts as channel for"@en .


###  https://tuos.org/qm#actualizes
qm:actualizes rdf:type owl:ObjectProperty ;
              rdfs:comment "Indicates the process of making a potential state into a definite, actual one."@en ;
              rdfs:label "actualizes"@en .


###  https://tuos.org/qm#addressesLimitationsOf
qm:addressesLimitationsOf rdf:type owl:ObjectProperty ;
                          rdfs:comment "Indicates that a process or application is designed to mitigate or resolve specific dysfunctions or challenges."@en ;
                          rdfs:label "addresses limitations of"@en .


###  https://tuos.org/qm#arisesFrom
qm:arisesFrom rdf:type owl:ObjectProperty ;
              owl:inverseOf qm:stemsFrom ;
              rdfs:domain qm:PsychologicalDisharmony ;
              rdfs:range qm:DestructiveInterference ;
              rdfs:comment "Indicates the origin or cause of a psychological state, particularly in the context of dimensional dynamics."@en ;
              rdfs:label "arises from"@en .


###  https://tuos.org/qm#biases
qm:biases rdf:type owl:ObjectProperty ;
          rdfs:comment "Indicates a systematic pattern that influences interpretation."@en ;
          rdfs:label "biases"@en .


###  https://tuos.org/qm#bridgesTo
qm:bridgesTo rdf:type owl:ObjectProperty ;
             rdfs:domain qm:PsychoAestheticDimension ;
             rdfs:range qm:PsychoMotivationalDimension ;
             rdfs:comment "Indicates the creation of a connection that channels energy or insights into another dimension for purposeful action."@en ;
             rdfs:label "bridges to"@en .


###  https://tuos.org/qm#canDurablyAlter
qm:canDurablyAlter rdf:type owl:ObjectProperty ;
                   owl:inverseOf qm:isAlteredBy ;
                   rdfs:comment "Indicates a mechanism where repeated mental states can durably alter an underlying variable of the system, such as a trait."@en ;
                   rdfs:label "can durably alter"@en .


###  https://tuos.org/qm#canHaveInterferencePattern
qm:canHaveInterferencePattern rdf:type owl:ObjectProperty ;
                              rdfs:domain qm:PsychodynamicDimension ;
                              rdfs:comment "Indicates that the interaction between dimensions can lead to constructive (amplifying) or destructive (conflicting) patterns."@en ;
                              rdfs:label "can have interference pattern"@en .


###  https://tuos.org/qm#composedOf
qm:composedOf rdf:type owl:ObjectProperty ;
              owl:inverseOf qm:constituentOf ;
              rdfs:domain qm:CognitiveModality ;
              rdfs:range qm:PsychodynamicDimension ;
              rdfs:label "composed of"@en .


###  https://tuos.org/qm#connection_Pd1_Pd2
qm:connection_Pd1_Pd2 rdf:type owl:ObjectProperty ;
                      rdfs:subPropertyOf qm:hasInterdimensionalConnection ;
                      rdfs:domain qm:PsychoVolitionalDimension ;
                      rdfs:range qm:PsychoConceptiveDimension ;
                      rdfs:comment "Describes the flow from pure psychic intentionality and initial psychic impetus to the formation of raw, unformed concepts and intuitive insights." ;
                      rdfs:label "Connection from Pd1 to Pd2 (Initial Conceptualization)" .


###  https://tuos.org/qm#connection_Pd1_Pd3
qm:connection_Pd1_Pd3 rdf:type owl:ObjectProperty ;
                      rdfs:subPropertyOf qm:hasInterdimensionalConnection ;
                      rdfs:domain qm:PsychoVolitionalDimension ;
                      rdfs:range qm:PsychoMeditativeDimension ;
                      rdfs:comment "Describes how primal will and psychic potential translate into organized mental structures and comprehensive understanding." ;
                      rdfs:label "Connection from Pd1 to Pd3 (Volition to Structure)" .


###  https://tuos.org/qm#connection_Pd1_Pd6
qm:connection_Pd1_Pd6 rdf:type owl:ObjectProperty ;
                      rdfs:subPropertyOf qm:hasInterdimensionalConnection ;
                      rdfs:domain qm:PsychoVolitionalDimension ;
                      rdfs:range qm:PsychoAestheticDimension ;
                      rdfs:comment "The fundamental manifestation of psychic will and potential into the balanced, integrated core of the self." ;
                      rdfs:label "Connection from Pd1 to Pd6 (Integration of Psychic Origin)" .


###  https://tuos.org/qm#connection_Pd2_Pd3
qm:connection_Pd2_Pd3 rdf:type owl:ObjectProperty ;
                      rdfs:subPropertyOf qm:hasInterdimensionalConnection ;
                      rdfs:domain qm:PsychoConceptiveDimension ;
                      rdfs:range qm:PsychoMeditativeDimension ;
                      rdfs:comment "The process of giving structure, logic, and concrete understanding to raw, intuitive insights and concepts." ;
                      rdfs:label "Connection from Pd2 to Pd3 (From Insight to Form)" .


###  https://tuos.org/qm#connection_Pd2_Pd4
qm:connection_Pd2_Pd4 rdf:type owl:ObjectProperty ;
                      rdfs:subPropertyOf qm:hasInterdimensionalConnection ;
                      rdfs:domain qm:PsychoConceptiveDimension ;
                      rdfs:range qm:PsychoEmpathicDimension ;
                      rdfs:comment "The flow from pure conceptual insight into benevolent emotional expansion and the capacity for deep empathy." ;
                      rdfs:label "Connection from Pd2 to Pd4 (Insightful Empathy)" .


###  https://tuos.org/qm#connection_Pd2_Pd6
qm:connection_Pd2_Pd6 rdf:type owl:ObjectProperty ;
                      rdfs:subPropertyOf qm:hasInterdimensionalConnection ;
                      rdfs:domain qm:PsychoConceptiveDimension ;
                      rdfs:range qm:PsychoAestheticDimension ;
                      rdfs:comment "How creative insight directly contributes to the harmony, balance, and integrated expression of the self." ;
                      rdfs:label "Connection from Pd2 to Pd6 (Conceptual Self-Expression)" .


###  https://tuos.org/qm#connection_Pd3_Pd5
qm:connection_Pd3_Pd5 rdf:type owl:ObjectProperty ;
                      rdfs:subPropertyOf qm:hasInterdimensionalConnection ;
                      rdfs:domain qm:PsychoMeditativeDimension ;
                      rdfs:range qm:PsychoProtectiveDimension ;
                      rdfs:comment "How structured thought leads to the establishment of clear psychic discipline and protective internal boundaries." ;
                      rdfs:label "Connection from Pd3 to Pd5 (Thought to Boundaries)" .


###  https://tuos.org/qm#connection_Pd3_Pd6
qm:connection_Pd3_Pd6 rdf:type owl:ObjectProperty ;
                      rdfs:subPropertyOf qm:hasInterdimensionalConnection ;
                      rdfs:domain qm:PsychoMeditativeDimension ;
                      rdfs:range qm:PsychoAestheticDimension ;
                      rdfs:comment "How reasoned understanding and mental structures contribute to the overall harmony and balance of the self." ;
                      rdfs:label "Connection from Pd3 to Pd6 (Structured Self-Integration)" .


###  https://tuos.org/qm#connection_Pd4_Pd5
qm:connection_Pd4_Pd5 rdf:type owl:ObjectProperty ;
                      rdfs:subPropertyOf qm:hasInterdimensionalConnection ;
                      rdfs:domain qm:PsychoEmpathicDimension ;
                      rdfs:range qm:PsychoProtectiveDimension ;
                      rdfs:comment "The dynamic interplay between expansive empathy and necessary self-protection or disciplined emotional management." ;
                      rdfs:label "Connection from Pd4 to Pd5 (Compassionate Boundaries)" .


###  https://tuos.org/qm#connection_Pd4_Pd6
qm:connection_Pd4_Pd6 rdf:type owl:ObjectProperty ;
                      rdfs:subPropertyOf qm:hasInterdimensionalConnection ;
                      rdfs:domain qm:PsychoEmpathicDimension ;
                      rdfs:range qm:PsychoAestheticDimension ;
                      rdfs:comment "How expansive compassion and benevolent emotion contribute to the beauty, balance, and integration of the self." ;
                      rdfs:label "Connection from Pd4 to Pd6 (Empathic Self-Support)" .


###  https://tuos.org/qm#connection_Pd4_Pd7
qm:connection_Pd4_Pd7 rdf:type owl:ObjectProperty ;
                      rdfs:subPropertyOf qm:hasInterdimensionalConnection ;
                      rdfs:domain qm:PsychoEmpathicDimension ;
                      rdfs:range qm:PsychoMotivationalDimension ;
                      rdfs:comment "The flow from benevolent emotional expansion into persistent drive, inspiring action and motivational force." ;
                      rdfs:label "Connection from Pd4 to Pd7 (Empathy to Motivation)" .


###  https://tuos.org/qm#connection_Pd5_Pd6
qm:connection_Pd5_Pd6 rdf:type owl:ObjectProperty ;
                      rdfs:subPropertyOf qm:hasInterdimensionalConnection ;
                      rdfs:domain qm:PsychoProtectiveDimension ;
                      rdfs:range qm:PsychoAestheticDimension ;
                      rdfs:comment "How setting psychic boundaries and inner strength contribute to the overall harmony and balance of the self." ;
                      rdfs:label "Connection from Pd5 to Pd6 (Discipline for Integration)" .


###  https://tuos.org/qm#connection_Pd5_Pd8
qm:connection_Pd5_Pd8 rdf:type owl:ObjectProperty ;
                      rdfs:subPropertyOf qm:hasInterdimensionalConnection ;
                      rdfs:domain qm:PsychoProtectiveDimension ;
                      rdfs:range qm:PsychoReceptiveDimension ;
                      rdfs:comment "The flow from inner strength and boundaries to clear, effective intellectual communication or receptive capacity." ;
                      rdfs:label "Connection from Pd5 to Pd8 (Protective Expression)" .


###  https://tuos.org/qm#connection_Pd6_Pd7
qm:connection_Pd6_Pd7 rdf:type owl:ObjectProperty ;
                      rdfs:subPropertyOf qm:hasInterdimensionalConnection ;
                      rdfs:domain qm:PsychoAestheticDimension ;
                      rdfs:range qm:PsychoMotivationalDimension ;
                      rdfs:comment "The manifestation of the balanced self into passionate drive, endurance, and focused motivational force." ;
                      rdfs:label "Connection from Pd6 to Pd7 (Integrated Drive)" .


###  https://tuos.org/qm#connection_Pd6_Pd8
qm:connection_Pd6_Pd8 rdf:type owl:ObjectProperty ;
                      rdfs:subPropertyOf qm:hasInterdimensionalConnection ;
                      rdfs:domain qm:PsychoAestheticDimension ;
                      rdfs:range qm:PsychoReceptiveDimension ;
                      rdfs:comment "How the integrated self finds its voice and expresses itself through intellectual processes and communication." ;
                      rdfs:label "Connection from Pd6 to Pd8 (Integrated Expression)" .


###  https://tuos.org/qm#connection_Pd6_Pd9
qm:connection_Pd6_Pd9 rdf:type owl:ObjectProperty ;
                      rdfs:subPropertyOf qm:hasInterdimensionalConnection ;
                      rdfs:domain qm:PsychoAestheticDimension ;
                      rdfs:range qm:PsychoFoundationalDimension ;
                      rdfs:comment "The connection from the integrated self to its deeper subconscious roots and fundamental psychic drives." ;
                      rdfs:label "Connection from Pd6 to Pd9 (Self to Foundation)" .


###  https://tuos.org/qm#connection_Pd7_Pd10
qm:connection_Pd7_Pd10 rdf:type owl:ObjectProperty ;
                       rdfs:subPropertyOf qm:hasInterdimensionalConnection ;
                       rdfs:domain qm:PsychoMotivationalDimension ;
                       rdfs:range qm:PsychoTranspersonalDimension ;
                       rdfs:comment "How inner drive and willpower find their expression and impact in the external, manifested reality of experience." ;
                       rdfs:label "Connection from Pd7 to Pd10 (Drive Manifestation)" .


###  https://tuos.org/qm#connection_Pd7_Pd8
qm:connection_Pd7_Pd8 rdf:type owl:ObjectProperty ;
                      rdfs:subPropertyOf qm:hasInterdimensionalConnection ;
                      rdfs:domain qm:PsychoMotivationalDimension ;
                      rdfs:range qm:PsychoReceptiveDimension ;
                      rdfs:comment "The dynamic interplay between raw drive/willpower and its intellectual reception, processing, and communication." ;
                      rdfs:label "Connection from Pd7 to Pd8 (Drive to Intellect)" .


###  https://tuos.org/qm#connection_Pd7_Pd9
qm:connection_Pd7_Pd9 rdf:type owl:ObjectProperty ;
                      rdfs:subPropertyOf qm:hasInterdimensionalConnection ;
                      rdfs:domain qm:PsychoMotivationalDimension ;
                      rdfs:range qm:PsychoFoundationalDimension ;
                      rdfs:comment "How raw drives and motivations connect to the deep subconscious energetic foundation of the personality." ;
                      rdfs:label "Connection from Pd7 to Pd9 (Motivational Foundation)" .


###  https://tuos.org/qm#connection_Pd8_Pd10
qm:connection_Pd8_Pd10 rdf:type owl:ObjectProperty ;
                       rdfs:subPropertyOf qm:hasInterdimensionalConnection ;
                       rdfs:domain qm:PsychoReceptiveDimension ;
                       rdfs:range qm:PsychoTranspersonalDimension ;
                       rdfs:comment "How intellectual expression and communication find their manifestation and impact in the experienced world." ;
                       rdfs:label "Connection from Pd8 to Pd10 (Expressive Manifestation)" .


###  https://tuos.org/qm#connection_Pd8_Pd9
qm:connection_Pd8_Pd9 rdf:type owl:ObjectProperty ;
                      rdfs:subPropertyOf qm:hasInterdimensionalConnection ;
                      rdfs:domain qm:PsychoReceptiveDimension ;
                      rdfs:range qm:PsychoFoundationalDimension ;
                      rdfs:comment "The connection from formal intellect and receptive capacity to the deeper subconscious and foundational drives." ;
                      rdfs:label "Connection from Pd8 to Pd9 (Intellect to Subconscious)" .


###  https://tuos.org/qm#connection_Pd9_Pd10
qm:connection_Pd9_Pd10 rdf:type owl:ObjectProperty ;
                       rdfs:subPropertyOf qm:hasInterdimensionalConnection ;
                       rdfs:domain qm:PsychoFoundationalDimension ;
                       rdfs:range qm:PsychoTranspersonalDimension ;
                       rdfs:comment "The fundamental connection between the subconscious foundation of personality and its full manifestation in reality." ;
                       rdfs:label "Connection from Pd9 to Pd10 (Foundation to Reality)" .


###  https://tuos.org/qm#consolidates
qm:consolidates rdf:type owl:ObjectProperty ;
                rdfs:domain qm:PsychoFoundationalDimension ;
                rdfs:comment "Indicates the function of solidifying memory and experiential learning."@en ;
                rdfs:label "consolidates"@en .


###  https://tuos.org/qm#constituentOf
qm:constituentOf rdf:type owl:ObjectProperty ;
                 rdfs:domain qm:PsychodynamicDimension ;
                 rdfs:range qm:CognitiveModality ;
                 rdfs:comment "A property indicating that one concept is a component or part of a larger whole."@en ;
                 rdfs:label "constituent of"@en ;
                 skos:definition "Serving as a part of a whole."@en .


###  https://tuos.org/qm#contains
qm:contains rdf:type owl:ObjectProperty ;
            rdfs:domain qm:PsychoFoundationalDimension ;
            rdfs:comment "Indicates that a dimension holds foundational psychological structures."@en ;
            rdfs:label "contains"@en .


###  https://tuos.org/qm#contrastsWith
qm:contrastsWith rdf:type owl:ObjectProperty ;
                 rdfs:comment "Indicates that a concept or principle fundamentally diverges from another model or idea."@en ;
                 rdfs:label "contrasts with"@en .


###  https://tuos.org/qm#contributesTo
qm:contributesTo rdf:type owl:ObjectProperty ;
                 rdfs:domain qm:PsychoMeditativeDimension ;
                 rdfs:comment "Indicates that the subject is a contributing factor to the object."@en ;
                 rdfs:label "contributes to"@en ;
                 skos:definition "A property indicating that the subject adds to or helps cause the object."@en .


###  https://tuos.org/qm#definesRoleOfObserverAs
qm:definesRoleOfObserverAs rdf:type owl:ObjectProperty ;
                           rdfs:comment "Defines the conceptual role of the conscious observer within a specific mindfulness paradigm."@en ;
                           rdfs:label "defines role of observer as"@en .


###  https://tuos.org/qm#dependsOn
qm:dependsOn rdf:type owl:ObjectProperty ;
             owl:inverseOf qm:providesFoundationFor ;
             rdfs:domain qm:PsychodynamicDimension ;
             rdfs:range qm:PsychodynamicDimension ;
             rdfs:comment "Indicates a relationship where the subject requires the object for its existence or function."@en ;
             rdfs:label "depends on"@en ;
             skos:definition "A property indicating that the subject is dependent on the object."@en .


###  https://tuos.org/qm#describes
qm:describes rdf:type owl:ObjectProperty ;
             rdfs:comment "Indicates that a principle provides the conceptual language for a mechanism or process."@en ;
             rdfs:label "describes"@en .


###  https://tuos.org/qm#develops
qm:develops rdf:type owl:ObjectProperty ;
            owl:inverseOf qm:isDevelopedBy ;
            rdfs:comment "Indicates that a practice leads to the enhancement of a specific capacity."@en ;
            rdfs:label "develops"@en .


###  https://tuos.org/qm#differsFrom
qm:differsFrom rdf:type owl:ObjectProperty ;
               rdfs:comment "Indicates a conceptual or methodological distinction from another concept."@en ;
               rdfs:label "differs from"@en .


###  https://tuos.org/qm#dissolves
qm:dissolves rdf:type owl:ObjectProperty ;
             rdfs:domain qm:PsychoVolitionalDimension ;
             rdfs:comment "Indicates the 'annihilative' property of a dimension, allowing it to negate perceived limitations, mental blocks, and constricting conceptual frameworks."@en ;
             rdfs:label "dissolves"@en .


###  https://tuos.org/qm#embodies
qm:embodies rdf:type owl:ObjectProperty ;
            rdfs:domain qm:PsychoVolitionalDimension ;
            rdfs:label "embodies"@en .


###  https://tuos.org/qm#embodiesPrinciple
qm:embodiesPrinciple rdf:type owl:ObjectProperty ;
                     rdfs:domain qm:PsychoProtectiveDimension ;
                     rdfs:comment "Indicates that a dimension represents a primordial psychological principle."@en ;
                     rdfs:label "embodies principle"@en .


###  https://tuos.org/qm#emergesFromInteractionOf
qm:emergesFromInteractionOf rdf:type owl:ObjectProperty ;
                            rdfs:domain qm:PsychologicalState ;
                            rdfs:range qm:PsychodynamicDimension ;
                            rdfs:comment "Describes how complex states arise from the dynamic interplay and weighted sum of multiple psychodynamic dimensions."@en ;
                            rdfs:label "emerges from interaction of"@en .


###  https://tuos.org/qm#employs
qm:employs rdf:type owl:ObjectProperty ;
           rdfs:comment "Indicates that a process or practice makes use of a specific mechanism or function."@en ;
           rdfs:label "employs"@en .


###  https://tuos.org/qm#enables
qm:enables rdf:type owl:ObjectProperty ;
           rdfs:domain qm:InternalMap ;
           rdfs:range qm:ConsciousnessRefinement ;
           rdfs:comment "Indicates that a conceptual framework provides the capability for a specific process or outcome."@en ,
                        "Indicates that a mechanism makes a specific process or state possible."@en ;
           rdfs:label "enables"@en .


###  https://tuos.org/qm#enablesConversionOf
qm:enablesConversionOf rdf:type owl:ObjectProperty ;
                       rdfs:domain qm:PsychoReceptiveDimension ;
                       rdfs:comment "Indicates the function of a sophisticated translation mechanism, converting abstract internal experiences into concrete external realities."@en ;
                       rdfs:label "enables conversion of"@en .


###  https://tuos.org/qm#facilitatesEmbodimentOf
qm:facilitatesEmbodimentOf rdf:type owl:ObjectProperty ;
                           rdfs:domain qm:PsychoReceptiveDimension ;
                           rdfs:comment "Indicates the function of a mental-physical interface, integrating somatic awareness into cognitive processing."@en ;
                           rdfs:label "facilitates embodiment of"@en .


###  https://tuos.org/qm#filters
qm:filters rdf:type owl:ObjectProperty ;
           rdfs:comment "Indicates that a mechanism unconsciously shapes a process like perception."@en ;
           rdfs:label "filters"@en .


###  https://tuos.org/qm#follows
qm:follows rdf:type owl:ObjectProperty ,
                    owl:TransitiveProperty ;
           rdfs:domain qm:PsychodynamicDimension ;
           rdfs:range qm:PsychodynamicDimension ;
           rdfs:label "follows"@en .


###  https://tuos.org/qm#formsBasisFor
qm:formsBasisFor rdf:type owl:ObjectProperty ;
                 rdfs:comment "Indicates that a foundational state is a prerequisite for a more advanced cognitive capacity."@en ;
                 rdfs:label "forms basis for"@en .


###  https://tuos.org/qm#formsFoundationOf
qm:formsFoundationOf rdf:type owl:ObjectProperty ;
                     rdfs:domain qm:PsychodynamicDimension ;
                     rdfs:comment "Indicates that a dimension serves as a core constituent or operational basis for a broader aspect of consciousness."@en ;
                     rdfs:label "forms foundation of"@en .


###  https://tuos.org/qm#functionsAs
qm:functionsAs rdf:type owl:ObjectProperty ;
               rdfs:domain qm:PsychoAestheticDimension ;
               rdfs:comment "Describes a dimension's role as a fundamental organizing principle or psychological mechanism."@en ;
               rdfs:label "functions as"@en .


###  https://tuos.org/qm#generates
qm:generates rdf:type owl:ObjectProperty ;
             rdfs:domain qm:PsychoFoundationalDimension ;
             rdfs:comment "Indicates that a dimension can produce specific psychological structures based on experience."@en ;
             rdfs:label "generates"@en .


###  https://tuos.org/qm#governs
qm:governs rdf:type owl:ObjectProperty ;
           rdfs:domain qm:PsychoVolitionalField ;
           rdfs:range qm:CognitiveProcess ;
           rdfs:label "governs"@en .


###  https://tuos.org/qm#harmonizes
qm:harmonizes rdf:type owl:ObjectProperty ;
              rdfs:domain qm:PsychoMeditativeDimension ;
              rdfs:comment "A property indicating the function of bringing different elements into a state of balance and agreement."@en ;
              rdfs:label "harmonizes"@en ;
              skos:definition "To bring into accord or agreement."@en .


###  https://tuos.org/qm#hasCapacityFor
qm:hasCapacityFor rdf:type owl:ObjectProperty ;
                  rdfs:domain qm:PsychoMeditativeDimension ;
                  rdfs:range qm:CognitiveCapacity ;
                  rdfs:label "has capacity for"@en .


###  https://tuos.org/qm#hasConstraint
qm:hasConstraint rdf:type owl:ObjectProperty ;
                 owl:equivalentProperty qm:isConstrainedBy ;
                 rdfs:comment "Indicates fixed constraints, such as physical laws or biological requirements, that limit a constructed reality."@en ;
                 rdfs:label "has constraint"@en .


###  https://tuos.org/qm#hasDynamic
qm:hasDynamic rdf:type owl:ObjectProperty ;
              rdfs:comment "Indicates a fundamental principle or interaction model that governs a process."@en ;
              rdfs:label "has dynamic"@en .


###  https://tuos.org/qm#hasEngagementStyle
qm:hasEngagementStyle rdf:type owl:ObjectProperty ;
                      rdfs:comment "Defines the characteristic approach a methodology takes when interacting with internal mental phenomena."@en ;
                      rdfs:label "has engagement style"@en .


###  https://tuos.org/qm#hasInterdimensionalConnection
qm:hasInterdimensionalConnection rdf:type owl:ObjectProperty ;
                                 rdfs:comment "A generic property representing a conceptual connection or dynamic flow between Psychodynamic Dimensions." ;
                                 rdfs:label "has Interdimensional Connection" .


###  https://tuos.org/qm#hasMode
qm:hasMode rdf:type owl:ObjectProperty ;
           rdfs:comment "Indicates that a process can occur in different ways, such as intentionally or reactively."@en ;
           rdfs:label "has mode"@en .


###  https://tuos.org/qm#hasNegativeConsequence
qm:hasNegativeConsequence rdf:type owl:ObjectProperty ;
                          rdfs:comment "Indicates a potential maladaptive outcome if a state is not properly managed or resolved."@en ;
                          rdfs:label "has negative consequence"@en .


###  https://tuos.org/qm#hasPhase
qm:hasPhase rdf:type owl:ObjectProperty ;
            rdfs:domain qm:LiberationProcess ;
            rdfs:comment "Indicates a distinct stage within a larger process, such as the liberation from inherited scripts."@en ;
            rdfs:label "has phase"@en .


###  https://tuos.org/qm#hasPractice
qm:hasPractice rdf:type owl:ObjectProperty ;
               rdfs:comment "Indicates that a specific mode of collapse is associated with certain techniques or practices."@en ;
               rdfs:label "has practice"@en .


###  https://tuos.org/qm#hasPrimacyOver
qm:hasPrimacyOver rdf:type owl:ObjectProperty ,
                           owl:TransitiveProperty ;
                  rdfs:domain qm:PsychodynamicDimension ;
                  rdfs:range qm:PsychodynamicDimension ;
                  rdfs:comment "A relationship indicating that one dimension has a controlling or overriding influence over another."@en ;
                  rdfs:label "has primacy over"@en ;
                  skos:definition "A property indicating that one element takes precedence over another."@en .


###  https://tuos.org/qm#hasResultingOutcome
qm:hasResultingOutcome rdf:type owl:ObjectProperty ;
                       rdfs:comment "Indicates the enhanced capacities or beneficial states achieved through a process or application."@en ;
                       rdfs:label "has resulting outcome"@en .


###  https://tuos.org/qm#hasSubStrategy
qm:hasSubStrategy rdf:type owl:ObjectProperty ;
                  rdfs:comment "Indicates a hierarchical relationship where a broader strategy encompasses more specific ones."@en ;
                  rdfs:label "has sub-strategy"@en .


###  https://tuos.org/qm#hasViewOfPerception
qm:hasViewOfPerception rdf:type owl:ObjectProperty ;
                       rdfs:comment "Defines the epistemological stance a methodology takes regarding the nature of perception."@en ;
                       rdfs:label "has view of perception"@en .


###  https://tuos.org/qm#impliesNeedFor
qm:impliesNeedFor rdf:type owl:ObjectProperty ;
                  rdfs:comment "Indicates that a particular challenge necessitates a specific approach or epistemology."@en ;
                  rdfs:label "implies need for"@en .


###  https://tuos.org/qm#influences
qm:influences rdf:type owl:ObjectProperty ;
              rdfs:domain qm:PsychodynamicDimension ;
              rdfs:range qm:PsychodynamicDimension ;
              rdfs:comment "Indicates that an external or internal factor can affect the nature or outcome of the collapse process."@en ,
                           "Indicates that one dimension affects the calibration or function of another."@en ;
              rdfs:label "influences"@en .


###  https://tuos.org/qm#informs
qm:informs rdf:type owl:ObjectProperty ;
           rdfs:comment "Indicates that an entity provides the primary input or data for a subsequent process or judgment."@en ;
           rdfs:label "informs"@en .


###  https://tuos.org/qm#initiates
qm:initiates rdf:type owl:ObjectProperty ;
             rdfs:domain qm:PsychoVolitionalDimension ;
             rdfs:range qm:CognitiveProcess ;
             rdfs:label "initiates"@en .


###  https://tuos.org/qm#initiatesModality
qm:initiatesModality rdf:type owl:ObjectProperty ;
                     rdfs:domain qm:PsychodynamicDimension ;
                     rdfs:range qm:CognitiveModality ;
                     rdfs:comment "Indicates that a dimension is the inaugural element of a specific modality."@en ;
                     rdfs:label "initiates modality"@en .


###  https://tuos.org/qm#interferesWith
qm:interferesWith rdf:type owl:ObjectProperty ;
                  rdfs:comment "Indicates a disruptive or distorting influence on a natural process or development."@en ;
                  rdfs:label "interferes with"@en .


###  https://tuos.org/qm#isAchievedThrough
qm:isAchievedThrough rdf:type owl:ObjectProperty ;
                     rdfs:comment "Indicates the method or process by which a state or goal is reached."@en ;
                     rdfs:label "is achieved through"@en ;
                     skos:definition "A property specifying the means of achieving the subject."@en .


###  https://tuos.org/qm#isAlteredBy
qm:isAlteredBy rdf:type owl:ObjectProperty ;
               rdfs:comment "Indicates that the subject can be changed or modified by the object."@en ;
               rdfs:label "is altered by"@en ;
               skos:definition "A property specifying that the subject is capable of being changed by the object."@en .


###  https://tuos.org/qm#isAppliedTo
qm:isAppliedTo rdf:type owl:ObjectProperty ;
               rdfs:comment "Indicates that a meta-level principle is the basis for a more specific concept or application."@en ;
               rdfs:label "is applied to"@en .


###  https://tuos.org/qm#isArchitectOf
qm:isArchitectOf rdf:type owl:ObjectProperty ;
                 rdfs:domain qm:PsychoProtectiveDimension ;
                 rdfs:comment "Indicates that a dimension provides the structural integrity for a psychological construct."@en ;
                 rdfs:label "is architect of"@en .


###  https://tuos.org/qm#isBalancedBy
qm:isBalancedBy rdf:type owl:ObjectProperty ,
                         owl:SymmetricProperty ;
                rdfs:domain qm:PsychodynamicDimension ;
                rdfs:range qm:PsychodynamicDimension ;
                rdfs:comment "Indicates a crucial dynamic where one dimension provides a necessary structuring or containing counterbalance to another."@en ;
                rdfs:label "is balanced by"@en .


###  https://tuos.org/qm#isCalculatedFrom
qm:isCalculatedFrom rdf:type owl:ObjectProperty ;
                    owl:inverseOf qm:isDeterminedBy ;
                    rdfs:comment "Indicates that the value of the subject is derived from the object through a specific calculation."@en ;
                    rdfs:label "is calculated from"@en ;
                    skos:definition "A property specifying that the subject is a result of a calculation involving the object."@en .


###  https://tuos.org/qm#isConfirmedBy
qm:isConfirmedBy rdf:type owl:ObjectProperty ;
                 rdfs:comment "Indicates that the existence of a phenomenon is known through its consistent influence or discernible patterns, rather than direct observation."@en ;
                 rdfs:label "is confirmed by"@en .


###  https://tuos.org/qm#isConstrainedBy
qm:isConstrainedBy rdf:type owl:ObjectProperty ;
                   rdfs:comment "Indicates that the subject is limited or restricted by the object."@en ;
                   rdfs:label "is constrained by"@en ;
                   skos:definition "A property specifying that the subject is subject to limitations from the object."@en .


###  https://tuos.org/qm#isCultivatedBy
qm:isCultivatedBy rdf:type owl:ObjectProperty ;
                  owl:inverseOf qm:yields ;
                  rdfs:comment "Indicates a method or practice used to develop or work skillfully with a cognitive state."@en ;
                  rdfs:label "is cultivated by"@en .


###  https://tuos.org/qm#isDeterminedBy
qm:isDeterminedBy rdf:type owl:ObjectProperty ;
                  rdfs:comment "Indicates the specific factors that calculate or define a component within the formal architecture."@en ;
                  rdfs:label "is determined by"@en .


###  https://tuos.org/qm#isDevelopedBy
qm:isDevelopedBy rdf:type owl:ObjectProperty ;
                 rdfs:comment "Indicates the practice or method through which a capacity or skill is cultivated."@en ;
                 rdfs:label "is developed by"@en ;
                 skos:definition "A property specifying the means by which the subject is developed."@en .


###  https://tuos.org/qm#isEngagedBy
qm:isEngagedBy rdf:type owl:ObjectProperty ;
               rdfs:comment "Indicates a process or practice that activates or makes use of a particular function or capacity."@en ;
               rdfs:label "is engaged by"@en ;
               skos:definition "A property indicating that the subject is activated or used by the object."@en .


###  https://tuos.org/qm#isEngineOf
qm:isEngineOf rdf:type owl:ObjectProperty ;
              rdfs:comment "Indicates that a practice is the primary driver for a specific type of cognitive collapse."@en ;
              rdfs:label "is engine of"@en .


###  https://tuos.org/qm#isFirstStepIn
qm:isFirstStepIn rdf:type owl:ObjectProperty ;
                 rdfs:comment "Indicates that a process is the initial, active trigger for a larger dynamic or theory."@en ;
                 rdfs:label "is first step in"@en .


###  https://tuos.org/qm#isFormedBy
qm:isFormedBy rdf:type owl:ObjectProperty ;
              rdfs:comment "Indicates that a psychological construct is shaped or created by a specific type of external influence or conditioning mechanism."@en ;
              rdfs:label "is formed by"@en .


###  https://tuos.org/qm#isFoundationFor
qm:isFoundationFor rdf:type owl:ObjectProperty ;
                   owl:inverseOf qm:reliesOn ;
                   rdfs:comment "Indicates that a mechanism is the fundamental support for a more advanced mode of awareness."@en ;
                   rdfs:label "is foundation for"@en .


###  https://tuos.org/qm#isFundamentalTo
qm:isFundamentalTo rdf:type owl:ObjectProperty ;
                   rdfs:comment "Indicates that a concept or process is an essential prerequisite or underlying basis for another."@en ;
                   rdfs:label "is fundamental to"@en .


###  https://tuos.org/qm#isFundamentalUnitOf
qm:isFundamentalUnitOf rdf:type owl:ObjectProperty ;
                       rdfs:label "is fundamental unit of"@en .


###  https://tuos.org/qm#isInputTo
qm:isInputTo rdf:type owl:ObjectProperty ;
             rdfs:comment "Indicates that the subject serves as data or a starting component for the object process."@en ;
             rdfs:label "is input to"@en ;
             skos:definition "A property specifying that the subject is an input for the object."@en .


###  https://tuos.org/qm#isKeyTo
qm:isKeyTo rdf:type owl:ObjectProperty ;
           rdfs:domain qm:PsychoAestheticDimension ;
           rdfs:range qm:PsychodynamicHarmonicAlignment ;
           rdfs:comment "Indicates that a dimension is a crucial element in achieving a specific state or process."@en ;
           rdfs:label "is key to"@en .


###  https://tuos.org/qm#isLiberatedBy
qm:isLiberatedBy rdf:type owl:ObjectProperty ;
                 rdfs:comment "Indicates the systematic process or methodology for transcending a limiting psychological construct."@en ;
                 rdfs:label "is liberated by"@en .


###  https://tuos.org/qm#isLocusOf
qm:isLocusOf rdf:type owl:ObjectProperty ;
             rdfs:domain qm:PsychodynamicDimension ;
             rdfs:range qm:CognitiveProcess ;
             rdfs:comment "Indicates that a dimension or concept is the central point or primary site of a particular process or function."@en ;
             rdfs:label "is locus of"@en ;
             skos:definition "A property indicating the central location or focus of something."@en .


###  https://tuos.org/qm#isMediatedBy
qm:isMediatedBy rdf:type owl:ObjectProperty ;
                rdfs:domain qm:PsychodynamicDimension ;
                rdfs:range qm:PsychodynamicDimension ;
                rdfs:comment "Indicates that a dimension serves as an emotional modulator, resolving the dynamic tension between two other dimensions."@en ,
                             "Indicates that a form of knowledge or experience is not apprehended directly but is filtered through another process or entity."@en ;
                rdfs:label "is mediated by"@en .


###  https://tuos.org/qm#isModulatedBy
qm:isModulatedBy rdf:type owl:ObjectProperty ;
                 rdfs:domain qm:SecondaryModality ;
                 rdfs:range qm:PrimeModality ;
                 rdfs:comment "Indicates a hierarchical yet dynamically interactive relationship where one modality's output shapes the texture and functioning of another."@en ,
                              "Indicates that a component's influence is weighted or adjusted by a personal tendency or dispositional factor."@en ;
                 rdfs:label "is modulated by"@en .


###  https://tuos.org/qm#isNegatedBy
qm:isNegatedBy rdf:type owl:ObjectProperty ;
               rdfs:domain qm:PsychoTranspersonalDimension ;
               rdfs:range qm:PsychoVolitionalDimension ;
               rdfs:comment "Indicates that the expression of a passive dimension can be overridden or negated by a dimension with volitional primacy."@en ;
               rdfs:label "is negated by"@en .


###  https://tuos.org/qm#isOutputOf
qm:isOutputOf rdf:type owl:ObjectProperty ;
              rdfs:comment "Indicates that the subject is the result or product of the object process."@en ;
              rdfs:label "is output of"@en ;
              skos:definition "A property specifying that the subject is a result of the object."@en .


###  https://tuos.org/qm#isRegulatedBy
qm:isRegulatedBy rdf:type owl:ObjectProperty ;
                 rdfs:domain qm:EmotionalResponse ;
                 rdfs:range qm:PsychodynamicDimension ;
                 rdfs:comment "Indicates that an emotional response is modulated or balanced by the function of a specific dimension."@en ;
                 rdfs:label "is regulated by"@en .


###  https://tuos.org/qm#isResolvedBy
qm:isResolvedBy rdf:type owl:ObjectProperty ;
                rdfs:comment "Indicates the catalyst or process through which a probabilistic state collapses into a definite experience."@en ;
                rdfs:label "is resolved by"@en .


###  https://tuos.org/qm#isSegregatedBy
qm:isSegregatedBy rdf:type owl:ObjectProperty ;
                  rdfs:comment "Indicates that a fundamental structural feature separates two different modes of being or knowing."@en ;
                  rdfs:label "is segregated by"@en .


###  https://tuos.org/qm#isShapedByTechnique
qm:isShapedByTechnique rdf:type owl:ObjectProperty ;
                       rdfs:comment "Indicates that a process can be influenced by a deliberate practice or method."@en ;
                       rdfs:label "is shaped by technique"@en .


###  https://tuos.org/qm#isSourceOf
qm:isSourceOf rdf:type owl:ObjectProperty ;
              rdfs:domain qm:PsychoVolitionalDimension ;
              rdfs:comment "Indicates that the subject is the origin or genesis of the object."@en ;
              rdfs:label "is source of"@en ;
              skos:definition "A property indicating that the subject gives rise to the object."@en .


###  https://tuos.org/qm#isSubjectTo
qm:isSubjectTo rdf:type owl:ObjectProperty ;
               rdfs:comment "Indicates that a class of entities can exhibit a specific principle or characteristic."@en ;
               rdfs:label "is subject to"@en .


###  https://tuos.org/qm#isSupportedByMechanism
qm:isSupportedByMechanism rdf:type owl:ObjectProperty ;
                          rdfs:domain qm:PsychoMotivationalDimension ;
                          rdfs:comment "Indicates that a dimension's sustained drive is supported by specific psychological mechanisms."@en ;
                          rdfs:label "is supported by mechanism"@en .


###  https://tuos.org/qm#isTransformedUsing
qm:isTransformedUsing rdf:type owl:ObjectProperty ;
                      rdfs:comment "Indicates the mathematical function used to convert a raw value into a final, normalized intensity."@en ;
                      rdfs:label "is transformed using"@en .


###  https://tuos.org/qm#isTransmittedVia
qm:isTransmittedVia rdf:type owl:ObjectProperty ;
                    rdfs:comment "Indicates the channel or method through which a concept, such as an Inherited Script, is passed on."@en ;
                    rdfs:label "is transmitted via"@en .


###  https://tuos.org/qm#isTriggeredBy
qm:isTriggeredBy rdf:type owl:ObjectProperty ;
                 rdfs:domain qm:PsychodynamicCollapse ;
                 rdfs:range qm:ConsciousAttention ;
                 rdfs:comment "Indicates the catalyst for a psychodynamic process."@en ;
                 rdfs:label "is triggered by"@en .


###  https://tuos.org/qm#leadsTo
qm:leadsTo rdf:type owl:ObjectProperty ;
           rdfs:comment "Indicates a causal or developmental progression from one state to another."@en ;
           rdfs:label "leads to"@en .


###  https://tuos.org/qm#leverages
qm:leverages rdf:type owl:ObjectProperty ;
             rdfs:comment "Indicates that a process makes strategic use of a particular resource or dimension."@en ;
             rdfs:label "leverages"@en ;
             skos:definition "To use something to maximum advantage."@en .


###  https://tuos.org/qm#mapsDirectlyTo
qm:mapsDirectlyTo rdf:type owl:ObjectProperty ;
                  rdfs:comment "Indicates a direct functional correspondence between a practice and a psychodynamic dimension."@en ;
                  rdfs:label "maps directly to"@en .


###  https://tuos.org/qm#modifies
qm:modifies rdf:type owl:ObjectProperty ;
            rdfs:comment "Indicates that an act or process inherently influences the nature and character of what is observed."@en ;
            rdfs:label "modifies"@en .


###  https://tuos.org/qm#mutuallyInfluences
qm:mutuallyInfluences rdf:type owl:ObjectProperty ,
                               owl:SymmetricProperty ;
                      rdfs:domain qm:PsychodynamicDimension ;
                      rdfs:range qm:PsychodynamicDimension ;
                      rdfs:comment "Indicates that dimensions exist in a network of simultaneous, bidirectional relationships, creating emergent properties."@en ;
                      rdfs:label "mutually influences"@en .


###  https://tuos.org/qm#navigatesWithin
qm:navigatesWithin rdf:type owl:ObjectProperty ;
                   rdfs:comment "Indicates that a process must operate within the context of certain fixed limits."@en ;
                   rdfs:label "navigates within"@en .


###  https://tuos.org/qm#operatesAs
qm:operatesAs rdf:type owl:ObjectProperty ;
              rdfs:domain qm:PsychoVolitionalDimension ;
              rdfs:comment "Indicates the specific role or function that a concept or dimension fulfills."@en ;
              rdfs:label "operates as"@en ;
              skos:definition "A property that describes the functional role of the subject."@en .


###  https://tuos.org/qm#operatesThrough
qm:operatesThrough rdf:type owl:ObjectProperty ;
                   rdfs:domain qm:PsychodynamicDimension ;
                   rdfs:range qm:ProcessingMechanism ;
                   rdfs:comment "Indicates the primary mechanism or process by which a dimension or concept functions."@en ;
                   rdfs:label "operates through"@en ;
                   skos:definition "A property that specifies the means by which something functions."@en .


###  https://tuos.org/qm#orchestrates
qm:orchestrates rdf:type owl:ObjectProperty ;
                rdfs:domain qm:PsychoReceptiveDimension ;
                rdfs:comment "Indicates the management of developing subtle internal 'proto-impulses' into authentic external expressions."@en ;
                rdfs:label "orchestrates"@en .


###  https://tuos.org/qm#performs
qm:performs rdf:type owl:ObjectProperty ;
            rdfs:comment "Indicates an action or process carried out by a specific type of agent or state of awareness."@en ;
            rdfs:label "performs"@en .


###  https://tuos.org/qm#posits
qm:posits rdf:type owl:ObjectProperty ;
          rdfs:comment "Indicates that a theory asserts or puts forward a specific concept or relationship."@en ;
          rdfs:label "posits"@en .


###  https://tuos.org/qm#practices
qm:practices rdf:type owl:ObjectProperty ;
             rdfs:comment "A property linking an agent to a practice or method they perform."@en ;
             rdfs:label "practices"@en ;
             skos:definition "To perform or carry out a particular activity or method."@en .


###  https://tuos.org/qm#precedes
qm:precedes rdf:type owl:ObjectProperty ;
            rdfs:comment "Indicates that a state or process exists prior to another in the cognitive flow."@en ;
            rdfs:label "precedes"@en .


###  https://tuos.org/qm#produces
qm:produces rdf:type owl:ObjectProperty ;
            rdfs:comment "Indicates the outcome or result of a process or method."@en ;
            rdfs:label "produces"@en .


###  https://tuos.org/qm#progressesTo
qm:progressesTo rdf:type owl:ObjectProperty ;
                rdfs:domain qm:PsychoConceptiveDimension ;
                rdfs:range qm:PsychoMeditativeDimension ;
                rdfs:label "progresses to"@en .


###  https://tuos.org/qm#providesFoundationFor
qm:providesFoundationFor rdf:type owl:ObjectProperty ;
                         rdfs:domain qm:PsychodynamicDimension ;
                         rdfs:range qm:PsychodynamicDimension ;
                         rdfs:comment "Indicates that the subject provides the necessary basis or support for the object."@en ;
                         rdfs:label "provides foundation for"@en ;
                         skos:definition "A property indicating that the subject is a fundamental support for the object."@en .


###  https://tuos.org/qm#receivesInputFrom
qm:receivesInputFrom rdf:type owl:ObjectProperty ;
                     rdfs:domain qm:PsychoMeditativeDimension ;
                     rdfs:range qm:PsychoConceptiveDimension ;
                     rdfs:label "receives input from"@en .


###  https://tuos.org/qm#reliesOn
qm:reliesOn rdf:type owl:ObjectProperty ;
            rdfs:comment "Indicates that a mechanism or process depends on a specific dimension or component for its operation."@en ;
            rdfs:label "relies on"@en .


###  https://tuos.org/qm#servesAs
qm:servesAs rdf:type owl:ObjectProperty ;
            rdfs:domain qm:PsychoFoundationalDimension ;
            rdfs:comment "Indicates that a dimension provides a fundamental function for the psyche."@en ;
            rdfs:label "serves as"@en .


###  https://tuos.org/qm#shapes
qm:shapes rdf:type owl:ObjectProperty ;
          rdfs:domain qm:PsychodynamicDimension ;
          rdfs:range qm:PsychologicalPhenomenon ;
          rdfs:comment "Indicates that a dimension actively directs or determines the nature of a psychological phenomenon."@en ;
          rdfs:label "shapes"@en .


###  https://tuos.org/qm#stemsFrom
qm:stemsFrom rdf:type owl:ObjectProperty ;
             rdfs:label "stems from"@en .


###  https://tuos.org/qm#targets
qm:targets rdf:type owl:ObjectProperty ;
           rdfs:comment "Defines the primary psychological phenomena or constructs that a given strategy aims to influence or transform."@en ;
           rdfs:label "targets"@en .


###  https://tuos.org/qm#translatesValuesInto
qm:translatesValuesInto rdf:type owl:ObjectProperty ;
                        rdfs:domain qm:PsychoMotivationalDimension ;
                        rdfs:comment "Indicates the psychological mechanism through which abstract principles and internal value systems achieve concrete manifestation in consistent external action."@en ;
                        rdfs:label "translates values into"@en .


###  https://tuos.org/qm#underpins
qm:underpins rdf:type owl:ObjectProperty ;
             rdfs:domain qm:PsychoProtectiveDimension ;
             rdfs:comment "Indicates that a dimension provides the foundation for a crucial psychological capacity."@en ;
             rdfs:label "underpins"@en .


###  https://tuos.org/qm#uses
qm:uses rdf:type owl:ObjectProperty ;
        rdfs:comment "Indicates the methods or tools employed by a process."@en ;
        rdfs:label "uses"@en .


###  https://tuos.org/qm#yields
qm:yields rdf:type owl:ObjectProperty ;
          rdfs:comment "Indicates the outcome or product of a sustained practice."@en ;
          rdfs:label "yields"@en .


#################################################################
#    Classes
#################################################################

###  https://tuos.org/qm#AbstractInternalExperience
qm:AbstractInternalExperience rdf:type owl:Class ;
                              rdfs:subClassOf qm:PsychoReceptiveDimension ;
                              rdfs:comment "Internal states such as insights, principles, values, and intuitive understandings."@en ;
                              rdfs:label "Abstract Internal Experience"@en .


###  https://tuos.org/qm#ActionableIntelligence
qm:ActionableIntelligence rdf:type owl:Class ;
                          rdfs:subClassOf qm:PsychoFoundationalDimension ;
                          rdfs:comment "Practical guidance applicable in real-world situations, synthesized from diverse information sources."@en ;
                          rdfs:label "Actionable Intelligence"@en .


###  https://tuos.org/qm#ActiveConstitutiveForceView
qm:ActiveConstitutiveForceView rdf:type owl:Class ;
                               rdfs:subClassOf qm:ViewOfPerception ;
                               rdfs:comment "The view that perception is an active, creative force that significantly shapes and generates experienced reality."@en ;
                               rdfs:label "Active Constitutive Force View"@en .


###  https://tuos.org/qm#ActiveKnowing
qm:ActiveKnowing rdf:type owl:Class ;
                 rdfs:subClassOf qm:PracticesCategory ;
                 rdfs:label "Active Knowing"@en .


###  https://tuos.org/qm#ActiveMastery
qm:ActiveMastery rdf:type owl:Class ;
                 rdfs:subClassOf qm:AdvancedPracticesAndMethodologiesCategory ,
                                 [ rdf:type owl:Restriction ;
                                   owl:onProperty qm:isAchievedThrough ;
                                   owl:someValuesFrom qm:Contemplation
                                 ] ;
                 rdfs:comment "The deliberate shaping of perception and conscious selection of focal points for awareness, enabling skillful influence over how potential experiences collapse into actual experiences."@en ;
                 rdfs:label "Active Mastery"@en .


###  https://tuos.org/qm#ActiveReframingProcess
qm:ActiveReframingProcess rdf:type owl:Class ;
                          rdfs:subClassOf qm:AdvancedPracticesAndMethodologiesCategory ,
                                          [ rdf:type owl:Restriction ;
                                            owl:onProperty qm:leverages ;
                                            owl:hasValue qm:Pd1
                                          ] ,
                                          [ rdf:type owl:Restriction ;
                                            owl:onProperty qm:leverages ;
                                            owl:hasValue qm:Pd2
                                          ] ,
                                          [ rdf:type owl:Restriction ;
                                            owl:onProperty qm:leverages ;
                                            owl:hasValue qm:Pd3
                                          ] ;
                          rdfs:comment "The three-step engagement with the Prime Modality to consciously re-evaluate and transform the Cognitive Appraisal."@en ;
                          rdfs:label "Active Reframing Process" .


###  https://tuos.org/qm#ActiveStructuralInvestigation
qm:ActiveStructuralInvestigation rdf:type owl:Class ;
                                 rdfs:subClassOf qm:QuantumMindfulnessApplication ;
                                 rdfs:comment "The practice of actively investigating the structure and origins of mental phenomena, treating them as artifacts generated by underlying psychological systems."@en ;
                                 rdfs:label "Active Structural Investigation"@en .


###  https://tuos.org/qm#ActualizationProcess
qm:ActualizationProcess rdf:type owl:Class ;
                        rdfs:subClassOf qm:FormalArchitectureCategory ,
                                        [ rdf:type owl:Restriction ;
                                          owl:onProperty qm:isOutputOf ;
                                          owl:allValuesFrom qm:FinalIntensity
                                        ] ,
                                        [ rdf:type owl:Restriction ;
                                          owl:onProperty qm:isTransformedUsing ;
                                          owl:allValuesFrom qm:SigmoidFunction
                                        ] ;
                        rdfs:comment "The final stage of the psychodynamic process where the raw potential of Dimensional Activation (Kj) is transformed into a normalized Final Intensity (xj) via a Sigmoid Function. This represents the definitive 'collapse' for each dimension, moving it from a state of potential activation to a specific level of expression."@en ,
                                     "The final stage where the raw potential of Dimensional Activation (Kj) is transformed into a Final Intensity (xj) via a Sigmoid Function, which then constitutes the Overall Mental State (S)."@en ,
                                     "The process where the raw potential of Dimensional Activation (Kj) is transformed into a Final Intensity (xj) via a Sigmoid Function."@en ;
                        rdfs:label "Actualization Process"@en ;
                        rdfs:subClassOf "Psychodynamic Model"@en .


###  https://tuos.org/qm#ActualizedExperience
qm:ActualizedExperience rdf:type owl:Class ;
                        rdfs:subClassOf qm:PsychodynamicWaveCollapse ;
                        rdfs:comment "The singular, definite, and consciously experienced outcome resulting from Psychodynamic Wave Collapse. This is the manifested reality of a mental state."@en ;
                        rdfs:label "Actualized Experience"@en .


###  https://tuos.org/qm#AdvancedPracticesAndMethodologiesCategory
qm:AdvancedPracticesAndMethodologiesCategory rdf:type owl:Class ;
                                             rdfs:comment "A grouping for more sophisticated techniques and approaches within the framework."@en ,
                                                          "A structured methodology within Quantum Mindfulness for engaging directly with the generative systems of consciousness, enabling a more sophisticated and agentic relationship with one's internal experience."@en ;
                                             rdfs:label "Advanced Practices and Methodologies"@en .


###  https://tuos.org/qm#AestheticPrinciple
qm:AestheticPrinciple rdf:type owl:Class ;
                      rdfs:subClassOf qm:PsychoAestheticDimension ;
                      rdfs:comment "A principle governing the perception and integration of experiences related to beauty, proportion, and harmonic relationship."@en ;
                      rdfs:label "Aesthetic Principle"@en .


###  https://tuos.org/qm#AestheticResolution
qm:AestheticResolution rdf:type owl:Class ;
                       rdfs:subClassOf qm:AdvancedPracticesAndMethodologiesCategory ;
                       rdfs:comment "A form of conflict resolution that involves finding solutions that honor all parties' essential needs and transcend the limitations of the original conflict."@en ;
                       rdfs:label "Aesthetic Resolution"@en .


###  https://tuos.org/qm#AnalyticalReasoning
qm:AnalyticalReasoning rdf:type owl:Class ;
                       rdfs:subClassOf qm:ProcessingMechanism .


###  https://tuos.org/qm#Anxiety
qm:Anxiety rdf:type owl:Class ;
           rdfs:subClassOf qm:Examples_Emergent ,
                           [ rdf:type owl:Restriction ;
                             owl:onProperty qm:emergesFromInteractionOf ;
                             owl:hasValue qm:Pd4
                           ] ,
                           [ rdf:type owl:Restriction ;
                             owl:onProperty qm:emergesFromInteractionOf ;
                             owl:hasValue qm:Pd5
                           ] ,
                           [ rdf:type owl:Restriction ;
                             owl:onProperty qm:emergesFromInteractionOf ;
                             owl:hasValue qm:Pd7
                           ] ,
                           [ rdf:type owl:Restriction ;
                             owl:onProperty qm:emergesFromInteractionOf ;
                             owl:hasValue qm:Pd8
                           ] ;
           rdfs:comment "An emergent pattern where the Psycho-Protective Dimension becomes hyperactive, the Psycho-Empathic Dimension contracts, the Psycho-Motivational Dimension fragments, and the Psycho-Receptive Dimension becomes hypersensitive."@en ;
           rdfs:label "Anxiety"@en .


###  https://tuos.org/qm#AssignedMeaning
qm:AssignedMeaning rdf:type owl:Class ;
                   owl:equivalentClass qm:PerceivedMeaning ;
                   rdfs:subClassOf qm:ObservationComponentsCategory ;
                   rdfs:comment "The interpretation or significance that the mind attributes to a raw perception or stimulus."@en ;
                   rdfs:label "Assigned Meaning"@en ;
                   skos:definition "The meaning attributed to a stimulus during the process of perception."@en .


###  https://tuos.org/qm#AttentionSculpting
qm:AttentionSculpting rdf:type owl:Class ;
                      rdfs:subClassOf qm:PracticesCategory ;
                      rdfs:label "Attention Sculpting"@en .


###  https://tuos.org/qm#Attunement
qm:Attunement rdf:type owl:Class ;
              rdfs:subClassOf qm:Phenomenon ;
              rdfs:comment "The ability to sense and respond to the internal states of others with precision and care across emotional, cognitive, somatic, and energetic levels."@en ;
              rdfs:label "Attunement"@en .


###  https://tuos.org/qm#AverageValenceOfPriorState
qm:AverageValenceOfPriorState rdf:type owl:Class ;
                              rdfs:subClassOf qm:CognitiveAppraisalComponentsCategory ;
                              rdfs:comment "Captures the idea of 'emotional inertia' or the lingering overall mood from the immediately preceding mental state (S_t-1)."@en ;
                              rdfs:label "Average Valence of Prior State (AvgValence(S_t-1))"@en ,
                                         "Average Valence of Prior State (AvgValence(S_t-1))" .


###  https://tuos.org/qm#BalancingDimensionalEnergies
qm:BalancingDimensionalEnergies rdf:type owl:Class ;
                                rdfs:subClassOf qm:PracticesCategory .


###  https://tuos.org/qm#BehavioralManifestation
qm:BehavioralManifestation rdf:type owl:Class ;
                           rdfs:subClassOf qm:PsychologicalPhenomenon ;
                           rdfs:label "Behavioral Manifestation"@en .


###  https://tuos.org/qm#BeliefFormation
qm:BeliefFormation rdf:type owl:Class ;
                   rdfs:subClassOf qm:FormalArchitectureCategory ,
                                   [ rdf:type owl:Restriction ;
                                     owl:onProperty qm:isAlteredBy ;
                                     owl:someValuesFrom qm:OverallMentalState
                                   ] ;
                   rdfs:comment "The mechanism by which stable, long-term cognitive structures (Traits) are altered. It is governed by the principle 'Practice Becomes Belief', where repeated mental states (S), especially those driven by strong activations within the Secondary Modality, can durably modify foundational Trait variables (Tj)."@en ;
                   rdfs:label "Belief Formation"@en ,
                              "Belief Formation" ;
                   rdfs:subClassOf "Cognitive Influence Model"@en .


###  https://tuos.org/qm#BiologicalOverrideSystem
qm:BiologicalOverrideSystem rdf:type owl:Class ;
                            rdfs:subClassOf qm:InfluentialFactor ;
                            rdfs:label "Biological Override System"@en .


###  https://tuos.org/qm#BonesOfReality
qm:BonesOfReality rdf:type owl:Class ;
                  rdfs:subClassOf qm:ChallengesAndLimitationsCategory ;
                  rdfs:comment "Fixed constraints such as physical laws, biological requirements, and material circumstances that are not subject to perceptual construction."@en ;
                  rdfs:label "Bones of Reality"@en .


###  https://tuos.org/qm#BoundedCompassion
qm:BoundedCompassion rdf:type owl:Class ;
                     rdfs:subClassOf qm:Phenomenon ;
                     rdfs:comment "The ability to care deeply while maintaining the structural integrity necessary for sustained caring, enabled by the balance of Pd4 and Pd5."@en ;
                     rdfs:label "Bounded Compassion"@en .


###  https://tuos.org/qm#CalculatedTurbulence
qm:CalculatedTurbulence rdf:type owl:Class ;
                        rdfs:subClassOf qm:Phenomenon .


###  https://tuos.org/qm#ChallengesAndLimitations
qm:ChallengesAndLimitations rdf:type owl:Class ;
                            rdfs:subClassOf qm:CoreConceptsCategory ;
                            rdfs:comment "A class encompassing obstacles, inherent restrictions, or difficulties that impede optimal psychological functioning, hinder conscious development, or constrain the direct application of Quantum Mindfulness principles."@en ;
                            rdfs:label "Challenges and Limitations"@en .


###  https://tuos.org/qm#ChallengesAndLimitationsCategory
qm:ChallengesAndLimitationsCategory rdf:type owl:Class ;
                                    rdfs:comment "Acknowledged difficulties or boundaries in the theory or application of Quantum Mindfulness."@en ;
                                    rdfs:label "Challenges and Limitations"@en .


###  https://tuos.org/qm#ChaosConciergePattern
qm:ChaosConciergePattern rdf:type owl:Class ;
                         rdfs:subClassOf qm:DysfunctionalPattern ,
                                         qm:PsychologicalDysfunctionAndImbalance ;
                         rdfs:comment "A specific manifestation of Psycho-Protective dysfunction where the corrupted protective mechanism inadvertently or intentionally creates disruption."@en ;
                         rdfs:label "Chaos Concierge Pattern"@en .


###  https://tuos.org/qm#ClassicalMindfulness
qm:ClassicalMindfulness rdf:type owl:Class ;
                        rdfs:subClassOf qm:MindfulnessApproachesComparisonCategory ,
                                        qm:MindfulnessIntervention ,
                                        [ rdf:type owl:Restriction ;
                                          owl:onProperty qm:definesRoleOfObserverAs ;
                                          owl:someValuesFrom qm:WitnessConsciousness
                                        ] ,
                                        [ rdf:type owl:Restriction ;
                                          owl:onProperty qm:hasEngagementStyle ;
                                          owl:someValuesFrom qm:NonReactiveObservation
                                        ] ,
                                        [ rdf:type owl:Restriction ;
                                          owl:onProperty qm:hasViewOfPerception ;
                                          owl:someValuesFrom qm:PassiveRecipientView
                                        ] ,
                                        [ rdf:type owl:Restriction ;
                                          owl:onProperty qm:providesFoundationFor ;
                                          owl:someValuesFrom qm:Contemplation
                                        ] ,
                                        [ rdf:type owl:Restriction ;
                                          owl:onProperty qm:targets ;
                                          owl:someValuesFrom qm:ObservationValence
                                        ] ,
                                        [ rdf:type owl:Restriction ;
                                          owl:onProperty qm:targets ;
                                          owl:someValuesFrom qm:PersonalTendency
                                        ] ,
                                        [ rdf:type owl:Restriction ;
                                          owl:onProperty qm:targets ;
                                          owl:hasValue qm:CognitiveInfluence
                                        ] ;
                        owl:disjointWith qm:QuantumMindfulnessApplication ;
                        rdfs:comment "A methodological approach emphasizing intentional, non-judgmental observation of moment-to-moment phenomena to cultivate stable, present-centered awareness and 'passive mastery'."@en ,
                                     "A regulatory or dampening practice aiming to neutralize a negative Cognitive Appraisal by reducing reactivity (lowering wΨ and wS) and observing without judgment (pushing Valence(Ψ) toward zero). It is a practice of non-reactive observation."@en ,
                                     "A regulatory or dampening practice aiming to reduce the intensity of emotional reactions by cultivating a stable, non-judgmental, non-elaborative observation of present-moment experience. Its goal is 'passive mastery' and equanimity."@en ;
                        rdfs:label "Classical Mindfulness"@en ,
                                   "Classical Mindfulness (Passive)"@en ,
                                   "Classical Mindfulness (Passive)" .


###  https://tuos.org/qm#CognitiveAgency
qm:CognitiveAgency rdf:type owl:Class ;
                   rdfs:subClassOf qm:OtherKeyConcepts ,
                                   [ rdf:type owl:Restriction ;
                                     owl:onProperty qm:uses ;
                                     owl:someValuesFrom qm:CognitiveAnchoring
                                   ] ;
                   rdfs:comment "The capacity developed through intentional attention management to consciously guide the psychodynamic collapse process towards desired mental potentials."@en ;
                   rdfs:label "Cognitive Agency"@en .


###  https://tuos.org/qm#CognitiveAnchoring
qm:CognitiveAnchoring rdf:type owl:Class ;
                      rdfs:subClassOf qm:CognitiveMechanism ,
                                      qm:CoreConceptsCategory ,
                                      qm:ProcessingMechanism ,
                                      qm:SustainedActionMechanism ,
                                      [ rdf:type owl:Restriction ;
                                        owl:onProperty qm:composedOf ;
                                        owl:someValuesFrom qm:CognitiveAnchoringComponent
                                      ] ,
                                      [ rdf:type owl:Restriction ;
                                        owl:onProperty qm:enables ;
                                        owl:someValuesFrom qm:SuperpositionalCognitiveEngineering
                                      ] ,
                                      [ rdf:type owl:Restriction ;
                                        owl:onProperty qm:isFoundationFor ;
                                        owl:someValuesFrom qm:VectorizedAwareness
                                      ] ,
                                      [ rdf:type owl:Restriction ;
                                        owl:onProperty qm:reliesOn ;
                                        owl:someValuesFrom qm:PsychoVolitionalDimension
                                      ] ;
                      rdfs:comment "A fundamental psychological mechanism responsible for stabilizing intent and enabling purposeful action by selecting and focusing on specific possibilities from a probabilistic field. It is an active process of maintaining a mental orientation or intentional set over time."@en ,
                                   "A mechanism by which mental intention resists external distractions through resonance with nonlocal goal states."@en ,
                                   "The tendency to rely too heavily on an initial piece of information (the 'anchor') when making decisions or judgments, influencing subsequent processing."@en ;
                      rdfs:label "Cognitive Anchoring"@en .


###  https://tuos.org/qm#CognitiveAnchoringComponent
qm:CognitiveAnchoringComponent rdf:type owl:Class ;
                               rdfs:subClassOf qm:CognitiveAnchoring ;
                               rdfs:comment "A primary and interdependent component of the Cognitive Anchoring stabilization system."@en ;
                               rdfs:label "Cognitive Anchoring Component"@en .


###  https://tuos.org/qm#CognitiveAnchoringFailure
qm:CognitiveAnchoringFailure rdf:type owl:Class ;
                             rdfs:subClassOf qm:CognitiveStrainAndDysfunction ,
                                             qm:UnresolvedSuperpositionConsequence .


###  https://tuos.org/qm#CognitiveAnchoringFailureConsequence
qm:CognitiveAnchoringFailureConsequence rdf:type owl:Class ;
                                        rdfs:subClassOf qm:CognitiveAnchoring ,
                                                        qm:PsychologicalDisharmony ;
                                        rdfs:comment "A form of psychological distress or functional impairment resulting from failed or compromised Cognitive Anchoring."@en ;
                                        rdfs:label "Cognitive Anchoring Failure Consequence"@en .


###  https://tuos.org/qm#CognitiveAppraisal
qm:CognitiveAppraisal rdf:type owl:Class ;
                      rdfs:subClassOf qm:CognitiveMechanism ,
                                      qm:FormalArchitectureCategory ,
                                      [ rdf:type owl:Restriction ;
                                        owl:onProperty qm:composedOf ;
                                        owl:someValuesFrom qm:CognitiveAppraisalComponent
                                      ] ,
                                      [ rdf:type owl:Restriction ;
                                        owl:onProperty qm:isDeterminedBy ;
                                        owl:someValuesFrom qm:CognitiveAppraisalBias
                                      ] ,
                                      [ rdf:type owl:Restriction ;
                                        owl:onProperty qm:isDeterminedBy ;
                                        owl:someValuesFrom qm:ObservationValence
                                      ] .


###  https://tuos.org/qm#CognitiveAppraisalBias
qm:CognitiveAppraisalBias rdf:type owl:Class ;
                          owl:equivalentClass qm:InherentDisposition ;
                          rdfs:subClassOf qm:CognitiveAppraisalComponentsCategory ;
                          rdfs:comment "A baseline cognitive or affective bias rooted in the individual's stable characteristics (e.g., optimism, pessimism), which is contributed by the Prime Modality to the Cognitive Appraisal."@en ;
                          rdfs:label "Cognitive Appraisal Bias (Bias_M1)"@en .


###  https://tuos.org/qm#CognitiveAppraisalComponent
qm:CognitiveAppraisalComponent rdf:type owl:Class ;
                               rdfs:subClassOf qm:CognitiveAppraisalComponentsCategory ;
                               rdfs:comment "A distinct force that contributes to the dynamically calculated, weighted sum that forms the Cognitive Appraisal (C)."@en ;
                               rdfs:label "Cognitive Appraisal Component"@en .


###  https://tuos.org/qm#CognitiveAppraisalComponentsCategory
qm:CognitiveAppraisalComponentsCategory rdf:type owl:Class ;
                                        rdfs:subClassOf qm:CognitiveAppraisal ;
                                        rdfs:comment "Conceptual container for the constituent parts of a Cognitive Appraisal."@en ;
                                        rdfs:label "Components (C = wΨ ⋅ Valence(Ψ) + wS ⋅ AvgValence(S_t-1) + Bias_M1)"@en .


###  https://tuos.org/qm#CognitiveBias
qm:CognitiveBias rdf:type owl:Class ;
                 rdfs:subClassOf qm:InfluentialFactor ;
                 rdfs:label "Cognitive Bias"@en .


###  https://tuos.org/qm#CognitiveCapacity
qm:CognitiveCapacity rdf:type owl:Class ;
                     rdfs:subClassOf qm:GoalsCategory .


###  https://tuos.org/qm#CognitiveCollapse
qm:CognitiveCollapse rdf:type owl:Class ;
                     rdfs:subClassOf qm:CognitiveMechanism .


###  https://tuos.org/qm#CognitiveDecoherence
qm:CognitiveDecoherence rdf:type owl:Class ;
                        rdfs:subClassOf qm:CognitiveStrainAndDysfunction ,
                                        qm:UnresolvedSuperpositionConsequence ;
                        rdfs:label "Cognitive Decoherence"@en .


###  https://tuos.org/qm#CognitiveDistillation
qm:CognitiveDistillation rdf:type owl:Class ;
                         rdfs:subClassOf qm:GoalsCategory ;
                         rdfs:comment "The process of extracting functional insights from traditional wisdom systems and translating them into a modern psychodynamic context."@en ;
                         rdfs:label "Cognitive Distillation"@en .


###  https://tuos.org/qm#CognitiveEmergenceField
qm:CognitiveEmergenceField rdf:type owl:Class ;
                           rdfs:subClassOf qm:FormalArchitectureCategory ;
                           rdfs:comment "An abstract space where the raw activation potentials (Kj) of the psychodynamic dimensions reside before they manifest as concrete aspects of conscious experience through the Actualization process."@en ;
                           rdfs:label "Cognitive Emergence Field"@en .


###  https://tuos.org/qm#CognitiveEmotionalPatternInheritance
qm:CognitiveEmotionalPatternInheritance rdf:type owl:Class ;
                                        rdfs:subClassOf qm:ExternalInfluence ;
                                        rdfs:label "Cognitive-Emotional Pattern Inheritance"@en .


###  https://tuos.org/qm#CognitiveEndurance
qm:CognitiveEndurance rdf:type owl:Class ;
                      rdfs:subClassOf qm:PsychoMotivationalDimension ;
                      rdfs:comment "The capacity to sustain motivation and enable long-term pattern recognition essential for achieving goals across extended time periods."@en ;
                      rdfs:label "Cognitive Endurance"@en .


###  https://tuos.org/qm#CognitiveEnhancement
qm:CognitiveEnhancement rdf:type owl:Class ;
                        rdfs:subClassOf qm:MainStrategiesCategory ,
                                        [ rdf:type owl:Restriction ;
                                          owl:onProperty qm:addressesLimitationsOf ;
                                          owl:someValuesFrom qm:CognitiveStrainAndDysfunction
                                        ] ,
                                        [ rdf:type owl:Restriction ;
                                          owl:onProperty qm:hasSubStrategy ;
                                          owl:someValuesFrom qm:CognitiveOptimization
                                        ] ,
                                        [ rdf:type owl:Restriction ;
                                          owl:onProperty qm:isAchievedThrough ;
                                          owl:someValuesFrom qm:TherapeuticStrategy
                                        ] ;
                        rdfs:comment "A comprehensive process aiming to optimize mental function, improve cognitive abilities, and cultivate optimal cognitive states for enhanced personal and professional effectiveness. It is a dynamic, multidimensional process requiring deliberate cultivation through evidence-based practices and a nuanced comprehension of cognitive architecture."@en ,
                                     "Methodologies specifically designed to enhance cognitive clarity, creativity, and overall effectiveness by addressing personal cognitive limitations and fostering optimal mental states."@en ,
                                     "The improvement or augmentation of cognitive abilities through practices or understanding from the framework."@en ;
                        rdfs:label "Cognitive Enhancement"@en .


###  https://tuos.org/qm#CognitiveEntropicDrift
qm:CognitiveEntropicDrift rdf:type owl:Class ;
                          rdfs:subClassOf qm:CognitiveStrainAndDysfunction ,
                                          qm:UnresolvedSuperpositionConsequence ;
                          rdfs:label "Cognitive Entropic Drift"@en .


###  https://tuos.org/qm#CognitiveFieldManipulation
qm:CognitiveFieldManipulation rdf:type owl:Class ;
                              rdfs:subClassOf qm:PerceptualShapingTechnique ;
                              rdfs:label "Cognitive Field Manipulation"@en .


###  https://tuos.org/qm#CognitiveFilteringMechanism
qm:CognitiveFilteringMechanism rdf:type owl:Class ;
                               rdfs:subClassOf qm:CognitiveMechanism ,
                                               qm:Perception ;
                               rdfs:label "Cognitive Filtering Mechanism"@en .


###  https://tuos.org/qm#CognitiveFlow
qm:CognitiveFlow rdf:type owl:Class ;
                 rdfs:subClassOf qm:PsychologicalPhenomenon ;
                 rdfs:label "Cognitive Flow"@en .


###  https://tuos.org/qm#CognitiveFluency
qm:CognitiveFluency rdf:type owl:Class ;
                    rdfs:subClassOf qm:GoalsCategory ,
                                    [ rdf:type owl:Restriction ;
                                      owl:onProperty qm:isDevelopedBy ;
                                      owl:someValuesFrom qm:Contemplation
                                    ] ;
                    rdfs:comment "The ability to skillfully work with the formative processes of consciousness, resulting from the synergistic integration of mindfulness and contemplation."@en ;
                    rdfs:label "Cognitive Fluency"@en .


###  https://tuos.org/qm#CognitiveInfluence
qm:CognitiveInfluence rdf:type owl:Class ;
                      rdfs:subClassOf qm:DimensionalActivationInfluence ,
                                      qm:DimensionalActivationInfluencesCategory ,
                                      [ rdf:type owl:Restriction ;
                                        owl:onProperty qm:isDeterminedBy ;
                                        owl:someValuesFrom qm:CognitiveAppraisal
                                      ] ,
                                      [ rdf:type owl:Restriction ;
                                        owl:onProperty qm:isModulatedBy ;
                                        owl:someValuesFrom qm:PersonalTendency_CognitiveResponsiveness
                                      ] ,
                                      [ rdf:type owl:Restriction ;
                                        owl:onProperty qm:isDeterminedBy ;
                                        owl:allValuesFrom qm:CognitiveAppraisal
                                      ] ,
                                      [ rdf:type owl:Restriction ;
                                        owl:onProperty qm:isDeterminedBy ;
                                        owl:hasValue qm:CognitiveAppraisal
                                      ] .


###  https://tuos.org/qm#CognitiveMapping
qm:CognitiveMapping rdf:type owl:Class ;
                    rdfs:subClassOf qm:CognitiveStructuringApproaches ;
                    rdfs:label "Cognitive Mapping"@en .


###  https://tuos.org/qm#CognitiveMeasurement
qm:CognitiveMeasurement rdf:type owl:Class ;
                        rdfs:subClassOf qm:CognitiveMechanism ;
                        rdfs:comment "The conscious recognition and apprehension of cognitive states, acting as an active, ontological intervention that leads to the probabilistic collapse of potential interpretations into defined perceptions and experiences."@en ;
                        rdfs:label "Cognitive Measurement"@en .


###  https://tuos.org/qm#CognitiveMechanism
qm:CognitiveMechanism rdf:type owl:Class ;
                      rdfs:subClassOf qm:ProcessingMechanism ;
                      rdfs:comment "Underlying processes or structures that facilitate cognitive functions and states within the Quantum Mindfulness framework."@en ;
                      rdfs:label "Cognitive Mechanism"@en .


###  https://tuos.org/qm#CognitiveModality
qm:CognitiveModality rdf:type owl:Class ;
                     rdfs:subClassOf qm:SecondaryModalityCategory ;
                     rdfs:label "Cognitive Modality"@en .


###  https://tuos.org/qm#CognitiveMultiStateAwareness
qm:CognitiveMultiStateAwareness rdf:type owl:Class ;
                                rdfs:subClassOf qm:CognitiveCapacity .


###  https://tuos.org/qm#CognitiveOptimization
qm:CognitiveOptimization rdf:type owl:Class ;
                         rdfs:subClassOf qm:AdvancedPracticesAndMethodologiesCategory ;
                         rdfs:label "Cognitive Optimization and Refinement"@en .


###  https://tuos.org/qm#CognitiveOptimizationAndRefinement
qm:CognitiveOptimizationAndRefinement rdf:type owl:Class ;
                                      rdfs:subClassOf qm:PracticesCategory ;
                                      rdfs:comment "Practices aimed at enhancing cognitive function, clarity, and efficiency through specific mindful techniques."@en ;
                                      rdfs:label "Cognitive Optimization and Refinement"@en .


###  https://tuos.org/qm#CognitiveOverwhelm
qm:CognitiveOverwhelm rdf:type owl:Class ;
                      rdfs:subClassOf qm:UnresolvedSuperpositionConsequence ;
                      rdfs:label "Cognitive Overwhelm"@en .


###  https://tuos.org/qm#CognitiveProcess
qm:CognitiveProcess rdf:type owl:Class ;
                    rdfs:subClassOf qm:FormalArchitectureCategory ;
                    rdfs:label "Cognitive Process"@en .


###  https://tuos.org/qm#CognitiveResources
qm:CognitiveResources rdf:type owl:Class ;
                      rdfs:subClassOf qm:InfluentialFactor ;
                      rdfs:label "Cognitive Resources"@en .


###  https://tuos.org/qm#CognitiveStrainAndDysfunction
qm:CognitiveStrainAndDysfunction rdf:type owl:Class ;
                                 rdfs:subClassOf qm:ChallengesAndLimitations ,
                                                 qm:ChallengesAndLimitationsCategory ;
                                 rdfs:comment "Issues arising from mental effort or maladaptive cognitive processes in the context of the framework."@en ,
                                              "Mental exhaustion and impaired cognitive function resulting from intense mental demands, information saturation, or internal conflicts."@en ;
                                 rdfs:label "Cognitive Strain and Dysfunction"@en .


###  https://tuos.org/qm#CognitiveStructuringApproaches
qm:CognitiveStructuringApproaches rdf:type owl:Class ;
                                  rdfs:subClassOf qm:CognitiveOptimization ;
                                  rdfs:label "Cognitive Structuring Approaches"@en .


###  https://tuos.org/qm#CognitiveSuperposition
qm:CognitiveSuperposition rdf:type owl:Class ;
                          owl:equivalentClass qm:PerceptualSuperposition ,
                                              qm:ProbabilisticField ;
                          rdfs:subClassOf qm:CoreConceptsCategory ,
                                          [ rdf:type owl:Restriction ;
                                            owl:onProperty qm:composedOf ;
                                            owl:someValuesFrom qm:MentalQuanta
                                          ] ,
                                          [ rdf:type owl:Restriction ;
                                            owl:onProperty qm:enables ;
                                            owl:someValuesFrom qm:MentalFlexibility
                                          ] ,
                                          [ rdf:type owl:Restriction ;
                                            owl:onProperty qm:formsBasisFor ;
                                            owl:someValuesFrom qm:SuperpositionalCognition
                                          ] ,
                                          [ rdf:type owl:Restriction ;
                                            owl:onProperty qm:hasNegativeConsequence ;
                                            owl:someValuesFrom qm:UnresolvedSuperpositionConsequence
                                          ] ,
                                          [ rdf:type owl:Restriction ;
                                            owl:onProperty qm:isCultivatedBy ;
                                            owl:someValuesFrom qm:SuperpositionCultivationMethod
                                          ] ,
                                          [ rdf:type owl:Restriction ;
                                            owl:onProperty qm:isResolvedBy ;
                                            owl:someValuesFrom qm:ConsciousAttention
                                          ] ,
                                          [ rdf:type owl:Restriction ;
                                            owl:onProperty qm:precedes ;
                                            owl:someValuesFrom qm:PsychodynamicCollapse
                                          ] ;
                          rdfs:comment "A foundational pre-conscious state where mental phenomena exist not as fixed entities, but as dynamic probability fields containing multiple simultaneous configurational possibilities. It is characterized by multiplicity, unresolved potential, and ambiguous boundaries, forming the basis for mental flexibility and creative potential."@en ,
                                       "A state where multiple potential thoughts, perceptions, or insights coexist as a dynamic probability field without definite resolution, prior to psychodynamic collapse."@en ,
                                       "The state of potentiality and multiple co-existing possibilities within the cognitive landscape before a 'collapse' into a single perceived reality."@en ;
                          rdfs:label "Cognitive Superposition"@en ;
                          skos:altLabel "Pre-convergence state of potentiality"@en .


###  https://tuos.org/qm#CollapseDysfunction
qm:CollapseDysfunction rdf:type owl:Class ;
                       rdfs:subClassOf qm:PsychologicalDisharmony ;
                       rdfs:label "Collapse Dysfunction"@en .


###  https://tuos.org/qm#CollapseFatigue
qm:CollapseFatigue rdf:type owl:Class ;
                   rdfs:subClassOf qm:CollapseDysfunction ;
                   rdfs:label "Collapse Fatigue"@en .


###  https://tuos.org/qm#CollapseInfluencePractice
qm:CollapseInfluencePractice rdf:type owl:Class ;
                             rdfs:subClassOf qm:CultivationMethod ;
                             rdfs:comment "A practice or technique for consciously and skillfully influencing the psychodynamic collapse process."@en ;
                             rdfs:label "Collapse Influence Practice"@en .


###  https://tuos.org/qm#CollapseMode
qm:CollapseMode rdf:type owl:Class ;
                rdfs:subClassOf qm:CognitiveSuperposition .


###  https://tuos.org/qm#CollapsePointInterventions
qm:CollapsePointInterventions rdf:type owl:Class ;
                              rdfs:subClassOf qm:CognitiveOptimization ;
                              rdfs:label "Collapse Point Interventions"@en .


###  https://tuos.org/qm#ConditioningMechanism
qm:ConditioningMechanism rdf:type owl:Class ;
                         rdfs:subClassOf qm:ExternalInfluence ;
                         rdfs:comment "A psychological or social mechanism that facilitates the formation and embedding of Inherited Scripts."@en ;
                         rdfs:label "Conditioning Mechanism"@en .


###  https://tuos.org/qm#ConfirmationBiasCycle
qm:ConfirmationBiasCycle rdf:type owl:Class ;
                         rdfs:subClassOf qm:ConditioningMechanism ;
                         rdfs:label "Confirmation Bias and Reality Construction Cycle"@en .


###  https://tuos.org/qm#ConsciousAttention
qm:ConsciousAttention rdf:type owl:Class ;
                      rdfs:subClassOf qm:PracticesCategory ;
                      rdfs:comment "The catalyst that triggers psychodynamic collapse, resolving a probability field of multiple potential states into a single definite experience."@en ;
                      rdfs:label "Conscious Attention"@en ;
                      skos:altLabel "Catalyst"@en ,
                                    "Collapse Vector"@en ,
                                    "Cognitive Measurement" ,
                                    "Collapse Vector" ,
                                    "Conscious Observation" ,
                                    "Focused Attention" .


###  https://tuos.org/qm#ConsciousAwareness
qm:ConsciousAwareness rdf:type owl:Class ;
                      rdfs:subClassOf qm:AdvancedPracticesAndMethodologiesCategory ;
                      rdfs:comment "The operational foundation of conscious awareness and individual character, which the dimensions collectively form."@en ;
                      rdfs:label "Conscious Awareness"@en .


###  https://tuos.org/qm#ConsciousObservation
qm:ConsciousObservation rdf:type owl:Class ;
                        rdfs:subClassOf qm:AdvancedPracticesAndMethodologiesCategory ,
                                        [ rdf:type owl:Restriction ;
                                          owl:onProperty qm:initiates ;
                                          owl:someValuesFrom qm:PsychodynamicCollapse
                                        ] ,
                                        [ rdf:type owl:Restriction ;
                                          owl:onProperty qm:modifies ;
                                          owl:someValuesFrom qm:MentalState
                                        ] ,
                                        [ rdf:type owl:Restriction ;
                                          owl:onProperty qm:shapes ;
                                          owl:someValuesFrom qm:ExperiencedReality
                                        ] ;
                        rdfs:comment "The act of bringing awareness to any mental state, which is not neutral but is a creative intervention that inherently modifies both the state and the broader field of consciousness."@en ;
                        rdfs:label "Conscious Observation"@en .


###  https://tuos.org/qm#ConsciousRealityConstruction
qm:ConsciousRealityConstruction rdf:type owl:Class ;
                                rdfs:subClassOf qm:MainStrategiesCategory ,
                                                [ rdf:type owl:Restriction ;
                                                  owl:onProperty qm:hasPractice ;
                                                  owl:someValuesFrom qm:PerceptualFraming
                                                ] ;
                                rdfs:comment "A deliberate, systematic process of shaping one's perceived reality through intentional cognitive and perceptual strategies, based on the principle that perception is an active, constitutive force."@en ;
                                rdfs:label "Conscious Reality Construction"@en .


###  https://tuos.org/qm#ConsciousRealityCreation
qm:ConsciousRealityCreation rdf:type owl:Class ;
                            rdfs:subClassOf qm:CollapseInfluencePractice ;
                            rdfs:label "Conscious Reality Creation / Perceptual Reframing"@en .


###  https://tuos.org/qm#ConsciousStack
qm:ConsciousStack rdf:type owl:Class ;
                  rdfs:subClassOf qm:PrimeModality ;
                  rdfs:comment "That segment of psychological functioning directly accessible to mindful observation and conscious intervention, acting as the interface between unconscious processing and explicit awareness. It is co-extensive with the Prime Modality."@en ;
                  rdfs:label "Conscious Stack"@en .


###  https://tuos.org/qm#ConsciousStateManagement
qm:ConsciousStateManagement rdf:type owl:Class ;
                            rdfs:subClassOf qm:CognitiveOptimization ;
                            rdfs:label "Conscious State Management"@en .


###  https://tuos.org/qm#ConsciousnessFortification
qm:ConsciousnessFortification rdf:type owl:Class ;
                              rdfs:subClassOf qm:PracticesCategory ;
                              rdfs:label "Consciousness Fortification"@en .


###  https://tuos.org/qm#ConsciousnessRefinement
qm:ConsciousnessRefinement rdf:type owl:Class ;
                           rdfs:subClassOf qm:MainStrategiesCategory ,
                                           [ rdf:type owl:Restriction ;
                                             owl:onProperty qm:hasPractice ;
                                             owl:someValuesFrom qm:ContemplativeInquiry
                                           ] ;
                           rdfs:comment "A sophisticated approach to self-regulation and psychological development enabled by understanding dimensional dynamics."@en ,
                                        "Practices specifically designed for skillfully working with and refining the Psychodynamic Dimensions, with the aim of fostering personal growth and holistic well-being."@en ;
                           rdfs:label "Consciousness Refinement"@en .


###  https://tuos.org/qm#ConsciousnessWaveFunction
qm:ConsciousnessWaveFunction rdf:type owl:Class ;
                             rdfs:subClassOf qm:CognitiveSuperposition ;
                             rdfs:comment "The conceptual space or field within which Cognitive Superposition exists."@en ;
                             rdfs:label "Consciousness Wave Function"@en ;
                             skos:altLabel "Mental Wave Function"@en .


###  https://tuos.org/qm#ConsensusReality
qm:ConsensusReality rdf:type owl:Class ;
                    rdfs:subClassOf qm:SharedReality .


###  https://tuos.org/qm#ConstructedReality
qm:ConstructedReality rdf:type owl:Class ;
                      rdfs:subClassOf qm:ExperiencedReality ,
                                      [ rdf:type owl:Restriction ;
                                        owl:onProperty qm:hasConstraint ;
                                        owl:someValuesFrom qm:BonesOfReality
                                      ] ;
                      rdfs:comment "The understanding that perception is an active, constructive process that shapes the reality an individual experiences, rather than a passive reception of objective reality."@en ;
                      rdfs:label "Constructed Reality"@en .


###  https://tuos.org/qm#ConstructiveInterference
qm:ConstructiveInterference rdf:type owl:Class ;
                            rdfs:subClassOf qm:InterferencePatterns ;
                            rdfs:comment "When dimensions align harmoniously, amplifying each other’s positive qualities and leading to states of flow and fulfillment."@en ;
                            rdfs:label "Constructive Interference"@en .


###  https://tuos.org/qm#Contemplation
qm:Contemplation rdf:type owl:Class ;
                 rdfs:subClassOf qm:PracticesCategory ,
                                 [ rdf:type owl:Restriction ;
                                   owl:onProperty qm:develops ;
                                   owl:someValuesFrom qm:CognitiveFluency
                                 ] ,
                                 [ rdf:type owl:Restriction ;
                                   owl:onProperty qm:differsFrom ;
                                   owl:someValuesFrom qm:ClassicalMindfulness
                                 ] ,
                                 [ rdf:type owl:Restriction ;
                                   owl:onProperty qm:employs ;
                                   owl:someValuesFrom qm:PsychoMeditativeStructuring
                                 ] ,
                                 [ rdf:type owl:Restriction ;
                                   owl:onProperty qm:isEngineOf ;
                                   owl:someValuesFrom qm:PsychoMeditativeCollapse
                                 ] ,
                                 [ rdf:type owl:Restriction ;
                                   owl:onProperty qm:leadsTo ;
                                   owl:someValuesFrom qm:StructuredUnderstanding
                                 ] ,
                                 [ rdf:type owl:Restriction ;
                                   owl:onProperty qm:mapsDirectlyTo ;
                                   owl:hasValue qm:Pd3
                                 ] .


###  https://tuos.org/qm#ContemplativeExperimentation
qm:ContemplativeExperimentation rdf:type owl:Class ;
                                rdfs:subClassOf qm:PracticesCategory ;
                                rdfs:comment "The practice of designing specific behavioral experiments to test and refine understanding through practical application, bridging inner understanding with manifest reality."@en ;
                                rdfs:label "Contemplative Experimentation"@en .


###  https://tuos.org/qm#ContemplativeInquiry
qm:ContemplativeInquiry rdf:type owl:Class ;
                        rdfs:subClassOf qm:AdvancedPracticesAndMethodologiesCategory ;
                        rdfs:label "Contemplative Inquiry"@en .


###  https://tuos.org/qm#ContinuousMentationModel
qm:ContinuousMentationModel rdf:type owl:Class ;
                            rdfs:subClassOf qm:QuantumPrinciple ;
                            rdfs:comment "Traditional models that conceptualize mentation as a continuous or undifferentiated phenomenon, which the QM_Quantum principle contrasts with."@en ;
                            rdfs:label "Continuous Mentation Model"@en .


###  https://tuos.org/qm#CoreConceptsCategory
qm:CoreConceptsCategory rdf:type owl:Class ;
                        rdfs:comment "A conceptual grouping for fundamental ideas within the Quantum Mindfulness framework."@en ,
                                     "A new main class for foundational concepts within the Quantum Mindfulness framework."@en ;
                        rdfs:label "Core Concept"@en ,
                                   "Core Concepts"@en .


###  https://tuos.org/qm#CraftsmanshipOfCollapse
qm:CraftsmanshipOfCollapse rdf:type owl:Class ;
                           rdfs:subClassOf qm:CollapseInfluencePractice ;
                           rdfs:label "Craftsmanship of Collapse"@en .


###  https://tuos.org/qm#CreativeGenesis
qm:CreativeGenesis rdf:type owl:Class ;
                   rdfs:subClassOf qm:Phenomenon .


###  https://tuos.org/qm#CreativeParalysis
qm:CreativeParalysis rdf:type owl:Class ;
                     rdfs:subClassOf qm:CognitiveStrainAndDysfunction ;
                     rdfs:label "Creative Paralysis"@en .


###  https://tuos.org/qm#CreativePotential
qm:CreativePotential rdf:type owl:Class ;
                     rdfs:subClassOf qm:CognitiveCapacity ;
                     rdfs:label "Creative Potential"@en .


###  https://tuos.org/qm#CultivationMethod
qm:CultivationMethod rdf:type owl:Class ;
                     rdfs:subClassOf qm:PsychodynamicWaveCollapse ;
                     rdfs:comment "Mindfulness-based practices designed to develop and strengthen psychodynamic capacities."@en ;
                     rdfs:label "Cultivation Method"@en .


###  https://tuos.org/qm#CulturalNarrative
qm:CulturalNarrative rdf:type owl:Class ;
                     rdfs:subClassOf qm:SecondhandExperience ;
                     rdfs:comment "The broadest category of secondhand experience, encompassing shared stories, symbols, and interpretive frameworks that define cultural identity."@en ;
                     rdfs:label "Cultural Narrative"@en .


###  https://tuos.org/qm#DecisionArchitecture
qm:DecisionArchitecture rdf:type owl:Class ;
                        rdfs:subClassOf qm:CognitiveOptimization ;
                        rdfs:label "Decision Architecture"@en .


###  https://tuos.org/qm#DecoherenceBacklog
qm:DecoherenceBacklog rdf:type owl:Class ;
                      rdfs:subClassOf qm:CognitiveStrainAndDysfunction ,
                                      qm:UnresolvedSuperpositionConsequence .


###  https://tuos.org/qm#DecouplingPhase
qm:DecouplingPhase rdf:type owl:Class ;
                   rdfs:subClassOf qm:LiberationProcess .


###  https://tuos.org/qm#DeepPsychologicalTrauma
qm:DeepPsychologicalTrauma rdf:type owl:Class ;
                           rdfs:subClassOf qm:Phenomenon ;
                           rdfs:label "Deep Psychological Trauma"@en .


###  https://tuos.org/qm#DestructiveInterference
qm:DestructiveInterference rdf:type owl:Class ;
                           rdfs:subClassOf qm:InterferencePatterns ;
                           rdfs:comment "When dimensions conflict or compete, diminishing possibilities or creating internal conflict and decision paralysis."@en ;
                           rdfs:label "Destructive Interference"@en .


###  https://tuos.org/qm#DevelopmentalInterferencePattern
qm:DevelopmentalInterferencePattern rdf:type owl:Class ;
                                    rdfs:subClassOf qm:DestructiveInterference ;
                                    rdfs:comment "The disruptive effect of an Inherited Script on the natural unfolding of an individual's potential."@en ;
                                    rdfs:label "Developmental Interference Pattern"@en .


###  https://tuos.org/qm#DimensionalActivation
qm:DimensionalActivation rdf:type owl:Class ;
                         rdfs:subClassOf qm:CognitiveMechanism ,
                                         qm:FormalArchitectureCategory ,
                                         [ rdf:type owl:Restriction ;
                                           owl:onProperty qm:composedOf ;
                                           owl:someValuesFrom qm:DimensionalActivationInfluence
                                         ] ,
                                         [ rdf:type owl:Restriction ;
                                           owl:onProperty qm:isDeterminedBy ;
                                           owl:someValuesFrom qm:CognitiveAppraisal
                                         ] ,
                                         [ rdf:type owl:Restriction ;
                                           owl:onProperty qm:isDeterminedBy ;
                                           owl:someValuesFrom qm:DimensionalActivationInfluence
                                         ] ,
                                         [ rdf:type owl:Restriction ;
                                           owl:onProperty qm:isDeterminedBy ;
                                           owl:someValuesFrom qm:Observation
                                         ] ,
                                         [ rdf:type owl:Restriction ;
                                           owl:onProperty qm:isInputTo ;
                                           owl:someValuesFrom qm:ActualizationProcess
                                         ] ,
                                         [ rdf:type owl:Restriction ;
                                           owl:onProperty qm:isInputTo ;
                                           owl:allValuesFrom qm:ActualizationProcess
                                         ] ;
                         rdfs:comment "The 'Heart of the Collapse'. It is the calculated activation level for each psychodynamic dimension (Kj), representing its 'raw potential' or 'charge' to contribute to the emergent Mental State. It is the sum of five distinct contributing influences."@en ,
                                      "The 'Heart of the Collapse'. It is the calculated activation level for each psychodynamic dimension, representing its 'raw potential' or 'charge' to contribute to the emergent Mental State. It is the sum of five distinct contributing influences."@en ,
                                      "The calculated collapse activation level for each psychodynamic dimension (Kj), representing its raw potential to contribute to the emergent Mental State. It is the sum of five distinct contributing influences."@en ;
                         rdfs:label "Dimensional Activation (Kj)"@en ,
                                    "Dimensional Activation (Kj)" ;
                         rdfs:subClassOf "Psychodynamic Model"@en .


###  https://tuos.org/qm#DimensionalActivationInfluence
qm:DimensionalActivationInfluence rdf:type owl:Class ;
                                  rdfs:subClassOf qm:DimensionalActivationInfluencesCategory ;
                                  rdfs:comment "A distinct contributing influence that determines the total activation (Kj) for a single dimension."@en ;
                                  rdfs:label "Dimensional Activation Influence"@en .


###  https://tuos.org/qm#DimensionalActivationInfluencesCategory
qm:DimensionalActivationInfluencesCategory rdf:type owl:Class ;
                                           rdfs:subClassOf qm:FormalArchitectureCategory ;
                                           rdfs:comment "Conceptual container for the influences contributing to Dimensional Activation."@en ;
                                           rdfs:label "Influences (Kj = I_Sj + I_Cj + I_Tj + I_Ψj + εj)"@en .


###  https://tuos.org/qm#DimensionalAttunement
qm:DimensionalAttunement rdf:type owl:Class ;
                         rdfs:subClassOf qm:CollapseInfluencePractice ,
                                         qm:PracticesCategory ;
                         rdfs:comment "A sophisticated capacity to 'read and work with the subtle energies of consciousness' by recognizing which dimensions are active, suppressed, or imbalanced."@en ;
                         rdfs:label "Dimensional Attunement"@en .


###  https://tuos.org/qm#DimensionalCrystallization
qm:DimensionalCrystallization rdf:type owl:Class ;
                              rdfs:subClassOf qm:PsychodynamicWaveCollapse ;
                              rdfs:comment "The process by which potential psychological states, existing as dynamic probability fields, consolidate into actual experience and observable behavior."@en ;
                              rdfs:label "Dimensional Crystallization"@en .


###  https://tuos.org/qm#DimensionalLiteracy
qm:DimensionalLiteracy rdf:type owl:Class ;
                       rdfs:subClassOf qm:CognitiveCapacity .


###  https://tuos.org/qm#DimensionalMisalignment
qm:DimensionalMisalignment rdf:type owl:Class ;
                           rdfs:subClassOf qm:PsychologicalDysfunctionAndImbalance ;
                           rdfs:label "Dimensional Misalignment"@en .


###  https://tuos.org/qm#DirectedFocus
qm:DirectedFocus rdf:type owl:Class ;
                 rdfs:subClassOf qm:Observation ,
                                 qm:ObservationComponentsCategory ;
                 rdfs:comment "Directed cognitive engagement or the specific allocation of attentional resources onto a particular stimulus; a key aspect of 'volitional awareness'."@en ,
                              "Represents directed cognitive engagement or the specific allocation of attentional resources onto a particular stimulus. It is a key aspect of 'volitional awareness'."@en ;
                 rdfs:label "Directed Cognitive Engagement (f)"@en ,
                            "Directed Cognitive Engagement (f)" .


###  https://tuos.org/qm#DissociativeState
qm:DissociativeState rdf:type owl:Class ;
                     rdfs:subClassOf qm:CognitiveAnchoringFailureConsequence ;
                     rdfs:comment "Detachment from thoughts, emotions, actions, or sense of self, leading to fragmented consciousness due to the loss of stable intentional direction."@en ;
                     rdfs:label "Dissociative State"@en .


###  https://tuos.org/qm#DynamicInterconnectedNetwork
qm:DynamicInterconnectedNetwork rdf:type owl:Class ;
                                rdfs:subClassOf qm:OtherKeyConcepts ;
                                rdfs:comment "The conceptualization of the ten Psychodynamic Dimensions as a unified psychological whole, where each dimension perpetually influences and is influenced by all others, creating the multifaceted tapestry of experience."@en ;
                                rdfs:label "Dynamic and Interconnected Network"@en .


###  https://tuos.org/qm#DysfunctionalPattern
qm:DysfunctionalPattern rdf:type owl:Class ;
                        rdfs:subClassOf qm:ChallengesAndLimitationsCategory ;
                        rdfs:comment "A distorted or imbalanced expression of a psychodynamic dimension."@en ;
                        rdfs:label "Dysfunctional Pattern"@en .


###  https://tuos.org/qm#EmbodiedMindfulness
qm:EmbodiedMindfulness rdf:type owl:Class ;
                       rdfs:subClassOf qm:PracticesCategory ;
                       rdfs:comment "The extension of the Quantum Mindfulness framework to the physical body, viewing body language as an observable manifestation of internal psychodynamic processes."@en ;
                       rdfs:label "Embodied Mindfulness"@en .


###  https://tuos.org/qm#EmergentPropertiesCategory
qm:EmergentPropertiesCategory rdf:type owl:Class ;
                              rdfs:comment "Properties or phenomena that arise from the interaction of components within the psychodynamic system, not reducible to individual parts."@en ;
                              rdfs:label "Emergent Properties"@en .


###  https://tuos.org/qm#EmotionalCollapseSculpting
qm:EmotionalCollapseSculpting rdf:type owl:Class ;
                              rdfs:subClassOf qm:PracticesCategory ;
                              rdfs:label "Emotional Collapse Sculpting"@en .


###  https://tuos.org/qm#EmotionalCreativity
qm:EmotionalCreativity rdf:type owl:Class ;
                       rdfs:subClassOf qm:Phenomenon ;
                       rdfs:comment "An enhanced capacity for navigating complex emotional terrain, fostered by the Psycho-Aesthetic Dimension."@en ;
                       rdfs:label "Emotional Creativity"@en .


###  https://tuos.org/qm#EmotionalOpenness
qm:EmotionalOpenness rdf:type owl:Class ;
                     rdfs:subClassOf qm:Phenomenon ;
                     rdfs:comment "A fundamental orientation toward receiving and processing affective information without immediate defensive filtering."@en ;
                     rdfs:label "Emotional Openness"@en .


###  https://tuos.org/qm#EmotionalQuantumEntanglement
qm:EmotionalQuantumEntanglement rdf:type owl:Class ;
                                rdfs:subClassOf qm:PsychodynamicWaveCollapse ;
                                rdfs:comment "The persistent interconnectedness of mental and emotional states between individuals, operating at sub-perceptual levels."@en ;
                                rdfs:label "Emotional Quantum Entanglement"@en .


###  https://tuos.org/qm#EmotionalReactivityPattern
qm:EmotionalReactivityPattern rdf:type owl:Class ;
                              rdfs:subClassOf qm:SubconsciousInfrastructure ;
                              rdfs:comment "Psychological templates that automatically influence how individuals interpret and respond to stimuli, particularly in interpersonal contexts."@en ;
                              rdfs:label "Emotional Reactivity Pattern"@en .


###  https://tuos.org/qm#EmotionalRegulation
qm:EmotionalRegulation rdf:type owl:Class ;
                       rdfs:subClassOf qm:CognitiveAnchoringComponent ;
                       rdfs:comment "The capacity to manage the emotional landscape to support and stabilize intentional commitment."@en ;
                       rdfs:label "Emotional Regulation / Affective Modulation"@en .


###  https://tuos.org/qm#EmotionalResponse
qm:EmotionalResponse rdf:type owl:Class ;
                     rdfs:subClassOf qm:PsychologicalPhenomenon ,
                                     [ rdf:type owl:Restriction ;
                                       owl:onProperty qm:isRegulatedBy ;
                                       owl:someValuesFrom qm:PsychoAestheticDimension
                                     ] ,
                                     [ rdf:type owl:Restriction ;
                                       owl:onProperty qm:isRegulatedBy ;
                                       owl:someValuesFrom qm:PsychoProtectiveDimension
                                     ] .


###  https://tuos.org/qm#EmotionalRewilding
qm:EmotionalRewilding rdf:type owl:Class ;
                      rdfs:subClassOf qm:PracticesCategory ;
                      rdfs:label "Emotional Rewilding"@en .


###  https://tuos.org/qm#EmotionalStormTheory
qm:EmotionalStormTheory rdf:type owl:Class ;
                        rdfs:subClassOf qm:CollapseDysfunction ;
                        rdfs:label "Emotional Storm Theory"@en .


###  https://tuos.org/qm#EmpiricalAbsence
qm:EmpiricalAbsence rdf:type owl:Class ;
                    rdfs:subClassOf qm:CoreConceptsCategory ,
                                    [ rdf:type owl:Restriction ;
                                      owl:onProperty qm:isConfirmedBy ;
                                      owl:someValuesFrom qm:ObservableEffect
                                    ] ;
                    rdfs:comment "A concept referring to aspects of reality or experience that are beyond direct empirical observation but are inferred to exist or influence the system."@en ,
                                 "The principle that certain dimensions of reality are fundamentally inaccessible to direct empirical verification, yet their existence is confirmed by their effects and systematic patterns of manifestation. This inaccessibility itself functions as positive knowledge."@en ;
                    rdfs:label "Empirical Absence"@en .


###  https://tuos.org/qm#EngagementStyle
qm:EngagementStyle rdf:type owl:Class ;
                   rdfs:subClassOf qm:AdvancedPracticesAndMethodologiesCategory ;
                   rdfs:label "Engagement Style"@en .


###  https://tuos.org/qm#EnhancedDecisionMaking
qm:EnhancedDecisionMaking rdf:type owl:Class ;
                          rdfs:subClassOf qm:GoalsCategory ;
                          rdfs:comment "A practical application of Vectorized Awareness, enabling comprehensive exploration of a decision field and alignment with deeper intentions."@en ;
                          rdfs:label "Enhanced Decision-Making"@en .


###  https://tuos.org/qm#EnvironmentalInfluence
qm:EnvironmentalInfluence rdf:type owl:Class ;
                          rdfs:subClassOf qm:InfluentialFactor ;
                          rdfs:label "Environmental Influence"@en .


###  https://tuos.org/qm#EnvironmentalResonance
qm:EnvironmentalResonance rdf:type owl:Class ;
                          rdfs:subClassOf qm:CognitiveAnchoringComponent ;
                          rdfs:comment "The degree to which external conditions (physical, social, cultural) align with and reinforce an individual's anchored intention."@en ;
                          rdfs:label "Environmental Resonance"@en .


###  https://tuos.org/qm#EpistemologicalChallenges
qm:EpistemologicalChallenges rdf:type owl:Class ;
                             rdfs:subClassOf qm:ChallengesAndLimitations ,
                                             qm:ChallengesAndLimitationsCategory ,
                                             [ rdf:type owl:Restriction ;
                                               owl:onProperty qm:impliesNeedFor ;
                                               owl:someValuesFrom qm:InferentialEpistemology
                                             ] ;
                             rdfs:comment "Difficulties in acquiring, validating, or understanding knowledge, particularly concerning subjective or unobservable phenomena that are intrinsically inaccessible to conventional empirical methods."@en ,
                                          "Difficulties related to the nature of knowledge, justification, and belief within the framework."@en ;
                             rdfs:label "Epistemological Challenges"@en .


###  https://tuos.org/qm#EpistemologicalDiscernment
qm:EpistemologicalDiscernment rdf:type owl:Class ;
                              rdfs:subClassOf qm:CognitiveCapacity ;
                              rdfs:comment "The crucial cognitive skill of distinguishing between different types of secondhand information, evaluating source reliability, and integrating valuable insights while maintaining cognitive sovereignty."@en ;
                              rdfs:label "Epistemological Discernment"@en .


###  https://tuos.org/qm#EthicalBoundaries
qm:EthicalBoundaries rdf:type owl:Class ;
                     rdfs:subClassOf qm:PracticalLimitationsOfQMApplication .


###  https://tuos.org/qm#Examples_Emergent
qm:Examples_Emergent rdf:type owl:Class ;
                     rdfs:subClassOf qm:EmergentPropertiesCategory ;
                     rdfs:comment "Specific instances or manifestations of emergent properties."@en ;
                     rdfs:label "Examples"@en .


###  https://tuos.org/qm#ExecutiveFunctionTraining
qm:ExecutiveFunctionTraining rdf:type owl:Class ;
                             rdfs:subClassOf qm:CognitiveOptimization ;
                             rdfs:label "Executive Function Training"@en .


###  https://tuos.org/qm#ExistentialDissonance
qm:ExistentialDissonance rdf:type owl:Class ;
                         rdfs:subClassOf qm:PsychologicalDysfunctionAndImbalance ;
                         rdfs:label "Existential Dissonance"@en .


###  https://tuos.org/qm#ExperiencedReality
qm:ExperiencedReality rdf:type owl:Class ;
                      rdfs:subClassOf qm:Perception ;
                      rdfs:comment "The subjective world as it is lived and perceived by an individual, understood as a malleable manifestation of potential states co-created by perceptual engagement."@en ;
                      rdfs:label "Experienced Reality"@en .


###  https://tuos.org/qm#ExperientialLimit
qm:ExperientialLimit rdf:type owl:Class ;
                     rdfs:subClassOf qm:Phenomenon ;
                     rdfs:label "Experiential Limit"@en .


###  https://tuos.org/qm#ExternalInfluence
qm:ExternalInfluence rdf:type owl:Class ;
                     rdfs:subClassOf qm:CoreConceptsCategory ;
                     rdfs:comment "A distinct category of external source that contributes to the formation of Inherited Scripts."@en ;
                     rdfs:label "External Influence"@en .


###  https://tuos.org/qm#FinalIntensity
qm:FinalIntensity rdf:type owl:Class ;
                  rdfs:subClassOf qm:ActualizationProcess ,
                                  qm:FormalArchitectureCategory ,
                                  [ rdf:type owl:Restriction ;
                                    owl:onProperty qm:isOutputOf ;
                                    owl:allValuesFrom qm:ActualizationProcess
                                  ] ,
                                  [ rdf:type owl:Restriction ;
                                    owl:onProperty qm:isTransformedUsing ;
                                    owl:hasValue qm:SigmoidFunction
                                  ] ;
                  rdfs:comment "The scaled and transformed value (between 0 and 1) of a Psychodynamic Dimension's raw activation (Kj), representing its actualized contribution to the conscious experience. Calculated as xj = 1 / (1 + e^-Kj)."@en ,
                               "The scaled and transformed value (between 0 and 1) of a Psychodynamic Dimension's raw activation (Kj), representing its actualized contribution to the conscious experience. It is calculated for each dimension j using the sigmoid function: xj = 1 / (1 + e^-Kj)."@en ;
                  rdfs:label "Final Intensity (xj)"@en ,
                             "Final Intensity (xj)" ;
                  rdfs:subClassOf "Psychodynamic Model"@en .


###  https://tuos.org/qm#FlowDynamicsInConsciousness
qm:FlowDynamicsInConsciousness rdf:type owl:Class ;
                               rdfs:subClassOf qm:QuantumPrinciple ;
                               rdfs:comment "The understanding of how mental states arise, evolve, and dissolve as energetic flows, providing insight into the temporal dimensions of psychological experience."@en ;
                               rdfs:label "Flow Dynamics in Consciousness"@en .


###  https://tuos.org/qm#FormalArchitectureCategory
qm:FormalArchitectureCategory rdf:type owl:Class ;
                              rdfs:subClassOf qm:FormalArchitectureCategory ;
                              rdfs:comment "A conceptual grouping for the formal, structured model of psychodynamic processes."@en ,
                                           "A parameter within the formal architectural model of psychodynamic states."@en ;
                              rdfs:label "Formal Architectural Parameter"@en ,
                                         "Formal Architecture"@en .


###  https://tuos.org/qm#FormalTestimony
qm:FormalTestimony rdf:type owl:Class ;
                   rdfs:subClassOf qm:SecondhandExperience ;
                   rdfs:comment "The most explicit form of secondhand experience, encompassing deliberate knowledge transfer such as academic instruction, expert consultation, and curated sources."@en ;
                   rdfs:label "Formal Testimony"@en .


###  https://tuos.org/qm#FrameworkPrinciple
qm:FrameworkPrinciple rdf:type owl:Class ;
                      rdfs:subClassOf qm:CoreConceptsCategory ,
                                      qm:FrameworkPrinciplesCategory ;
                      rdfs:comment "A meta-level principle that defines the nature or foundational philosophy of the Quantum Mindfulness framework."@en ;
                      rdfs:label "Framework Principle"@en ,
                                 "X. Framework Principle"@en .


###  https://tuos.org/qm#FrameworkPrinciplesCategory
qm:FrameworkPrinciplesCategory rdf:type owl:Class ;
                               rdfs:comment "Fundamental tenets or guiding rules of the Quantum Mindfulness framework."@en ;
                               rdfs:label "Framework Principles"@en .


###  https://tuos.org/qm#FreeWill
qm:FreeWill rdf:type owl:Class ;
            rdfs:subClassOf qm:PsychoVolitionalDimension ,
                            [ rdf:type owl:Restriction ;
                              owl:onProperty qm:isSourceOf ;
                              owl:hasValue qm:Pd1
                            ] ;
            rdfs:comment "The capacity to exercise meaningful agency by developing awareness of influences on collapse patterns and choosing different collapse directions in future situations. Its irreducible source is the Psycho-Volitional Dimension."@en ;
            rdfs:label "Free Will"@en .


###  https://tuos.org/qm#FundamentalEnergeticSubstrate
qm:FundamentalEnergeticSubstrate rdf:type owl:Class ;
                                 rdfs:subClassOf qm:QuantumPrinciple ;
                                 rdfs:comment "The nature of a Psychodynamic Dimension as a dynamic, generative force that actively participates in the ongoing creation of conscious experience."@en ;
                                 rdfs:label "Fundamental Energetic Substrate"@en .


###  https://tuos.org/qm#GeneralAwareness
qm:GeneralAwareness rdf:type owl:Class ;
                    rdfs:subClassOf qm:Observation ,
                                    qm:ObservationComponentsCategory ;
                    rdfs:comment "Represents the raw availability of general awareness or the overall capacity for conscious processing at a given moment, reflecting the mind's general receptivity to any incoming information."@en ,
                                 "The raw availability of general awareness or the overall capacity for conscious processing at a given moment."@en ;
                    rdfs:label "General Awareness (A)"@en ,
                               "General Awareness (A)" .


###  https://tuos.org/qm#GeometricDimensionsOfAwareness
qm:GeometricDimensionsOfAwareness rdf:type owl:Class ;
                                  rdfs:subClassOf qm:AdvancedPracticesAndMethodologiesCategory ;
                                  rdfs:comment "The recognition of spatial and relational qualities of psychological phenomena, such as their locations, boundaries, densities, and orientations within the field of consciousness."@en ;
                                  rdfs:label "Geometric Dimensions of Awareness"@en .


###  https://tuos.org/qm#GoalAbandonment
qm:GoalAbandonment rdf:type owl:Class ;
                   rdfs:subClassOf qm:CognitiveAnchoringFailureConsequence ;
                   rdfs:comment "The dissipation of sustained focus and effort due to the inability to consistently stabilize the underlying intention for a goal."@en ;
                   rdfs:label "Goal Abandonment"@en .


###  https://tuos.org/qm#GoalsCategory
qm:GoalsCategory rdf:type owl:Class ;
                 rdfs:subClassOf qm:AdvancedPracticesAndMethodologiesCategory ;
                 rdfs:comment "Desired outcomes or objectives of applying Quantum Mindfulness principles and practices."@en ;
                 rdfs:label "Goals"@en .


###  https://tuos.org/qm#GroundingFunction
qm:GroundingFunction rdf:type owl:Class ;
                     rdfs:subClassOf qm:Perception ;
                     rdfs:comment "A psychological anchor that prevents individuals from becoming lost in abstract speculation and ensures sustained engagement with reality."@en ;
                     rdfs:label "Grounding Function"@en .


###  https://tuos.org/qm#HistoricalImprint
qm:HistoricalImprint rdf:type owl:Class ;
                     rdfs:subClassOf qm:InfluentialFactor ;
                     rdfs:label "Historical Imprint / Trauma Imprint"@en .


###  https://tuos.org/qm#HumanCapacitiesCategory
qm:HumanCapacitiesCategory rdf:type owl:Class ;
                           rdfs:comment "Inherent abilities or potentials of human consciousness relevant to the framework."@en ;
                           rdfs:label "Human Capacities"@en .


###  https://tuos.org/qm#HumorAsCognitiveTechnology
qm:HumorAsCognitiveTechnology rdf:type owl:Class ;
                              rdfs:subClassOf qm:IntegratedTherapeuticApproaches .


###  https://tuos.org/qm#Identity
qm:Identity rdf:type owl:Class ;
            rdfs:subClassOf qm:Perception ;
            rdfs:comment "A dynamic construct formed by the sum and pattern of perceptions, beliefs, and self-concepts repeatedly solidified through Psychodynamic Collapse over time."@en ;
            rdfs:label "Identity"@en .


###  https://tuos.org/qm#IdentityTransformationProcess
qm:IdentityTransformationProcess rdf:type owl:Class ;
                                 rdfs:subClassOf qm:PracticesCategory ;
                                 rdfs:label "Identity Transformation Process"@en .


###  https://tuos.org/qm#ImpactOfTheNow
qm:ImpactOfTheNow rdf:type owl:Class ;
                  rdfs:subClassOf qm:CognitiveAppraisalComponent ,
                                  qm:CognitiveAppraisalComponentsCategory ,
                                  [ rdf:type owl:Restriction ;
                                    owl:onProperty qm:isModulatedBy ;
                                    owl:someValuesFrom qm:PersonalTendency_Reactivity
                                  ] ,
                                  [ rdf:type owl:Restriction ;
                                    owl:onProperty qm:isDeterminedBy ;
                                    owl:allValuesFrom qm:ObservationValence
                                  ] ,
                                  [ rdf:type owl:Restriction ;
                                    owl:onProperty qm:isModulatedBy ;
                                    owl:allValuesFrom qm:PersonalTendency_Reactivity
                                  ] ,
                                  [ rdf:type owl:Restriction ;
                                    owl:onProperty qm:composedOf ;
                                    owl:hasValue qm:ObservationValence
                                  ] ;
                  rdfs:comment "The component of Cognitive Appraisal representing the perceived emotional quality of the current observation (Valence(Ψ)), modulated by an individual's reactivity to new events (wΨ)."@en ,
                               "The component representing the perceived emotional quality of the current observation (Valence(Ψ)), modulated by an individual's reactivity to new events (wΨ)."@en ;
                  rdfs:label "Impact of the Now"@en ,
                             "Impact of the Now" .


###  https://tuos.org/qm#ImposterSyndrome
qm:ImposterSyndrome rdf:type owl:Class ;
                    rdfs:subClassOf qm:PsychologicalDysfunctionAndImbalance .


###  https://tuos.org/qm#ImpulseReactivity
qm:ImpulseReactivity rdf:type owl:Class ;
                     rdfs:subClassOf qm:CognitiveAnchoringFailureConsequence ;
                     rdfs:comment "Behavior driven by immediate stimuli or emotional reactions rather than considered intentions, due to a weakened capacity for thoughtful deliberation."@en ;
                     rdfs:label "Impulse Reactivity"@en .


###  https://tuos.org/qm#ImpulseTowardGenerativeSharing
qm:ImpulseTowardGenerativeSharing rdf:type owl:Class ;
                                  rdfs:subClassOf qm:Phenomenon ;
                                  rdfs:comment "An inherent drive to give, connect, and contribute to others' well-being, arising from a recognition of interconnectedness."@en ;
                                  rdfs:label "Impulse Toward Generative Sharing"@en .


###  https://tuos.org/qm#IncompleteProcessTension
qm:IncompleteProcessTension rdf:type owl:Class ;
                            rdfs:subClassOf qm:UnresolvedSuperpositionConsequence ;
                            rdfs:label "Incomplete Process Tension"@en .


###  https://tuos.org/qm#InertiaOfThePast
qm:InertiaOfThePast rdf:type owl:Class ;
                    rdfs:subClassOf qm:CognitiveAppraisalComponent ,
                                    qm:CognitiveAppraisalComponentsCategory ,
                                    [ rdf:type owl:Restriction ;
                                      owl:onProperty qm:composedOf ;
                                      owl:someValuesFrom qm:AverageValenceOfPriorState
                                    ] ,
                                    [ rdf:type owl:Restriction ;
                                      owl:onProperty qm:isModulatedBy ;
                                      owl:someValuesFrom qm:PersonalTendency_MoodPersistence
                                    ] ,
                                    [ rdf:type owl:Restriction ;
                                      owl:onProperty qm:isDeterminedBy ;
                                      owl:allValuesFrom qm:AverageValenceOfPriorState
                                    ] ,
                                    [ rdf:type owl:Restriction ;
                                      owl:onProperty qm:isModulatedBy ;
                                      owl:allValuesFrom qm:PersonalTendency_MoodPersistence
                                    ] ;
                    rdfs:comment "The component of Cognitive Appraisal representing the lingering overall mood from the previous moment (AvgValence(S_t-1)), modulated by an individual's mood persistence (wS)."@en ,
                                 "The component representing the lingering overall mood from the previous moment (AvgValence(S_t-1)), modulated by an individual's mood persistence (wS)."@en ;
                    rdfs:label "Inertia of the Past"@en ,
                               "Inertia of the Past" .


###  https://tuos.org/qm#InferentialEpistemology
qm:InferentialEpistemology rdf:type owl:Class ;
                           rdfs:subClassOf qm:EpistemologicalChallenges ;
                           rdfs:comment "An approach to understanding phenomena through their effects, manifestation patterns, and systematic resistance to direct observation."@en ;
                           rdfs:label "Inferential Epistemology"@en .


###  https://tuos.org/qm#InfluentialFactor
qm:InfluentialFactor rdf:type owl:Class ;
                     rdfs:subClassOf qm:PsychodynamicWaveCollapse ;
                     rdfs:comment "A factor that can influence the patterns and outcomes of psychodynamic collapse."@en ;
                     rdfs:label "Influential Factors"@en .


###  https://tuos.org/qm#InherentDisposition
qm:InherentDisposition rdf:type owl:Class ;
                       rdfs:subClassOf qm:CognitiveAppraisalComponent ,
                                       qm:CognitiveAppraisalComponentsCategory ;
                       rdfs:comment "The component of Cognitive Appraisal representing a baseline cognitive or affective bias rooted in the stable characteristics of the individual's Prime Modality (M1), such as a general tendency towards optimism or pessimism."@en ,
                                    "The component of Cognitive Appraisal representing a baseline cognitive or affective bias rooted in the stable characteristics of the individual's Prime Modality (M1), such as a general tendency towards optimism or pessimism. It is a fixed part of the personality structure."@en ,
                                    "The component representing a baseline cognitive or affective bias rooted in the stable characteristics of the individual's Prime Modality (M1). It is a fixed part of the personality structure."@en ;
                       rdfs:label "Inherent Disposition (Bias_M1)"@en ,
                                  "Inherent Disposition (Bias_M1)" .


###  https://tuos.org/qm#InheritedScript
qm:InheritedScript rdf:type owl:Class ;
                   rdfs:subClassOf qm:EpistemologicalChallenges ,
                                   [ rdf:type owl:Restriction ;
                                     owl:onProperty qm:interferesWith ;
                                     owl:someValuesFrom qm:NaturalDevelopment
                                   ] ,
                                   [ rdf:type owl:Restriction ;
                                     owl:onProperty qm:isFormedBy ;
                                     owl:someValuesFrom qm:ExternalInfluence
                                   ] ,
                                   [ rdf:type owl:Restriction ;
                                     owl:onProperty qm:isLiberatedBy ;
                                     owl:someValuesFrom qm:LiberationProcess
                                   ] ,
                                   [ rdf:type owl:Restriction ;
                                     owl:onProperty qm:isTransmittedVia ;
                                     owl:someValuesFrom qm:SecondhandExperience
                                   ] ,
                                   [ rdf:type owl:Restriction ;
                                     owl:onProperty qm:leadsTo ;
                                     owl:someValuesFrom qm:OntologicalMisalignment
                                   ] ;
                   rdfs:comment "A comprehensive system of external influences, learned behavioral repertoires, and pervasive cultural programming that fundamentally shapes an individual's perceptual framework and subsequent actions, often operating beneath conscious awareness and creating a 'false native architecture'."@en ;
                   rdfs:label "Inherited Script"@en .


###  https://tuos.org/qm#InheritedScripts
qm:InheritedScripts rdf:type owl:Class ;
                    rdfs:subClassOf qm:CoreConceptsCategory ;
                    rdfs:comment "Pre-existing mental patterns, biases, or narratives that influence perception and interpretation, often formed from past experiences or societal conditioning."@en ;
                    rdfs:label "Inherited Scripts"@en .


###  https://tuos.org/qm#InstitutionalArchitectureImposition
qm:InstitutionalArchitectureImposition rdf:type owl:Class ;
                                       rdfs:subClassOf qm:ExternalInfluence .


###  https://tuos.org/qm#IntegratedTherapeuticApproaches
qm:IntegratedTherapeuticApproaches rdf:type owl:Class ;
                                   rdfs:subClassOf qm:MainStrategiesCategory ;
                                   rdfs:comment "Holistic and comprehensive approaches that combine various Quantum Mindfulness strategies and insights from diverse fields to address the whole system of a person rather than focusing on isolated symptoms or behaviors."@en ;
                                   rdfs:label "Integrated Therapeutic Approaches"@en .


###  https://tuos.org/qm#IntentionalCollapse
qm:IntentionalCollapse rdf:type owl:Class ;
                       rdfs:subClassOf qm:PracticesCategory ,
                                       [ rdf:type owl:Restriction ;
                                         owl:onProperty qm:hasPractice ;
                                         owl:someValuesFrom qm:SuperpositionalCognitiveEngineering
                                       ] ;
                       rdfs:comment "Deliberate guidance of the collapse process by the conscious observer, often via the Psycho-Meditative Dimension."@en ,
                                    "The conscious choice of which potential mental or emotional state is permitted to stabilize and manifest as experienced reality, by selectively attending to desired states."@en ;
                       rdfs:label "Intentional Collapse"@en ;
                       skos:altLabel "Volitional State Collapsing"@en ,
                                     "Intentional Collapse Direction" .


###  https://tuos.org/qm#InterferencePattern
qm:InterferencePattern rdf:type owl:Class ;
                       rdfs:subClassOf qm:PsychodynamicWaveCollapse ;
                       rdfs:comment "A sophisticated pattern of interaction between dimensions which can be either constructive or destructive."@en ;
                       rdfs:label "Interference Pattern"@en .


###  https://tuos.org/qm#InterferencePatterns
qm:InterferencePatterns rdf:type owl:Class ;
                        rdfs:subClassOf qm:EmergentPropertiesCategory ;
                        rdfs:comment "Complex patterns arising from the interaction of psychodynamic dimensions, akin to wave interference."@en ;
                        rdfs:label "Interference Patterns"@en .


###  https://tuos.org/qm#InternalCartography
qm:InternalCartography rdf:type owl:Class ;
                       rdfs:subClassOf qm:PracticesCategory ;
                       rdfs:comment "The practice of creating detailed, dynamic maps of the internal psychological terrain by identifying distinct regions of experience, their boundaries, and their interactions."@en ;
                       rdfs:label "Internal Cartography"@en ;
                       skos:definition "The practice of mapping one's internal psychological landscape to better understand and navigate it."@en .


###  https://tuos.org/qm#InternalConflictResolution
qm:InternalConflictResolution rdf:type owl:Class ;
                              rdfs:subClassOf qm:PracticesCategory ;
                              rdfs:comment "The systematic exploration of conflicting needs or desires to develop creative approaches for resolution without forcing a choice."@en ;
                              rdfs:label "Internal Conflict Resolution"@en .


###  https://tuos.org/qm#InternalMap
qm:InternalMap rdf:type owl:Class ;
               rdfs:subClassOf qm:InheritedScripts ,
                               [ rdf:type owl:Restriction ;
                                 owl:onProperty qm:enables ;
                                 owl:someValuesFrom qm:ConsciousnessRefinement
                               ] ;
               rdfs:comment "A framework for tracing specific thoughts, feelings, and behavioral impulses back to their underlying dimensional sources, enabling more precise intervention and navigation of the inner world."@en ;
               rdfs:label "Internal Map of Psychological Functioning"@en .


###  https://tuos.org/qm#InterpersonalRelationshipExperience
qm:InterpersonalRelationshipExperience rdf:type owl:Class ;
                                       rdfs:subClassOf qm:SecondhandExperience ;
                                       rdfs:comment "Implicit knowledge and reality construction acquired through social interaction and emotional dynamics, such as emotional contagion."@en ;
                                       rdfs:label "Interpersonal Relationship Experience"@en .


###  https://tuos.org/qm#IntersubjectiveReality
qm:IntersubjectiveReality rdf:type owl:Class ;
                          rdfs:subClassOf qm:SharedReality ;
                          rdfs:label "Intersubjective Reality"@en .


###  https://tuos.org/qm#IntersubjectiveResonance
qm:IntersubjectiveResonance rdf:type owl:Class ;
                            rdfs:subClassOf qm:Phenomenon ;
                            rdfs:comment "The capacity to feel with others, creating a shared emotional space."@en ;
                            rdfs:label "Intersubjective Resonance"@en .


###  https://tuos.org/qm#IntuitiveCognition
qm:IntuitiveCognition rdf:type owl:Class ;
                      rdfs:subClassOf qm:ProcessingMechanism ;
                      rdfs:label "Intuitive Cognition"@en .


###  https://tuos.org/qm#Jealousy
qm:Jealousy rdf:type owl:Class ;
            rdfs:subClassOf qm:Examples_Emergent ;
            rdfs:comment "An emergent property of dimensional interactions relating to security needs, self-worth validation, and relational bonding."@en ;
            rdfs:label "Jealousy"@en .


###  https://tuos.org/qm#KnowledgeAcquisition
qm:KnowledgeAcquisition rdf:type owl:Class ;
                        rdfs:subClassOf qm:EmpiricalAbsence ,
                                        [ rdf:type owl:Restriction ;
                                          owl:onProperty qm:uses ;
                                          owl:someValuesFrom qm:InferentialEpistemology
                                        ] ;
                        rdfs:comment "Defines how understanding is formed about phenomena subject to Empirical Absence."@en ;
                        rdfs:label "Knowledge Acquisition"@en .


###  https://tuos.org/qm#LearnedBehavioralRepertoire
qm:LearnedBehavioralRepertoire rdf:type owl:Class ;
                               rdfs:subClassOf qm:ExternalInfluence .


###  https://tuos.org/qm#LiberationFromInheritedScripts
qm:LiberationFromInheritedScripts rdf:type owl:Class ;
                                  rdfs:subClassOf qm:MainStrategiesCategory ;
                                  rdfs:comment "A specific pathway focused on transcending pervasive external conditioning (Inherited Scripts) to foster genuine Authentic Self-Origination."@en ;
                                  rdfs:label "Liberation from Inherited Scripts"@en .


###  https://tuos.org/qm#LiberationPhase
qm:LiberationPhase rdf:type owl:Class ;
                   rdfs:subClassOf qm:InheritedScripts .


###  https://tuos.org/qm#LiberationProcess
qm:LiberationProcess rdf:type owl:Class ;
                     rdfs:subClassOf qm:InheritedScripts ,
                                     [ rdf:type owl:Restriction ;
                                       owl:onProperty qm:hasPhase ;
                                       owl:someValuesFrom qm:LiberationProcess
                                     ] ;
                     rdfs:comment "A distinct phase within the process of achieving liberation from inherited scripts."@en ,
                                  "A sophisticated methodology for identifying, understanding, and transcending the limiting influence of Inherited Scripts."@en ;
                     rdfs:label "Liberation Process"@en .


###  https://tuos.org/qm#LimitationOfDirectObservation
qm:LimitationOfDirectObservation rdf:type owl:Class ;
                                 rdfs:subClassOf qm:EpistemologicalChallenges ;
                                 rdfs:comment "Inherent barriers to direct empirical investigation, often necessitating proxy-based approaches."@en ;
                                 rdfs:label "Limitation of Direct Observation"@en .


###  https://tuos.org/qm#MainStrategiesCategory
qm:MainStrategiesCategory rdf:type owl:Class ;
                          rdfs:subClassOf qm:TherapeuticStrategy ;
                          rdfs:comment "Primary therapeutic approaches employed within the framework."@en ;
                          rdfs:label "Main Strategies"@en .


###  https://tuos.org/qm#ManagementOfCognitiveStrain
qm:ManagementOfCognitiveStrain rdf:type owl:Class ;
                               rdfs:subClassOf qm:MainStrategiesCategory ,
                                               [ rdf:type owl:Restriction ;
                                                 owl:onProperty qm:targets ;
                                                 owl:hasValue qm:ResolutionFatigue
                                               ] ;
                               rdfs:comment "Strategies to address the contemporary crisis of cognitive overwhelm, fatigue, and dysfunction by cultivating cognitive agency and preserving mental well-being in information-rich environments."@en ;
                               rdfs:label "Management of Cognitive Strain and Dysfunction"@en .


###  https://tuos.org/qm#ManipulationOfConstructedReality
qm:ManipulationOfConstructedReality rdf:type owl:Class ;
                                    rdfs:subClassOf qm:EpistemologicalChallenges ;
                                    rdfs:label "Manipulation of Constructed Reality"@en .


###  https://tuos.org/qm#Memory
qm:Memory rdf:type owl:Class ;
          rdfs:subClassOf qm:PsychoFoundationalDimension .


###  https://tuos.org/qm#MentalFilesystemOrganization
qm:MentalFilesystemOrganization rdf:type owl:Class ;
                                rdfs:subClassOf qm:CognitiveStructuringApproaches ;
                                rdfs:label "Mental Filesystem Organization"@en .


###  https://tuos.org/qm#MentalFlexibility
qm:MentalFlexibility rdf:type owl:Class ;
                     rdfs:subClassOf qm:CognitiveCapacity .


###  https://tuos.org/qm#MentalPhysicalInterface
qm:MentalPhysicalInterface rdf:type owl:Class ;
                           rdfs:subClassOf qm:PsychoReceptiveDimension ;
                           rdfs:comment "A function facilitating the bidirectional flow and embodiment of psychological states and somatic awareness."@en ;
                           rdfs:label "Mental-Physical Interface"@en .


###  https://tuos.org/qm#MentalQuanta
qm:MentalQuanta rdf:type owl:Class ;
                rdfs:subClassOf qm:CognitiveSuperposition ;
                rdfs:comment "Fundamental units of cognitive or experiential possibility that compose the state of Cognitive Superposition."@en ;
                rdfs:label "Mental Quanta"@en .


###  https://tuos.org/qm#MentalState
qm:MentalState rdf:type owl:Class ;
               rdfs:subClassOf qm:QuantumPrinciple ;
               rdfs:comment "Encompasses thoughts, emotions, memories, and experiential potentials, which initially exist as fluid, probabilistic fields."@en ;
               rdfs:label "Mental State"@en .


###  https://tuos.org/qm#MindControlsBrainPrinciple
qm:MindControlsBrainPrinciple rdf:type owl:Class ;
                              rdfs:subClassOf qm:FrameworkPrinciple ,
                                              qm:FrameworkPrinciplesCategory ;
                              rdfs:comment "The principle that the brain is construed as a mediating organ through which thought is transduced into phenomenological experience, rather than its progenitor."@en ;
                              rdfs:label "Mind Controls Brain Principle"@en .


###  https://tuos.org/qm#MindfulnessApproachesComparisonCategory
qm:MindfulnessApproachesComparisonCategory rdf:type owl:Class ;
                                           rdfs:comment "A section for comparing and contrasting different mindfulness methodologies."@en ;
                                           rdfs:label "Mindfulness Approaches Comparison"@en .


###  https://tuos.org/qm#MindfulnessBasedCognitiveTherapy
qm:MindfulnessBasedCognitiveTherapy rdf:type owl:Class ;
                                    rdfs:subClassOf qm:StandardizedProtocol .


###  https://tuos.org/qm#MindfulnessBasedStressReduction
qm:MindfulnessBasedStressReduction rdf:type owl:Class ;
                                   rdfs:subClassOf qm:StandardizedProtocol ;
                                   rdfs:label "Mindfulness-Based Stress Reduction (MBSR)"@en .


###  https://tuos.org/qm#MindfulnessGoal
qm:MindfulnessGoal rdf:type owl:Class ;
                   rdfs:subClassOf qm:GoalsCategory ;
                   rdfs:label "Mindfulness Goal"@en ,
                              "X. Mindfulness Goal"@en .


###  https://tuos.org/qm#MindfulnessIntervention
qm:MindfulnessIntervention rdf:type owl:Class ;
                           rdfs:subClassOf qm:AdvancedPracticesAndMethodologiesCategory ,
                                           [ rdf:type owl:Restriction ;
                                             owl:onProperty qm:targets ;
                                             owl:allValuesFrom qm:CognitiveAppraisal
                                           ] ;
                           rdfs:comment "An intentional practice that interfaces with the Cognitive Appraisal mechanism to shape one's mental state."@en ;
                           rdfs:label "Mindfulness Intervention" .


###  https://tuos.org/qm#MultidimensionalScanning
qm:MultidimensionalScanning rdf:type owl:Class ;
                            rdfs:subClassOf qm:EmbodiedMindfulness ,
                                            qm:SomaticLiteracy ;
                            rdfs:comment "The practice of simultaneously tracking various nonverbal streams (posture, micro-expressions, breathing) to gain insight into internal states."@en ;
                            rdfs:label "Multidimensional Scanning"@en .


###  https://tuos.org/qm#NarrativeManagement
qm:NarrativeManagement rdf:type owl:Class ;
                       rdfs:subClassOf qm:PracticesCategory ;
                       rdfs:label "Narrative Management"@en .


###  https://tuos.org/qm#NaturalDevelopment
qm:NaturalDevelopment rdf:type owl:Class ;
                      rdfs:subClassOf qm:InheritedScripts ;
                      rdfs:comment "The authentic, self-originated unfolding of an individual's potential."@en ;
                      rdfs:label "Natural Development"@en .


###  https://tuos.org/qm#NeurologicalEmbedding
qm:NeurologicalEmbedding rdf:type owl:Class ;
                         rdfs:subClassOf qm:ConditioningMechanism .


###  https://tuos.org/qm#NonLocalCognition
qm:NonLocalCognition rdf:type owl:Class ;
                     rdfs:subClassOf qm:CognitiveCapacity ,
                                     qm:PracticesCategory ;
                     rdfs:comment "Attentional capacities that transcend ordinary spatial and temporal limitations, allowing access to information or insights beyond immediate sensory input or logical processes."@en ;
                     rdfs:label "Non-Local Cognition"@en .


###  https://tuos.org/qm#NonMaterialPhenomenon
qm:NonMaterialPhenomenon rdf:type owl:Class ;
                         rdfs:subClassOf qm:Phenomenon ;
                         rdfs:label "Non-Material Phenomenon"@en .


###  https://tuos.org/qm#NonReactiveObservation
qm:NonReactiveObservation rdf:type owl:Class ;
                          rdfs:subClassOf qm:EngagementStyle ;
                          rdfs:comment "The practice of observing mental phenomena without judgment, allowing them to arise and pass naturally without attempting to change or analyze them."@en ;
                          rdfs:label "Non-Reactive Observation"@en .


###  https://tuos.org/qm#NonlocalGoalState
qm:NonlocalGoalState rdf:type owl:Class ;
                     rdfs:subClassOf qm:AdvancedPracticesAndMethodologiesCategory ;
                     rdfs:comment "A desired outcome that, while not immediately present, exerts an ongoing orienting influence on current thought and action, enabling resistance to distractions."@en ;
                     rdfs:label "Nonlocal Goal State"@en .


###  https://tuos.org/qm#ObjectiveConstraints
qm:ObjectiveConstraints rdf:type owl:Class ;
                        rdfs:subClassOf qm:ChallengesAndLimitations ;
                        rdfs:comment "Inherent limitations imposed by physical laws, biological requirements, and material circumstances that conscious perception cannot alter. They represent the 'bones of reality'."@en ;
                        rdfs:label "Objective Constraints"@en .


###  https://tuos.org/qm#ObservableEffect
qm:ObservableEffect rdf:type owl:Class ;
                    rdfs:subClassOf qm:ObserverParticipantDynamic ;
                    rdfs:comment "A discernible pattern or systematic influence that confirms the existence of an empirically absent phenomenon."@en ;
                    rdfs:label "Observable Effect"@en .


###  https://tuos.org/qm#Observation
qm:Observation rdf:type owl:Class ;
               rdfs:subClassOf qm:FormalArchitectureCategory ,
                               qm:ObservationComponentsCategory ,
                               [ rdf:type owl:Restriction ;
                                 owl:onProperty qm:composedOf ;
                                 owl:someValuesFrom qm:Observation
                               ] ,
                               [ rdf:type owl:Restriction ;
                                 owl:onProperty qm:informs ;
                                 owl:someValuesFrom qm:CognitiveAppraisal
                               ] ,
                               [ rdf:type owl:Restriction ;
                                 owl:onProperty qm:isFirstStepIn ;
                                 owl:someValuesFrom qm:ObserverParticipantTheory
                               ] ,
                               [ rdf:type owl:Restriction ;
                                 owl:onProperty qm:informs ;
                                 owl:allValuesFrom qm:CognitiveAppraisal
                               ] ;
               rdfs:comment "A contributing factor that synergistically forms a complex Observation (Ψ)."@en ,
                            "The pivotal 'central trigger' or initial 'Cognitive Measurement' that instigates the psychodynamic process. It is a complex perception formed by the synergistic, multiplicative interplay of its four components. It marks the first active step in the 'Observer-Participant' dynamic."@en ,
                            "The pivotal 'central trigger' or initial 'Cognitive Measurement' that instigates the psychodynamic process. It is a complex perception formed by the synergistic, multiplicative interplay of its four components: raw perceptual imprint (α), perceived meaning (β), general awareness (A), and directed focus (f). This marks the first active step in the 'Observer-Participant' dynamic."@en ,
                            "The pivotal central trigger or initial 'Cognitive Measurement' that instigates the psychodynamic process. It is a complex perception formed by the dynamic interplay of raw sensory data/internal stimuli (α), assigned meaning (β), general awareness (A), and directed focus (f)."@en ,
                            "The pivotal central trigger or initial Cognitive Measurement that instigates the psychodynamic process."@en ;
               rdfs:label "Observation (Ψ)"@en ,
                          "Observation Component"@en ,
                          "Observation (Ψ)" ;
               rdfs:subClassOf "Psychodynamic Model"@en .


###  https://tuos.org/qm#ObservationComponentsCategory
qm:ObservationComponentsCategory rdf:type owl:Class ;
                                 rdfs:subClassOf qm:FormalArchitectureCategory ;
                                 rdfs:comment "Conceptual container for the constituent parts of an Observation."@en ;
                                 rdfs:label "Components (Ψ = α(β + 1)(A + f))"@en .


###  https://tuos.org/qm#ObservationInfluence
qm:ObservationInfluence rdf:type owl:Class ;
                        rdfs:subClassOf qm:DimensionalActivationInfluence ,
                                        qm:DimensionalActivationInfluencesCategory ,
                                        [ rdf:type owl:Restriction ;
                                          owl:onProperty qm:isDeterminedBy ;
                                          owl:someValuesFrom qm:RelevanceFunction
                                        ] ,
                                        [ rdf:type owl:Restriction ;
                                          owl:onProperty qm:isModulatedBy ;
                                          owl:someValuesFrom qm:PersonalTendency_ObservationReactivity
                                        ] ;
                        rdfs:comment "Represents the direct, specific impact of the current Observation (Ψ) itself on a dimension (IΨj = wΨj ⋅ Relevance(Ψ, Pdj))."@en ,
                                     "Represents the direct, specific impact of the current Observation (Ψ) itself on a dimension (IΨj = wΨj ⋅ Relevance(Ψ, Pdj)). It addresses: 'How much does the specific content of what I am observing directly impact this feeling?'."@en ,
                                     "Represents the direct, specific impact of the current Observation (Ψ) itself on a dimension, based on the observation's relevance to the dimension's nature."@en ;
                        rdfs:label "Observation Influence (IΨj)"@en ,
                                   "Observation Influence (IΨj)" .


###  https://tuos.org/qm#ObservationValence
qm:ObservationValence rdf:type owl:Class ;
                      rdfs:subClassOf qm:QuantumMindfulnessApplication .


###  https://tuos.org/qm#ObserverEffectParadox
qm:ObserverEffectParadox rdf:type owl:Class ;
                         rdfs:subClassOf qm:EpistemologicalChallenges .


###  https://tuos.org/qm#ObserverFunction
qm:ObserverFunction rdf:type owl:Class ;
                    rdfs:subClassOf qm:ObserverParticipantDynamic ,
                                    [ rdf:type owl:Restriction ;
                                      owl:onProperty qm:isEngagedBy ;
                                      owl:someValuesFrom qm:Contemplation
                                    ] ;
                    rdfs:comment "A specific capacity of awareness within the Quantum Observer that, when engaged, actively participates in resolving superimposed potentials by stabilizing cognitive content."@en ;
                    rdfs:label "Observer Function"@en .


###  https://tuos.org/qm#ObserverParticipantDynamic
qm:ObserverParticipantDynamic rdf:type owl:Class ;
                              rdfs:subClassOf qm:CoreConceptsCategory ;
                              rdfs:label "Observer-Participant Dynamic"@en .


###  https://tuos.org/qm#ObserverParticipantRole
qm:ObserverParticipantRole rdf:type owl:Class ;
                           rdfs:subClassOf qm:ObserverRole ;
                           rdfs:comment "The recognition that the act of observation inherently modifies the observed mental state, positioning the observer as an active co-creator of experience."@en ;
                           rdfs:label "Observer-Participant Role"@en .


###  https://tuos.org/qm#ObserverParticipantTheory
qm:ObserverParticipantTheory rdf:type owl:Class ;
                             rdfs:subClassOf qm:Perception ,
                                             [ rdf:type owl:Restriction ;
                                               owl:onProperty qm:posits ;
                                               owl:someValuesFrom qm:ConsciousObservation
                                             ] ;
                             rdfs:comment "A comprehensive framework that reconceptualizes the role of awareness in human experience, demonstrating that conscious engagement with mental phenomena constitutes an active, participatory process that inherently shapes and co-creates the fabric of experienced reality."@en ;
                             rdfs:label "Observer-Participant Theory"@en .


###  https://tuos.org/qm#ObserverRole
qm:ObserverRole rdf:type owl:Class ;
                rdfs:subClassOf qm:ObserverParticipantDynamic .


###  https://tuos.org/qm#OntologicalFieldTheory
qm:OntologicalFieldTheory rdf:type owl:Class ;
                          rdfs:subClassOf qm:CoreConceptsCategory ;
                          rdfs:comment "Posits that individual mental frameworks—encompassing beliefs, assumptions, and unconscious cognitive structures—actively contribute to shaping perceived reality rather than merely filtering or interpreting it."@en ;
                          rdfs:label "Ontological Field Theory"@en .


###  https://tuos.org/qm#OntologicalFirewall
qm:OntologicalFirewall rdf:type owl:Class ;
                       rdfs:subClassOf qm:EmpiricalAbsence ,
                                       [ rdf:type owl:Restriction ;
                                         owl:onProperty qm:isSegregatedBy ;
                                         owl:someValuesFrom qm:PsychoVolitionalDimension
                                       ] ;
                       rdfs:comment "Fundamental structural features of reality that create categorical boundaries between different modes of being and knowing, particularly between consciousness and its source."@en ;
                       rdfs:label "Ontological Firewall"@en .


###  https://tuos.org/qm#OntologicalMisalignment
qm:OntologicalMisalignment rdf:type owl:Class ;
                           rdfs:subClassOf qm:PsychologicalDisharmony ,
                                           qm:PsychologicalDysfunctionAndImbalance ;
                           rdfs:comment "A fundamental discrepancy between an individual's true nature and their lived experience, resulting from operating according to inherited scripts."@en ;
                           rdfs:label "Ontological Misalignment"@en .


###  https://tuos.org/qm#OntologicalReassignment
qm:OntologicalReassignment rdf:type owl:Class ;
                           rdfs:subClassOf qm:CollapseInfluencePractice .


###  https://tuos.org/qm#OntologicalRestructuring
qm:OntologicalRestructuring rdf:type owl:Class ;
                            rdfs:subClassOf qm:PracticesCategory .


###  https://tuos.org/qm#OntologicalStarvation
qm:OntologicalStarvation rdf:type owl:Class ;
                         rdfs:subClassOf qm:CognitiveStrainAndDysfunction ,
                                         qm:CollapseDysfunction ;
                         rdfs:comment "A profound form of cognitive strain where a loss of authentic engagement and volition occurs, related to Resolution Fatigue."@en ;
                         rdfs:label "Ontological Starvation"@en .


###  https://tuos.org/qm#OntologicalStatecraft
qm:OntologicalStatecraft rdf:type owl:Class ;
                         rdfs:subClassOf qm:PracticesCategory ;
                         rdfs:label "Ontological Statecraft"@en .


###  https://tuos.org/qm#OptimalCognitiveState
qm:OptimalCognitiveState rdf:type owl:Class ;
                         rdfs:subClassOf qm:CognitiveSuperposition .


###  https://tuos.org/qm#OsmoticIntegration
qm:OsmoticIntegration rdf:type owl:Class ;
                      rdfs:subClassOf qm:ConditioningMechanism .


###  https://tuos.org/qm#OtherKeyConcepts
qm:OtherKeyConcepts rdf:type owl:Class ;
                    rdfs:comment "A general category for important concepts not explicitly covered in other major sections."@en ;
                    rdfs:label "Other Key Concepts"@en .


###  https://tuos.org/qm#OverallMentalState
qm:OverallMentalState rdf:type owl:Class ;
                      rdfs:subClassOf qm:FormalArchitectureCategory ,
                                      [ rdf:type owl:Restriction ;
                                        owl:onProperty qm:composedOf ;
                                        owl:allValuesFrom qm:FinalIntensity
                                      ] ;
                      rdfs:comment "The final, composite, and holistic conscious experience emerging from the specific configuration and actualized intensities of all ten Psychodynamic Dimensions."@en ,
                                   "The final, composite, and holistic conscious experience emerging from the specific configuration and actualized intensities of all ten Psychodynamic Dimensions. It is a complex blend where each dimension's qualitative nature is weighted by its calculated Final Intensity."@en ;
                      rdfs:label "Overall Mental State (S)"@en ,
                                 "Overall Mental State (S)" ;
                      rdfs:subClassOf "Psychodynamic Model"@en .


###  https://tuos.org/qm#ParadoxTolerance
qm:ParadoxTolerance rdf:type owl:Class ;
                    rdfs:subClassOf qm:CognitiveCapacity ;
                    rdfs:label "Paradox Tolerance"@en .


###  https://tuos.org/qm#PassiveMastery
qm:PassiveMastery rdf:type owl:Class ;
                  rdfs:subClassOf qm:ClassicalMindfulness ;
                  rdfs:comment "The achievement of equanimity and present-moment presence, largely independent of the specific content of experience."@en ;
                  rdfs:label "Passive Mastery"@en .


###  https://tuos.org/qm#PassiveRecipientView
qm:PassiveRecipientView rdf:type owl:Class ;
                        rdfs:subClassOf qm:ClassicalMindfulness ;
                        rdfs:comment "The view that consciousness passively receives an internal representation of a pre-existing, objective reality."@en ;
                        rdfs:label "Passive Recipient View"@en .


###  https://tuos.org/qm#PatternedPresence
qm:PatternedPresence rdf:type owl:Class ;
                     rdfs:subClassOf qm:PracticesCategory ;
                     rdfs:comment "A sophisticated mode of awareness that goes beyond merely observing 'what' is experienced to also apprehending the 'how', 'from where', and 'according to what patterns' of experiential emergence."@en ,
                                  "A state of being present that is simultaneously receptive and structured, involving the deliberate organization of attention. It is a central mechanism used by Vectorized Awareness to enable precise navigation of the internal psychological terrain."@en ;
                     rdfs:label "Patterned Presence"@en .


###  https://tuos.org/qm#PerceivedLimitation
qm:PerceivedLimitation rdf:type owl:Class ;
                       rdfs:subClassOf qm:Perception ;
                       rdfs:comment "Mental blocks, constricting conceptual frameworks, or other perceived boundaries that can be dissolved by the Psycho-Volitional Dimension."@en ;
                       rdfs:label "Perceived Limitation"@en .


###  https://tuos.org/qm#PerceivedMeaning
qm:PerceivedMeaning rdf:type owl:Class ;
                    rdfs:subClassOf qm:Observation ,
                                    qm:ObservationComponentsCategory ;
                    rdfs:comment "Represents the initial layer of meaning, significance, or intent that the mind rapidly and often automatically assigns to raw data (α). It is a 'first-pass interpretation'. The '+ 1' factor in its formal use implies a baseline level of 'being-ness' to the meaning component."@en ,
                                 "The initial layer of meaning or 'first-pass interpretation' that the mind rapidly assigns to raw data (α). The '+1' factor implies a baseline 'being-ness' to the meaning component."@en ;
                    rdfs:label "Perceived Meaning/Intent (β)"@en ,
                               "Perceived Meaning/Intent (β)" .


###  https://tuos.org/qm#PerceivedProblem
qm:PerceivedProblem rdf:type owl:Class ;
                    rdfs:subClassOf qm:Perception ;
                    rdfs:comment "Phenomena experienced as 'problems' that are not fixed, objective entities, but are significantly shaped by interpretive frameworks and perceptual habits, and are susceptible to conscious reconfiguration."@en ;
                    rdfs:label "Perceived Problem"@en .


###  https://tuos.org/qm#Perception
qm:Perception rdf:type owl:Class ;
              rdfs:subClassOf qm:CoreConceptsCategory ,
                              [ rdf:type owl:Restriction ;
                                owl:onProperty qm:filters ;
                                owl:someValuesFrom qm:CognitiveFilteringMechanism
                              ] ,
                              [ rdf:type owl:Restriction ;
                                owl:onProperty qm:hasDynamic ;
                                owl:someValuesFrom qm:ObserverParticipantTheory
                              ] ,
                              [ rdf:type owl:Restriction ;
                                owl:onProperty qm:influences ;
                                owl:someValuesFrom qm:ExperiencedReality
                              ] ,
                              [ rdf:type owl:Restriction ;
                                owl:onProperty qm:isFundamentalTo ;
                                owl:someValuesFrom qm:SecondhandExperience
                              ] ,
                              [ rdf:type owl:Restriction ;
                                owl:onProperty qm:isShapedByTechnique ;
                                owl:someValuesFrom qm:PerceptualShapingTechnique
                              ] ,
                              [ rdf:type owl:Restriction ;
                                owl:onProperty qm:operatesThrough ;
                                owl:someValuesFrom qm:PsychodynamicCollapse
                              ] ;
              rdfs:comment "A dynamic and active process through which ambiguous, multi-potential cognitive states (superposition) resolve into singular, definitive conscious experiences, largely driven by conscious attention and interpretive frameworks. It is a generative force in the construction of experienced reality."@en ,
                           "The process of interpreting and understanding sensory information and internal stimuli, leading to a subjective experience of reality."@en ;
              rdfs:label "Perception"@en .


###  https://tuos.org/qm#PerceptualAgility
qm:PerceptualAgility rdf:type owl:Class ;
                     rdfs:subClassOf qm:AdvancedPracticesAndMethodologiesCategory ,
                                     qm:PerceptualGoal ;
                     rdfs:comment "The intentional modification of perceptual modalities and the advanced ability to effortlessly navigate and hold multiple perceptual frameworks."@en ;
                     rdfs:label "Perceptual Agility"@en .


###  https://tuos.org/qm#PerceptualConstructionTheory
qm:PerceptualConstructionTheory rdf:type owl:Class ;
                                rdfs:subClassOf qm:CoreConceptsCategory ;
                                rdfs:comment "A framework wherein consciousness operates as a dynamic field that constructs and reconstructs the landscape of mental reality."@en ;
                                rdfs:label "Perceptual Construction Theory"@en .


###  https://tuos.org/qm#PerceptualContract
qm:PerceptualContract rdf:type owl:Class ;
                      rdfs:subClassOf qm:InfluentialFactor ;
                      rdfs:label "Perceptual Contract"@en .


###  https://tuos.org/qm#PerceptualDistortion
qm:PerceptualDistortion rdf:type owl:Class ;
                        rdfs:subClassOf qm:PsychologicalDisharmony ;
                        rdfs:comment "A maladaptive response arising from Dimensional Misalignment or Sub-dynamic Interference, such as an overactive threat-detection dimension framing neutral situations as dangerous."@en ;
                        rdfs:label "Perceptual Distortion"@en .


###  https://tuos.org/qm#PerceptualFraming
qm:PerceptualFraming rdf:type owl:Class ;
                     rdfs:subClassOf qm:CognitiveMechanism ,
                                     qm:PerceptualShapingTechnique ;
                     rdfs:label "Perceptual Framing"@en .


###  https://tuos.org/qm#PerceptualFreedom
qm:PerceptualFreedom rdf:type owl:Class ;
                     rdfs:subClassOf qm:PerceptualGoal ;
                     rdfs:comment "The capacity to consciously choose how potential experiences actualize, enabling adaptive engagement with challenges and conscious evolution. It is the ultimate goal of Quantum Mindfulness."@en ;
                     rdfs:label "Perceptual Freedom"@en .


###  https://tuos.org/qm#PerceptualGoal
qm:PerceptualGoal rdf:type owl:Class ;
                  rdfs:subClassOf qm:Perception ;
                  rdfs:comment "A desired state or capacity that is the aim of perceptual work within the Quantum Mindfulness framework."@en ;
                  rdfs:label "Perceptual Goal"@en .


###  https://tuos.org/qm#PerceptualMastery
qm:PerceptualMastery rdf:type owl:Class ;
                     rdfs:subClassOf qm:PerceptualGoal .


###  https://tuos.org/qm#PerceptualReframing
qm:PerceptualReframing rdf:type owl:Class ;
                       rdfs:subClassOf qm:PerceptualShapingTechnique ;
                       rdfs:label "Perceptual Reframing"@en .


###  https://tuos.org/qm#PerceptualShapingTechnique
qm:PerceptualShapingTechnique rdf:type owl:Class ;
                              rdfs:subClassOf qm:CultivationMethod ;
                              rdfs:comment "A deliberate practice or method used to consciously influence perceptual processes."@en ;
                              rdfs:label "Perceptual Shaping Technique"@en .


###  https://tuos.org/qm#PerceptualSophistication
qm:PerceptualSophistication rdf:type owl:Class ;
                            rdfs:subClassOf qm:CognitiveCapacity ;
                            rdfs:comment "The capacity to discern subtle differences between externally conditioned responses and internally generated awareness."@en ;
                            rdfs:label "Perceptual Sophistication"@en .


###  https://tuos.org/qm#PerceptualSuperposition
qm:PerceptualSuperposition rdf:type owl:Class ;
                           rdfs:subClassOf qm:Perception ;
                           rdfs:label "Perceptual Superposition"@en .


###  https://tuos.org/qm#PersonalTendency
qm:PersonalTendency rdf:type owl:Class ;
                    rdfs:subClassOf qm:CognitiveAppraisalComponentsCategory ;
                    rdfs:comment "A weighting factor that quantifies inherent individual differences in reactivity, emotional inertia, or other dispositional traits that modulate the Cognitive Appraisal."@en ;
                    rdfs:label "Personal Tendency (w)"@en ,
                               "Personal Tendency (w)" .


###  https://tuos.org/qm#PersonalTendency_CognitiveResponsiveness
qm:PersonalTendency_CognitiveResponsiveness rdf:type owl:Class ;
                                            rdfs:subClassOf qm:DimensionalActivationInfluencesCategory ,
                                                            qm:PersonalTendency .


###  https://tuos.org/qm#PersonalTendency_MoodPersistence
qm:PersonalTendency_MoodPersistence rdf:type owl:Class ;
                                    rdfs:subClassOf qm:PersonalTendency .


###  https://tuos.org/qm#PersonalTendency_ObservationReactivity
qm:PersonalTendency_ObservationReactivity rdf:type owl:Class ;
                                          rdfs:subClassOf qm:DimensionalActivationInfluencesCategory ,
                                                          qm:PersonalTendency ;
                                          rdfs:label "Personal Tendency (Observation Reactivity - wΨj)"@en .


###  https://tuos.org/qm#PersonalTendency_Persistence
qm:PersonalTendency_Persistence rdf:type owl:Class ;
                                rdfs:subClassOf qm:DimensionalActivationInfluencesCategory ,
                                                qm:PersonalTendency .


###  https://tuos.org/qm#PersonalTendency_Reactivity
qm:PersonalTendency_Reactivity rdf:type owl:Class ;
                               rdfs:subClassOf qm:PersonalTendency .


###  https://tuos.org/qm#PersonalTendency_TraitExpression
qm:PersonalTendency_TraitExpression rdf:type owl:Class ;
                                    rdfs:subClassOf qm:DimensionalActivationInfluencesCategory ,
                                                    qm:PersonalTendency ;
                                    rdfs:label "Personal Tendency (Trait Expression - wTj)"@en .


###  https://tuos.org/qm#PersonalityOrganization
qm:PersonalityOrganization rdf:type owl:Class ;
                           rdfs:subClassOf qm:PsychodynamicDimension ;
                           rdfs:comment "The structural foundation of personality, formed by the dynamic interplay of the Psychodynamic Dimensions."@en ;
                           rdfs:label "Personality Organization"@en .


###  https://tuos.org/qm#Phenomenon
qm:Phenomenon rdf:type owl:Class ;
              rdfs:subClassOf qm:EmpiricalAbsence ,
                              [ rdf:type owl:Restriction ;
                                owl:onProperty qm:isSubjectTo ;
                                owl:someValuesFrom qm:EmpiricalAbsence
                              ] ;
              rdfs:comment "A general class for entities or processes that can exhibit the characteristic of Empirical Absence."@en ;
              rdfs:label "Phenomenon"@en .


###  https://tuos.org/qm#PlausibilityEngineering
qm:PlausibilityEngineering rdf:type owl:Class ;
                           rdfs:subClassOf qm:PerceptualShapingTechnique ;
                           rdfs:label "Plausibility Engineering"@en .


###  https://tuos.org/qm#PracticalLimitationsOfQMApplication
qm:PracticalLimitationsOfQMApplication rdf:type owl:Class ;
                                       rdfs:subClassOf qm:ChallengesAndLimitations ,
                                                       qm:ChallengesAndLimitationsCategory ;
                                       rdfs:comment "Constraints or difficulties in implementing Quantum Mindfulness practices in real-world scenarios."@en ,
                                                    "Real-world constraints and considerations that limit the direct application, scope, or effectiveness of Quantum Mindfulness principles and techniques."@en ;
                                       rdfs:label "Practical Limitations of QM Application"@en .


###  https://tuos.org/qm#PracticalWisdom
qm:PracticalWisdom rdf:type owl:Class ;
                   rdfs:subClassOf qm:CognitiveCapacity ,
                                   [ rdf:type owl:Restriction ;
                                     owl:onProperty qm:isCultivatedBy ;
                                     owl:hasValue qm:Contemplation
                                   ] ;
                   rdfs:comment "The capacity to discern appropriate action in specific circumstances based on deep understanding, developed through contemplative inquiry."@en ;
                   rdfs:label "Practical Wisdom"@en .


###  https://tuos.org/qm#PracticesCategory
qm:PracticesCategory rdf:type owl:Class ;
                     rdfs:subClassOf qm:AdvancedPracticesAndMethodologiesCategory ;
                     rdfs:comment "Specific methods or exercises undertaken to apply Quantum Mindfulness principles."@en ;
                     rdfs:label "Practices"@en .


###  https://tuos.org/qm#PrimeModality
qm:PrimeModality rdf:type owl:Class ;
                 rdfs:subClassOf qm:PrimeModalityCategory ,
                                 [ rdf:type owl:Restriction ;
                                   owl:onProperty qm:contributesTo ;
                                   owl:someValuesFrom qm:CognitiveAppraisal
                                 ] ,
                                 [ rdf:type owl:Restriction ;
                                   owl:onProperty qm:contributesTo ;
                                   owl:someValuesFrom qm:CognitiveAppraisalBias
                                 ] ,
                                 [ rdf:type owl:Restriction ;
                                   owl:onProperty qm:composedOf ;
                                   owl:allValuesFrom qm:PsychodynamicDimension
                                 ] ,
                                 [ rdf:type owl:Restriction ;
                                   owl:onProperty qm:composedOf ;
                                   owl:hasValue qm:Pd1
                                 ] ,
                                 [ rdf:type owl:Restriction ;
                                   owl:onProperty qm:composedOf ;
                                   owl:hasValue qm:Pd2
                                 ] ,
                                 [ rdf:type owl:Restriction ;
                                   owl:onProperty qm:composedOf ;
                                   owl:hasValue qm:Pd3
                                 ] ;
                 rdfs:comment "The cognitive-executive triad (Pd1-Pd3) governing perception, intention, and interpretation. It is the paramount, highest-order cognitive structure, serving as the underlying matrix for all subjective awareness and providing the 'scaffolding of consciousness itself'."@en ,
                              "The cognitive-executive triad (Pd1-Pd3) that governs the mind's capacity for perception, intention, and interpretation, and is the source of 'volitional awareness'. It contributes a baseline bias to the Cognitive Appraisal process."@en ,
                              "The cognitive-executive triad (Pd1-Pd3) that governs the mind’s capacity for perception, intention, and interpretation. It is the paramount, highest-order, foundational cognitive structure, serving as the underlying matrix for all subjective awareness and providing the 'scaffolding of consciousness itself'."@en ,
                              "The paramount, highest-order, foundational cognitive structure within the Quantum Mindfulness framework."@en ;
                 rdfs:label "Prime Modality (M1)"@en ,
                            "Prime Modality (M1)" ;
                 rdfs:subClassOf "Psychodynamic Model"@en .


###  https://tuos.org/qm#PrimeModalityCategory
qm:PrimeModalityCategory rdf:type owl:Class ;
                         rdfs:subClassOf qm:PsychodynamicDimensionsCategory ;
                         rdfs:comment "Conceptual container for the Prime Modality dimensions, governing perception, intention, and interpretation."@en ;
                         rdfs:label "Prime Modality (M1) - Cognitive-Executive Triad"@en .


###  https://tuos.org/qm#PrincipleOfBalance
qm:PrincipleOfBalance rdf:type owl:Class ;
                      rdfs:subClassOf qm:AestheticPrinciple .


###  https://tuos.org/qm#PrincipleOfLimit
qm:PrincipleOfLimit rdf:type owl:Class ;
                    rdfs:subClassOf qm:ProtectivePrinciple .


###  https://tuos.org/qm#PrincipleOfMeasure
qm:PrincipleOfMeasure rdf:type owl:Class ;
                      rdfs:subClassOf qm:ProtectivePrinciple .


###  https://tuos.org/qm#PrincipleOfRestraint
qm:PrincipleOfRestraint rdf:type owl:Class ;
                        rdfs:subClassOf qm:ProtectivePrinciple ;
                        rdfs:label "Principle of Restraint"@en .


###  https://tuos.org/qm#PrincipleOfSymmetry
qm:PrincipleOfSymmetry rdf:type owl:Class ;
                       rdfs:subClassOf qm:AestheticPrinciple ;
                       rdfs:label "Principle of Symmetry"@en .


###  https://tuos.org/qm#PrincipleReceptivity
qm:PrincipleReceptivity rdf:type owl:Class ;
                        rdfs:subClassOf qm:Phenomenon ;
                        rdfs:comment "The capacity to recognize and align with guiding insights that emerge from deeper levels of consciousness."@en ;
                        rdfs:label "Principle Receptivity"@en .


###  https://tuos.org/qm#PriorStateInfluence
qm:PriorStateInfluence rdf:type owl:Class ;
                       rdfs:subClassOf qm:DimensionalActivationInfluence ,
                                       qm:DimensionalActivationInfluencesCategory ,
                                       [ rdf:type owl:Restriction ;
                                         owl:onProperty qm:isDeterminedBy ;
                                         owl:someValuesFrom qm:FinalIntensity
                                       ] ,
                                       [ rdf:type owl:Restriction ;
                                         owl:onProperty qm:isModulatedBy ;
                                         owl:someValuesFrom qm:PersonalTendency_Persistence
                                       ] ;
                       rdfs:comment "Accounts for the inertia or momentum of each specific dimension from the immediately preceding moment."@en ,
                                    "Captures the 'inertia' or 'momentum' of a specific psychodynamic dimension from the immediately preceding mental state (ISj = wSj ⋅ xj,t-1)."@en ,
                                    "Captures the 'inertia' or 'momentum' of a specific psychodynamic dimension from the immediately preceding mental state (ISj = wSj ⋅ xj,t-1). It addresses: 'How much does my previous experience of this specific feeling contribute to its potential now?'."@en ;
                       rdfs:label "Prior State Influence (ISj)"@en ,
                                  "Prior State Influence (ISj)" .


###  https://tuos.org/qm#ProactiveSelfRegulation
qm:ProactiveSelfRegulation rdf:type owl:Class ;
                           rdfs:subClassOf qm:EmbodiedMindfulness ;
                           rdfs:comment "Using somatic signatures as an early warning system to manage emerging internal states before they become overwhelming, enabling pre-resolution intervention."@en ;
                           rdfs:label "Proactive Self-Regulation"@en ;
                           skos:definition "The practice of anticipating and managing one's internal states and behaviors in advance to achieve goals."@en .


###  https://tuos.org/qm#ProbabilisticField
qm:ProbabilisticField rdf:type owl:Class ;
                      rdfs:subClassOf qm:CoreConceptsCategory ;
                      rdfs:comment "A dynamic field of multiple simultaneous possibilities that mental states initially exist in prior to focused attention and cognitive processing."@en ;
                      rdfs:label "Probabilistic Field"@en .


###  https://tuos.org/qm#ProbabilisticMentalState
qm:ProbabilisticMentalState rdf:type owl:Class ;
                            rdfs:subClassOf qm:CognitiveSuperposition ;
                            rdfs:comment "The state where multiple potential cognitive, emotional, and perceptual states coexist simultaneously as possibilities before conscious attention focuses them into definite experience."@en ;
                            rdfs:label "Probabilistic Mental State"@en ;
                            skos:altLabel "Mental Wave Function"@en .


###  https://tuos.org/qm#ProbabilisticSteering
qm:ProbabilisticSteering rdf:type owl:Class ;
                         rdfs:subClassOf qm:PerceptualShapingTechnique .


###  https://tuos.org/qm#ProcessingMechanism
qm:ProcessingMechanism rdf:type owl:Class ;
                       rdfs:subClassOf qm:Phenomenon ;
                       rdfs:label "Processing Mechanism"@en .


###  https://tuos.org/qm#ProjectedAnxietySystem
qm:ProjectedAnxietySystem rdf:type owl:Class ;
                          rdfs:subClassOf qm:ExternalInfluence ;
                          rdfs:label "Projected Anxiety System"@en .


###  https://tuos.org/qm#ProtectivePrinciple
qm:ProtectivePrinciple rdf:type owl:Class ;
                       rdfs:subClassOf qm:Phenomenon ;
                       rdfs:comment "A primordial psychological principle embodied by the Psycho-Protective Dimension."@en ;
                       rdfs:label "Protective Principle"@en .


###  https://tuos.org/qm#ProtoImpulse
qm:ProtoImpulse rdf:type owl:Class ;
                rdfs:subClassOf qm:Phenomenon ;
                rdfs:comment "Subtle internal impulses arising from unconscious processing, intuitive insight, creative inspiration, or ethical sensitivity."@en ;
                rdfs:label "Proto-Impulse"@en .


###  https://tuos.org/qm#Proxy
qm:Proxy rdf:type owl:Class ;
         rdfs:subClassOf qm:Phenomenon ;
         rdfs:comment "Any indirect representation, model, inference, or description that provides access to phenomena that cannot be directly grasped through conventional empirical means."@en ;
         rdfs:label "Proxy"@en .


###  https://tuos.org/qm#PsychicArchitecture
qm:PsychicArchitecture rdf:type owl:Class ;
                       rdfs:subClassOf qm:QuantumPrinciple ;
                       rdfs:comment "The conceptual structure of the psyche within the Quantum Mindfulness framework."@en ;
                       rdfs:label "Psychic Architecture"@en .


###  https://tuos.org/qm#PsychoAestheticDimension
qm:PsychoAestheticDimension rdf:type owl:Class ;
                            rdfs:subClassOf qm:PsychodynamicDimension ,
                                            qm:SecondaryModality ,
                                            [ rdf:type owl:Restriction ;
                                              owl:onProperty qm:bridgesTo ;
                                              owl:someValuesFrom qm:PsychoMotivationalDimension
                                            ] ,
                                            [ rdf:type owl:Restriction ;
                                              owl:onProperty qm:isKeyTo ;
                                              owl:someValuesFrom qm:PsychodynamicHarmonicAlignment
                                            ] ,
                                            [ rdf:type owl:Restriction ;
                                              owl:onProperty qm:isMediatedBy ;
                                              owl:someValuesFrom qm:PsychoAestheticDimension
                                            ] ;
                            rdfs:comment "A crucial balancing cognitive mechanism that harmonizes seemingly opposing forces within the psyche, establishing harmonious integration between opposing psychological forces. It functions as an integration hub, specializing in harmonious synthesis among opposing energies."@en ,
                                         "Pd6: The dimension of sensory appeal, beauty, and attraction."@en ,
                                         "The dimension of sensory appeal, beauty, and attraction. It functions as a crucial balancing cognitive mechanism that harmonizes opposing forces within the psyche, such as empathy and protection, thereby promoting integration and emotional maturity."@en ,
                                         "The sixth dimension, which serves as an emotional modulator, seeking a harmonious midpoint between contradictory tendencies like care and boundary."@en ,
                                         "The central integrating force of the psyche, balancing internal experiences with external reality, fostering harmony and authenticity of the self." ;
                            rdfs:label "Psycho-Aesthetic Dimension (Pd6)"@en ,
                                       "Psycho-Aesthetic Dimension (Pd6)" .


###  https://tuos.org/qm#PsychoConceptiveDimension
qm:PsychoConceptiveDimension rdf:type owl:Class ;
                             rdfs:subClassOf qm:PsychodynamicDimension ,
                                             [ rdf:type owl:Restriction ;
                                               owl:onProperty qm:operatesThrough ;
                                               owl:someValuesFrom qm:IntuitiveCognition
                                             ] ,
                                             [ rdf:type owl:Restriction ;
                                               owl:onProperty qm:dependsOn ;
                                               owl:allValuesFrom qm:PsychoVolitionalDimension
                                             ] ,
                                             [ rdf:type owl:Restriction ;
                                               owl:onProperty qm:progressesTo ;
                                               owl:allValuesFrom qm:PsychoMeditativeDimension
                                             ] ;
                             rdfs:comment "A dynamic, highly intuitive cognitive function that facilitates spontaneous insight and pattern recognition. It represents the psyche’s initial creative act, where abstract, unformed potential begins to coalesce into nascent concepts, functioning as the subconscious wellspring of wisdom and intellect."@en ,
                                          "A dynamic, intuitive function for spontaneous insight, pattern recognition, and apprehension of complex relationships beyond linear thought. It represents the psyche’s initial creative act where abstract potential coalesces into nascent concepts."@en ,
                                          "Pd2: Pertains to intuition, ideation, and the 'spark' of novel insight and meaning-generation. It contributes to generating new insights during active reframing."@en ,
                                          "The primordial threshold where undifferentiated mental potential transforms into recognizable ideational forms. It facilitates spontaneous insight, holistic pattern recognition, and non-linear synthesis, serving as the subconscious wellspring of wisdom and intellect."@en ,
                                          "The second stratum of the Primary Modality, where abstract potential coalesces into intuitive, pre-linguistic ideas."@en ,
                                          "The capacity for rapid, pre-verbal insight, generative ideation, and the initial formation of raw concepts." ;
                             rdfs:label "Psycho-Conceptive Dimension (Pd2)"@en ,
                                        "Psycho-Conceptive Dimension (Pd2)" ;
                             skos:altLabel "Psycho-Conceptive Processing"@en .


###  https://tuos.org/qm#PsychoEmpathicDimension
qm:PsychoEmpathicDimension rdf:type owl:Class ;
                           rdfs:subClassOf qm:PsychodynamicDimension ,
                                           qm:SecondaryModality ,
                                           [ rdf:type owl:Restriction ;
                                             owl:onProperty qm:dependsOn ;
                                             owl:someValuesFrom qm:PrimeModality
                                           ] ,
                                           [ rdf:type owl:Restriction ;
                                             owl:onProperty qm:isBalancedBy ;
                                             owl:someValuesFrom qm:PsychoProtectiveDimension
                                           ] ,
                                           [ rdf:type owl:Restriction ;
                                             owl:onProperty qm:isSourceOf ;
                                             owl:someValuesFrom qm:IntersubjectiveResonance
                                           ] ,
                                           [ rdf:type owl:Restriction ;
                                             owl:onProperty qm:initiatesModality ;
                                             owl:hasValue qm:M2
                                           ] ;
                           rdfs:comment "An expansive cognitive state promoting creative association, cognitive flexibility, and openness; the foundation for empathy and compassion. It is the foundational source of love and compassion, driving intersubjective resonance."@en ,
                                        "Pd4: The dimension of affection, love, and compassion."@en ,
                                        "The dimension of affection, love, and compassion. It embodies the capacity for authentic connection and emotional resonance with others and serves as the foundation for human connection."@en ,
                                        "The fourth dimension and inaugural element of the Secondary Modality, representing the origin of love, compassion, and empathy, and providing feeling intelligence."@en ,
                                        "The dimension of expansive emotional connection, capacity for altruism, and the compassionate drive for growth and connection with others." ;
                           rdfs:label "Psycho-Empathic Dimension (Pd4)"@en ,
                                      "Psycho-Empathic Dimension (Pd4)" .


###  https://tuos.org/qm#PsychoFoundationalDimension
qm:PsychoFoundationalDimension rdf:type owl:Class ;
                               rdfs:subClassOf qm:PsychodynamicDimension ,
                                               qm:SecondaryModality ,
                                               [ rdf:type owl:Restriction ;
                                                 owl:onProperty qm:contains ;
                                                 owl:someValuesFrom qm:SubconsciousInfrastructure
                                               ] ,
                                               [ rdf:type owl:Restriction ;
                                                 owl:onProperty qm:operatesThrough ;
                                                 owl:someValuesFrom qm:PsychoFoundationalEncoding
                                               ] ,
                                               [ rdf:type owl:Restriction ;
                                                 owl:onProperty qm:servesAs ;
                                                 owl:someValuesFrom qm:GroundingFunction
                                               ] ;
                               rdfs:comment "Pd9: The dimension of familiarity, values, belonging, and moral grounding."@en ,
                                            "The dimension of familiarity, values, belonging, and moral grounding. It is crucial for learning consolidation, memory integration, and translating abstract knowledge into practical, actionable intelligence, serving as a critical link between mental and physical realms."@en ,
                                            "The function for learning consolidation, memory integration, and translating abstract knowledge into practical, actionable intelligence. It serves as the bedrock of emotional architecture and the primary conduit for internal states to achieve concrete expression."@en ,
                                            "The ninth dimension, which specifically integrates learning and grounds awareness in practical, actionable intelligence."@en ,
                                            "The deepest layers of the subconscious, primal drives, energetic libido, and the fundamental energetic basis that structures personality." ;
                               rdfs:label "Psycho-Foundational Dimension (Pd9)"@en ,
                                          "Psycho-Foundational Dimension (Pd9)" .


###  https://tuos.org/qm#PsychoFoundationalEncoding
qm:PsychoFoundationalEncoding rdf:type owl:Class ;
                              rdfs:subClassOf qm:ProcessingMechanism ;
                              rdfs:comment "A foundational cognitive function that consolidates memory, encodes experiential learning, and translates abstract knowledge into practical, actionable intelligence."@en ;
                              rdfs:label "Psycho-Foundational Encoding"@en .


###  https://tuos.org/qm#PsychoMeditativeCollapse
qm:PsychoMeditativeCollapse rdf:type owl:Class ;
                            rdfs:subClassOf qm:PsychodynamicCollapse ;
                            rdfs:comment "A specific form of Cognitive Collapse wherein mental potential transforms into Actualized Experience through contemplative engagement, mediated by the Observer Function."@en .


###  https://tuos.org/qm#PsychoMeditativeDimension
qm:PsychoMeditativeDimension rdf:type owl:Class ;
                             rdfs:subClassOf qm:PsychodynamicDimension ,
                                             [ rdf:type owl:Restriction ;
                                               owl:onProperty qm:enables ;
                                               owl:someValuesFrom qm:Contemplation
                                             ] ,
                                             [ rdf:type owl:Restriction ;
                                               owl:onProperty qm:isLocusOf ;
                                               owl:someValuesFrom qm:IntentionalCollapse
                                             ] ,
                                             [ rdf:type owl:Restriction ;
                                               owl:onProperty qm:operatesThrough ;
                                               owl:someValuesFrom qm:AnalyticalReasoning
                                             ] ,
                                             [ rdf:type owl:Restriction ;
                                               owl:onProperty qm:providesFoundationFor ;
                                               owl:allValuesFrom qm:SecondaryModality
                                             ] ,
                                             [ rdf:type owl:Restriction ;
                                               owl:onProperty qm:receivesInputFrom ;
                                               owl:allValuesFrom qm:PsychoConceptiveDimension
                                             ] ;
                             rdfs:comment "Pd3: Encompasses cognition, reflection, and interpretive processing, facilitating learning and integrative understanding. It assists in analyzing situations from new perspectives during active reframing."@en ,
                                          "Pd3: Encompasses cognition, reflection, and interpretive processing, facilitating learning and integrative understanding. It assists in analyzing situations from new perspectives during reframing."@en ,
                                          "The structured, analytical cognitive function responsible for categorization, logical organization, and conceptual stabilization. It transforms intuitive insights from Pd2 into definite, coherent understanding and is the primary locus of 'cognitive collapse' and conscious intervention."@en ,
                                          "The structured, analytical cognitive function responsible for categorization, logical organization, and conceptual stabilization. It transforms intuitive insights into coherent understanding and integrates intellect and affect. It is the explicit locus of psycho-meditative collapse."@en ,
                                          "The structured, analytical cognitive function responsible for categorization, logical organization, and conceptual stabilization. This dimension transforms intuitive insights into coherent understanding and is the primary domain for conscious intervention in the psychodynamic collapse process."@en ,
                                          "The third stratum of the Prime Modality, serving as the primary seat of reason, structuring, and analytical comprehension."@en ,
                                          "The faculty for systematic thought, logical construction, and the analytical organization of ideas into coherent understanding." ;
                             rdfs:label "Psycho-Meditative Dimension (Pd3)"@en ,
                                        "Psycho-Meditative Dimension (Pd3)" .


###  https://tuos.org/qm#PsychoMeditativeStructuring
qm:PsychoMeditativeStructuring rdf:type owl:Class ;
                               rdfs:subClassOf qm:CognitiveMechanism .


###  https://tuos.org/qm#PsychoMotivationalDimension
qm:PsychoMotivationalDimension rdf:type owl:Class ;
                               rdfs:subClassOf qm:PsychodynamicDimension ,
                                               qm:SecondaryModality ,
                                               [ rdf:type owl:Restriction ;
                                                 owl:onProperty qm:actsAsChannelFor ;
                                                 owl:someValuesFrom qm:PsychodynamicDimension
                                               ] ,
                                               [ rdf:type owl:Restriction ;
                                                 owl:onProperty qm:embodies ;
                                                 owl:someValuesFrom qm:PsychoMotivationalMomentum
                                               ] ,
                                               [ rdf:type owl:Restriction ;
                                                 owl:onProperty qm:isSupportedByMechanism ;
                                                 owl:someValuesFrom qm:SustainedActionMechanism
                                               ] ,
                                               [ rdf:type owl:Restriction ;
                                                 owl:onProperty qm:translatesValuesInto ;
                                                 owl:someValuesFrom qm:SustainedAction
                                               ] ;
                               rdfs:comment "Forward-projecting cognitive energy responsible for sustaining motivation, fostering cognitive endurance, and enabling long-term pattern recognition for achieving goals across extended time periods."@en ,
                                            "Pd7: The dimension of purpose, drive, and long-term ambition."@en ,
                                            "The dimension of purpose, drive, and long-term ambition. It represents forward-projecting cognitive energy for sustaining motivation, cognitive endurance, and achieving long-term goals, translating internal values into consistent external action."@en ,
                                            "The wellspring of instinctual drives, persistent willpower, and the energetic force that propels action and perseverance." ;
                               rdfs:label "Psycho-Motivational Dimension (Pd7)"@en ,
                                          "Psycho-Motivational Dimension (Pd7)" .


###  https://tuos.org/qm#PsychoMotivationalMomentum
qm:PsychoMotivationalMomentum rdf:type owl:Class ;
                              rdfs:subClassOf qm:SecondaryModalityCategory ;
                              rdfs:comment "A specialized form of forward-projecting cognitive energy responsible for sustaining motivation and endurance through challenges."@en ;
                              rdfs:label "Psycho-Motivational Momentum"@en .


###  https://tuos.org/qm#PsychoProtectiveDimension
qm:PsychoProtectiveDimension rdf:type owl:Class ;
                             rdfs:subClassOf qm:PsychodynamicDimension ,
                                             qm:SecondaryModality ,
                                             [ rdf:type owl:Restriction ;
                                               owl:onProperty qm:embodiesPrinciple ;
                                               owl:someValuesFrom qm:ProtectivePrinciple
                                             ] ,
                                             [ rdf:type owl:Restriction ;
                                               owl:onProperty qm:isArchitectOf ;
                                               owl:someValuesFrom qm:PsychologicalStructure
                                             ] ,
                                             [ rdf:type owl:Restriction ;
                                               owl:onProperty qm:isBalancedBy ;
                                               owl:someValuesFrom qm:PsychoEmpathicDimension
                                             ] ;
                             rdfs:comment "Cognitive mechanisms regulating decision-making and maintaining psychological coherence through inhibition, boundary formation, and selective focus. It embodies principles of measure, limit, and restraint."@en ,
                                          "Pd5: The dimension of power, fear, and boundaries."@en ,
                                          "The dimension of power, fear, and boundaries. It regulates decision-making and maintains psychological coherence through inhibition and selective focus, embodying principles of measure, limit, and restraint."@en ,
                                          "The fifth dimension, embodying qualities of discernment, appropriate boundaries, healthy limits, and protective judgment."@en ,
                                          "The ability for setting and maintaining boundaries, exercising self-discipline, and containing psychic energy or impulses." ;
                             rdfs:label "Psycho-Protective Dimension (Pd5)"@en ,
                                        "Psycho-Protective Dimension (Pd5)" .


###  https://tuos.org/qm#PsychoReceptiveDimension
qm:PsychoReceptiveDimension rdf:type owl:Class ;
                            rdfs:subClassOf qm:PsychodynamicDimension ,
                                            qm:SecondaryModality ,
                                            [ rdf:type owl:Restriction ;
                                              owl:onProperty qm:enablesConversionOf ;
                                              owl:someValuesFrom qm:AbstractInternalExperience
                                            ] ,
                                            [ rdf:type owl:Restriction ;
                                              owl:onProperty qm:hasCapacityFor ;
                                              owl:someValuesFrom qm:EmotionalOpenness
                                            ] ,
                                            [ rdf:type owl:Restriction ;
                                              owl:onProperty qm:receivesInputFrom ;
                                              owl:someValuesFrom qm:PsychosocialEmotiveTriad
                                            ] ;
                            rdfs:comment "A sophisticated cognitive self-correction mechanism for refining perception, reassessing beliefs, and enhancing precision through feedback integration. It functions as an essential cognitive self-correction mechanism, continuously refining perception and prompting reassessment of established beliefs."@en ,
                                         "Pd8: The dimension of realization, perceptual clarity, and receptivity."@en ,
                                         "The dimension of realization, perceptual clarity, and receptivity. It functions as a cognitive self-correction mechanism for refining perception and reassessing beliefs through feedback integration, bridging abstract principles to practical living."@en ,
                                         "The eighth dimension, which refines perception, reassesses beliefs, and enhances precision through feedback integration."@en ,
                                         "The capacity for intellectual assimilation, structured communication, and the formal expression or reception of thought." ;
                            rdfs:label "Psycho-Receptive Dimension (Pd8)"@en ,
                                       "Psycho-Receptive Dimension (Pd8)" .


###  https://tuos.org/qm#PsychoTranspersonalDimension
qm:PsychoTranspersonalDimension rdf:type owl:Class ;
                                rdfs:subClassOf qm:PsychodynamicDimension ,
                                                qm:SecondaryModality ,
                                                [ rdf:type owl:Restriction ;
                                                  owl:onProperty qm:isNegatedBy ;
                                                  owl:someValuesFrom qm:PsychoVolitionalDimension
                                                ] ;
                                rdfs:comment "Pd10: This passive dimension acts as a conduit for collective influence and external resonance, allowing the final state of M2 to be expressed unless negated by the Psycho-Volitional dimension (Pd1)."@en ,
                                             "Responsible for externalizing internalized awareness into actionable, observable behavior within the physical world. It represents the ultimate manifestation of consciousness development within temporal reality."@en ,
                                             "The dimension representing the ultimate manifestation of consciousness development in temporal reality. It is a passive conduit that receives, integrates, and expresses the synthesized energies of the preceding nine dimensions, serving as the interface between internal psychodynamic systems and external reality."@en ,
                                             "The tenth dimension, representing the ultimate manifestation of consciousness development within temporal reality by externalizing awareness into observable behavior."@en ,
                                             "The interface with manifested reality, concrete action, and the experience of the physical world." ;
                                rdfs:label "Psycho-Transpersonal Dimension (Pd10)"@en ,
                                           "Psycho-Transpersonal Dimension (Pd10)" .


###  https://tuos.org/qm#PsychoVolitionalDimension
qm:PsychoVolitionalDimension rdf:type owl:Class ;
                             rdfs:subClassOf qm:PsychodynamicDimension ,
                                             [ rdf:type owl:Restriction ;
                                               owl:onProperty qm:dissolves ;
                                               owl:someValuesFrom qm:PerceivedLimitation
                                             ] ,
                                             [ rdf:type owl:Restriction ;
                                               owl:onProperty qm:embodies ;
                                               owl:someValuesFrom qm:PurePotentiality
                                             ] ,
                                             [ rdf:type owl:Restriction ;
                                               owl:onProperty qm:hasPrimacyOver ;
                                               owl:someValuesFrom qm:PsychodynamicDimension
                                             ] ,
                                             [ rdf:type owl:Restriction ;
                                               owl:onProperty qm:isSegregatedBy ;
                                               owl:someValuesFrom qm:OntologicalFirewall
                                             ] ,
                                             [ rdf:type owl:Restriction ;
                                               owl:onProperty qm:isSourceOf ;
                                               owl:someValuesFrom qm:Will
                                             ] ,
                                             [ rdf:type owl:Restriction ;
                                               owl:onProperty qm:isSubjectTo ;
                                               owl:someValuesFrom qm:EmpiricalAbsence
                                             ] ,
                                             [ rdf:type owl:Restriction ;
                                               owl:onProperty qm:providesFoundationFor ;
                                               owl:someValuesFrom qm:PsychoConceptiveDimension
                                             ] ;
                             rdfs:comment "Embodies unified awareness and primal will; serves as the organizing principle, dissolves limitations, and governs intention formation. It is the absolute genesis of cognitive activity and a state of pure potentiality, pre-cognitive and pre-emotional. It possesses an 'annihilative' property to dissolve perceived limitations."@en ,
                                          "Pd1: Embodies will, drive, and decision-making, representing intentional action. It is specifically involved in the active reframing process by shifting attention."@en ,
                                          "The absolute genesis of cognitive activity and a state of pure potentiality. It embodies pure consciousness and primal will, serving as the organizing principle and the ultimate source of all creative thought. It possesses 'annihilative' properties to dissolve perceived limitations and is considered the highest point on the 'vertical map of consciousness'."@en ,
                                          "The apex of consciousness architecture, embodying unified awareness and primal will. It is the ultimate source of pure potentiality, desire, self-determination, and creative thought, serving as the primary organizing principle and initiating force for all subsequent mental phenomena. It possesses an 'annihilative property,' dissolving perceived limitations."@en ,
                                          "The first and most fundamental stratum of the Primary Modality, serving as the absolute origin of will and potential."@en ,
                                          "Represents the fundamental origin of psychic energy, primal intentionality, and the source of consciousness." ;
                             rdfs:label "Psycho-Volitional Dimension (Pd1)"@en ,
                                        "Psycho-Volitional Dimension (Pd1)" .


###  https://tuos.org/qm#PsychoVolitionalDynamics
qm:PsychoVolitionalDynamics rdf:type owl:Class ;
                            rdfs:subClassOf qm:Phenomenon .


###  https://tuos.org/qm#PsychoVolitionalField
qm:PsychoVolitionalField rdf:type owl:Class ;
                         rdfs:subClassOf qm:PrimeModality ;
                         rdfs:label "Psycho-Volitional Field"@en .


###  https://tuos.org/qm#PsychodynamicBalanceRestoration
qm:PsychodynamicBalanceRestoration rdf:type owl:Class ;
                                   rdfs:subClassOf qm:MainStrategiesCategory ,
                                                   [ rdf:type owl:Restriction ;
                                                     owl:onProperty qm:targets ;
                                                     owl:hasValue qm:CalculatedTurbulence
                                                   ] ;
                                   rdfs:comment "Methodologies focused on achieving Harmonic Alignment among the ten Psychodynamic Dimensions, based on the understanding that psychological distress often stems from an imbalance within this dynamic dimensional network."@en ;
                                   rdfs:label "Psychodynamic Balance Restoration"@en .


###  https://tuos.org/qm#PsychodynamicCollapse
qm:PsychodynamicCollapse rdf:type owl:Class ;
                         rdfs:subClassOf qm:PsychodynamicWaveCollapse ,
                                         [ rdf:type owl:Restriction ;
                                           owl:onProperty qm:hasMode ;
                                           owl:someValuesFrom qm:CollapseMode
                                         ] ,
                                         [ rdf:type owl:Restriction ;
                                           owl:onProperty qm:isTriggeredBy ;
                                           owl:someValuesFrom qm:ConsciousAttention
                                         ] ;
                         rdfs:comment "The fundamental transition where probabilistic, multi-state pre-conscious mental phenomena (cognitive superposition) resolve into singular, definite, and consciously experienced outcomes, forming subjective reality. Conscious attention acts as the primary catalyst."@en ,
                                      "The fundamental transition whereby a mental or cognitive system moves from a state of indeterminacy or superposition into a singular, definite, and consciously experienced outcome, triggered by sustained attention."@en ;
                         skos:altLabel "Cognitive Solidification"@en ,
                                       "Present Collapse of Perception"@en ,
                                       "Cognitive Collapse" ,
                                       "Wave Function Collapse" .


###  https://tuos.org/qm#PsychodynamicDimension
qm:PsychodynamicDimension rdf:type owl:Class ;
                          rdfs:subClassOf qm:PsychodynamicDimensionsCategory ,
                                          [ rdf:type owl:Restriction ;
                                            owl:onProperty qm:formsFoundationOf ;
                                            owl:someValuesFrom qm:ConsciousAwareness
                                          ] ,
                                          [ rdf:type owl:Restriction ;
                                            owl:onProperty qm:formsFoundationOf ;
                                            owl:someValuesFrom qm:PersonalityOrganization
                                          ] ,
                                          [ rdf:type owl:Restriction ;
                                            owl:onProperty qm:functionsAs ;
                                            owl:someValuesFrom qm:FundamentalEnergeticSubstrate
                                          ] ,
                                          [ rdf:type owl:Restriction ;
                                            owl:onProperty qm:mutuallyInfluences ;
                                            owl:someValuesFrom qm:PsychodynamicDimension
                                          ] ,
                                          [ rdf:type owl:Restriction ;
                                            owl:onProperty qm:shapes ;
                                            owl:someValuesFrom qm:PsychologicalPhenomenon
                                          ] ;
                          rdfs:comment "The elemental 'quanta' or irreducible building blocks of mental and emotional life. They are conceptualized as fundamental energetic substrates from which cognitions, emotions, and motivations emerge, forming the substance of conscious awareness and the structural foundation of personality organization."@en ,
                                       "The fundamental, discrete, and elementary 'quanta' of mental and emotional life. These are the irreducible core units from which the entire spectrum of subjective experience is constructed. This is a formal, conceptual model, not a model of brain computation."@en ,
                                       "The irreducible core units or 'quanta' of mental and emotional life."@en ,
                                       "A conceptual category representing various aspects of the psyche based on psychodynamic theory." ;
                          rdfs:label "Psychodynamic Dimension (Pdj)"@en ,
                                     "Psychodynamic Dimension (Pdj)" ,
                                     "Psychodynamic Dimension Category" ;
                          rdfs:subClassOf "Psychodynamic Model"@en ;
                          skos:altLabel "Cognitive Quanta"@en .


###  https://tuos.org/qm#PsychodynamicDimensionsCategory
qm:PsychodynamicDimensionsCategory rdf:type owl:Class ;
                                   rdfs:comment "Conceptual container for psychodynamic dimensions, serving as the elementary 'quanta' of mental life."@en ;
                                   rdfs:label "Psychodynamic Dimensions (QM_Quantum / Cognitive Quanta)"@en .


###  https://tuos.org/qm#PsychodynamicFriction
qm:PsychodynamicFriction rdf:type owl:Class ;
                         rdfs:subClassOf qm:CognitiveStrainAndDysfunction ,
                                         qm:UnresolvedSuperpositionConsequence ;
                         rdfs:label "Psychodynamic Friction"@en .


###  https://tuos.org/qm#PsychodynamicHarmonicAlignment
qm:PsychodynamicHarmonicAlignment rdf:type owl:Class ;
                                  rdfs:subClassOf qm:SecondaryModalityCategory ;
                                  rdfs:comment "A state of optimal psychological functioning characterized by the harmonious interaction and unified operation of all dimensional capacities."@en ;
                                  rdfs:label "Psychodynamic Harmonic Alignment"@en .


###  https://tuos.org/qm#PsychodynamicNavigation
qm:PsychodynamicNavigation rdf:type owl:Class ;
                           rdfs:subClassOf qm:AdvancedPracticesAndMethodologiesCategory ;
                           rdfs:comment "The process of guiding oneself through multi-dimensional psychological structures, recognizing that experience unfolds across cognitive, emotional, somatic, and relational domains."@en ;
                           rdfs:label "Psychodynamic Navigation"@en .


###  https://tuos.org/qm#PsychodynamicWaveCollapse
qm:PsychodynamicWaveCollapse rdf:type owl:Class ;
                             rdfs:subClassOf qm:CoreConceptsCategory ,
                                             qm:PsychodynamicWaveCollapse ;
                             rdfs:comment "The fundamental transition whereby a mental or cognitive system moves from a state of indeterminacy, superposition, or fluctuation into a singular, definite, and consciously experienced outcome. It is the pivotal process where the mind's probabilistic field resolves into a specific, actualized experience."@en ,
                                          "The process by which potential psychodynamic states resolve into a definitive conscious experience, analogous to quantum wave function collapse."@en ;
                             rdfs:label "Psychodynamic Wave Collapse"@en ;
                             skos:altLabel "Cognitive Solidification"@en ,
                                           "Cognitive Collapse" ,
                                           "Experiential Collapse" ,
                                           "Present Collapse of Perception" ,
                                           "Quantum Collapse Process" ,
                                           "Wave Function Collapse" .


###  https://tuos.org/qm#PsychologicalDisharmony
qm:PsychologicalDisharmony rdf:type owl:Class ;
                           rdfs:subClassOf qm:Examples_Emergent ,
                                           [ rdf:type owl:Restriction ;
                                             owl:onProperty qm:arisesFrom ;
                                             owl:someValuesFrom qm:DestructiveInterference
                                           ] ;
                           rdfs:comment "A general category for psychological difficulties, emotional suffering, and cognitive inefficiencies, viewed as 'misaligned configurations' or 'patterns of interference or disharmony'."@en ;
                           rdfs:label "Psychological Disharmony"@en ;
                           skos:altLabel "Misaligned Configuration"@en .


###  https://tuos.org/qm#PsychologicalDysfunctionAndImbalance
qm:PsychologicalDysfunctionAndImbalance rdf:type owl:Class ;
                                        rdfs:subClassOf qm:ChallengesAndLimitations ,
                                                        qm:ChallengesAndLimitationsCategory ,
                                                        [ rdf:type owl:Restriction ;
                                                          owl:onProperty qm:stemsFrom ;
                                                          owl:someValuesFrom qm:DimensionalMisalignment
                                                        ] ;
                                        rdfs:comment "Mental health issues or lack of equilibrium that may be addressed or present challenges."@en ,
                                                     "States arising from specific patterns, imbalances, or misaligned configurations of the Psychodynamic Dimensions, leading to distress, inefficiency, or pathological expressions in an individual's psyche."@en ;
                                        rdfs:label "Psychological Dysfunction and Imbalance"@en .


###  https://tuos.org/qm#PsychologicalEntanglement
qm:PsychologicalEntanglement rdf:type owl:Class ;
                             rdfs:subClassOf qm:EpistemologicalChallenges ,
                                             qm:InfluentialFactor ;
                             rdfs:label "Psychological Entanglement"@en ;
                             skos:altLabel "Interpersonal Entanglement"@en ,
                                           "Cognitive Entanglement" .


###  https://tuos.org/qm#PsychologicalHeart
qm:PsychologicalHeart rdf:type owl:Class ;
                      rdfs:subClassOf qm:PsychoAestheticDimension ;
                      rdfs:comment "A role serving crucial regulatory functions that maintain psychological coherence and prevent systemic fragmentation."@en ;
                      rdfs:label "Psychological Heart"@en .


###  https://tuos.org/qm#PsychologicalPhenomenon
qm:PsychologicalPhenomenon rdf:type owl:Class ;
                           rdfs:subClassOf qm:OtherKeyConcepts ;
                           rdfs:comment "A general category for the experiential and behavioral manifestations that are shaped by Psychodynamic Dimensions."@en ;
                           rdfs:label "Psychological Phenomenon"@en .


###  https://tuos.org/qm#PsychologicalSelfSurgery
qm:PsychologicalSelfSurgery rdf:type owl:Class ;
                            rdfs:subClassOf qm:PracticesCategory .


###  https://tuos.org/qm#PsychologicalState
qm:PsychologicalState rdf:type owl:Class ;
                      rdfs:subClassOf qm:TherapeuticStrategy ;
                      rdfs:comment "Complex emergent patterns (e.g., anxiety, joy) understood not as monolithic entities but as multi-dimensional field collapses involving specific combinations and interactions of underlying Psychodynamic Dimensions."@en ;
                      rdfs:label "Psychological State"@en .


###  https://tuos.org/qm#PsychologicalStructure
qm:PsychologicalStructure rdf:type owl:Class ;
                          rdfs:subClassOf qm:PsychoProtectiveDimension ;
                          rdfs:comment "The overall order and equilibrium within an individual's internal world."@en ;
                          rdfs:label "Psychological Structure"@en .


###  https://tuos.org/qm#PsychologicalTransformationViaOntologicalReassignment
qm:PsychologicalTransformationViaOntologicalReassignment rdf:type owl:Class ;
                                                         rdfs:subClassOf qm:MainStrategiesCategory ,
                                                                         [ rdf:type owl:Restriction ;
                                                                           owl:onProperty qm:hasPractice ;
                                                                           owl:someValuesFrom qm:OntologicalRestructuring
                                                                         ] ;
                                                         rdfs:comment "A systematic and fundamental approach for restructuring an individual’s experiential relationship with both selfhood and reality itself."@en ;
                                                         rdfs:label "Psychological Transformation via Ontological Reassignment"@en .


###  https://tuos.org/qm#PsychosocialEmotiveTriad
qm:PsychosocialEmotiveTriad rdf:type owl:Class ;
                            rdfs:subClassOf qm:SecondaryModalityCategory ;
                            rdfs:comment "A triad of dimensions (Pd4, Pd5, Pd6) within the Secondary Modality that governs feeling states, relational dynamics, and social-emotional intelligence. Also known as the 'Realm of Feeling'."@en ;
                            rdfs:label "Psychosocial Emotive Triad"@en .


###  https://tuos.org/qm#PurePotentiality
qm:PurePotentiality rdf:type owl:Class ;
                    rdfs:subClassOf qm:PsychoVolitionalDimension ;
                    rdfs:label "Pure Potentiality"@en .


###  https://tuos.org/qm#PurposeRedefinition
qm:PurposeRedefinition rdf:type owl:Class ;
                       rdfs:subClassOf qm:PracticesCategory ;
                       rdfs:label "Purpose Redefinition"@en .


###  https://tuos.org/qm#QuantumDiplomacy
qm:QuantumDiplomacy rdf:type owl:Class ;
                    rdfs:subClassOf qm:QuantumPrinciple ,
                                    [ rdf:type owl:Restriction ;
                                      owl:onProperty qm:isAppliedTo ;
                                      owl:hasValue qm:QM_Quantum
                                    ] ;
                    rdfs:label "Quantum Diplomacy"@en .


###  https://tuos.org/qm#QuantumMindfulnessApplication
qm:QuantumMindfulnessApplication rdf:type owl:Class ;
                                 rdfs:subClassOf qm:MindfulnessApproachesComparisonCategory ,
                                                 qm:MindfulnessIntervention ,
                                                 [ rdf:type owl:Restriction ;
                                                   owl:onProperty qm:definesRoleOfObserverAs ;
                                                   owl:someValuesFrom qm:ObserverParticipantRole
                                                 ] ,
                                                 [ rdf:type owl:Restriction ;
                                                   owl:onProperty qm:hasEngagementStyle ;
                                                   owl:someValuesFrom qm:ActiveStructuralInvestigation
                                                 ] ,
                                                 [ rdf:type owl:Restriction ;
                                                   owl:onProperty qm:hasPractice ;
                                                   owl:someValuesFrom qm:PatternedPresence
                                                 ] ,
                                                 [ rdf:type owl:Restriction ;
                                                   owl:onProperty qm:hasViewOfPerception ;
                                                   owl:someValuesFrom qm:ActiveConstitutiveForceView
                                                 ] ,
                                                 [ rdf:type owl:Restriction ;
                                                   owl:onProperty qm:targets ;
                                                   owl:someValuesFrom qm:CognitiveAppraisalBias
                                                 ] ,
                                                 [ rdf:type owl:Restriction ;
                                                   owl:onProperty qm:targets ;
                                                   owl:someValuesFrom qm:ObservationValence
                                                 ] ,
                                                 [ rdf:type owl:Restriction ;
                                                   owl:onProperty qm:employs ;
                                                   owl:allValuesFrom qm:ActiveReframingProcess
                                                 ] ,
                                                 [ rdf:type owl:Restriction ;
                                                   owl:onProperty qm:targets ;
                                                   owl:allValuesFrom qm:InherentDisposition
                                                 ] ,
                                                 [ rdf:type owl:Restriction ;
                                                   owl:onProperty qm:targets ;
                                                   owl:allValuesFrom qm:ObservationValence
                                                 ] ,
                                                 [ rdf:type owl:Restriction ;
                                                   owl:onProperty qm:targets ;
                                                   owl:hasValue qm:CognitiveInfluence
                                                 ] ;
                                 rdfs:comment "A transformative or reframing practice aiming to actively generate positive outcomes by changing the foundation of perception and understanding the structure of consciousness. Its goal is 'active mastery' and 'perceptual freedom'."@en ,
                                              "An active/transformative practice aiming to make the Cognitive Appraisal positive by altering Valence(Ψ) through intentional reframing and, more profoundly, by altering the baseline Bias_M1 over time. It is a practice of meaning-generation."@en ;
                                 rdfs:label "Quantum Mindfulness (Active)"@en ,
                                            "Quantum Mindfulness Application"@en ,
                                            "Quantum Mindfulness (Active)" .


###  https://tuos.org/qm#QuantumObserver
qm:QuantumObserver rdf:type owl:Class ;
                   rdfs:subClassOf qm:QuantumPrinciple ,
                                   [ rdf:type owl:Restriction ;
                                     owl:onProperty qm:performs ;
                                     owl:someValuesFrom qm:CognitiveMeasurement
                                   ] ,
                                   [ rdf:type owl:Restriction ;
                                     owl:onProperty qm:practices ;
                                     owl:someValuesFrom qm:Contemplation
                                   ] ,
                                   [ rdf:type owl:Restriction ;
                                     owl:onProperty qm:isAppliedTo ;
                                     owl:hasValue qm:QM_Quantum
                                   ] ;
                   rdfs:comment "The conscious, self-aware aspect of individual awareness, capable of deliberate attention direction and intentional focus, acting as the primary catalyst in transforming potential states into actual experiences."@en ;
                   rdfs:label "Quantum Observer"@en .


###  https://tuos.org/qm#QuantumPerception
qm:QuantumPerception rdf:type owl:Class ;
                     rdfs:subClassOf qm:Perception ,
                                     [ rdf:type owl:Restriction ;
                                       owl:onProperty qm:isAppliedTo ;
                                       owl:hasValue qm:QM_Quantum
                                     ] ;
                     rdfs:label "Quantum Perception"@en .


###  https://tuos.org/qm#QuantumPrinciple
qm:QuantumPrinciple rdf:type owl:Class ;
                    rdfs:subClassOf qm:CoreConceptsCategory ,
                                    [ rdf:type owl:Restriction ;
                                      owl:onProperty qm:contrastsWith ;
                                      owl:someValuesFrom qm:ContinuousMentationModel
                                    ] ,
                                    [ rdf:type owl:Restriction ;
                                      owl:onProperty qm:describes ;
                                      owl:someValuesFrom qm:PsychodynamicCollapse
                                    ] ,
                                    [ rdf:type owl:Restriction ;
                                      owl:onProperty qm:isAppliedTo ;
                                      owl:someValuesFrom qm:PsychodynamicDimension
                                    ] ,
                                    [ rdf:type owl:Restriction ;
                                      owl:onProperty qm:isFundamentalUnitOf ;
                                      owl:someValuesFrom qm:PsychicArchitecture
                                    ] ;
                    rdfs:comment "A fundamental principle guiding the understanding and application of Quantum Mindfulness, often related to the observer's role or the nature of reality."@en ,
                                 "Refers to the most granular, operationally distinct constituent of psychic architecture. It signifies that subjective experience is not a continuous phenomenon, but is constituted by identifiable, discrete psychodynamic dimensions. The term is used conceptually to describe distinct experiential configurations."@en ;
                    rdfs:label "QM_Quantum"@en ,
                               "Quantum Principle"@en .


###  https://tuos.org/qm#RawPerceptualImprint
qm:RawPerceptualImprint rdf:type owl:Class ;
                        owl:equivalentClass qm:RawSensoryData ;
                        rdfs:subClassOf qm:Observation ,
                                        qm:ObservationComponentsCategory ;
                        rdfs:comment "Represents the initial, unprocessed strength or salience of the sensory or internal data. It is the 'raw signal strength' of the stimulus before any significant cognitive processing or interpretive layer has been applied."@en ,
                                     "Represents the initial, unprocessed strength or salience of the sensory or internal data; the 'raw signal strength'."@en ;
                        rdfs:label "Raw Perceptual Imprint (α)"@en ,
                                   "Raw Perceptual Imprint (α)" .


###  https://tuos.org/qm#RawSensoryData
qm:RawSensoryData rdf:type owl:Class ;
                  rdfs:subClassOf qm:ObservationComponentsCategory ;
                  rdfs:label "Raw Sensory Data"@en .


###  https://tuos.org/qm#ReConvergence
qm:ReConvergence rdf:type owl:Class ;
                 rdfs:subClassOf qm:PracticesCategory ;
                 rdfs:label "Re-Convergence"@en .


###  https://tuos.org/qm#RecognitionPhase
qm:RecognitionPhase rdf:type owl:Class ;
                    rdfs:subClassOf qm:LiberationProcess ;
                    rdfs:label "Phase 1: Recognition & Perceptual Distinction"@en .


###  https://tuos.org/qm#RelationalConsciousness
qm:RelationalConsciousness rdf:type owl:Class ;
                           rdfs:subClassOf qm:SecondhandExperience ;
                           rdfs:comment "Awareness of how one’s own psychological states are influenced by others and how one’s states influence those around them, crucial for navigating the subtle psychological influences inherent in secondhand experience."@en ;
                           rdfs:label "Relational Consciousness"@en .


###  https://tuos.org/qm#RelationalHealth
qm:RelationalHealth rdf:type owl:Class ;
                    rdfs:subClassOf qm:SecondaryModalityCategory ;
                    rdfs:comment "The capacity to form relationships characterized by trust, emotional attunement, and mutual support."@en ;
                    rdfs:label "Relational Health"@en .


###  https://tuos.org/qm#RelationalMindfulness
qm:RelationalMindfulness rdf:type owl:Class ;
                         rdfs:subClassOf qm:CollapseInfluencePractice .


###  https://tuos.org/qm#RelevanceFunction
qm:RelevanceFunction rdf:type owl:Class ;
                     rdfs:subClassOf qm:ObservationComponentsCategory ;
                     rdfs:comment "A function that quantifies how directly the content of an Observation (Ψ) relates to each specific psychodynamic dimension (Pd_j), determining the strength of the Observation Influence (I_Ψj) on Dimensional Activation."@en ;
                     rdfs:label "Relevance Function (Relevance(Ψ, Pd_j))"@en ,
                                "Relevance Function (Relevance(Ψ, Pdj))"@en ,
                                "Relevance Function (Relevance(Ψ, Pdj))" .


###  https://tuos.org/qm#ReligiousFluidity
qm:ReligiousFluidity rdf:type owl:Class ;
                     rdfs:subClassOf qm:GoalsCategory ;
                     rdfs:comment "The capacity of the QM framework to integrate with diverse spiritual and philosophical orientations without requiring adherence to new doctrines."@en ;
                     rdfs:label "Religious Fluidity"@en .


###  https://tuos.org/qm#Reputation
qm:Reputation rdf:type owl:Class ;
              rdfs:subClassOf qm:InfluentialFactor ;
              rdfs:label "Reputation"@en .


###  https://tuos.org/qm#RequiredTrainingAndCapacity
qm:RequiredTrainingAndCapacity rdf:type owl:Class ;
                               rdfs:subClassOf qm:PracticalLimitationsOfQMApplication ;
                               rdfs:label "Required Training and Capacity Development"@en .


###  https://tuos.org/qm#ResolutionFatigue
qm:ResolutionFatigue rdf:type owl:Class ;
                     rdfs:subClassOf qm:CognitiveStrainAndDysfunction ,
                                     qm:PsychologicalDisharmony .


###  https://tuos.org/qm#ResponseRePatterning
qm:ResponseRePatterning rdf:type owl:Class ;
                        rdfs:subClassOf qm:CognitiveOptimization ;
                        rdfs:label "Response Re-Patterning"@en .


###  https://tuos.org/qm#ReverseEngineeringCollapsePatterns
qm:ReverseEngineeringCollapsePatterns rdf:type owl:Class ;
                                      rdfs:subClassOf qm:CollapseInfluencePractice ;
                                      rdfs:label "Reverse Engineering Collapse Patterns"@en .


###  https://tuos.org/qm#ReverseEngineeringEmotionalStates
qm:ReverseEngineeringEmotionalStates rdf:type owl:Class ;
                                     rdfs:subClassOf qm:CognitiveOptimization .


###  https://tuos.org/qm#SecondaryModality
qm:SecondaryModality rdf:type owl:Class ;
                     rdfs:subClassOf qm:SecondaryModalityCategory ,
                                     [ rdf:type owl:Restriction ;
                                       owl:onProperty qm:canDurablyAlter ;
                                       owl:someValuesFrom qm:TraitVariable
                                     ] ,
                                     [ rdf:type owl:Restriction ;
                                       owl:onProperty qm:isModulatedBy ;
                                       owl:someValuesFrom qm:PrimeModality
                                     ] ,
                                     [ rdf:type owl:Restriction ;
                                       owl:onProperty qm:canDurablyAlter ;
                                       owl:allValuesFrom qm:TraitVariable
                                     ] ,
                                     [ rdf:type owl:Restriction ;
                                       owl:onProperty qm:composedOf ;
                                       owl:hasValue qm:Pd10
                                     ] ,
                                     [ rdf:type owl:Restriction ;
                                       owl:onProperty qm:composedOf ;
                                       owl:hasValue qm:Pd4
                                     ] ,
                                     [ rdf:type owl:Restriction ;
                                       owl:onProperty qm:composedOf ;
                                       owl:hasValue qm:Pd5
                                     ] ,
                                     [ rdf:type owl:Restriction ;
                                       owl:onProperty qm:composedOf ;
                                       owl:hasValue qm:Pd6
                                     ] ,
                                     [ rdf:type owl:Restriction ;
                                       owl:onProperty qm:composedOf ;
                                       owl:hasValue qm:Pd7
                                     ] ,
                                     [ rdf:type owl:Restriction ;
                                       owl:onProperty qm:composedOf ;
                                       owl:hasValue qm:Pd8
                                     ] ,
                                     [ rdf:type owl:Restriction ;
                                       owl:onProperty qm:composedOf ;
                                       owl:hasValue qm:Pd9
                                     ] ;
                     rdfs:comment "Comprises Pd4-Pd10 and articulates the complex processes through which foundational cognitive functions manifest and interact within lived experience and observable behavior, shaping the affective, social, and relational texture of experience."@en ,
                                  "Comprises Pd4-Pd10 and shapes the affective, social, and relational texture of experience. It is particularly implicated in the 'Practice Becomes Belief' mechanism."@en ,
                                  "Consists of the seven Psychodynamic Dimensions (Pd4-Pd10) that are modulated by the output of the Prime Modality and are responsible for shaping the affective, social, and relational texture of experience."@en ;
                     rdfs:label "Secondary Modality (M2)"@en ,
                                "Secondary Modality (M2)" ;
                     rdfs:subClassOf "Psychodynamic Model"@en .


###  https://tuos.org/qm#SecondaryModalityCategory
qm:SecondaryModalityCategory rdf:type owl:Class ;
                             rdfs:subClassOf qm:PsychodynamicDimensionsCategory ;
                             rdfs:comment "Conceptual container for the Secondary Modality dimensions, shaping affective, social, and relational experience."@en ;
                             rdfs:label "Secondary Modality (M2)"@en .


###  https://tuos.org/qm#SecondhandExperience
qm:SecondhandExperience rdf:type owl:Class ;
                        rdfs:subClassOf qm:CoreConceptsCategory ,
                                        qm:EpistemologicalChallenges ,
                                        qm:InfluentialFactor ,
                                        [ rdf:type owl:Restriction ;
                                          owl:onProperty qm:isMediatedBy ;
                                          owl:someValuesFrom qm:Perception
                                        ] ;
                        rdfs:comment "Experiences or information acquired indirectly, through others' accounts, media, or cultural narratives, rather than direct personal encounter."@en ,
                                     "The complex web of information, narratives, and interpretations transmitted through others, representing knowledge acquired indirectly beyond immediate personal sensory perception."@en ;
                        rdfs:label "Secondhand Experience"@en .


###  https://tuos.org/qm#SelectivePermeability
qm:SelectivePermeability rdf:type owl:Class ;
                         rdfs:subClassOf qm:PsychoReceptiveDimension ;
                         rdfs:comment "The ability to discern which information deserves attention and integration, operating as a cognitive self-correction mechanism."@en ;
                         rdfs:label "Selective Permeability"@en .


###  https://tuos.org/qm#SelfAsDynamicObserverParticipant
qm:SelfAsDynamicObserverParticipant rdf:type owl:Class ;
                                    rdfs:subClassOf qm:ObserverParticipantDynamic ,
                                                    [ rdf:type owl:Restriction ;
                                                      owl:onProperty qm:leadsTo ;
                                                      owl:someValuesFrom qm:PerceptualFreedom
                                                    ] ;
                                    rdfs:comment "An evolved state of being where an individual moves from predominantly reactive modes to a proactive, co-creative stance toward experience, involving the conscious recognition of one’s inherent role in reality construction."@en ;
                                    rdfs:label "Self as Dynamic Observer-Participant"@en .


###  https://tuos.org/qm#SelfConceptConstruction
qm:SelfConceptConstruction rdf:type owl:Class ;
                           rdfs:subClassOf qm:GoalsCategory ;
                           rdfs:comment "The conscious participation in identity formation by identifying, choosing, and integrating aspects of self in alignment with evolving values."@en ;
                           rdfs:label "Self-Concept Construction"@en .


###  https://tuos.org/qm#SelfIntegrity
qm:SelfIntegrity rdf:type owl:Class ;
                 rdfs:subClassOf qm:PsychoProtectiveDimension ;
                 rdfs:comment "The preservation of core beliefs, values, and identity structures."@en ;
                 rdfs:label "Self Integrity"@en .


###  https://tuos.org/qm#SharedReality
qm:SharedReality rdf:type owl:Class ;
                 rdfs:subClassOf qm:ExperiencedReality ;
                 rdfs:comment "A collectively negotiated framework for reality emerging through language, culture, and social interaction."@en ;
                 rdfs:label "Shared Reality"@en .


###  https://tuos.org/qm#SigmoidFunction
qm:SigmoidFunction rdf:type owl:Class ;
                   rdfs:subClassOf qm:DimensionalActivationInfluencesCategory .


###  https://tuos.org/qm#SocialInfluence
qm:SocialInfluence rdf:type owl:Class ;
                   rdfs:subClassOf qm:InfluentialFactor .


###  https://tuos.org/qm#SomaticLiteracy
qm:SomaticLiteracy rdf:type owl:Class ;
                   rdfs:subClassOf qm:PerceptualGoal ;
                   rdfs:comment "The cultivated capacity to read and work with the subtle energies of consciousness as manifested in the body."@en ;
                   rdfs:label "Somatic Literacy"@en .


###  https://tuos.org/qm#SovereignArchitecture
qm:SovereignArchitecture rdf:type owl:Class ;
                         rdfs:subClassOf qm:DecouplingPhase ;
                         rdfs:comment "An individual's internal locus of control, volitional capacity, and self-mastery."@en ,
                                      "The positive outcome of script liberation, characterized by internal self-mastery, volitional control, dimensional awareness, and self-originated thought and action."@en ;
                         rdfs:label "Sovereign Architecture"@en .


###  https://tuos.org/qm#StandardizedProtocol
qm:StandardizedProtocol rdf:type owl:Class ;
                        rdfs:subClassOf qm:AdvancedPracticesAndMethodologiesCategory ;
                        rdfs:label "Standardized Protocol"@en .


###  https://tuos.org/qm#StochasticInfluence
qm:StochasticInfluence rdf:type owl:Class ;
                       rdfs:subClassOf qm:DimensionalActivationInfluence ,
                                       qm:DimensionalActivationInfluencesCategory ;
                       rdfs:comment "Represents an inherent element of randomness, noise, or unpredictability within mental processes for each dimension (εj), acknowledging that consciousness is not perfectly deterministic."@en ,
                                    "Represents an inherent element of randomness, noise, or unpredictability within mental processes."@en ,
                                    "Represents the inherent element of randomness, noise, or unpredictability within mental processes for each dimension."@en ;
                       rdfs:label "Stochastic Influence (εj)"@en ,
                                  "Stochastic Influence (εj)" .


###  https://tuos.org/qm#StrategicAttentionManagement
qm:StrategicAttentionManagement rdf:type owl:Class ;
                                rdfs:subClassOf qm:CognitiveOptimization ;
                                rdfs:label "Strategic Attention Management"@en .


###  https://tuos.org/qm#StrategicCognitiveTrajectoryManipulation
qm:StrategicCognitiveTrajectoryManipulation rdf:type owl:Class ;
                                            rdfs:subClassOf qm:CognitiveOptimization .


###  https://tuos.org/qm#StrategicWaveformArchitecture
qm:StrategicWaveformArchitecture rdf:type owl:Class ;
                                 rdfs:subClassOf qm:CollapseInfluencePractice ;
                                 rdfs:label "Strategic Waveform Architecture"@en .


###  https://tuos.org/qm#StructuralAwareness
qm:StructuralAwareness rdf:type owl:Class ;
                       rdfs:subClassOf qm:HumanCapacitiesCategory ;
                       rdfs:comment "The ability to discern the intricate contributions of each psychodynamic dimension within a seemingly monolithic feeling, essential for conscious influence and transformation within the Quantum Mindfulness framework."@en ,
                                    "The ability to discern the intricate contributions of each psychodynamic dimension within a seemingly monolithic feeling, essential for conscious influence and transformation."@en ;
                       rdfs:label "Structural Awareness"@en .


###  https://tuos.org/qm#StructuralIntrospection
qm:StructuralIntrospection rdf:type owl:Class ;
                           rdfs:subClassOf qm:PracticesCategory .


###  https://tuos.org/qm#StructuredUnderstanding
qm:StructuredUnderstanding rdf:type owl:Class ;
                           rdfs:subClassOf qm:PsychoMeditativeDimension ,
                                           [ rdf:type owl:Restriction ;
                                             owl:onProperty qm:isCultivatedBy ;
                                             owl:hasValue qm:Contemplation
                                           ] ;
                           rdfs:comment "A mode of comprehension that encompasses the deep organizational principles underlying experiential phenomena, combining intuitive insight with analytical clarity."@en ;
                           rdfs:label "Structured Understanding"@en .


###  https://tuos.org/qm#SubDynamicInterference
qm:SubDynamicInterference rdf:type owl:Class ;
                          rdfs:subClassOf qm:PsychologicalDysfunctionAndImbalance ;
                          rdfs:label "Sub-dynamic Interference"@en .


###  https://tuos.org/qm#SubconsciousInfrastructure
qm:SubconsciousInfrastructure rdf:type owl:Class ;
                              rdfs:subClassOf qm:PsychoFoundationalDimension ;
                              rdfs:comment "The 'hidden architecture' comprising deeply ingrained emotional responses, automatic behavioral patterns, and unconscious assumptions."@en ;
                              rdfs:label "Subconscious Infrastructure"@en .


###  https://tuos.org/qm#SuperpositionCultivationMethod
qm:SuperpositionCultivationMethod rdf:type owl:Class ;
                                  rdfs:subClassOf qm:CultivationMethod ;
                                  rdfs:comment "A practice for skillfully working with Cognitive Superposition, such as meditation or cognitive non-attachment."@en ;
                                  rdfs:label "Superposition Cultivation Method"@en .


###  https://tuos.org/qm#SuperpositionalCognition
qm:SuperpositionalCognition rdf:type owl:Class ;
                            rdfs:subClassOf qm:CognitiveCapacity ,
                                            qm:CognitiveMechanism ;
                            rdfs:comment "An advanced cognitive capacity involving the intentional maintenance of multiple perspectives and possibilities without premature collapse."@en ;
                            rdfs:label "Superpositional Cognition"@en .


###  https://tuos.org/qm#SuperpositionalCognitiveEngineering
qm:SuperpositionalCognitiveEngineering rdf:type owl:Class ;
                                       rdfs:subClassOf qm:CognitiveSuperposition ,
                                                       qm:PsychodynamicCollapse ,
                                                       [ rdf:type owl:Restriction ;
                                                         owl:onProperty qm:isAppliedTo ;
                                                         owl:hasValue qm:QM_Quantum
                                                       ] ;
                                       rdfs:comment "The deliberate intervention in the pre-collapse state of multiple coexisting mental possibilities to influence outcomes."@en ;
                                       rdfs:label "Superpositional Cognitive Engineering"@en .


###  https://tuos.org/qm#SustainedAction
qm:SustainedAction rdf:type owl:Class ;
                   rdfs:subClassOf qm:PsychoMotivationalDimension ;
                   rdfs:comment "Consistent external action patterns over time, translated from internal value systems."@en ;
                   rdfs:label "Sustained Action"@en .


###  https://tuos.org/qm#SustainedActionMechanism
qm:SustainedActionMechanism rdf:type owl:Class ;
                            rdfs:subClassOf qm:PsychoMotivationalDimension ;
                            rdfs:comment "A specific psychological mechanism that supports the sustained drive of the Psycho-Motivational Dimension."@en ;
                            rdfs:label "Sustained Action Mechanism"@en .


###  https://tuos.org/qm#SystemDeconstruction
qm:SystemDeconstruction rdf:type owl:Class ;
                        rdfs:subClassOf qm:PracticesCategory .


###  https://tuos.org/qm#TacitKnowledge
qm:TacitKnowledge rdf:type owl:Class ;
                  rdfs:subClassOf qm:Phenomenon .


###  https://tuos.org/qm#TherapeuticInterventionForDistress
qm:TherapeuticInterventionForDistress rdf:type owl:Class ;
                                      rdfs:subClassOf qm:MainStrategiesCategory ,
                                                      [ rdf:type owl:Restriction ;
                                                        owl:onProperty qm:hasPractice ;
                                                        owl:someValuesFrom qm:ReverseEngineeringEmotionalStates
                                                      ] ;
                                      rdfs:comment "Applications of Quantum Mindfulness principles to reframe perceived psychological 'problems' as malleable constructs shaped by interpretive frameworks, enabling targeted and precise interventions."@en ;
                                      rdfs:label "Therapeutic Intervention for Distress and Dysfunction"@en .


###  https://tuos.org/qm#TherapeuticStrategy
qm:TherapeuticStrategy rdf:type owl:Class ;
                       rdfs:subClassOf owl:Thing ;
                       rdfs:comment "A systematic approach or set of practices, methods, and techniques employed within the Quantum Mindfulness framework to understand, influence, and transform an individual's internal psychological states and their manifestation in experienced reality. Aims to rebalance the underlying system architecture of consciousness."@en ,
                                    "Approaches and methods used for therapeutic intervention within the Quantum Mindfulness framework."@en ;
                       rdfs:label "Therapeutic Strategies"@en ,
                                  "Therapeutic Strategy"@en .


###  https://tuos.org/qm#TracingOriginsPhase
qm:TracingOriginsPhase rdf:type owl:Class ;
                       rdfs:subClassOf qm:LiberationProcess ;
                       rdfs:label "Phase 2: Tracing Origins"@en .


###  https://tuos.org/qm#TraitInfluence
qm:TraitInfluence rdf:type owl:Class ;
                  rdfs:subClassOf qm:DimensionalActivationInfluence ,
                                  qm:DimensionalActivationInfluencesCategory ,
                                  [ rdf:type owl:Restriction ;
                                    owl:onProperty qm:isDeterminedBy ;
                                    owl:someValuesFrom qm:TraitVariable
                                  ] ,
                                  [ rdf:type owl:Restriction ;
                                    owl:onProperty qm:isModulatedBy ;
                                    owl:someValuesFrom qm:PersonalTendency_TraitExpression
                                  ] ;
                  rdfs:comment "Incorporates the influence of an individual's stable, long-term personality Trait (Tj) associated with a specific dimension (ITj = wTj ⋅ Tj)."@en ,
                               "Incorporates the influence of an individual's stable, long-term personality Trait (Tj) associated with that specific dimension (ITj = wTj ⋅ Tj). It addresses: 'How much does my fundamental personality influence this feeling?'. This is the locus of the 'practice becomes belief' mechanism."@en ,
                               "Incorporates the influence of an individual's stable, long-term personality Trait (Tj) associated with that specific dimension."@en ;
                  rdfs:label "Trait Influence (ITj)"@en ,
                             "Trait Influence (ITj)" .


###  https://tuos.org/qm#TraitVariable
qm:TraitVariable rdf:type owl:Class ;
                 rdfs:subClassOf qm:DimensionalActivationInfluencesCategory ,
                                 [ rdf:type owl:Restriction ;
                                   owl:onProperty qm:isAlteredBy ;
                                   owl:someValuesFrom qm:OverallMentalState
                                 ] ;
                 rdfs:comment "A stable, long-term personality characteristic associated with a Psychodynamic Dimension. It can be durably altered by repeated mental states, effectively forming new beliefs."@en ,
                              "A stable, underlying personality trait (Tj) associated with a Psychodynamic Dimension. The model asserts that 'practice becomes belief', meaning repeated strong dimensional activations can durably alter these foundational Trait variables over time."@en ,
                              "A stable, underlying personality trait associated with a Psychodynamic Dimension, which can be durably altered by repeated mental states driven by strong social or emotional experiences (the 'practice becomes belief' mechanism)."@en ;
                 rdfs:label "Trait Variable (Tj)"@en ,
                            "Trait Variable (Tj)" .


###  https://tuos.org/qm#TransitionalModalities
qm:TransitionalModalities rdf:type owl:Class ;
                          rdfs:subClassOf qm:SecondaryModalityCategory ;
                          rdfs:comment "A grouping of dimensions (Pd7-9) that link internal psychological states to external reality."@en ;
                          rdfs:label "Transitional Modalities"@en .


###  https://tuos.org/qm#TranslationChallengeInPsychology
qm:TranslationChallengeInPsychology rdf:type owl:Class ;
                                    rdfs:subClassOf qm:EpistemologicalChallenges .


###  https://tuos.org/qm#TranslationFatigue
qm:TranslationFatigue rdf:type owl:Class ;
                      rdfs:subClassOf qm:CognitiveStrainAndDysfunction ;
                      rdfs:label "Translation Fatigue"@en .


###  https://tuos.org/qm#TraumaticCollapse
qm:TraumaticCollapse rdf:type owl:Class ;
                     rdfs:subClassOf qm:UnconsciousReactiveCollapse .


###  https://tuos.org/qm#UnconsciousReactiveCollapse
qm:UnconsciousReactiveCollapse rdf:type owl:Class ;
                               rdfs:subClassOf qm:CollapseMode ,
                                               qm:PsychologicalDysfunctionAndImbalance ;
                               rdfs:comment "Automatic solidification of a mental state based on ingrained patterns or external influences."@en ;
                               rdfs:label "Unconscious Reactive Collapse"@en .


###  https://tuos.org/qm#UnresolvedSuperpositionConsequence
qm:UnresolvedSuperpositionConsequence rdf:type owl:Class ;
                                      rdfs:subClassOf qm:PsychologicalDisharmony ;
                                      rdfs:comment "A negative outcome resulting from the failure to manage or resolve a state of Cognitive Superposition."@en ;
                                      rdfs:label "Unresolved Superposition Consequence"@en .


###  https://tuos.org/qm#ValueAlignment
qm:ValueAlignment rdf:type owl:Class ;
                  rdfs:subClassOf qm:GoalsCategory ;
                  rdfs:comment "The practice of identifying, clarifying, and consistently implementing personal values in daily life."@en ;
                  rdfs:label "Value Alignment"@en .


###  https://tuos.org/qm#VectorizedAwareness
qm:VectorizedAwareness rdf:type owl:Class ;
                       rdfs:subClassOf qm:ConsciousAwareness ,
                                       qm:Perception ,
                                       [ rdf:type owl:Restriction ;
                                         owl:onProperty qm:reliesOn ;
                                         owl:someValuesFrom qm:CognitiveAnchoring
                                       ] ,
                                       [ rdf:type owl:Restriction ;
                                         owl:onProperty qm:uses ;
                                         owl:someValuesFrom qm:PatternedPresence
                                       ] ;
                       rdfs:comment "A core operational mode of consciousness and active instrument for shaping internal reality, characterized by attention that possesses both intensity and precise directionality. It is a specialized tool for navigating complex psychological terrain and actively influencing the emergence of mental phenomena."@en ,
                                    "A precise, directional mode of attention for perceiving and constructing internal reality."@en ;
                       rdfs:label "Vectorized Awareness"@en .


###  https://tuos.org/qm#ViewOfPerception
qm:ViewOfPerception rdf:type owl:Class ;
                    rdfs:subClassOf qm:QuantumMindfulnessApplication ;
                    rdfs:label "View of Perception"@en .


###  https://tuos.org/qm#VolitionalCommitment
qm:VolitionalCommitment rdf:type owl:Class ;
                        rdfs:subClassOf qm:CognitiveAnchoringComponent ;
                        rdfs:comment "The conscious, deliberate decision to adopt and sustain adherence to a specific intention or goal. It is the cornerstone of effective Cognitive Anchoring."@en ;
                        rdfs:label "Volitional Commitment"@en .


###  https://tuos.org/qm#VolitionalContinuity
qm:VolitionalContinuity rdf:type owl:Class ;
                        rdfs:subClassOf qm:SustainedActionMechanism ;
                        rdfs:comment "A psychological structure that maintains its integrity and holds psychological form even amidst uncertainty or cognitive dissonance, representing the fundamental persistence of intentional commitment."@en ;
                        rdfs:label "Volitional Continuity"@en .


###  https://tuos.org/qm#VolitionalImpulse
qm:VolitionalImpulse rdf:type owl:Class ;
                     rdfs:subClassOf qm:PsychoVolitionalDimension ;
                     rdfs:label "Volitional Impulse"@en .


###  https://tuos.org/qm#VolitionalReframing
qm:VolitionalReframing rdf:type owl:Class ;
                       rdfs:subClassOf qm:CognitiveMechanism .


###  https://tuos.org/qm#VulnerabilityStructure
qm:VulnerabilityStructure rdf:type owl:Class ;
                          rdfs:subClassOf qm:SubconsciousInfrastructure ;
                          rdfs:comment "Deeply encoded patterns generated when fundamental human needs for emotional safety, connection, and validation are chronically unmet."@en ;
                          rdfs:label "Vulnerability Structure"@en .


###  https://tuos.org/qm#Will
qm:Will rdf:type owl:Class ;
        rdfs:subClassOf qm:PsychoVolitionalDimension .


###  https://tuos.org/qm#WillToConnection
qm:WillToConnection rdf:type owl:Class ;
                    rdfs:subClassOf qm:PsychoVolitionalDimension ;
                    rdfs:comment "A fundamental drive toward meaning, identity, and interconnectedness, operating with a consistent directional force."@en ;
                    rdfs:label "Will-to-Connection"@en .


###  https://tuos.org/qm#WitnessConsciousness
qm:WitnessConsciousness rdf:type owl:Class ;
                        rdfs:subClassOf qm:ObserverRole ;
                        rdfs:comment "The cultivation of a detached, non-judgmental awareness that observes mental phenomena without altering their natural course."@en ;
                        rdfs:label "Witness Consciousness"@en .


###  https://tuos.org/qm#ZeigarnikEffect
qm:ZeigarnikEffect rdf:type owl:Class ;
                   rdfs:subClassOf qm:InfluentialFactor .


#################################################################
#    Individuals
#################################################################

###  https://tuos.org/qm#AnalyticalReasoning
qm:AnalyticalReasoning rdf:type owl:NamedIndividual ,
                                qm:ProcessingMechanism .


###  https://tuos.org/qm#BalancingDimensionalEnergies
qm:BalancingDimensionalEnergies rdf:type owl:NamedIndividual ,
                                         qm:AdvancedPracticesAndMethodologiesCategory .


###  https://tuos.org/qm#CalculatedTurbulence
qm:CalculatedTurbulence rdf:type owl:NamedIndividual .


###  https://tuos.org/qm#CognitiveAnchoringFailure
qm:CognitiveAnchoringFailure rdf:type owl:NamedIndividual ,
                                      qm:CognitiveStrainAndDysfunction .


###  https://tuos.org/qm#CognitiveAppraisal
qm:CognitiveAppraisal rdf:type owl:NamedIndividual .


###  https://tuos.org/qm#CognitiveCapacity
qm:CognitiveCapacity rdf:type owl:NamedIndividual ,
                              qm:GoalsCategory .


###  https://tuos.org/qm#CognitiveInfluence
qm:CognitiveInfluence rdf:type owl:NamedIndividual .


###  https://tuos.org/qm#CognitiveMultiStateAwareness
qm:CognitiveMultiStateAwareness rdf:type owl:NamedIndividual ,
                                         qm:CognitiveCapacity .


###  https://tuos.org/qm#CollapseMode
qm:CollapseMode rdf:type owl:NamedIndividual ,
                         qm:CognitiveSuperposition .


###  https://tuos.org/qm#ConsensusReality
qm:ConsensusReality rdf:type owl:NamedIndividual ,
                             qm:SharedReality .


###  https://tuos.org/qm#Contemplation
qm:Contemplation rdf:type owl:NamedIndividual .


###  https://tuos.org/qm#CreativeGenesis
qm:CreativeGenesis rdf:type owl:NamedIndividual ,
                            qm:Phenomenon .


###  https://tuos.org/qm#DecoherenceBacklog
qm:DecoherenceBacklog rdf:type owl:NamedIndividual ,
                               qm:CognitiveStrainAndDysfunction .


###  https://tuos.org/qm#DecouplingPhase
qm:DecouplingPhase rdf:type owl:NamedIndividual ,
                            qm:LiberationPhase .


###  https://tuos.org/qm#DimensionalLiteracy
qm:DimensionalLiteracy rdf:type owl:NamedIndividual ,
                                qm:CognitiveCapacity .


###  https://tuos.org/qm#EmotionalResponse
qm:EmotionalResponse rdf:type owl:NamedIndividual ,
                              qm:PsychologicalPhenomenon .


###  https://tuos.org/qm#EthicalBoundaries
qm:EthicalBoundaries rdf:type owl:NamedIndividual ,
                              qm:PracticalLimitationsOfQMApplication .


###  https://tuos.org/qm#HumorAsCognitiveTechnology
qm:HumorAsCognitiveTechnology rdf:type owl:NamedIndividual ,
                                       qm:IntegratedTherapeuticApproaches .


###  https://tuos.org/qm#ImposterSyndrome
qm:ImposterSyndrome rdf:type owl:NamedIndividual ,
                             qm:OntologicalMisalignment .


###  https://tuos.org/qm#InstitutionalArchitectureImposition
qm:InstitutionalArchitectureImposition rdf:type owl:NamedIndividual ,
                                                qm:ExternalInfluence .


###  https://tuos.org/qm#LearnedBehavioralRepertoire
qm:LearnedBehavioralRepertoire rdf:type owl:NamedIndividual ,
                                        qm:ExternalInfluence .


###  https://tuos.org/qm#M1
qm:M1 rdf:type owl:NamedIndividual ,
               qm:ConsciousStack ,
               qm:PrimeModality ;
      qm:composedOf qm:Pd1 ,
                    qm:Pd2 ,
                    qm:Pd3 ;
      rdfs:label "The Prime Modality (M1)"@en .


###  https://tuos.org/qm#M2
qm:M2 rdf:type owl:NamedIndividual ,
               qm:SecondaryModality ;
      qm:composedOf qm:Pd7 ,
                    qm:Pd8 ,
                    qm:Pd9 ;
      qm:isModulatedBy qm:M1 .


###  https://tuos.org/qm#Memory
qm:Memory rdf:type owl:NamedIndividual .


###  https://tuos.org/qm#MentalFlexibility
qm:MentalFlexibility rdf:type owl:NamedIndividual ,
                              qm:CognitiveCapacity .


###  https://tuos.org/qm#MindfulnessBasedCognitiveTherapy
qm:MindfulnessBasedCognitiveTherapy rdf:type owl:NamedIndividual ,
                                             qm:StandardizedProtocol .


###  https://tuos.org/qm#NeurologicalEmbedding
qm:NeurologicalEmbedding rdf:type owl:NamedIndividual ,
                                  qm:ConditioningMechanism .


###  https://tuos.org/qm#ObservationValence
qm:ObservationValence rdf:type owl:NamedIndividual .


###  https://tuos.org/qm#ObserverEffectParadox
qm:ObserverEffectParadox rdf:type owl:NamedIndividual ,
                                  qm:EpistemologicalChallenges .


###  https://tuos.org/qm#ObserverRole
qm:ObserverRole rdf:type owl:NamedIndividual ,
                         qm:ObserverParticipantDynamic .


###  https://tuos.org/qm#OntologicalReassignment
qm:OntologicalReassignment rdf:type owl:NamedIndividual ,
                                    qm:CollapseInfluencePractice .


###  https://tuos.org/qm#OntologicalRestructuring
qm:OntologicalRestructuring rdf:type owl:NamedIndividual ,
                                     qm:AdvancedPracticesAndMethodologiesCategory .


###  https://tuos.org/qm#OsmoticIntegration
qm:OsmoticIntegration rdf:type owl:NamedIndividual ,
                               qm:ConditioningMechanism .


###  https://tuos.org/qm#Pd1
qm:Pd1 rdf:type owl:NamedIndividual ,
                qm:PsychoVolitionalDimension ,
                qm:PsychodynamicDimension ;
       qm:constituentOf qm:M1 ;
       qm:dissolves [ rdf:type qm:PerceivedLimitation
                    ] ;
       qm:embodies [ rdf:type qm:PurePotentiality
                   ] ;
       qm:hasPrimacyOver qm:Pd2 ,
                         qm:Pd3 ;
       qm:isSourceOf [ rdf:type qm:Will
                     ] ;
       qm:providesFoundationFor qm:Pd2 ,
                                qm:Pd3 ;
       rdfs:label "Psycho-Volitional Dimension (Pd1)"@en ,
                  "The Psycho-Volitional Dimension (Pd1)"@en .


###  https://tuos.org/qm#Pd10
qm:Pd10 rdf:type owl:NamedIndividual ,
                 qm:PsychoTranspersonalDimension ;
        qm:constituentOf qm:M2 ;
        qm:isNegatedBy qm:Pd1 ;
        rdfs:label "The Psycho-Transpersonal Dimension (Pd10)"@en .


###  https://tuos.org/qm#Pd2
qm:Pd2 rdf:type owl:NamedIndividual ,
                qm:PsychoConceptiveDimension ,
                qm:PsychodynamicDimension ;
       qm:constituentOf qm:M1 ;
       qm:dependsOn qm:Pd1 ;
       qm:follows qm:Pd1 ;
       qm:operatesThrough [ rdf:type qm:IntuitiveCognition
                          ] ;
       qm:progressesTo qm:Pd3 ;
       rdfs:label "Psycho-Conceptive Dimension (Pd2)"@en ,
                  "The Psycho-Conceptive Dimension (Pd2)"@en .


###  https://tuos.org/qm#Pd3
qm:Pd3 rdf:type owl:NamedIndividual ,
                qm:PsychoMeditativeDimension ,
                qm:PsychodynamicDimension ;
       qm:constituentOf qm:M1 ;
       qm:follows qm:Pd2 ;
       qm:harmonizes [ rdf:type qm:VolitionalImpulse
                     ] ,
                     [ ] ;
qm:hasCapacityFor [ rdf:type qm:ParadoxTolerance
                  ] ;
qm:isLocusOf [ rdf:type qm:IntentionalCollapse
             ] ;
qm:operatesThrough [ rdf:type qm:AnalyticalReasoning
                   ] ;
qm:providesFoundationFor [ rdf:type qm:SecondaryModality
                         ] ;
qm:receivesInputFrom qm:Pd2 ;
rdfs:label "Psycho-Meditative Dimension (Pd3)"@en ,
           "The Psycho-Meditative Dimension (Pd3)"@en .


###  https://tuos.org/qm#Pd4
qm:Pd4 rdf:type owl:NamedIndividual ,
                qm:PsychoEmpathicDimension ;
       qm:constituentOf qm:M2 ;
       qm:dependsOn qm:Pd1 ,
                    qm:Pd2 ,
                    qm:Pd3 ;
       qm:initiatesModality qm:M2 ;
       qm:isBalancedBy qm:Pd5 ;
       qm:isMediatedBy qm:Pd6 ;
       qm:providesFoundationFor qm:Pd7 ;
       rdfs:label "The Psycho-Empathic Dimension (Pd4)"@en .


###  https://tuos.org/qm#Pd5
qm:Pd5 rdf:type owl:NamedIndividual ,
                qm:PsychoProtectiveDimension ;
       qm:constituentOf qm:M2 ;
       qm:embodiesPrinciple [ rdf:type qm:PrincipleOfMeasure
                            ] ,
                            [ rdf:type qm:PrincipleOfLimit
                            ] ,
                            [ rdf:type qm:PrincipleOfRestraint
                            ] ;
       qm:influences qm:Pd8 ;
       qm:isArchitectOf [ rdf:type qm:PsychologicalStructure
                        ] ;
       qm:isMediatedBy qm:Pd6 ;
       qm:underpins [ rdf:type qm:SelfIntegrity
                    ] ;
       rdfs:label "The Psycho-Protective Dimension (Pd5)"@en .


###  https://tuos.org/qm#Pd6
qm:Pd6 rdf:type owl:NamedIndividual ,
                qm:PsychoAestheticDimension ;
       qm:bridgesTo qm:Pd7 ;
       qm:constituentOf qm:M2 ;
       qm:embodiesPrinciple [ rdf:type qm:PrincipleOfBalance
                            ] ,
                            [ rdf:type qm:PrincipleOfSymmetry
                            ] ;
       qm:functionsAs [ rdf:type qm:PsychologicalHeart
                      ] ;
       qm:isKeyTo [ rdf:type qm:PsychodynamicHarmonicAlignment
                  ] ;
       rdfs:label "The Psycho-Aesthetic Dimension (Pd6)"@en .


###  https://tuos.org/qm#Pd7
qm:Pd7 rdf:type owl:NamedIndividual ,
                qm:PsychoMotivationalDimension ;
       qm:constituentOf qm:M2 ,
                        qm:TheTransitionalModalities ;
       qm:embodies [ rdf:type qm:PsychoMotivationalMomentum
                   ] ;
       qm:isSupportedByMechanism [ rdf:type qm:CognitiveAnchoring
                                 ] ,
                                 [ rdf:type qm:VolitionalContinuity
                                 ] ;
       qm:translatesValuesInto [ rdf:type qm:SustainedAction
                               ] ;
       rdfs:label "The Psycho-Motivational Dimension (Pd7)"@en .


###  https://tuos.org/qm#Pd8
qm:Pd8 rdf:type owl:NamedIndividual ,
                qm:PsychoReceptiveDimension ;
       qm:constituentOf qm:M2 ,
                        qm:TheTransitionalModalities ;
       qm:enablesConversionOf [ rdf:type qm:AbstractInternalExperience
                              ] ;
       qm:facilitatesEmbodimentOf [ rdf:type qm:MentalPhysicalInterface
                                  ] ;
       qm:hasCapacityFor [ rdf:type qm:EmotionalOpenness
                         ] ,
                         [ rdf:type qm:PrincipleReceptivity
                         ] ;
       qm:orchestrates [ rdf:type qm:ProtoImpulse
                       ] ;
       qm:receivesInputFrom qm:Pd4 ,
                            qm:Pd5 ,
                            qm:Pd6 ;
       rdfs:label "The Psycho-Receptive Dimension (Pd8)"@en .


###  https://tuos.org/qm#Pd9
qm:Pd9 rdf:type owl:NamedIndividual ,
                qm:PsychoFoundationalDimension ;
       qm:consolidates [ rdf:type qm:Memory
                       ] ;
       qm:constituentOf qm:M2 ,
                        qm:TheTransitionalModalities ;
       qm:contains [ rdf:type qm:SubconsciousInfrastructure
                   ] ;
       qm:generates [ rdf:type qm:VulnerabilityStructure
                    ] ;
       qm:operatesThrough [ rdf:type qm:PsychoFoundationalEncoding
                          ] ;
       qm:servesAs [ rdf:type qm:GroundingFunction
                   ] ;
       rdfs:label "The Psycho-Foundational Dimension (Pd9)"@en .


###  https://tuos.org/qm#PerceptualMastery
qm:PerceptualMastery rdf:type owl:NamedIndividual ,
                              qm:PerceptualGoal .


###  https://tuos.org/qm#PersonalTendency_CognitiveResponsiveness
qm:PersonalTendency_CognitiveResponsiveness rdf:type owl:NamedIndividual ,
                                                     qm:PersonalTendency .


###  https://tuos.org/qm#PersonalTendency_MoodPersistence
qm:PersonalTendency_MoodPersistence rdf:type owl:NamedIndividual ,
                                             qm:PersonalTendency .


###  https://tuos.org/qm#PersonalTendency_Persistence
qm:PersonalTendency_Persistence rdf:type owl:NamedIndividual ,
                                         qm:PersonalTendency .


###  https://tuos.org/qm#PersonalTendency_Reactivity
qm:PersonalTendency_Reactivity rdf:type owl:NamedIndividual ,
                                        qm:PersonalTendency .


###  https://tuos.org/qm#PrincipleOfBalance
qm:PrincipleOfBalance rdf:type owl:NamedIndividual ,
                               qm:AestheticPrinciple .


###  https://tuos.org/qm#PrincipleOfLimit
qm:PrincipleOfLimit rdf:type owl:NamedIndividual ,
                             qm:ProtectivePrinciple .


###  https://tuos.org/qm#PrincipleOfMeasure
qm:PrincipleOfMeasure rdf:type owl:NamedIndividual ,
                               qm:ProtectivePrinciple .


###  https://tuos.org/qm#ProbabilisticSteering
qm:ProbabilisticSteering rdf:type owl:NamedIndividual ,
                                  qm:PerceptualShapingTechnique .


###  https://tuos.org/qm#PsychoVolitionalDynamics
qm:PsychoVolitionalDynamics rdf:type owl:NamedIndividual ,
                                     qm:Phenomenon .


###  https://tuos.org/qm#PsychologicalSelfSurgery
qm:PsychologicalSelfSurgery rdf:type owl:NamedIndividual ,
                                     qm:AdvancedPracticesAndMethodologiesCategory .


###  https://tuos.org/qm#QM_Quantum
qm:QM_Quantum rdf:type owl:NamedIndividual .


###  https://tuos.org/qm#RelationalMindfulness
qm:RelationalMindfulness rdf:type owl:NamedIndividual ,
                                  qm:CollapseInfluencePractice .


###  https://tuos.org/qm#ResolutionFatigue
qm:ResolutionFatigue rdf:type owl:NamedIndividual .


###  https://tuos.org/qm#ReverseEngineeringEmotionalStates
qm:ReverseEngineeringEmotionalStates rdf:type owl:NamedIndividual ,
                                              qm:AdvancedPracticesAndMethodologiesCategory .


###  https://tuos.org/qm#RighteousAnger
qm:RighteousAnger rdf:type owl:NamedIndividual ;
                  qm:emergesFromInteractionOf qm:Pd4 ,
                                              qm:Pd5 ,
                                              qm:Pd6 ;
                  rdfs:comment "An emergent psychological state arising from the interaction of compassionate identification, boundary judgment, and the recognition of a violation of moral beauty."@en ;
                  rdfs:label "Righteous Anger"@en .


###  https://tuos.org/qm#SigmoidFunction
qm:SigmoidFunction rdf:type owl:NamedIndividual .


###  https://tuos.org/qm#SocialInfluence
qm:SocialInfluence rdf:type owl:NamedIndividual ,
                            qm:InfluentialFactor .


###  https://tuos.org/qm#StrategicCognitiveTrajectoryManipulation
qm:StrategicCognitiveTrajectoryManipulation rdf:type owl:NamedIndividual ,
                                                     qm:AdvancedPracticesAndMethodologiesCategory .


###  https://tuos.org/qm#StructuralIntrospection
qm:StructuralIntrospection rdf:type owl:NamedIndividual ,
                                    qm:AdvancedPracticesAndMethodologiesCategory .


###  https://tuos.org/qm#SystemDeconstruction
qm:SystemDeconstruction rdf:type owl:NamedIndividual ,
                                 qm:AdvancedPracticesAndMethodologiesCategory .


###  https://tuos.org/qm#TacitKnowledge
qm:TacitKnowledge rdf:type owl:NamedIndividual ,
                           qm:Phenomenon .


###  https://tuos.org/qm#TheTransitionalModalities
qm:TheTransitionalModalities rdf:type owl:NamedIndividual ,
                                      qm:TransitionalModalities ;
                             qm:composedOf qm:Pd7 ,
                                           qm:Pd8 ,
                                           qm:Pd9 ;
                             rdfs:comment "A group of psychodynamic dimensions (Pd7-9) that serve as a bridge between internal psychological states and their expression in the external world."@en ;
                             rdfs:label "The Transitional Modalities (Pd7-9)"@en ;
                             skos:definition "The set of psychic functions that mediate between the inner and outer worlds."@en .


###  https://tuos.org/qm#TranslationChallengeInPsychology
qm:TranslationChallengeInPsychology rdf:type owl:NamedIndividual ,
                                             qm:EpistemologicalChallenges .


###  https://tuos.org/qm#TraumaticCollapse
qm:TraumaticCollapse rdf:type owl:NamedIndividual ,
                              qm:UnconsciousReactiveCollapse .


###  https://tuos.org/qm#Will
qm:Will rdf:type owl:NamedIndividual ,
                 qm:PsychoVolitionalDimension .


###  https://tuos.org/qm#ZeigarnikEffect
qm:ZeigarnikEffect rdf:type owl:NamedIndividual ,
                            qm:InfluentialFactor .


[ rdfs:comment "Formal Equation: Ψ = α(β + 1)(A + f)"@en
] .

[ rdfs:comment "The formal equation Kj = I_Sj + I_Cj + I_Tj + I_Ψj + εj signifies that the total activation emerges from the confluence of these multiple, distinct influences."@en
 ] .

[ rdfs:comment "Formal Equation: Kj = I_Sj + I_Cj + I_Tj + I_Ψj + εj"@en
 ] .

[ rdfs:comment "Formal Equation: C = wΨ ⋅ Valence(Ψ) + wS ⋅ AvgValence(S_t-1) + Bias_M1"@en
 ] .

[ rdfs:comment "Aims to actively make the Cognitive Appraisal positive by altering Valence(Ψ) through reframing and, more profoundly, by altering the baseline Bias_M1 over time."@en
 ] .

[ rdfs:comment "Aims to neutralize a negative Cognitive Influence by reducing reactivity (lowering wΨ and wS) and observing without judgment (pushing Valence(Ψ) to zero)."@en
 ] .

[ rdfs:comment "Aims to neutralize a negative Cognitive Appraisal by reducing reactivity (lowering wΨ and wS) and observing without judgment (pushing Valence(Ψ) toward zero)."@en
 ] .

[ rdfs:comment "The formal equation Ψ = α(β + 1)(A + f) underscores that these components are interdependent and contribute synergistically to the overall strength of the Observation."@en
 ] .

[ rdfs:comment "Formal Equation: S = Σ(xj * Pdj) for j=1 to 10. Represents the mental state as a vector in the 'space' of psychodynamic dimensions."@en
 ] .

[ rdfs:comment "The formal equation C = wΨ ⋅ Valence(Ψ) + wS ⋅ AvgValence(S_t-1) + Bias_M1 encapsulates the complex interplay of these factors."@en
 ] .

[ rdfs:comment "Formal Equation: S = Σ(xj * Pdj) for j=1 to 10. This represents the mental state as a vector in the 'space' of psychodynamic dimensions."@en
 ] .

[ rdfs:comment "Aims to actively ensure the Cognitive Influence becomes positive by altering Valence(Ψ) through reframing and, more profoundly, by altering the baseline Bias_M1."@en
 ] .

#################################################################
#    Annotations
#################################################################

:CognitiveSuperposition rdfs:comment "This class describes the state of pre-conscious mental potential. It is crucial to distinguish this from the physical principle; here, it is a conceptual tool to model the psyche's capacity to hold multiple, unresolved possibilities before an act of conscious attention."@en ;
                         skos:definition "The term 'superposition' is used here in a conceptual sense, derived from its Latin roots 'super-' (above) and 'positio' (to place), signifying multiple potentials being 'placed' in the same conceptual space. It describes a foundational pre-conscious state where multiple potential thoughts or perceptions coexist as a dynamic probability field. The term is thus used as a precise analogy for this state of unresolved mental potential, which precedes the 'collapse' into a single conscious thought."@en .


:ConsciousnessWaveFunction rdfs:comment "This class provides a conceptual label for the field in which mental potential exists. This is an abstract psychological concept, not a mathematical formula in the physical sense."@en ;
                           skos:definition "This term is constructed from its constituent parts to form a conceptual label. A 'function' describes a relationship between inputs and outputs, and a 'wave' represents a state of fluctuation and potential. The framework combines these to define the 'Consciousness Wave Function' as the conceptual space or probabilistic field  that contains the full range of potential mental states before they are actualized through psychodynamic collapse."@en .


:InterferencePatterns rdfs:comment "This class describes the emergent effects of combined psychodynamic dimensions, which can either amplify or diminish each other."@en ;
                      skos:definition "The term 'interference' is used in its general sense of one process affecting, modifying, or canceling another. In this ontology, it describes how the 'waves' of different psychodynamic dimensions interact. This can result in 'Constructive Interference,' where dimensions align to amplify positive qualities , or 'Destructive Interference,' where they conflict and create internal dissonance."@en .


:PsychodynamicWaveCollapse rdfs:comment "This class represents the pivotal process where the mind's probabilistic field resolves into a specific, actualized experience."@en ;
                           skos:definition "Grounded in the general meaning of 'collapse'—to fall together into a more compact or definite state—this term describes the fundamental psychological transition from potential to actuality. Within this framework, it is the specific process by which the 'wave' of multiple mental possibilities (defined in qm:CognitiveSuperposition) resolves into a singular, definite, and consciously experienced outcome, triggered by an act of attention."@en .


:PsychologicalEntanglement rdfs:comment "This class models the principle of deep and persistent interconnectedness between psychological systems, which may not be immediately obvious or causal in a linear sense."@en ;
                           skos:definition "Drawing from the general meaning of 'entanglement'—to be intricately intertwined or connected—this framework uses the term to describe a state of deep psychological interconnection. For example, qm:EmotionalQuantumEntanglement is defined as the persistent interconnectedness of mental and emotional states between individuals. The term is used as a powerful metaphor to describe profound, non-local connections that operate beyond direct perception."@en .


:QM_Quantum rdfs:comment "The conceptual principle that subjective experience is not a continuous phenomenon, but is constituted by identifiable, discrete psychodynamic dimensions. This term is used conceptually to describe distinct experiential configurations, not a model of brain computation."@en ;
            skos:definition "Grounded in its Latin origin 'quantus' (meaning 'how much' or 'an amount'), a 'quantum' in this framework is the smallest discrete amount or fundamental unit of the psychic architecture. While rooted in this primary definition, the framework extends this concept by creating a powerful psychological analogy with concepts from quantum physics. It uses related principles like 'superposition' (qm:CognitiveSuperposition) and 'collapse' (qm:PsychodynamicCollapse) to build a novel model of how the mind works, contrasting it with continuous models of mentation."@en .


qm:AnalyticalReasoning rdfs:comment "The ability to deconstruct information into smaller categories in order to draw conclusions."@en ;
                       rdfs:label "Analytical and Dialectical Reasoning"@en ;
                       skos:definition "A form of cognition that uses logic and systematic thinking to solve problems."@en .


qm:BalancingDimensionalEnergies rdfs:comment "The practice of consciously working to create harmony and equilibrium among the different psychodynamic dimensions."@en ;
                                rdfs:label "Balancing Dimensional Energies"@en ;
                                skos:definition "An advanced practice aimed at achieving balance between the various energetic dimensions of the psyche."@en .


qm:CalculatedTurbulence rdfs:comment "The optimal state of balance, conceived as a dynamic equilibrium where the dimensions remain actively engaged and responsive within productive thresholds."@en ;
                        rdfs:label "Calculated Turbulence"@en .


qm:CognitiveAnchoringFailure rdfs:comment "The inability to maintain a stable mental or intentional focus, leading to distraction, impulsivity, or a sense of being adrift."@en ;
                             rdfs:label "Cognitive Anchoring Failure"@en ;
                             skos:definition "The failure to maintain a stable cognitive or intentional state."@en .


qm:CognitiveAppraisal rdfs:comment "The mind's primary, high-level judgment or interpretation of an observed phenomenon, undertaken by the Prime Modality. It functions as a 'master control signal' or 'prime directive' that provides the overarching directional impetus for the subsequent Psychodynamic Collapse. It is a dynamic, potentially iterative process."@en ,
                                   "The mind's primary, high-level judgment or interpretation of an observed phenomenon, undertaken by the Prime Modality. It functions as a 'master control signal' that provides the overarching directional impetus for the subsequent Psychodynamic Collapse. Its value is a weighted sum of three distinct forces."@en ,
                                   "The pivotal 'master control signal' or 'prime directive' that translates a complex observation into a single, high-level judgment, driving the activation of the ten Psychodynamic Dimensions."@en ,
                                   "The pivotal 'master control signal' or 'prime directive' that translates a complex observation into a single, high-level judgment, driving the activation of the ten Psychodynamic Dimensions. It is determined by the observation's valence, the previous mental state, and an inherent bias from the Prime Modality."@en ;
                      rdfs:label "Cognitive Appraisal (C)"@en ,
                                 "Cognitive Appraisal (C)" ;
                      rdfs:subClassOf "Psychodynamic Model"@en ,
                                      "Psychodynamic Model, Cognitive Influence Model"@en .


qm:CognitiveCapacity rdfs:comment "An inherent mental ability or potential that can be developed through practice."@en ;
                     rdfs:label "Cognitive Capacity"@en ;
                     skos:definition "The mental ability to perform a particular task."@en .


qm:CognitiveInfluence rdfs:comment "Represents the direct impact of the overall Cognitive Appraisal (C) on the activation of a dimension."@en ,
                                   "Represents the direct impact of the overall Cognitive Appraisal (C) on the activation of a specific dimension (ICj = wCj ⋅ C)."@en ,
                                   "Represents the direct impact of the overall Cognitive Appraisal (C) on the activation of a specific dimension (ICj = wCj ⋅ C). It addresses: 'How much does my overall judgment of this situation influence this specific feeling?'. This is a key intervention point for both Classical and Quantum Mindfulness."@en ;
                      rdfs:label "Cognitive Influence (ICj)"@en ,
                                 "Cognitive Influence (ICj)" .


qm:CognitiveMultiStateAwareness rdfs:comment "The ability to hold multiple, even conflicting, ideas or perspectives in mind simultaneously without needing to resolve them immediately."@en ;
                                rdfs:label "Cognitive Multi-State Awareness"@en ;
                                skos:definition "The capacity to be aware of and entertain multiple mental states at once."@en .


qm:CollapseMode rdfs:comment "The manner in which a state of cognitive superposition resolves into a definite experience, which can be either intentional or reactive."@en ;
                rdfs:label "Collapse Mode"@en ;
                skos:definition "A specific way in which a field of possibilities collapses into a single reality."@en .


qm:ConsensusReality rdfs:comment "A shared set of beliefs and perceptions that a group of people agree upon, which forms their common understanding of reality."@en ;
                    rdfs:label "Consensus Reality"@en ;
                    skos:definition "An agreed-upon reality based on a shared understanding within a group."@en .


qm:Contemplation rdfs:comment "An active, deliberate cognitive process involving sustained, rigorous mental work to transform potential into Structured Understanding. It is integral to conscious awareness and instrumental in processing all conscious experience."@en ,
                              "An active, deliberate cognitive process involving sustained, rigorous mental work to transform raw cognitive potential into structured understanding. It is crucial for psycho-meditative collapse and complements foundational mindfulness."@en .


qm:CreativeGenesis rdfs:comment "The process of bringing new ideas, insights, or creations into being, often seen as emerging from a state of open potential."@en ;
                   rdfs:label "Creative Genesis"@en ;
                   skos:definition "The origin or beginning of a creative process."@en .


qm:DecoherenceBacklog rdfs:comment "An accumulation of unresolved cognitive superpositions, leading to a state of mental clutter and reduced cognitive efficiency."@en ;
                      rdfs:label "Decoherence Backlog"@en ;
                      skos:definition "A build-up of unresolved mental states that impairs cognitive function."@en .


qm:DecouplingPhase rdfs:comment "A stage in the process of liberation from inherited scripts, where one begins to dis-identify from and separate oneself from conditioned patterns."@en ;
                   rdfs:label "Phase 3: Decoupling & Cultivating Sovereign Architecture"@en ;
                   skos:definition "The phase of separating from conditioned patterns of thought and behavior."@en .


qm:DimensionalLiteracy rdfs:comment "The ability to recognize, understand, and skillfully navigate the various psychodynamic dimensions of experience."@en ;
                       rdfs:label "Dimensional Literacy"@en ;
                       skos:definition "The skill of understanding and working with the different dimensions of consciousness."@en .


qm:EmotionalResponse rdfs:comment "The reaction of an individual to a specific event or stimulus, involving physiological arousal, expressive behaviors, and conscious experience."@en ;
                     rdfs:label "Emotional Response"@en ;
                     skos:definition "A psychological and physiological reaction to a stimulus."@en .


qm:EthicalBoundaries rdfs:comment "The moral principles and professional standards that constrain the application of Quantum Mindfulness practices."@en ;
                     rdfs:label "Ethical Boundaries"@en ;
                     skos:definition "The ethical limits governing the use of a practice or technique."@en .


qm:HumorAsCognitiveTechnology rdfs:comment "The use of humor as a sophisticated tool for reframing perspectives, reducing cognitive rigidity, and fostering psychological well-being."@en ;
                              rdfs:label "Humor as Cognitive Technology"@en ;
                              skos:definition "Employing humor as a deliberate technique to shift cognitive and emotional states."@en .


qm:ImposterSyndrome rdfs:comment "A psychological pattern in which an individual doubts their skills, talents, or accomplishments and has a persistent internalized fear of being exposed as a 'fraud'."@en ;
                    rdfs:label "Imposter Syndrome"@en ;
                    skos:definition "The experience of feeling like a fraud, despite evidence of success."@en .


qm:InstitutionalArchitectureImposition rdfs:comment "The influence of societal institutions and their structures on an individual's beliefs, values, and behaviors."@en ;
                                       rdfs:label "Institutional Architecture Imposition"@en ;
                                       skos:definition "The shaping of an individual by the structures of institutions."@en .


qm:LearnedBehavioralRepertoire rdfs:comment "The collection of behaviors and responses that an individual has learned from their environment and experiences."@en ;
                               rdfs:label "Learned Behavioral Repertoire"@en ;
                               skos:definition "The set of behaviors that a person has acquired through learning."@en .


qm:Memory rdfs:label "Memory (Explicit and Implicit)"@en .


qm:MentalFlexibility rdfs:comment "The ability to adapt cognitive processing strategies to face new and unexpected conditions in the environment."@en ;
                     rdfs:label "Mental Flexibility"@en ;
                     skos:definition "The capacity to switch between different concepts or to think about multiple concepts simultaneously."@en .


qm:MindfulnessBasedCognitiveTherapy rdfs:comment "An evidence-based therapeutic approach that combines mindfulness techniques with cognitive-behavioral therapy to help prevent the relapse of depression."@en ;
                                    rdfs:label "Mindfulness-Based Cognitive Therapy (MBCT)"@en ;
                                    skos:definition "A therapeutic intervention combining mindfulness meditation with cognitive therapy."@en .


qm:NeurologicalEmbedding rdfs:comment "The process by which repeated thoughts and behaviors create and strengthen neural pathways in the brain, making those patterns more automatic."@en ;
                         rdfs:label "Repetition and Neurological Embedding"@en ;
                         skos:definition "The physical process of learning and habit formation in the brain."@en .


qm:ObservationValence rdfs:comment "The subjective emotional coloring or the numeric rating of positivity or negativity that the mind assigns to a specific observation. This valence is a crucial output of the perceptual and interpretive process and provides the 'Impact of the Now' component for the Cognitive Appraisal."@en ;
                      rdfs:label "Observation Valence (Valence(Ψ))"@en ,
                                 "Observation Valence (Valence(Ψ))" .


qm:ObserverEffectParadox rdfs:comment "The challenge of observing a system without altering it, particularly in the context of self-observation where the act of observing one's own mind inevitably changes it."@en ;
                         rdfs:label "Observer Effect Paradox"@en ;
                         skos:definition "The paradox that the act of observation can change the phenomenon being observed."@en .


qm:ObserverRole rdfs:comment "The function and stance of the observer in the process of perception and reality construction."@en ;
                rdfs:label "Observer Role"@en ;
                skos:definition "The part played by the observer in a system."@en .


qm:OntologicalReassignment rdfs:comment "The practice of shifting the fundamental classification or 'being-ness' of a phenomenon to alter one's relationship to it."@en ;
                           rdfs:label "Ontological Reassignment"@en ;
                           skos:definition "The act of changing the ontological category of a concept or experience."@en .


qm:OntologicalRestructuring rdfs:comment "The advanced practice of fundamentally altering one's understanding of being and reality."@en ;
                            rdfs:label "Ontological Restructuring"@en ;
                            skos:definition "The process of changing one's fundamental beliefs about existence."@en .


qm:OsmoticIntegration rdfs:comment "The gradual and often unconscious absorption of beliefs, attitudes, and behaviors from one's social and cultural environment."@en ;
                      rdfs:label "Osmotic Integration"@en ;
                      skos:definition "The process of absorbing information and behaviors from the surrounding environment."@en .


qm:PerceptualMastery rdfs:comment "The advanced ability to consciously and skillfully shape one's own perceptual experience."@en ;
                     rdfs:label "Perceptual Mastery"@en ;
                     skos:definition "A high level of skill in managing and directing one's own perception."@en .


qm:PersonalTendency_CognitiveResponsiveness rdfs:comment "An individual's characteristic level of reactivity to their own cognitive appraisals, influencing how strongly their judgments affect their subsequent mental state."@en ;
                                            rdfs:label "Personal Tendency (Cognitive Responsiveness - wCj)"@en ;
                                            skos:definition "The degree to which an individual's thoughts and judgments about a situation impact their subsequent emotional and cognitive state."@en .


qm:PersonalTendency_MoodPersistence rdfs:comment "An individual's natural tendency for a mood or emotional state to continue over time."@en ;
                                    rdfs:label "Personal Tendency (Mood Persistence - wS)"@en ,
                                               "Personal Tendency (Mood Persistence - wS)" ;
                                    skos:definition "The degree to which a person's mood tends to remain stable over time."@en .


qm:PersonalTendency_Persistence rdfs:comment "An individual's tendency to maintain a particular mental or emotional state over time."@en ;
                                rdfs:label "Personal Tendency (Dimensional Persistence - wSj)"@en ;
                                skos:definition "The disposition to continue in a particular state."@en .


qm:PersonalTendency_Reactivity rdfs:comment "An individual's characteristic level of emotional and cognitive reactivity to external events and internal stimuli."@en ;
                               rdfs:label "Personal Tendency (Reactivity to New Events - wΨ)"@en ,
                                          "Personal Tendency (Reactivity - wΨ)" ;
                               skos:definition "The degree to which a person reacts to stimuli."@en .


qm:PrincipleOfBalance rdfs:comment "A fundamental principle related to harmony, equilibrium, and the integration of opposing forces within the psyche."@en ;
                      rdfs:label "Principle of Balance"@en ;
                      skos:definition "The aesthetic principle concerned with achieving equilibrium and harmony."@en .


qm:PrincipleOfLimit rdfs:comment "The principle of establishing and maintaining healthy boundaries and constraints."@en ;
                    rdfs:label "Principle of Limit"@en ;
                    skos:definition "A guiding rule for setting necessary and healthy restrictions."@en .


qm:PrincipleOfMeasure rdfs:comment "The principle related to setting appropriate limits and boundaries."@en ;
                      rdfs:label "Principle of Measure"@en ;
                      skos:definition "A guiding rule for establishing proper proportion and limits."@en .


qm:ProbabilisticSteering rdfs:comment "The practice of consciously influencing the likelihood of certain mental states or outcomes by directing attention and intention, without forcing a specific result."@en ;
                         rdfs:label "Probabilistic Steering"@en ;
                         skos:definition "The conscious and subtle guidance of mental and emotional direction by managing the probabilities of various potential states."@en .


qm:PsychoVolitionalDynamics rdfs:comment "The interplay of will, intention, and psychic energy that drives cognitive and emotional processes."@en ;
                            rdfs:label "Psycho-Volitional Dynamics"@en ;
                            skos:definition "The study and application of the forces of will and intention within the psyche."@en .


qm:PsychologicalSelfSurgery rdfs:comment "A metaphorical concept for the advanced and deliberate practice of identifying, analyzing, and restructuring one's own deep-seated psychological patterns and beliefs."@en ;
                            rdfs:label "Psychological Self-Surgery"@en ;
                            skos:definition "The practice of applying deep introspection and self-analysis to fundamentally change one's own psychological makeup."@en .


qm:RelationalMindfulness rdfs:comment "The application of mindfulness principles to interpersonal relationships, focusing on awareness of oneself and others in social interactions."@en ;
                         rdfs:label "Relational Mindfulness"@en ;
                         skos:definition "The practice of being mindfully aware within the context of relationships."@en .


qm:ResolutionFatigue rdfs:comment "A profound form of cognitive strain where the mind's capacity to form definite mental states from possibilities is compromised, often due to external inputs overwriting internal signals."@en ;
                     rdfs:label "Resolution Fatigue"@en .


qm:ReverseEngineeringEmotionalStates rdfs:comment "The practice of deconstructing an emotional state to understand its constituent parts and underlying dimensional sources."@en ;
                                     rdfs:label "Reverse Engineering Emotional States"@en ;
                                     skos:definition "An advanced practice of analyzing an emotion to understand its origins and structure."@en .


qm:SigmoidFunction rdfs:comment "A mathematical function used to transform the raw Dimensional Activation (Kj) into a normalized Final Intensity (xj) between 0 and 1. It is chosen for its non-linearity and threshold-like behavior, which mirrors psychological phenomena."@en ,
                                "A mathematical function used to transform the raw Dimensional Activation (Kj) into a normalized Final Intensity (xj) between 0 and 1. It is chosen for its properties of normalization, non-linearity, and its threshold-like behavior, which accurately model how psychological phenomena manifest."@en ;
                   rdfs:label "Sigmoid Function"@en ,
                              "Sigmoid Function" ;
                   rdfs:subClassOf "Psychodynamic Model"@en .


qm:SocialInfluence rdfs:comment "The effect that the words, actions, or mere presence of other people have on our thoughts, feelings, attitudes, or behavior."@en ;
                   rdfs:label "Social Influence"@en ;
                   skos:definition "The process by which individuals' attitudes, beliefs or behavior are modified by the presence or action of others."@en .


qm:StrategicCognitiveTrajectoryManipulation rdfs:comment "The deliberate and strategic shaping of one's own cognitive and emotional path over time."@en ;
                                            rdfs:label "Strategic Cognitive Trajectory Manipulation"@en ;
                                            skos:definition "The practice of intentionally guiding the direction of one's own thoughts and feelings."@en .


qm:StructuralIntrospection rdfs:comment "A disciplined form of self-examination focused on understanding the underlying structures of one's own consciousness and psychological patterns."@en ;
                           rdfs:label "Structural Introspection"@en ;
                           skos:definition "The practice of looking inward to understand the architecture of one's own mind."@en .


qm:SystemDeconstruction rdfs:comment "The practice of breaking down complex psychological systems into their fundamental components to understand their functioning."@en ;
                        rdfs:label "System Deconstruction"@en ;
                        skos:definition "An analytical practice of taking apart a system to see how it works."@en .


qm:TacitKnowledge rdfs:comment "Knowledge that is difficult to express or articulate, often acquired through experience and practice rather than formal instruction."@en ;
                  rdfs:label "Tacit Knowledge"@en ;
                  skos:definition "Implicit understanding or know-how that is not easily verbalized."@en .


qm:TranslationChallengeInPsychology rdfs:comment "The difficulty of translating subjective psychological experiences into objective, scientific language without losing essential meaning."@en ;
                                    rdfs:label "Translation Challenge in Psychology"@en ;
                                    skos:definition "The problem of accurately conveying subjective psychological concepts."@en .


qm:TraumaticCollapse rdfs:comment "A rapid and overwhelming resolution of a cognitive superposition triggered by a traumatic event, leading to a rigid and often dysfunctional mental state."@en ;
                     rdfs:label "Traumatic Collapse"@en ;
                     skos:definition "The collapse of mental potential into a fixed state as a result of trauma."@en .


qm:Will rdfs:comment "The faculty of consciousness by which one deliberately chooses or decides upon a course of action."@en ;
        rdfs:label "Will"@en ;
        skos:definition "The cognitive faculty of conscious and deliberate choice."@en .


qm:ZeigarnikEffect rdfs:comment "The psychological tendency to remember uncompleted or interrupted tasks better than completed tasks."@en ;
                   rdfs:label "Zeigarnik Effect"@en ;
                   skos:definition "The phenomenon where people better remember unfinished tasks than finished ones."@en .


###  Generated by the OWL API (version 4.5.29.2024-05-13T12:11:03Z) https://github.com/owlcs/owlapi

: dc:title "Mindfulness Cuántico - El Poder de la Percepción y Dimensiones Psicodinámicas Ontología"@es ;
    rdfs:comment "Una ontología formal de la Modalidad Principal del marco de Mindfulness Cuántico. Esta versión utiliza restricciones OWL para definir relaciones a nivel de clase, asegurando una estructura robusta y legible por máquina."@es ,
                 "Una ontología formal de la arquitectura psicodinámica de la conciencia como se detalla en el material fuente de Mindfulness Cuántico. Este modelo define el proceso secuencial desde la Observación hasta la emergencia de un Estado Mental final, y el mecanismo de Formación de Creencias."@es ,
                 "Una ontología del marco de Mindfulness Cuántico. Nota: Aunque algunos textos fuente se refieren a once dimensiones, la enumeración detallada lista consistentemente diez (Pd1–Pd10). El concepto de 'once' puede aludir a un 'núcleo Psico-Volitivo' fundamental que sustenta las diez dimensiones enumerables."@es .

dc:creator rdfs:comment "Una entidad principalmente responsable de crear el recurso."@es .
dc:title rdfs:comment "Un nombre dado al recurso."@es .
rdfs:subClassOf rdfs:comment "El sujeto es una clase del objeto."@es .
skos:altLabel rdfs:comment "Una etiqueta léxica alternativa para un recurso."@es .
qm:hasDefinition rdfs:label "tiene definición"@es .

qm:actsAsChannelFor
    rdfs:comment "Indica una función que permite que influencias e ideas refinadas de dimensiones superiores fluyan hacia abajo e informen acciones concretas."@es ;
    rdfs:label "actúa como canal para"@es .

qm:actualizes
    rdfs:comment "Indica el proceso de convertir un estado potencial en uno definido y real."@es ;
    rdfs:label "actualiza"@es .

qm:addressesLimitationsOf
    rdfs:comment "Indica que un proceso o aplicación está diseñado para mitigar o resolver disfunciones o desafíos específicos."@es ;
    rdfs:label "aborda las limitaciones de"@es .

qm:arisesFrom
    rdfs:comment "Indica el origen o la causa de un estado psicológico, particularmente en el contexto de la dinámica dimensional."@es ;
    rdfs:label "surge de"@es .

qm:biases
    rdfs:comment "Indica un patrón sistemático que influye en la interpretación."@es ;
    rdfs:label "sesga"@es .

qm:bridgesTo
    rdfs:comment "Indica la creación de una conexión que canaliza energía o ideas hacia otra dimensión para una acción con propósito."@es ;
    rdfs:label "sirve de puente hacia"@es .

qm:canDurablyAlter
    rdfs:comment "Indica un mecanismo donde los estados mentales repetidos pueden alterar de forma duradera una variable subyacente del sistema, como un rasgo."@es ;
    rdfs:label "puede alterar duraderamente"@es .

qm:canHaveInterferencePattern
    rdfs:comment "Indica que la interacción entre dimensiones puede llevar a patrones constructivos (amplificadores) o destructivos (conflictivos)."@es ;
    rdfs:label "puede tener patrón de interferencia"@es .

qm:composedOf
    rdfs:label "compuesto de"@es .

qm:connection_Pd1_Pd2
    rdfs:comment "Describe el flujo desde la intencionalidad psíquica pura y el ímpetu psíquico inicial hasta la formación de conceptos brutos, no formados, e intuiciones."@es ;
    rdfs:label "Conexión de Pd1 a Pd2 (Conceptualización Inicial)"@es .

qm:connection_Pd1_Pd3
    rdfs:comment "Describe cómo la voluntad primigenia y el potencial psíquico se traducen en estructuras mentales organizadas y una comprensión integral."@es ;
    rdfs:label "Conexión de Pd1 a Pd3 (Voluntad a Estructura)"@es .

qm:connection_Pd1_Pd6
    rdfs:comment "La manifestación fundamental de la voluntad y el potencial psíquico en el núcleo equilibrado e integrado del ser."@es ;
    rdfs:label "Conexión de Pd1 a Pd6 (Integración del Origen Psíquico)"@es .

qm:connection_Pd2_Pd3
    rdfs:comment "El proceso de dar estructura, lógica y comprensión concreta a las intuiciones y conceptos brutos."@es ;
    rdfs:label "Conexión de Pd2 a Pd3 (De la Intuición a la Forma)"@es .

qm:connection_Pd2_Pd4
    rdfs:comment "El flujo desde la pura visión conceptual hacia la expansión emocional benevolente y la capacidad de empatía profunda."@es ;
    rdfs:label "Conexión de Pd2 a Pd4 (Empatía Intuitiva)"@es .

qm:connection_Pd2_Pd6
    rdfs:comment "Cómo la visión creativa contribuye directamente a la armonía, el equilibrio y la expresión integrada del ser."@es ;
    rdfs:label "Conexión de Pd2 a Pd6 (Autoexpresión Conceptual)"@es .

qm:connection_Pd3_Pd5
    rdfs:comment "Cómo el pensamiento estructurado conduce al establecimiento de una disciplina psíquica clara y límites internos protectores."@es ;
    rdfs:label "Conexión de Pd3 a Pd5 (Pensamiento a Límites)"@es .

qm:connection_Pd3_Pd6
    rdfs:comment "Cómo la comprensión razonada y las estructuras mentales contribuyen a la armonía y el equilibrio general del ser."@es ;
    rdfs:label "Conexión de Pd3 a Pd6 (Autointegración Estructurada)"@es .

qm:connection_Pd4_Pd5
    rdfs:comment "La interacción dinámica entre la empatía expansiva y la autoprotección necesaria o la gestión emocional disciplinada."@es ;
    rdfs:label "Conexión de Pd4 a Pd5 (Límites Compasivos)"@es .

qm:connection_Pd4_Pd6
    rdfs:comment "Cómo la compasión expansiva y la emoción benevolente contribuyen a la belleza, el equilibrio y la integración del ser."@es ;
    rdfs:label "Conexión de Pd4 a Pd6 (Autosoporte Empático)"@es .

qm:connection_Pd4_Pd7
    rdfs:comment "El flujo desde la expansión emocional benevolente hacia un impulso persistente, inspirando acción y fuerza motivacional."@es ;
    rdfs:label "Conexión de Pd4 a Pd7 (Empatía a Motivación)"@es .

qm:connection_Pd5_Pd6
    rdfs:comment "Cómo el establecimiento de límites psíquicos y la fuerza interior contribuyen a la armonía y el equilibrio general del ser."@es ;
    rdfs:label "Conexión de Pd5 a Pd6 (Disciplina para la Integración)"@es .

qm:connection_Pd5_Pd8
    rdfs:comment "El flujo desde la fuerza interior y los límites hacia una comunicación intelectual clara y efectiva o capacidad receptiva."@es ;
    rdfs:label "Conexión de Pd5 a Pd8 (Expresión Protectora)"@es .

qm:connection_Pd6_Pd7
    rdfs:comment "La manifestación del ser equilibrado en un impulso apasionado, resistencia y fuerza motivacional enfocada."@es ;
    rdfs:label "Conexión de Pd6 a Pd7 (Impulso Integrado)"@es .

qm:connection_Pd6_Pd8
    rdfs:comment "Cómo el ser integrado encuentra su voz y se expresa a través de procesos intelectuales y comunicación."@es ;
    rdfs:label "Conexión de Pd6 a Pd8 (Expresión Integrada)"@es .

qm:connection_Pd6_Pd9
    rdfs:comment "La conexión desde el ser integrado a sus raíces subconscientes más profundas e impulsos psíquicos fundamentales."@es ;
    rdfs:label "Conexión de Pd6 a Pd9 (Ser a Fundación)"@es .

qm:connection_Pd7_Pd10
    rdfs:comment "Cómo el impulso interno y la fuerza de voluntad encuentran su expresión e impacto en la realidad externa y manifestada de la experiencia."@es ;
    rdfs:label "Conexión de Pd7 a Pd10 (Manifestación del Impulso)"@es .

qm:connection_Pd7_Pd8
    rdfs:comment "La interacción dinámica entre el impulso/fuerza de voluntad en bruto y su recepción, procesamiento y comunicación intelectual."@es ;
    rdfs:label "Conexión de Pd7 a Pd8 (Impulso a Intelecto)"@es .

qm:connection_Pd7_Pd9
    rdfs:comment "Cómo los impulsos y motivaciones en bruto se conectan con el fundamento energético subconsciente profundo de la personalidad."@es ;
    rdfs:label "Conexión de Pd7 a Pd9 (Fundamento Motivacional)"@es .

qm:connection_Pd8_Pd10
    rdfs:comment "Cómo la expresión intelectual y la comunicación encuentran su manifestación e impacto en el mundo experimentado."@es ;
    rdfs:label "Conexión de Pd8 a Pd10 (Manifestación Expresiva)"@es .

qm:connection_Pd8_Pd9
    rdfs:comment "La conexión desde el intelecto formal y la capacidad receptiva hacia el subconsciente más profundo y los impulsos fundacionales."@es ;
    rdfs:label "Conexión de Pd8 a Pd9 (Intelecto a Subconsciente)"@es .

qm:connection_Pd9_Pd10
    rdfs:comment "La conexión fundamental entre el fundamento subconsciente de la personalidad y su plena manifestación en la realidad."@es ;
    rdfs:label "Conexión de Pd9 a Pd10 (Fundación a Realidad)"@es .

qm:consolidates
    rdfs:comment "Indica la función de solidificar la memoria y el aprendizaje experiencial."@es ;
    rdfs:label "consolida"@es .

qm:constituentOf
    rdfs:comment "Una propiedad que indica que un concepto es un componente o parte de un todo más grande."@es ;
    rdfs:label "constituyente de"@es ;
    skos:definition "Que sirve como parte de un todo."@es .

qm:contains
    rdfs:comment "Indica que una dimensión alberga estructuras psicológicas fundamentales."@es ;
    rdfs:label "contiene"@es .

qm:contrastsWith
    rdfs:comment "Indica que un concepto o principio diverge fundamentalmente de otro modelo o idea."@es ;
    rdfs:label "contrasta con"@es .

qm:contributesTo
    rdfs:comment "Indica que el sujeto es un factor que contribuye al objeto."@es ;
    rdfs:label "contribuye a"@es ;
    skos:definition "Una propiedad que indica que el sujeto añade o ayuda a causar el objeto."@es .

qm:definesRoleOfObserverAs
    rdfs:comment "Define el rol conceptual del observador consciente dentro de un paradigma de mindfulness específico."@es ;
    rdfs:label "define el rol del observador como"@es .

qm:dependsOn
    rdfs:comment "Indica una relación donde el sujeto requiere del objeto para su existencia o función."@es ;
    rdfs:label "depende de"@es ;
    skos:definition "Una propiedad que indica que el sujeto depende del objeto."@es .

qm:describes
    rdfs:comment "Indica que un principio proporciona el lenguaje conceptual para un mecanismo o proceso."@es ;
    rdfs:label "describe"@es .

qm:develops
    rdfs:comment "Indica que una práctica conduce a la mejora de una capacidad específica."@es ;
    rdfs:label "desarrolla"@es .

qm:differsFrom
    rdfs:comment "Indica una distinción conceptual o metodológica de otro concepto."@es ;
    rdfs:label "difiere de"@es .

qm:dissolves
    rdfs:comment "Indica la propiedad 'aniquiladora' de una dimensión, permitiéndole negar limitaciones percibidas, bloqueos mentales y marcos conceptuales restrictivos."@es ;
    rdfs:label "disuelve"@es .

qm:embodies
    rdfs:label "encarna"@es .

qm:embodiesPrinciple
    rdfs:comment "Indica que una dimensión representa un principio psicológico primordial."@es ;
    rdfs:label "encarna el principio"@es .

qm:emergesFromInteractionOf
    rdfs:comment "Describe cómo los estados complejos surgen de la interacción dinámica y la suma ponderada de múltiples dimensiones psicodinámicas."@es ;
    rdfs:label "emerge de la interacción de"@es .

qm:employs
    rdfs:comment "Indica que un proceso o práctica hace uso de un mecanismo o función específica."@es ;
    rdfs:label "emplea"@es .

qm:enables
    rdfs:comment "Indica que un marco conceptual proporciona la capacidad para un proceso o resultado específico."@es ,
                 "Indica que un mecanismo hace posible un proceso o estado específico."@es ;
    rdfs:label "habilita"@es .

qm:enablesConversionOf
    rdfs:comment "Indica la función de un mecanismo de traducción sofisticado, que convierte experiencias internas abstractas en realidades externas concretas."@es ;
    rdfs:label "habilita la conversión de"@es .

qm:facilitatesEmbodimentOf
    rdfs:comment "Indica la función de una interfaz mente-cuerpo, integrando la conciencia somática en el procesamiento cognitivo."@es ;
    rdfs:label "facilita la encarnación de"@es .

qm:filters
    rdfs:comment "Indica que un mecanismo moldea inconscientemente un proceso como la percepción."@es ;
    rdfs:label "filtra"@es .

qm:follows
    rdfs:label "sigue a"@es .

qm:formsBasisFor
    rdfs:comment "Indica que un estado fundamental es un prerrequisito para una capacidad cognitiva más avanzada."@es ;
    rdfs:label "forma la base para"@es .

qm:formsFoundationOf
    rdfs:comment "Indica que una dimensión sirve como un constituyente central o base operativa para un aspecto más amplio de la conciencia."@es ;
    rdfs:label "forma el fundamento de"@es .

qm:functionsAs
    rdfs:comment "Describe el rol de una dimensión como un principio organizador fundamental o mecanismo psicológico."@es ;
    rdfs:label "funciona como"@es .

qm:generates
    rdfs:comment "Indica que una dimensión puede producir estructuras psicológicas específicas basadas en la experiencia."@es ;
    rdfs:label "genera"@es .

qm:governs
    rdfs:label "gobierna"@es .

qm:harmonizes
    rdfs:comment "Una propiedad que indica la función de llevar diferentes elementos a un estado de equilibrio y acuerdo."@es ;
    rdfs:label "armoniza"@es ;
    skos:definition "Llevar a un estado de concordia o acuerdo."@es .

qm:hasCapacityFor
    rdfs:label "tiene capacidad para"@es .

# --- Section 2 ---

qm:hasConstraint
    rdfs:comment "Indica restricciones fijas, como leyes físicas o requisitos biológicos, que limitan una realidad construida."@es ;
    rdfs:label "tiene restricción"@es .

qm:hasDynamic
    rdfs:comment "Indica un principio fundamental o modelo de interacción que gobierna un proceso."@es ;
    rdfs:label "tiene dinámica"@es .

qm:hasEngagementStyle
    rdfs:comment "Define el enfoque característico que una metodología adopta al interactuar con los fenómenos mentales internos."@es ;
    rdfs:label "tiene estilo de compromiso"@es .

qm:hasInterdimensionalConnection
    rdfs:comment "Una propiedad genérica que representa una conexión conceptual o flujo dinámico entre Dimensiones Psicodinámicas."@es ;
    rdfs:label "tiene Conexión Interdimensional"@es .

qm:hasMode
    rdfs:comment "Indica que un proceso puede ocurrir de diferentes maneras, como de forma intencional o reactiva."@es ;
    rdfs:label "tiene modo"@es .

qm:hasNegativeConsequence
    rdfs:comment "Indica un posible resultado desadaptativo si un estado no se gestiona o resuelve adecuadamente."@es ;
    rdfs:label "tiene consecuencia negativa"@es .

qm:hasPhase
    rdfs:comment "Indica una etapa distintiva dentro de un proceso más amplio, como la liberación de guiones heredados."@es ;
    rdfs:label "tiene fase"@es .

qm:hasPractice
    rdfs:comment "Indica que un modo específico de colapso está asociado con ciertas técnicas o prácticas."@es ;
    rdfs:label "tiene práctica"@es .

qm:hasPrimacyOver
    rdfs:comment "Una relación que indica que una dimensión tiene una influencia controladora o predominante sobre otra."@es ;
    rdfs:label "tiene primacía sobre"@es ;
    skos:definition "Una propiedad que indica que un elemento prevalece sobre otro."@es .

qm:hasResultingOutcome
    rdfs:comment "Indica las capacidades mejoradas o los estados beneficiosos logrados a través de un proceso o aplicación."@es ;
    rdfs:label "tiene resultado consecuente"@es .

qm:hasSubStrategy
    rdfs:comment "Indica una relación jerárquica donde una estrategia más amplia engloba otras más específicas."@es ;
    rdfs:label "tiene sub-estrategia"@es .

qm:hasViewOfPerception
    rdfs:comment "Define la postura epistemológica que una metodología adopta con respecto a la naturaleza de la percepción."@es ;
    rdfs:label "tiene visión de la percepción"@es .

qm:impliesNeedFor
    rdfs:comment "Indica que un desafío particular necesita un enfoque o epistemología específica."@es ;
    rdfs:label "implica la necesidad de"@es .

qm:influences
    rdfs:comment "Indica que un factor externo o interno puede afectar la naturaleza o el resultado del proceso de colapso."@es ,
                 "Indica que una dimensión afecta la calibración o función de otra."@es ;
    rdfs:label "influencia"@es .

qm:informs
    rdfs:comment "Indica que una entidad proporciona la entrada o los datos primarios para un proceso o juicio posterior."@es ;
    rdfs:label "informa"@es .

qm:initiates
    rdfs:label "inicia"@es .

qm:initiatesModality
    rdfs:comment "Indica que una dimensión es el elemento inaugural de una modalidad específica."@es ;
    rdfs:label "inicia modalidad"@es .

qm:interferesWith
    rdfs:comment "Indica una influencia disruptiva o distorsionadora en un proceso o desarrollo natural."@es ;
    rdfs:label "interfiere con"@es .

qm:isAchievedThrough
    rdfs:comment "Indica el método o proceso mediante el cual se alcanza un estado u objetivo."@es ;
    rdfs:label "se logra a través de"@es ;
    skos:definition "Una propiedad que especifica los medios para lograr el sujeto."@es .

qm:isAlteredBy
    rdfs:comment "Indica que el sujeto puede ser cambiado o modificado por el objeto."@es ;
    rdfs:label "es alterado por"@es ;
    skos:definition "Una propiedad que especifica que el sujeto es capaz de ser cambiado por el objeto."@es .

qm:isAppliedTo
    rdfs:comment "Indica que un principio de meta-nivel es la base para un concepto o aplicación más específico."@es ;
    rdfs:label "se aplica a"@es .

qm:isArchitectOf
    rdfs:comment "Indica que una dimensión proporciona la integridad estructural para una construcción psicológica."@es ;
    rdfs:label "es arquitecto de"@es .

qm:isBalancedBy
    rdfs:comment "Indica una dinámica crucial donde una dimensión proporciona un contrapeso estructurador o contenedor necesario para otra."@es ;
    rdfs:label "es equilibrado por"@es .

qm:isCalculatedFrom
    rdfs:comment "Indica que el valor del sujeto se deriva del objeto a través de un cálculo específico."@es ;
    rdfs:label "se calcula a partir de"@es ;
    skos:definition "Una propiedad que especifica que el sujeto es el resultado de un cálculo que involucra al objeto."@es .

qm:isConfirmedBy
    rdfs:comment "Indica que la existencia de un fenómeno se conoce a través de su influencia constante o patrones discernibles, en lugar de la observación directa."@es ;
    rdfs:label "es confirmado por"@es .

qm:isConstrainedBy
    rdfs:comment "Indica que el sujeto está limitado o restringido por el objeto."@es ;
    rdfs:label "es restringido por"@es ;
    skos:definition "Una propiedad que especifica que el sujeto está sujeto a limitaciones del objeto."@es .

qm:isCultivatedBy
    rdfs:comment "Indica un método o práctica utilizada para desarrollar o trabajar hábilmente con un estado cognitivo."@es ;
    rdfs:label "es cultivado por"@es .

qm:isDeterminedBy
    rdfs:comment "Indica los factores específicos que calculan o definen un componente dentro de la arquitectura formal."@es ;
    rdfs:label "es determinado por"@es .

qm:isDevelopedBy
    rdfs:comment "Indica la práctica o método a través del cual se cultiva una capacidad o habilidad."@es ;
    rdfs:label "es desarrollado por"@es ;
    skos:definition "Una propiedad que especifica los medios por los cuales se desarrolla el sujeto."@es .

qm:isEngagedBy
    rdfs:comment "Indica un proceso o práctica que activa o hace uso de una función o capacidad particular."@es ;
    rdfs:label "es activado por"@es ;
    skos:definition "Una propiedad que indica que el sujeto es activado o utilizado por el objeto."@es .

qm:isEngineOf
    rdfs:comment "Indica que una práctica es el motor principal para un tipo específico de colapso cognitivo."@es ;
    rdfs:label "es motor de"@es .

qm:isFirstStepIn
    rdfs:comment "Indica que un proceso es el desencadenante inicial y activo de una dinámica o teoría más amplia."@es ;
    rdfs:label "es el primer paso en"@es .

qm:isFormedBy
    rdfs:comment "Indica que una construcción psicológica es moldeada o creada por un tipo específico de influencia externa o mecanismo de condicionamiento."@es ;
    rdfs:label "es formado por"@es .

qm:isFoundationFor
    rdfs:comment "Indica que un mecanismo es el soporte fundamental para un modo de conciencia más avanzado."@es ;
    rdfs:label "es fundamento para"@es .

qm:isFundamentalTo
    rdfs:comment "Indica que un concepto o proceso es un prerrequisito esencial o una base subyacente para otro."@es ;
    rdfs:label "es fundamental para"@es .

qm:isFundamentalUnitOf
    rdfs:label "es unidad fundamental de"@es .

qm:isInputTo
    rdfs:comment "Indica que el sujeto sirve como datos o un componente de partida para el proceso del objeto."@es ;
    rdfs:label "es entrada para"@es ;
    skos:definition "Una propiedad que especifica que el sujeto es una entrada para el objeto."@es .

qm:isKeyTo
    rdfs:comment "Indica que una dimensión es un elemento crucial para lograr un estado o proceso específico."@es ;
    rdfs:label "es clave para"@es .

qm:isLiberatedBy
    rdfs:comment "Indica el proceso o la metodología sistemática para trascender una construcción psicológica limitante."@es ;
    rdfs:label "es liberado por"@es .

qm:isLocusOf
    rdfs:comment "Indica que una dimensión o concepto es el punto central o el sitio principal de un proceso o función particular."@es ;
    rdfs:label "es locus de"@es ;
    skos:definition "Una propiedad que indica la ubicación central o el foco de algo."@es .

qm:isMediatedBy
    rdfs:comment "Indica que una dimensión sirve como un modulador emocional, resolviendo la tensión dinámica entre otras dos dimensiones."@es ,
                 "Indica que una forma de conocimiento o experiencia no se aprehende directamente, sino que se filtra a través de otro proceso o entidad."@es ;
    rdfs:label "es mediado por"@es .

qm:isModulatedBy
    rdfs:comment "Indica una relación jerárquica pero dinámicamente interactiva donde la salida de una modalidad moldea la textura y el funcionamiento de otra."@es ,
                 "Indica que la influencia de un componente es ponderada o ajustada por una tendencia personal o un factor disposicional."@es ;
    rdfs:label "es modulado por"@es .

qm:isNegatedBy
    rdfs:comment "Indica que la expresión de una dimensión pasiva puede ser anulada o negada por una dimensión con primacía volitiva."@es ;
    rdfs:label "es negado por"@es .

qm:isOutputOf
    rdfs:comment "Indica que el sujeto es el resultado o producto del proceso del objeto."@es ;
    rdfs:label "es salida de"@es ;
    skos:definition "Una propiedad que especifica que el sujeto es un resultado del objeto."@es .

qm:isRegulatedBy
    rdfs:comment "Indica que una respuesta emocional es modulada o equilibrada por la función de una dimensión específica."@es ;
    rdfs:label "es regulado por"@es .

qm:isResolvedBy
    rdfs:comment "Indica el catalizador o proceso a través del cual un estado probabilístico colapsa en una experiencia definida."@es ;
    rdfs:label "es resuelto por"@es .

qm:isSegregatedBy
    rdfs:comment "Indica que una característica estructural fundamental separa dos modos diferentes de ser o conocer."@es ;
    rdfs:label "es segregado por"@es .

qm:isShapedByTechnique
    rdfs:comment "Indica que un proceso puede ser influenciado por una práctica o método deliberado."@es ;
    rdfs:label "es moldeado por técnica"@es .

qm:isSourceOf
    rdfs:comment "Indica que el sujeto es el origen o la génesis del objeto."@es ;
    rdfs:label "es fuente de"@es ;
    skos:definition "Una propiedad que indica que el sujeto da origen al objeto."@es .

qm:isSubjectTo
    rdfs:comment "Indica que una clase de entidades puede exhibir un principio o característica específica."@es ;
    rdfs:label "está sujeto a"@es .

qm:isSupportedByMechanism
    rdfs:comment "Indica que el impulso sostenido de una dimensión es apoyado por mecanismos psicológicos específicos."@es ;
    rdfs:label "es apoyado por mecanismo"@es .

qm:isTransformedUsing
    rdfs:comment "Indica la función matemática utilizada para convertir un valor bruto en una intensidad final y normalizada."@es ;
    rdfs:label "se transforma usando"@es .

qm:isTransmittedVia
    rdfs:comment "Indica el canal o método a través del cual se transmite un concepto, como un Guion Heredado."@es ;
    rdfs:label "se transmite vía"@es .

qm:isTriggeredBy
    rdfs:comment "Indica el catalizador para un proceso psicodinámico."@es ;
    rdfs:label "es desencadenado por"@es .

qm:leadsTo
    rdfs:comment "Indica una progresión causal o de desarrollo de un estado a otro."@es ;
    rdfs:label "conduce a"@es .

qm:leverages
    rdfs:comment "Indica que un proceso hace un uso estratégico de un recurso o dimensión particular."@es ;
    rdfs:label "aprovecha"@es ;
    skos:definition "Usar algo para obtener la máxima ventaja."@es .

qm:mapsDirectlyTo
    rdfs:comment "Indica una correspondencia funcional directa entre una práctica y una dimensión psicodinámica."@es ;
    rdfs:label "mapea directamente a"@es .

qm:modifies
    rdfs:comment "Indica que un acto o proceso influye inherentemente en la naturaleza y el carácter de lo que se observa."@es ;
    rdfs:label "modifica"@es .

qm:mutuallyInfluences
    rdfs:comment "Indica que las dimensiones existen en una red de relaciones simultáneas y bidireccionales, creando propiedades emergentes."@es ;
    rdfs:label "se influencian mutuamente"@es .

qm:navigatesWithin
    rdfs:comment "Indica que un proceso debe operar dentro del contexto de ciertos límites fijos."@es ;
    rdfs:label "navega dentro de"@es .

qm:operatesAs
    rdfs:comment "Indica el rol o función específica que cumple un concepto o dimensión."@es ;
    rdfs:label "opera como"@es ;
    skos:definition "Una propiedad que describe el rol funcional del sujeto."@es .

qm:operatesThrough
    rdfs:comment "Indica el mecanismo o proceso principal por el cual funciona una dimensión o concepto."@es ;
    rdfs:label "opera a través de"@es ;
    skos:definition "Una propiedad que especifica los medios por los cuales algo funciona."@es .

qm:orchestrates
    rdfs:comment "Indica la gestión del desarrollo de sutiles 'proto-impulsos' internos en expresiones externas auténticas."@es ;
    rdfs:label "orquesta"@es .

qm:performs
    rdfs:comment "Indica una acción o proceso llevado a cabo por un tipo específico de agente o estado de conciencia."@es ;
    rdfs:label "realiza"@es .

qm:posits
    rdfs:comment "Indica que una teoría afirma o propone un concepto o relación específica."@es ;
    rdfs:label "postula"@es .

qm:practices
    rdfs:comment "Una propiedad que vincula a un agente con una práctica o método que realiza."@es ;
    rdfs:label "practica"@es ;
    skos:definition "Realizar o llevar a cabo una actividad o método particular."@es .

qm:precedes
    rdfs:comment "Indica que un estado o proceso existe antes que otro en el flujo cognitivo."@es ;
    rdfs:label "precede a"@es .

qm:produces
    rdfs:comment "Indica el resultado de un proceso o método."@es ;
    rdfs:label "produce"@es .

qm:progressesTo
    rdfs:label "progresa a"@es .

qm:providesFoundationFor
    rdfs:comment "Indica que el sujeto proporciona la base o el soporte necesario para el objeto."@es ;
    rdfs:label "proporciona fundamento para"@es ;
    skos:definition "Una propiedad que indica que el sujeto es un soporte fundamental para el objeto."@es .

qm:receivesInputFrom
    rdfs:label "recibe entrada de"@es .

qm:reliesOn
    rdfs:comment "Indica que un mecanismo o proceso depende de una dimensión o componente específico para su operación."@es ;
    rdfs:label "se basa en"@es .

qm:servesAs
    rdfs:comment "Indica que una dimensión proporciona una función fundamental para la psique."@es ;
    rdfs:label "sirve como"@es .

# --- Section 3 ---

qm:shapes
    rdfs:comment "Indica que una dimensión dirige o determina activamente la naturaleza de un fenómeno psicológico."@es ;
    rdfs:label "moldea"@es .

qm:stemsFrom
    rdfs:label "proviene de"@es .

qm:targets
    rdfs:comment "Define los fenómenos o constructos psicológicos primarios que una estrategia dada busca influenciar o transformar."@es ;
    rdfs:label "apunta a"@es .

qm:translatesValuesInto
    rdfs:comment "Indica el mecanismo psicológico a través del cual los principios abstractos y los sistemas de valores internos logran una manifestación concreta en una acción externa consistente."@es ;
    rdfs:label "traduce valores en"@es .

qm:underpins
    rdfs:comment "Indica que una dimensión proporciona la base para una capacidad psicológica crucial."@es ;
    rdfs:label "sustenta"@es .

qm:uses
    rdfs:comment "Indica los métodos o herramientas empleados por un proceso."@es ;
    rdfs:label "utiliza"@es .

qm:yields
    rdfs:comment "Indica el resultado o producto de una práctica sostenida."@es ;
    rdfs:label "produce"@es .

qm:AbstractInternalExperience
    rdfs:comment "Estados internos como intuiciones, principios, valores y comprensiones intuitivas."@es ;
    rdfs:label "Experiencia Interna Abstracta"@es .

qm:ActionableIntelligence
    rdfs:comment "Orientación práctica aplicable en situaciones del mundo real, sintetizada a partir de diversas fuentes de información."@es ;
    rdfs:label "Inteligencia Accionable"@es .

qm:ActiveConstitutiveForceView
    rdfs:comment "La visión de que la percepción es una fuerza activa y creativa que moldea y genera significativamente la realidad experimentada."@es ;
    rdfs:label "Visión de Fuerza Constitutiva Activa"@es .

qm:ActiveKnowing
    rdfs:label "Conocimiento Activo"@es .

qm:ActiveMastery
    rdfs:comment "El moldeamiento deliberado de la percepción y la selección consciente de puntos focales para la conciencia, permitiendo una influencia hábil sobre cómo las experiencias potenciales colapsan en experiencias reales."@es ;
    rdfs:label "Maestría Activa"@es .

qm:ActiveReframingProcess
    rdfs:comment "El compromiso en tres pasos con la Modalidad Principal para reevaluar y transformar conscientemente la Valoración Cognitiva."@es ;
    rdfs:label "Proceso de Reencuadre Activo"@es .

qm:ActiveStructuralInvestigation
    rdfs:comment "La práctica de investigar activamente la estructura y los orígenes de los fenómenos mentales, tratándolos como artefactos generados por sistemas psicológicos subyacentes."@es ;
    rdfs:label "Investigación Estructural Activa"@es .

qm:ActualizationProcess
    rdfs:comment "La etapa final del proceso psicodinámico donde el potencial bruto de la Activación Dimensional (Kj) se transforma en una Intensidad Final normalizada (xj) a través de una Función Sigmoidea. Esto representa el 'colapso' definitivo para cada dimensión, moviéndola de un estado de activación potencial a un nivel específico de expresión."@es ,
                 "La etapa final donde el potencial bruto de la Activación Dimensional (Kj) se transforma en una Intensidad Final (xj) a través de una Función Sigmoidea, que luego constituye el Estado Mental General (S)."@es ,
                 "El proceso donde el potencial bruto de la Activación Dimensional (Kj) se transforma en una Intensidad Final (xj) a través de una Función Sigmoidea."@es ;
    rdfs:label "Proceso de Actualización"@es .

qm:ActualizedExperience
    rdfs:comment "El resultado singular, definido y conscientemente experimentado resultante del Colapso de la Onda Psicodinámica. Esta es la realidad manifestada de un estado mental."@es ;
    rdfs:label "Experiencia Actualizada"@es .

qm:AdvancedPracticesAndMethodologiesCategory
    rdfs:comment "Una agrupación para técnicas y enfoques más sofisticados dentro del marco."@es ,
                 "Una metodología estructurada dentro de Mindfulness Cuántico para interactuar directamente con los sistemas generativos de la conciencia, permitiendo una relación más sofisticada y agéntica con la propia experiencia interna."@es ;
    rdfs:label "Prácticas y Metodologías Avanzadas"@es .

qm:AestheticPrinciple
    rdfs:comment "Un principio que gobierna la percepción e integración de experiencias relacionadas con la belleza, la proporción y la relación armónica."@es ;
    rdfs:label "Principio Estético"@es .

qm:AestheticResolution
    rdfs:comment "Una forma de resolución de conflictos que implica encontrar soluciones que honren las necesidades esenciales de todas las partes y trasciendan las limitaciones del conflicto original."@es ;
    rdfs:label "Resolución Estética"@es .

qm:Anxiety
    rdfs:comment "Un patrón emergente donde la Dimensión Psico-Protectora se vuelve hiperactiva, la Dimensión Psico-Empática se contrae, la Dimensión Psico-Motivacional se fragmenta y la Dimensión Psico-Receptiva se vuelve hipersensible."@es ;
    rdfs:label "Ansiedad"@es .

qm:AssignedMeaning
    rdfs:comment "La interpretación o significancia que la mente atribuye a una percepción o estímulo bruto."@es ;
    rdfs:label "Significado Asignado"@es ;
    skos:definition "El significado atribuido a un estímulo durante el proceso de percepción."@es .

qm:AttentionSculpting
    rdfs:label "Escultura de la Atención"@es .

qm:Attunement
    rdfs:comment "La capacidad de sentir y responder a los estados internos de los demás con precisión y cuidado a nivel emocional, cognitivo, somático y energético."@es ;
    rdfs:label "Sintonización"@es .

qm:AverageValenceOfPriorState
    rdfs:comment "Captura la idea de 'inercia emocional' o el estado de ánimo general persistente del estado mental inmediatamente anterior (S_t-1)."@es ;
    rdfs:label "Valencia Promedio del Estado Anterior (ValenciaProm(S_t-1))"@es .

qm:BehavioralManifestation
    rdfs:label "Manifestación Conductual"@es .

qm:BeliefFormation
    rdfs:comment "El mecanismo por el cual se alteran las estructuras cognitivas estables a largo plazo (Rasgos). Se rige por el principio 'La Práctica se Convierte en Creencia', donde los estados mentales repetidos (S), especialmente aquellos impulsados por fuertes activaciones dentro de la Modalidad Secundaria, pueden modificar de forma duradera las variables de Rasgo fundamentales (Tj)."@es ;
    rdfs:label "Formación de Creencias"@es .

qm:BiologicalOverrideSystem
    rdfs:label "Sistema de Anulación Biológica"@es .

qm:BonesOfReality
    rdfs:comment "Restricciones fijas como leyes físicas, requisitos biológicos y circunstancias materiales que no están sujetas a la construcción perceptual."@es ;
    rdfs:label "Huesos de la Realidad"@es .

qm:BoundedCompassion
    rdfs:comment "La capacidad de cuidar profundamente mientras se mantiene la integridad estructural necesaria para el cuidado sostenido, habilitada por el equilibrio de Pd4 y Pd5."@es ;
    rdfs:label "Compasión Delimitada"@es .

qm:ChallengesAndLimitations
    rdfs:comment "Una clase que abarca obstáculos, restricciones inherentes o dificultades que impiden el funcionamiento psicológico óptimo, obstaculizan el desarrollo consciente o restringen la aplicación directa de los principios de Mindfulness Cuántico."@es ;
    rdfs:label "Desafíos y Limitaciones"@es .

qm:ChallengesAndLimitationsCategory
    rdfs:comment "Dificultades o límites reconocidos en la teoría o aplicación de Mindfulness Cuántico."@es ;
    rdfs:label "Desafíos y Limitaciones"@es .

qm:ChaosConciergePattern
    rdfs:comment "Una manifestación específica de la disfunción Psico-Protectora donde el mecanismo protector corrupto crea disrupción de manera inadvertida o intencional."@es ;
    rdfs:label "Patrón de Conserje del Caos"@es .

qm:ClassicalMindfulness
    rdfs:comment "Un enfoque metodológico que enfatiza la observación intencional y sin juicios de los fenómenos momento a momento para cultivar una conciencia estable y centrada en el presente y una 'maestría pasiva'."@es ,
                 "Una práctica regulatoria o amortiguadora que tiene como objetivo neutralizar una Valoración Cognitiva negativa reduciendo la reactividad (disminuyendo wΨ y wS) y observando sin juzgar (llevando la Valencia(Ψ) hacia cero). Es una práctica de observación no reactiva."@es ,
                 "Una práctica regulatoria o amortiguadora que busca reducir la intensidad de las reacciones emocionales cultivando una observación estable, sin juicios y no elaborativa de la experiencia del momento presente. Su objetivo es la 'maestría pasiva' y la ecuanimidad."@es ;
    rdfs:label "Mindfulness Clásico"@es ,
               "Mindfulness Clásico (Pasivo)"@es .

qm:CognitiveAgency
    rdfs:comment "La capacidad desarrollada a través de la gestión intencional de la atención para guiar conscientemente el proceso de colapso psicodinámico hacia potenciales mentales deseados."@es ;
    rdfs:label "Agencia Cognitiva"@es .

qm:CognitiveAnchoring
    rdfs:comment "Un mecanismo psicológico fundamental responsable de estabilizar la intención y permitir la acción con propósito seleccionando y enfocándose en posibilidades específicas de un campo probabilístico. Es un proceso activo de mantener una orientación mental o un conjunto intencional a lo largo del tiempo."@es ,
                 "Un mecanismo por el cual la intención mental resiste las distracciones externas a través de la resonancia con estados-meta no locales."@es ,
                 "La tendencia a depender demasiado de una información inicial (el 'ancla') al tomar decisiones o juicios, influyendo en el procesamiento posterior."@es ;
    rdfs:label "Anclaje Cognitivo"@es .

qm:CognitiveAnchoringComponent
    rdfs:comment "Un componente primario e interdependiente del sistema de estabilización del Anclaje Cognitivo."@es ;
    rdfs:label "Componente de Anclaje Cognitivo"@es .

qm:CognitiveAnchoringFailureConsequence
    rdfs:comment "Una forma de malestar psicológico o deterioro funcional resultante de un Anclaje Cognitivo fallido o comprometido."@es ;
    rdfs:label "Consecuencia del Fallo del Anclaje Cognitivo"@es .

qm:CognitiveAppraisalBias
    rdfs:comment "Un sesgo cognitivo o afectivo de base arraigado en las características estables del individuo (p. ej., optimismo, pesimismo), que es contribuido por la Modalidad Principal a la Valoración Cognitiva."@es ;
    rdfs:label "Sesgo de Valoración Cognitiva (Sesgo_M1)"@es .

qm:CognitiveAppraisalComponent
    rdfs:comment "Una fuerza distintiva que contribuye a la suma ponderada y calculada dinámicamente que forma la Valoración Cognitiva (C)."@es ;
    rdfs:label "Componente de Valoración Cognitiva"@es .

qm:CognitiveAppraisalComponentsCategory
    rdfs:comment "Contenedor conceptual para las partes constituyentes de una Valoración Cognitiva."@es ;
    rdfs:label "Componentes (C = wΨ ⋅ Valencia(Ψ) + wS ⋅ ValenciaProm(S_t-1) + Sesgo_M1)"@es .

qm:CognitiveBias
    rdfs:label "Sesgo Cognitivo"@es .

qm:CognitiveDecoherence
    rdfs:label "Decoherencia Cognitiva"@es .

qm:CognitiveDistillation
    rdfs:comment "El proceso de extraer conocimientos funcionales de los sistemas de sabiduría tradicionales y traducirlos a un contexto psicodinámico moderno."@es ;
    rdfs:label "Destilación Cognitiva"@es .

qm:CognitiveEmergenceField
    rdfs:comment "Un espacio abstracto donde residen los potenciales de activación brutos (Kj) de las dimensiones psicodinámicas antes de manifestarse como aspectos concretos de la experiencia consciente a través del proceso de Actualización."@es ;
    rdfs:label "Campo de Emergencia Cognitiva"@es .

qm:CognitiveEmotionalPatternInheritance
    rdfs:label "Herencia de Patrones Cognitivo-Emocionales"@es .

qm:CognitiveEndurance
    rdfs:comment "La capacidad de sostener la motivación y permitir el reconocimiento de patrones a largo plazo, esencial para alcanzar metas en períodos de tiempo extendidos."@es ;
    rdfs:label "Resistencia Cognitiva"@es .

qm:CognitiveEnhancement
    rdfs:comment "Un proceso integral que tiene como objetivo optimizar la función mental, mejorar las habilidades cognitivas y cultivar estados mentales óptimos para una mayor eficacia personal y profesional. Es un proceso dinámico y multidimensional que requiere un cultivo deliberado a través de prácticas basadas en evidencia y una comprensión matizada de la arquitectura cognitiva."@es ,
                 "Metodologías diseñadas específicamente para mejorar la claridad cognitiva, la creatividad y la eficacia general al abordar las limitaciones cognitivas personales y fomentar estados mentales óptimos."@es ,
                 "La mejora o aumento de las habilidades cognitivas a través de prácticas o comprensión del marco."@es ;
    rdfs:label "Mejora Cognitiva"@es .

# --- Section 4 ---

qm:CognitiveEntropicDrift
    rdfs:label "Deriva Entrópica Cognitiva"@es .

qm:CognitiveFieldManipulation
    rdfs:label "Manipulación del Campo Cognitivo"@es .

qm:CognitiveFilteringMechanism
    rdfs:label "Mecanismo de Filtrado Cognitivo"@es .

qm:CognitiveFlow
    rdfs:label "Flujo Cognitivo"@es .

qm:CognitiveFluency
    rdfs:comment "La habilidad para trabajar diestramente con los procesos formativos de la conciencia, resultado de la integración sinérgica de la atención plena y la contemplación."@es ;
    rdfs:label "Fluidez Cognitiva"@es .

qm:CognitiveInfluence
    rdfs:label "Influencia Cognitiva"@es .

qm:CognitiveMapping
    rdfs:label "Mapeo Cognitivo"@es .

qm:CognitiveMeasurement
    rdfs:comment "El reconocimiento y la aprehensión conscientes de los estados cognitivos, actuando como una intervención activa y ontológica que conduce al colapso probabilístico de interpretaciones potenciales en percepciones y experiencias definidas."@es ;
    rdfs:label "Medición Cognitiva"@es .

qm:CognitiveMechanism
    rdfs:comment "Procesos o estructuras subyacentes que facilitan las funciones y estados cognitivos dentro del marco de Mindfulness Cuántico."@es ;
    rdfs:label "Mecanismo Cognitivo"@es .

qm:CognitiveModality
    rdfs:label "Modalidad Cognitiva"@es .

qm:CognitiveOptimization
    rdfs:label "Optimización y Refinamiento Cognitivo"@es .

qm:CognitiveOptimizationAndRefinement
    rdfs:comment "Prácticas destinadas a mejorar la función, claridad y eficiencia cognitiva a través de técnicas conscientes específicas."@es ;
    rdfs:label "Optimización y Refinamiento Cognitivo"@es .

qm:CognitiveOverwhelm
    rdfs:label "Sobrecarga Cognitiva"@es .

qm:CognitiveProcess
    rdfs:label "Proceso Cognitivo"@es .

qm:CognitiveResources
    rdfs:label "Recursos Cognitivos"@es .

qm:CognitiveStrainAndDysfunction
    rdfs:comment "Problemas que surgen del esfuerzo mental o de procesos cognitivos desadaptativos en el contexto del marco."@es ,
                 "Agotamiento mental y función cognitiva deteriorada como resultado de demandas mentales intensas, saturación de información o conflictos internos."@es ;
    rdfs:label "Tensión y Disfunción Cognitiva"@es .

qm:CognitiveStructuringApproaches
    rdfs:label "Enfoques de Estructuración Cognitiva"@es .

qm:CognitiveSuperposition
    rdfs:comment "Un estado preconsciente fundamental donde los fenómenos mentales existen no como entidades fijas, sino como campos de probabilidad dinámicos que contienen múltiples posibilidades de configuración simultáneas. Se caracteriza por la multiplicidad, el potencial no resuelto y los límites ambiguos, formando la base para la flexibilidad mental y el potencial creativo."@es ,
                 "Un estado donde múltiples pensamientos, percepciones o intuiciones potenciales coexisten como un campo de probabilidad dinámico sin resolución definitiva, antes del colapso psicodinámico."@es ,
                 "El estado de potencialidad y múltiples posibilidades coexistentes dentro del paisaje cognitivo antes de un 'colapso' en una única realidad percibida."@es ;
    rdfs:label "Superposición Cognitiva"@es ;
    skos:altLabel "estado de potencialidad pre-convergencia"@es .

qm:CollapseDysfunction
    rdfs:label "Disfunción del Colapso"@es .

qm:CollapseFatigue
    rdfs:label "Fatiga del Colapso"@es .

qm:CollapseInfluencePractice
    rdfs:comment "Una práctica o técnica para influir consciente y hábilmente en el proceso de colapso psicodinámico."@es ;
    rdfs:label "Práctica de Influencia en el Colapso"@es .

qm:CollapsePointInterventions
    rdfs:label "Intervenciones en el Punto de Colapso"@es .

qm:ConditioningMechanism
    rdfs:comment "Un mecanismo psicológico o social que facilita la formación e incrustación de Guiones Heredados."@es ;
    rdfs:label "Mecanismo de Condicionamiento"@es .

qm:ConfirmationBiasCycle
    rdfs:label "Ciclo de Sesgo de Confirmación y Construcción de la Realidad"@es .

qm:ConsciousAttention
    rdfs:comment "El catalizador que desencadena el colapso psicodinámico, resolviendo un campo de probabilidad de múltiples estados potenciales en una única experiencia definida."@es ;
    rdfs:label "Atención Consciente"@es ;
    skos:altLabel "Catalizador"@es ,
                  "Vector de Colapso"@es ,
                  "Medición Cognitiva"@es ,
                  "Observación Consciente"@es ,
                  "Atención Enfocada"@es .

qm:ConsciousAwareness
    rdfs:comment "La base operativa de la conciencia consciente y el carácter individual, que las dimensiones forman colectivamente."@es ;
    rdfs:label "Conciencia Consciente"@es .

qm:ConsciousObservation
    rdfs:comment "El acto de llevar la conciencia a cualquier estado mental, que no es neutral sino una intervención creativa que modifica inherentemente tanto el estado como el campo más amplio de la conciencia."@es ;
    rdfs:label "Observación Consciente"@es .

qm:ConsciousRealityConstruction
    rdfs:comment "Un proceso deliberado y sistemático de dar forma a la propia realidad percibida a través de estrategias cognitivas y perceptuales intencionales, basado en el principio de que la percepción es una fuerza activa y constitutiva."@es ;
    rdfs:label "Construcción Consciente de la Realidad"@es .

qm:ConsciousRealityCreation
    rdfs:label "Creación Consciente de la Realidad / Reencuadre Perceptual"@es .

qm:ConsciousStack
    rdfs:comment "Aquel segmento del funcionamiento psicológico directamente accesible a la observación consciente y la intervención consciente, que actúa como la interfaz entre el procesamiento inconsciente y la conciencia explícita. Es coextensivo con la Modalidad Principal."@es ;
    rdfs:label "Pila Consciente"@es .

qm:ConsciousStateManagement
    rdfs:label "Gestión Consciente del Estado"@es .

qm:ConsciousnessFortification
    rdfs:label "Fortificación de la Conciencia"@es .

qm:ConsciousnessRefinement
    rdfs:comment "Un enfoque sofisticado para la autorregulación y el desarrollo psicológico habilitado por la comprensión de la dinámica dimensional."@es ,
                 "Prácticas diseñadas específicamente para trabajar hábilmente y refinar las Dimensiones Psicodinámicas, con el objetivo de fomentar el crecimiento personal y el bienestar holístico."@es ;
    rdfs:label "Refinamiento de la Conciencia"@es .

qm:ConsciousnessWaveFunction
    rdfs:comment "El espacio o campo conceptual dentro del cual existe la Superposición Cognitiva."@es ;
    rdfs:label "Función de Onda de la Conciencia"@es ;
    skos:altLabel "Función de Onda Mental"@es .

qm:ConstructedReality
    rdfs:comment "La comprensión de que la percepción es un proceso activo y constructivo que moldea la realidad que un individuo experimenta, en lugar de una recepción pasiva de la realidad objetiva."@es ;
    rdfs:label "Realidad Construida"@es .

qm:ConstructiveInterference
    rdfs:comment "Cuando las dimensiones se alinean armoniosamente, amplificando las cualidades positivas de cada una y conduciendo a estados de flujo y plenitud."@es ;
    rdfs:label "Interferencia Constructiva"@es .

qm:ContemplativeExperimentation
    rdfs:comment "La práctica de diseñar experimentos conductuales específicos para probar y refinar la comprensión a través de la aplicación práctica, uniendo la comprensión interna con la realidad manifiesta."@es ;
    rdfs:label "Experimentación Contemplativa"@es .

qm:ContemplativeInquiry
    rdfs:label "Indagación Contemplativa"@es .

qm:ContinuousMentationModel
    rdfs:comment "Modelos tradicionales que conceptualizan la mentación como un fenómeno continuo o indiferenciado, con los que contrasta el principio QM_Quantum."@es ;
    rdfs:label "Modelo de Mentación Continua"@es .

qm:CoreConceptsCategory
    rdfs:comment "Una agrupación conceptual para ideas fundamentales dentro del marco de Mindfulness Cuántico."@es ,
                 "Una nueva clase principal para conceptos fundacionales dentro del marco de Mindfulness Cuántico."@es ;
    rdfs:label "Concepto Central"@es ,
               "Conceptos Centrales"@es .

qm:CraftsmanshipOfCollapse
    rdfs:label "Artesanía del Colapso"@es .

qm:CreativeParalysis
    rdfs:label "Parálisis Creativa"@es .

qm:CreativePotential
    rdfs:label "Potencial Creativo"@es .

qm:CultivationMethod
    rdfs:comment "Prácticas basadas en el mindfulness diseñadas para desarrollar y fortalecer las capacidades psicodinámicas."@es ;
    rdfs:label "Método de Cultivo"@es .

qm:CulturalNarrative
    rdfs:comment "La categoría más amplia de experiencia de segunda mano, que abarca historias compartidas, símbolos y marcos interpretativos que definen la identidad cultural."@es ;
    rdfs:label "Narrativa Cultural"@es .

qm:DecisionArchitecture
    rdfs:label "Arquitectura de Decisión"@es .

qm:DeepPsychologicalTrauma
    rdfs:label "Trauma Psicológico Profundo"@es .

qm:DestructiveInterference
    rdfs:comment "Cuando las dimensiones entran en conflicto o compiten, disminuyendo las posibilidades o creando un conflicto interno y parálisis en la toma de decisiones."@es ;
    rdfs:label "Interferencia Destructiva"@es .

qm:DevelopmentalInterferencePattern
    rdfs:comment "El efecto disruptivo de un Guion Heredado en el desarrollo natural del potencial de un individuo."@es ;
    rdfs:label "Patrón de Interferencia en el Desarrollo"@es .

qm:DimensionalActivation
    rdfs:comment "El 'Corazón del Colapso'. Es el nivel de activación calculado para cada dimensión psicodinámica (Kj), que representa su 'potencial bruto' o 'carga' para contribuir al Estado Mental emergente. Es la suma de cinco influencias contribuyentes distintas."@es ,
                 "El 'Corazón del Colapso'. Es el nivel de activación calculado para cada dimensión psicodinámica, que representa su 'potencial bruto' o 'carga' para contribuir al Estado Mental emergente. Es la suma de cinco influencias contribuyentes distintas."@es ,
                 "El nivel de activación de colapso calculado para cada dimensión psicodinámica (Kj), que representa su potencial bruto para contribuir al Estado Mental emergente. Es la suma de cinco influencias contribuyentes distintas."@es ;
    rdfs:label "Activación Dimensional (Kj)"@es .

# --- Section 5 ---

qm:DimensionalActivationInfluence
    rdfs:comment "Una influencia contribuyente distinta que determina la activación total (Kj) para una sola dimensión."@es ;
    rdfs:label "Influencia de Activación Dimensional"@es .

qm:DimensionalActivationInfluencesCategory
    rdfs:comment "Contenedor conceptual para las influencias que contribuyen a la Activación Dimensional."@es ;
    rdfs:label "Influencias (Kj = I_Sj + I_Cj + I_Tj + I_Ψj + εj)"@es .

qm:DimensionalAttunement
    rdfs:comment "Una capacidad sofisticada para 'leer y trabajar con las energías sutiles de la conciencia' al reconocer qué dimensiones están activas, suprimidas o desequilibradas."@es ;
    rdfs:label "Sintonización Dimensional"@es .

qm:DimensionalCrystallization
    rdfs:comment "El proceso por el cual los estados psicológicos potenciales, existentes como campos de probabilidad dinámicos, se consolidan en experiencia real y comportamiento observable."@es ;
    rdfs:label "Cristalización Dimensional"@es .

qm:DimensionalMisalignment
    rdfs:label "Desalineación Dimensional"@es .

qm:DirectedFocus
    rdfs:comment "Compromiso cognitivo dirigido o la asignación específica de recursos atencionales a un estímulo particular; un aspecto clave de la 'conciencia volitiva'."@es ,
                 "Representa el compromiso cognitivo dirigido o la asignación específica de recursos atencionales a un estímulo particular. Es un aspecto clave de la 'conciencia volitiva'."@es ;
    rdfs:label "Compromiso Cognitivo Dirigido (f)"@es .

qm:DissociativeState
    rdfs:comment "Desapego de pensamientos, emociones, acciones o sentido del yo, lo que conduce a una conciencia fragmentada debido a la pérdida de una dirección intencional estable."@es ;
    rdfs:label "Estado Disociativo"@es .

qm:DynamicInterconnectedNetwork
    rdfs:comment "La conceptualización de las diez Dimensiones Psicodinámicas como un todo psicológico unificado, donde cada dimensión influye perpetuamente y es influenciada por todas las demás, creando el tapiz multifacético de la experiencia."@es ;
    rdfs:label "Red Dinámica e Interconectada"@es .

qm:DysfunctionalPattern
    rdfs:comment "Una expresión distorsionada o desequilibrada de una dimensión psicodinámica."@es ;
    rdfs:label "Patrón Disfuncional"@es .

qm:EmbodiedMindfulness
    rdfs:comment "La extensión del marco de Mindfulness Cuántico al cuerpo físico, viendo el lenguaje corporal como una manifestación observable de los procesos psicodinámicos internos."@es ;
    rdfs:label "Mindfulness Encarnado"@es .

qm:EmergentPropertiesCategory
    rdfs:comment "Propiedades o fenómenos que surgen de la interacción de componentes dentro del sistema psicodinámico, no reducibles a partes individuales."@es ;
    rdfs:label "Propiedades Emergentes"@es .

qm:EmotionalCollapseSculpting
    rdfs:label "Escultura del Colapso Emocional"@es .

qm:EmotionalCreativity
    rdfs:comment "Una capacidad mejorada para navegar por terrenos emocionales complejos, fomentada por la Dimensión Psico-Estética."@es ;
    rdfs:label "Creatividad Emocional"@es .

qm:EmotionalOpenness
    rdfs:comment "Una orientación fundamental hacia la recepción y el procesamiento de información afectiva sin un filtrado defensivo inmediato."@es ;
    rdfs:label "Apertura Emocional"@es .

qm:EmotionalQuantumEntanglement
    rdfs:comment "La interconexión persistente de los estados mentales y emocionales entre individuos, que opera a niveles sub-perceptuales."@es ;
    rdfs:label "Entrelazamiento Cuántico Emocional"@es .

qm:EmotionalReactivityPattern
    rdfs:comment "Plantillas psicológicas que influyen automáticamente en cómo los individuos interpretan y responden a los estímulos, particularmente en contextos interpersonales."@es ;
    rdfs:label "Patrón de Reactividad Emocional"@es .

qm:EmotionalRegulation
    rdfs:comment "La capacidad de gestionar el paisaje emocional para apoyar y estabilizar el compromiso intencional."@es ;
    rdfs:label "Regulación Emocional / Modulación Afectiva"@es .

qm:EmotionalRewilding
    rdfs:label "Resilvestración Emocional"@es .

qm:EmotionalStormTheory
    rdfs:label "Teoría de la Tormenta Emocional"@es .

qm:EmpiricalAbsence
    rdfs:comment "Un concepto que se refiere a aspectos de la realidad o la experiencia que están más allá de la observación empírica directa pero que se infiere que existen o influyen en el sistema."@es ,
                 "El principio de que ciertas dimensiones de la realidad son fundamentalmente inaccesibles a la verificación empírica directa, pero su existencia se confirma por sus efectos y patrones sistemáticos de manifestación. Esta inaccesibilidad en sí misma funciona como conocimiento positivo."@es ;
    rdfs:label "Ausencia Empírica"@es .

qm:EngagementStyle
    rdfs:label "Estilo de Compromiso"@es .

qm:EnhancedDecisionMaking
    rdfs:comment "Una aplicación práctica de la Conciencia Vectorizada, que permite la exploración integral de un campo de decisión y la alineación con intenciones más profundas."@es ;
    rdfs:label "Toma de Decisiones Mejorada"@es .

qm:EnvironmentalInfluence
    rdfs:label "Influencia Ambiental"@es .

qm:EnvironmentalResonance
    rdfs:comment "El grado en que las condiciones externas (físicas, sociales, culturales) se alinean y refuerzan con la intención anclada de un individuo."@es ;
    rdfs:label "Resonancia Ambiental"@es .

qm:EpistemologicalChallenges
    rdfs:comment "Dificultades para adquirir, validar o comprender el conocimiento, particularmente en lo que respecta a fenómenos subjetivos o no observables que son intrínsecamente inaccesibles a los métodos empíricos convencionales."@es ,
                 "Dificultades relacionadas con la naturaleza del conocimiento, la justificación y la creencia dentro del marco."@es ;
    rdfs:label "Desafíos Epistemológicos"@es .

qm:EpistemologicalDiscernment
    rdfs:comment "La habilidad cognitiva crucial de distinguir entre diferentes tipos de información de segunda mano, evaluar la fiabilidad de la fuente e integrar conocimientos valiosos mientras se mantiene la soberanía cognitiva."@es ;
    rdfs:label "Discernimiento Epistemológico"@es .

qm:Examples_Emergent
    rdfs:comment "Instancias o manifestaciones específicas de propiedades emergentes."@es ;
    rdfs:label "Ejemplos"@es .

qm:ExecutiveFunctionTraining
    rdfs:label "Entrenamiento de la Función Ejecutiva"@es .

qm:ExistentialDissonance
    rdfs:label "Disonancia Existencial"@es .

qm:ExperiencedReality
    rdfs:comment "El mundo subjetivo tal como es vivido y percibido por un individuo, entendido como una manifestación maleable de estados potenciales co-creados por el compromiso perceptual."@es ;
    rdfs:label "Realidad Experimentada"@es .

qm:ExperientialLimit
    rdfs:label "Límite Experiencial"@es .

qm:ExternalInfluence
    rdfs:comment "Una categoría distinta de fuente externa que contribuye a la formación de Guiones Heredados."@es ;
    rdfs:label "Influencia Externa"@es .

qm:FinalIntensity
    rdfs:comment "El valor escalado y transformado (entre 0 y 1) de la activación bruta de una Dimensión Psicodinámica (Kj), que representa su contribución actualizada a la experiencia consciente. Calculado como xj = 1 / (1 + e^-Kj)."@es ,
                 "El valor escalado y transformado (entre 0 y 1) de la activación bruta de una Dimensión Psicodinámica (Kj), que representa su contribución actualizada a la experiencia consciente. Se calcula para cada dimensión j usando la función sigmoidea: xj = 1 / (1 + e^-Kj)."@es ;
    rdfs:label "Intensidad Final (xj)"@es .

qm:FlowDynamicsInConsciousness
    rdfs:comment "La comprensión de cómo los estados mentales surgen, evolucionan y se disuelven como flujos energéticos, proporcionando una visión de las dimensiones temporales de la experiencia psicológica."@es ;
    rdfs:label "Dinámicas de Flujo en la Conciencia"@es .

qm:FormalArchitectureCategory
    rdfs:comment "Una agrupación conceptual para el modelo formal y estructurado de los procesos psicodinámicos."@es ,
                 "Un parámetro dentro del modelo arquitectónico formal de los estados psicodinámicos."@es ;
    rdfs:label "Parámetro Arquitectónico Formal"@es ,
               "Arquitectura Formal"@es .

qm:FormalTestimony
    rdfs:comment "La forma más explícita de experiencia de segunda mano, que abarca la transferencia deliberada de conocimiento como la instrucción académica, la consulta de expertos y las fuentes seleccionadas."@es ;
    rdfs:label "Testimonio Formal"@es .

qm:FrameworkPrinciple
    rdfs:comment "Un principio de meta-nivel que define la naturaleza o la filosofía fundamental del marco de Mindfulness Cuántico."@es ;
    rdfs:label "Principio del Marco"@es ,
               "X. Principio del Marco"@es .

qm:FrameworkPrinciplesCategory
    rdfs:comment "Principios fundamentales o reglas rectoras del marco de Mindfulness Cuántico."@es ;
    rdfs:label "Principios del Marco"@es .

qm:FreeWill
    rdfs:comment "La capacidad de ejercer una agencia significativa desarrollando la conciencia de las influencias en los patrones de colapso y eligiendo diferentes direcciones de colapso en situaciones futuras. Su fuente irreductible es la Dimensión Psico-Volitiva."@es ;
    rdfs:label "Libre Albedrío"@es .

qm:FundamentalEnergeticSubstrate
    rdfs:comment "La naturaleza de una Dimensión Psicodinámica como una fuerza dinámica y generativa que participa activamente en la creación continua de la experiencia consciente."@es ;
    rdfs:label "Sustrato Energético Fundamental"@es .

qm:GeneralAwareness
    rdfs:comment "Representa la disponibilidad bruta de la conciencia general o la capacidad total para el procesamiento consciente en un momento dado, reflejando la receptividad general de la mente a cualquier información entrante."@es ,
                 "La disponibilidad bruta de la conciencia general o la capacidad total para el procesamiento consciente en un momento dado."@es ;
    rdfs:label "Conciencia General (A)"@es .

qm:GeometricDimensionsOfAwareness
    rdfs:comment "El reconocimiento de las cualidades espaciales y relacionales de los fenómenos psicológicos, como sus ubicaciones, límites, densidades y orientaciones dentro del campo de la conciencia."@es ;
    rdfs:label "Dimensiones Geométricas de la Conciencia"@es .

qm:GoalAbandonment
    rdfs:comment "La disipación del enfoque y el esfuerzo sostenidos debido a la incapacidad de estabilizar consistentemente la intención subyacente para un objetivo."@es ;
    rdfs:label "Abandono de Metas"@es .

qm:GoalsCategory
    rdfs:comment "Resultados u objetivos deseados de la aplicación de los principios y prácticas de Mindfulness Cuántico."@es ;
    rdfs:label "Metas"@es .

qm:GroundingFunction
    rdfs:comment "Un ancla psicológica que evita que los individuos se pierdan en la especulación abstracta y asegura un compromiso sostenido con la realidad."@es ;
    rdfs:label "Función de Anclaje"@es .

qm:HistoricalImprint
    rdfs:label "Impronta Histórica / Impronta de Trauma"@es .

qm:HumanCapacitiesCategory
    rdfs:comment "Habilidades o potenciales inherentes de la conciencia humana relevantes para el marco."@es ;
    rdfs:label "Capacidades Humanas"@es .

qm:HumorAsCognitiveTechnology
    rdfs:label "Humor como Tecnología Cognitiva"@es .

qm:Identity
    rdfs:comment "Un constructo dinámico formado por la suma y el patrón de percepciones, creencias y autoconceptos solidificados repetidamente a través del Colapso Psicodinámico a lo largo del tiempo."@es ;
    rdfs:label "Identidad"@es .

qm:IdentityTransformationProcess
    rdfs:label "Proceso de Transformación de la Identidad"@es .

qm:ImpactOfTheNow
    rdfs:comment "El componente de la Valoración Cognitiva que representa la calidad emocional percibida de la observación actual (Valencia(Ψ)), modulada por la reactividad de un individuo a nuevos eventos (wΨ)."@es ,
                 "El componente que representa la calidad emocional percibida de la observación actual (Valencia(Ψ)), modulada por la reactividad de un individuo a nuevos eventos (wΨ)."@es ;
    rdfs:label "Impacto del Ahora"@es .

qm:ImposterSyndrome
    rdfs:label "Síndrome del Impostor"@es .

qm:ImpulseReactivity
    rdfs:comment "Comportamiento impulsado por estímulos inmediatos o reacciones emocionales en lugar de intenciones consideradas, debido a una capacidad debilitada para la deliberación reflexiva."@es ;
    rdfs:label "Reactividad Impulsiva"@es .

qm:ImpulseTowardGenerativeSharing
    rdfs:comment "Un impulso inherente a dar, conectar y contribuir al bienestar de los demás, que surge de un reconocimiento de la interconexión."@es ;
    rdfs:label "Impulso hacia el Compartir Generativo"@es .

qm:IncompleteProcessTension
    rdfs:label "Tensión por Proceso Incompleto"@es .

qm:InertiaOfThePast
    rdfs:comment "El componente de la Valoración Cognitiva que representa el estado de ánimo general persistente del momento anterior (ValenciaProm(S_t-1)), modulado por la persistencia del estado de ánimo de un individuo (wS)."@es ,
                 "El componente que representa el estado de ánimo general persistente del momento anterior (ValenciaProm(S_t-1)), modulado por la persistencia del estado de ánimo de un individuo (wS)."@es ;
    rdfs:label "Inercia del Pasado"@es .

qm:InferentialEpistemology
    rdfs:comment "Un enfoque para comprender fenómenos a través de sus efectos, patrones de manifestación y resistencia sistemática a la observación directa."@es ;
    rdfs:label "Epistemología Inferencial"@es .

qm:InfluentialFactor
    rdfs:comment "Un factor que puede influir en los patrones y resultados del colapso psicodinámico."@es ;
    rdfs:label "Factores Influyentes"@es .

qm:InherentDisposition
    rdfs:comment "El componente de la Valoración Cognitiva que representa un sesgo cognitivo o afectivo de base arraigado en las características estables de la Modalidad Principal del individuo (M1), como una tendencia general hacia el optimismo o el pesimismo."@es ,
                 "El componente de la Valoración Cognitiva que representa un sesgo cognitivo o afectivo de base arraigado en las características estables de la Modalidad Principal del individuo (M1), como una tendencia general hacia el optimismo o el pesimismo. Es una parte fija de la estructura de la personalidad."@es ,
                 "El componente que representa un sesgo cognitivo o afectivo de base arraigado en las características estables de la Modalidad Principal del individuo (M1). Es una parte fija de la estructura de la personalidad."@es ;
    rdfs:label "Disposición Inherente (Sesgo_M1)"@es .

# --- Section 6 ---

qm:InheritedScript
    rdfs:comment "Un sistema integral de influencias externas, repertorios conductuales aprendidos y programación cultural generalizada que moldea fundamentalmente el marco perceptual de un individuo y sus acciones posteriores, operando a menudo por debajo de la conciencia y creando una 'falsa arquitectura nativa'."@es ;
    rdfs:label "Guion Heredado"@es .

qm:InheritedScripts
    rdfs:comment "Patrones mentales preexistentes, sesgos o narrativas que influyen en la percepción y la interpretación, a menudo formados a partir de experiencias pasadas o del condicionamiento social."@es ;
    rdfs:label "Guiones Heredados"@es .

qm:IntegratedTherapeuticApproaches
    rdfs:comment "Enfoques holísticos e integrales que combinan diversas estrategias de Mindfulness Cuántico y conocimientos de diversos campos para abordar el sistema completo de una persona en lugar de centrarse en síntomas o comportamientos aislados."@es ;
    rdfs:label "Enfoques Terapéuticos Integrados"@es .

qm:IntentionalCollapse
    rdfs:comment "Guía deliberada del proceso de colapso por parte del observador consciente, a menudo a través de la Dimensión Psico-Meditativa."@es ,
                 "La elección consciente de qué estado mental o emocional potencial se permite estabilizar y manifestar como realidad experimentada, al atender selectivamente a los estados deseados."@es ;
    rdfs:label "Colapso Intencional"@es ;
    skos:altLabel "Colapso de Estado Volitivo"@es ,
                  "Dirección de Colapso Intencional"@es .

qm:InterferencePattern
    rdfs:comment "Un patrón sofisticado de interacción entre dimensiones que puede ser constructivo o destructivo."@es ;
    rdfs:label "Patrón de Interferencia"@es .

qm:InterferencePatterns
    rdfs:comment "Patrones complejos que surgen de la interacción de las dimensiones psicodinámicas, análogos a la interferencia de ondas."@es ;
    rdfs:label "Patrones de Interferencia"@es .

qm:InternalCartography
    rdfs:comment "La práctica de crear mapas detallados y dinámicos del terreno psicológico interno identificando regiones distintas de experiencia, sus límites y sus interacciones."@es ;
    rdfs:label "Cartografía Interna"@es ;
    skos:definition "La práctica de mapear el propio paisaje psicológico interno para comprenderlo y navegarlo mejor."@es .

qm:InternalConflictResolution
    rdfs:comment "La exploración sistemática de necesidades o deseos en conflicto para desarrollar enfoques creativos para la resolución sin forzar una elección."@es ;
    rdfs:label "Resolución de Conflictos Internos"@es .

qm:InternalMap
    rdfs:comment "Un marco para rastrear pensamientos, sentimientos e impulsos conductuales específicos hasta sus fuentes dimensionales subyacentes, lo que permite una intervención y navegación más precisas del mundo interior."@es ;
    rdfs:label "Mapa Interno del Funcionamiento Psicológico"@es .

qm:InterpersonalRelationshipExperience
    rdfs:comment "Conocimiento implícito y construcción de la realidad adquiridos a través de la interacción social y la dinámica emocional, como el contagio emocional."@es ;
    rdfs:label "Experiencia de Relación Interpersonal"@es .

qm:IntersubjectiveReality
    rdfs:label "Realidad Intersubjetiva"@es .

qm:IntersubjectiveResonance
    rdfs:comment "La capacidad de sentir con los demás, creando un espacio emocional compartido."@es ;
    rdfs:label "Resonancia Intersubjetiva"@es .

qm:IntuitiveCognition
    rdfs:label "Cognición Intuitiva"@es .

qm:Jealousy
    rdfs:comment "Una propiedad emergente de las interacciones dimensionales relacionadas con las necesidades de seguridad, la validación de la autoestima y el vínculo relacional."@es ;
    rdfs:label "Celos"@es .

qm:KnowledgeAcquisition
    rdfs:comment "Define cómo se forma la comprensión sobre los fenómenos sujetos a la Ausencia Empírica."@es ;
    rdfs:label "Adquisición de Conocimiento"@es .

qm:LiberationFromInheritedScripts
    rdfs:comment "Un camino específico enfocado en trascender el condicionamiento externo generalizado (Guiones Heredados) para fomentar una auténtica Auto-Originación Auténtica."@es ;
    rdfs:label "Liberación de Guiones Heredados"@es .

qm:LiberationProcess
    rdfs:comment "Una fase distintiva dentro del proceso para lograr la liberación de los guiones heredados."@es ,
                 "Una metodología sofisticada para identificar, comprender y trascender la influencia limitante de los Guiones Heredados."@es ;
    rdfs:label "Proceso de Liberación"@es .

qm:LimitationOfDirectObservation
    rdfs:comment "Barreras inherentes a la investigación empírica directa, que a menudo requieren enfoques basados en proxies."@es ;
    rdfs:label "Limitación de la Observación Directa"@es .

qm:MainStrategiesCategory
    rdfs:comment "Enfoques terapéuticos primarios empleados dentro del marco."@es ;
    rdfs:label "Estrategias Principales"@es .

qm:ManagementOfCognitiveStrain
    rdfs:comment "Estrategias para abordar la crisis contemporánea de sobrecarga cognitiva, fatiga y disfunción mediante el cultivo de la agencia cognitiva y la preservación del bienestar mental en entornos ricos en información."@es ;
    rdfs:label "Manejo de la Tensión y Disfunción Cognitiva"@es .

qm:ManipulationOfConstructedReality
    rdfs:label "Manipulación de la Realidad Construida"@es .

qm:MentalFilesystemOrganization
    rdfs:label "Organización del Sistema de Archivos Mentales"@es .

qm:MentalPhysicalInterface
    rdfs:comment "Una función que facilita el flujo bidireccional y la encarnación de estados psicológicos y conciencia somática."@es ;
    rdfs:label "Interfaz Mente-Cuerpo"@es .

qm:MentalQuanta
    rdfs:comment "Unidades fundamentales de posibilidad cognitiva o experiencial que componen el estado de Superposición Cognitiva."@es ;
    rdfs:label "Cuantos Mentales"@es .

qm:MentalState
    rdfs:comment "Abarca pensamientos, emociones, recuerdos y potenciales experienciales, que inicialmente existen como campos fluidos y probabilísticos."@es ;
    rdfs:label "Estado Mental"@es .

qm:MindControlsBrainPrinciple
    rdfs:comment "El principio de que el cerebro se interpreta como un órgano mediador a través del cual el pensamiento se transduce en experiencia fenomenológica, en lugar de ser su progenitor."@es ;
    rdfs:label "Principio de la Mente Controla el Cerebro"@es .

qm:MindfulnessApproachesComparisonCategory
    rdfs:comment "Una sección para comparar y contrastar diferentes metodologías de mindfulness."@es ;
    rdfs:label "Comparación de Enfoques de Mindfulness"@es .

qm:MindfulnessBasedStressReduction
    rdfs:label "Reducción del Estrés Basada en Mindfulness (MBSR)"@es .

qm:MindfulnessGoal
    rdfs:label "Meta de Mindfulness"@es ,
               "X. Meta de Mindfulness"@es .

qm:MindfulnessIntervention
    rdfs:comment "Una práctica intencional que interactúa con el mecanismo de Valoración Cognitiva para dar forma al estado mental de uno."@es ;
    rdfs:label "Intervención de Mindfulness"@es .

qm:MultidimensionalScanning
    rdfs:comment "La práctica de rastrear simultáneamente varias corrientes no verbales (postura, microexpresiones, respiración) para obtener una visión de los estados internos."@es ;
    rdfs:label "Escaneo Multidimensional"@es .

qm:NarrativeManagement
    rdfs:label "Gestión de Narrativas"@es .

qm:NaturalDevelopment
    rdfs:comment "El despliegue auténtico y auto-originado del potencial de un individuo."@es ;
    rdfs:label "Desarrollo Natural"@es .

qm:NonLocalCognition
    rdfs:comment "Capacidades atencionales que trascienden las limitaciones espaciales y temporales ordinarias, permitiendo el acceso a información o conocimientos más allá de la entrada sensorial inmediata o los procesos lógicos."@es ;
    rdfs:label "Cognición No Local"@es .

qm:NonMaterialPhenomenon
    rdfs:label "Fenómeno No Material"@es .

qm:NonReactiveObservation
    rdfs:comment "La práctica de observar los fenómenos mentales sin juzgar, permitiéndoles surgir y pasar naturalmente sin intentar cambiarlos o analizarlos."@es ;
    rdfs:label "Observación No Reactiva"@es .

qm:NonlocalGoalState
    rdfs:comment "Un resultado deseado que, aunque no está presente de inmediato, ejerce una influencia orientadora continua sobre el pensamiento y la acción actuales, permitiendo la resistencia a las distracciones."@es ;
    rdfs:label "Estado Meta No Local"@es .

qm:ObjectiveConstraints
    rdfs:comment "Limitaciones inherentes impuestas por las leyes físicas, los requisitos biológicos y las circunstancias materiales que la percepción consciente no puede alterar. Representan los 'huesos de la realidad'."@es ;
    rdfs:label "Restricciones Objetivas"@es .

qm:ObservableEffect
    rdfs:comment "Un patrón discernible o influencia sistemática que confirma la existencia de un fenómeno empíricamente ausente."@es ;
    rdfs:label "Efecto Observable"@es .

qm:Observation
    rdfs:comment "Un factor contribuyente que forma sinérgicamente una Observación compleja (Ψ)."@es ,
                 "El 'disparador central' pivotal o 'Medición Cognitiva' inicial que instiga el proceso psicodinámico. Es una percepción compleja formada por la interacción sinérgica y multiplicativa de sus cuatro componentes. Marca el primer paso activo en la dinámica del 'Observador-Participante'."@es ,
                 "El 'disparador central' pivotal o 'Medición Cognitiva' inicial que instiga el proceso psicodinámico. Es una percepción compleja formada por la interacción sinérgica y multiplicativa de sus cuatro componentes: huella perceptual bruta (α), significado percibido (β), conciencia general (A) y enfoque dirigido (f). Esto marca el primer paso activo en la dinámica del 'Observador-Participante'."@es ,
                 "El disparador central pivotal o 'Medición Cognitiva' inicial que instiga el proceso psicodinámico. Es una percepción compleja formada por la interacción dinámica de datos sensoriales brutos/estímulos internos (α), significado asignado (β), conciencia general (A) y enfoque dirigido (f)."@es ,
                 "El disparador central pivotal o Medición Cognitiva inicial que instiga el proceso psicodinámico."@es ;
    rdfs:label "Observación (Ψ)"@es ,
               "Componente de Observación"@es .

qm:ObservationComponentsCategory
    rdfs:comment "Contenedor conceptual para las partes constituyentes de una Observación."@es ;
    rdfs:label "Componentes (Ψ = α(β + 1)(A + f))"@es .

qm:ObservationInfluence
    rdfs:comment "Representa el impacto directo y específico de la Observación actual (Ψ) en sí misma sobre una dimensión (IΨj = wΨj ⋅ Relevancia(Ψ, Pdj))."@es ,
                 "Representa el impacto directo y específico de la Observación actual (Ψ) en sí misma sobre una dimensión (IΨj = wΨj ⋅ Relevancia(Ψ, Pdj)). Aborda: '¿Cuánto impacta directamente el contenido específico de lo que estoy observando en este sentimiento?'."@es ,
                 "Representa el impacto directo y específico de la Observación actual (Ψ) en sí misma sobre una dimensión, basado en la relevancia de la observación para la naturaleza de la dimensión."@es ;
    rdfs:label "Influencia de la Observación (IΨj)"@es .

qm:ObserverEffectParadox
    rdfs:label "Paradoja del Efecto Observador"@es .

qm:ObserverFunction
    rdfs:comment "Una capacidad específica de la conciencia dentro del Observador Cuántico que, cuando se activa, participa activamente en la resolución de potenciales superpuestos al estabilizar el contenido cognitivo."@es ;
    rdfs:label "Función del Observador"@es .

qm:ObserverParticipantDynamic
    rdfs:label "Dinámica Observador-Participante"@es .

qm:ObserverParticipantRole
    rdfs:comment "El reconocimiento de que el acto de observación modifica inherentemente el estado mental observado, posicionando al observador como un co-creador activo de la experiencia."@es ;
    rdfs:label "Rol Observador-Participante"@es .

qm:ObserverParticipantTheory
    rdfs:comment "Un marco integral que reconceptualiza el papel de la conciencia en la experiencia humana, demostrando que el compromiso consciente con los fenómenos mentales constituye un proceso activo y participativo que inherentemente moldea y co-crea el tejido de la realidad experimentada."@es ;
    rdfs:label "Teoría del Observador-Participante"@es .

qm:OntologicalFieldTheory
    rdfs:comment "Postula que los marcos mentales individuales —que abarcan creencias, suposiciones y estructuras cognitivas inconscientes— contribuyen activamente a dar forma a la realidad percibida en lugar de simplemente filtrarla o interpretarla."@es ;
    rdfs:label "Teoría del Campo Ontológico"@es .

qm:OntologicalFirewall
    rdfs:comment "Características estructurales fundamentales de la realidad que crean límites categóricos entre diferentes modos de ser y conocer, particularmente entre la conciencia y su fuente."@es ;
    rdfs:label "Cortafuegos Ontológico"@es .

qm:OntologicalMisalignment
    rdfs:comment "Una discrepancia fundamental entre la verdadera naturaleza de un individuo y su experiencia vivida, resultante de operar según guiones heredados."@es ;
    rdfs:label "Desalineación Ontológica"@es .

# --- Section 7 ---

qm:OntologicalRestructuring
    rdfs:label "Reestructuración Ontológica"@es .

qm:OntologicalStarvation
    rdfs:comment "Una forma profunda de tensión cognitiva donde ocurre una pérdida de compromiso y volición auténticos, relacionada con la Fatiga de Resolución."@es ;
    rdfs:label "Inanición Ontológica"@es .

qm:OntologicalStatecraft
    rdfs:label "Estadismo Ontológico"@es .

qm:OtherKeyConcepts
    rdfs:comment "Una categoría general para conceptos importantes no cubiertos explícitamente en otras secciones principales."@es ;
    rdfs:label "Otros Conceptos Clave"@es .

qm:OverallMentalState
    rdfs:comment "La experiencia consciente final, compuesta y holística que emerge de la configuración específica y las intensidades actualizadas de las diez Dimensiones Psicodinámicas."@es ,
                 "La experiencia consciente final, compuesta y holística que emerge de la configuración específica y las intensidades actualizadas de las diez Dimensiones Psicodinámicas. Es una mezcla compleja donde la naturaleza cualitativa de cada dimensión está ponderada por su Intensidad Final calculada."@es ;
    rdfs:label "Estado Mental General (S)"@es .

qm:ParadoxTolerance
    rdfs:label "Tolerancia a la Paradoja"@es .

qm:PassiveMastery
    rdfs:comment "El logro de la ecuanimidad y la presencia en el momento presente, en gran medida independiente del contenido específico de la experiencia."@es ;
    rdfs:label "Maestría Pasiva"@es .

qm:PassiveRecipientView
    rdfs:comment "La visión de que la conciencia recibe pasivamente una representación interna de una realidad objetiva preexistente."@es ;
    rdfs:label "Visión de Receptor Pasivo"@es .

qm:PatternedPresence
    rdfs:comment "Un modo sofisticado de conciencia que va más allá de simplemente observar 'qué' se experimenta para aprehender también el 'cómo', 'de dónde' y 'según qué patrones' de la emergencia experiencial."@es ,
                 "Un estado de estar presente que es simultáneamente receptivo y estructurado, implicando la organización deliberada de la atención. Es un mecanismo central utilizado por la Conciencia Vectorizada para permitir una navegación precisa del terreno psicológico interno."@es ;
    rdfs:label "Presencia Pautada"@es .

qm:PerceivedLimitation
    rdfs:comment "Bloqueos mentales, marcos conceptuales restrictivos u otros límites percibidos que pueden ser disueltos por la Dimensión Psico-Volitiva."@es ;
    rdfs:label "Limitación Percibida"@es .

qm:PerceivedMeaning
    rdfs:comment "Representa la capa inicial de significado, significancia o intención que la mente asigna rápida y a menudo automáticamente a los datos brutos (α). Es una 'interpretación de primer paso'. El factor '+ 1' en su uso formal implica un nivel base de 'ser-idad' al componente de significado."@es ,
                 "La capa inicial de significado o 'interpretación de primer paso' que la mente asigna rápidamente a los datos brutos (α). El factor '+1' implica un 'ser-idad' base al componente de significado."@es ;
    rdfs:label "Significado/Intención Percibida (β)"@es .

qm:PerceivedProblem
    rdfs:comment "Fenómenos experimentados como 'problemas' que no son entidades fijas y objetivas, sino que están significativamente moldeados por marcos interpretativos y hábitos perceptuales, y son susceptibles de reconfiguración consciente."@es ;
    rdfs:label "Problema Percibido"@es .

qm:Perception
    rdfs:comment "Un proceso dinámico y activo a través del cual los estados cognitivos ambiguos y multipotenciales (superposición) se resuelven en experiencias conscientes singulares y definitivas, impulsado en gran medida por la atención consciente y los marcos interpretativos. Es una fuerza generativa en la construcción de la realidad experimentada."@es ,
                 "El proceso de interpretar y comprender la información sensorial y los estímulos internos, lo que conduce a una experiencia subjetiva de la realidad."@es ;
    rdfs:label "Percepción"@es .

qm:PerceptualAgility
    rdfs:comment "La modificación intencional de las modalidades perceptivas y la capacidad avanzada para navegar sin esfuerzo y sostener múltiples marcos perceptuales."@es ;
    rdfs:label "Agilidad Perceptual"@es .

qm:PerceptualConstructionTheory
    rdfs:comment "Un marco en el que la conciencia opera como un campo dinámico que construye y reconstruye el paisaje de la realidad mental."@es ;
    rdfs:label "Teoría de la Construcción Perceptual"@es .

qm:PerceptualContract
    rdfs:label "Contrato Perceptual"@es .

qm:PerceptualDistortion
    rdfs:comment "Una respuesta desadaptativa que surge de la Desalineación Dimensional o la Interferencia Sub-dinámica, como una dimensión de detección de amenazas hiperactiva que enmarca situaciones neutrales como peligrosas."@es ;
    rdfs:label "Distorsión Perceptual"@es .

qm:PerceptualFraming
    rdfs:label "Encuadre Perceptual"@es .

qm:PerceptualFreedom
    rdfs:comment "La capacidad de elegir conscientemente cómo se actualizan las experiencias potenciales, permitiendo un compromiso adaptativo con los desafíos y una evolución consciente. Es el objetivo final del Mindfulness Cuántico."@es ;
    rdfs:label "Libertad Perceptual"@es .

qm:PerceptualGoal
    rdfs:comment "Un estado o capacidad deseada que es el objetivo del trabajo perceptual dentro del marco de Mindfulness Cuántico."@es ;
    rdfs:label "Meta Perceptual"@es .

qm:PerceptualReframing
    rdfs:label "Reencuadre Perceptual"@es .

qm:PerceptualShapingTechnique
    rdfs:comment "Una práctica o método deliberado utilizado para influir conscientemente en los procesos perceptuales."@es ;
    rdfs:label "Técnica de Moldeamiento Perceptual"@es .

qm:PerceptualSophistication
    rdfs:comment "La capacidad de discernir diferencias sutiles entre las respuestas condicionadas externamente y la conciencia generada internamente."@es ;
    rdfs:label "Sofisticación Perceptual"@es .

qm:PerceptualSuperposition
    rdfs:label "Superposición Perceptual"@es .

qm:PersonalTendency
    rdfs:comment "Un factor de ponderación que cuantifica las diferencias individuales inherentes en la reactividad, la inercia emocional u otros rasgos disposicionales que modulan la Valoración Cognitiva."@es ;
    rdfs:label "Tendencia Personal (w)"@es .

qm:PersonalTendency_ObservationReactivity
    rdfs:label "Tendencia Personal (Reactividad a la Observación - wΨj)"@es .

qm:PersonalTendency_TraitExpression
    rdfs:label "Tendencia Personal (Expresión del Rasgo - wTj)"@es .

qm:PersonalityOrganization
    rdfs:comment "La base estructural de la personalidad, formada por la interacción dinámica de las Dimensiones Psicodinámicas."@es ;
    rdfs:label "Organización de la Personalidad"@es .

qm:Phenomenon
    rdfs:comment "Una clase general para entidades o procesos que pueden exhibir la característica de Ausencia Empírica."@es ;
    rdfs:label "Fenómeno"@es .

qm:PlausibilityEngineering
    rdfs:label "Ingeniería de Plausibilidad"@es .

qm:PracticalLimitationsOfQMApplication
    rdfs:comment "Restricciones o dificultades en la implementación de las prácticas de Mindfulness Cuántico en escenarios del mundo real."@es ,
                 "Restricciones y consideraciones del mundo real que limitan la aplicación directa, el alcance o la efectividad de los principios y técnicas de Mindfulness Cuántico."@es ;
    rdfs:label "Limitaciones Prácticas de la Aplicación de QM"@es .

qm:PracticalWisdom
    rdfs:comment "La capacidad de discernir la acción apropiada en circunstancias específicas basándose en una comprensión profunda, desarrollada a través de la indagación contemplativa."@es ;
    rdfs:label "Sabiduría Práctica"@es .

qm:PracticesCategory
    rdfs:comment "Métodos o ejercicios específicos que se realizan para aplicar los principios de Mindfulness Cuántico."@es ;
    rdfs:label "Prácticas"@es .

qm:PrimeModality
    rdfs:comment "La tríada cognitivo-ejecutiva (Pd1-Pd3) que gobierna la percepción, la intención y la interpretación. Es la estructura cognitiva suprema, de orden superior, que sirve como matriz subyacente para toda la conciencia subjetiva y proporciona el 'andamiaje de la conciencia misma'."@es ,
                 "La tríada cognitivo-ejecutiva (Pd1-Pd3) que gobierna la capacidad de la mente para la percepción, la intención y la interpretación, y es la fuente de la 'conciencia volitiva'. Contribuye con un sesgo base al proceso de Valoración Cognitiva."@es ,
                 "La tríada cognitivo-ejecutiva (Pd1-Pd3) que gobierna la capacidad de la mente para la percepción, la intención y la interpretación. Es la estructura cognitiva suprema, de orden superior y fundamental, que sirve como la matriz subyacente para toda la conciencia subjetiva y proporciona el 'andamiaje de la conciencia misma'."@es ,
                 "La estructura cognitiva suprema, de orden superior y fundamental dentro del marco de Mindfulness Cuántico."@es ;
    rdfs:label "Modalidad Principal (M1)"@es .

qm:PrimeModalityCategory
    rdfs:comment "Contenedor conceptual para las dimensiones de la Modalidad Principal, que gobiernan la percepción, la intención y la interpretación."@es ;
    rdfs:label "Modalidad Principal (M1) - Tríada Cognitivo-Ejecutiva"@es .

qm:PrincipleOfRestraint
    rdfs:label "Principio de Contención"@es .

qm:PrincipleOfSymmetry
    rdfs:label "Principio de Simetría"@es .

qm:PrincipleReceptivity
    rdfs:comment "La capacidad de reconocer y alinearse con las ideas rectoras que emergen de niveles más profundos de la conciencia."@es ;
    rdfs:label "Receptividad a los Principios"@es .

qm:PriorStateInfluence
    rdfs:comment "Tiene en cuenta la inercia o el impulso de cada dimensión específica desde el momento inmediatamente anterior."@es ,
                 "Captura la 'inercia' o el 'impulso' de una dimensión psicodinámica específica del estado mental inmediatamente anterior (ISj = wSj ⋅ xj,t-1)."@es ,
                 "Captura la 'inercia' o el 'impulso' de una dimensión psicodinámica específica del estado mental inmediatamente anterior (ISj = wSj ⋅ xj,t-1). Aborda: '¿Cuánto contribuye mi experiencia previa de este sentimiento específico a su potencial ahora?'."@es ;
    rdfs:label "Influencia del Estado Anterior (ISj)"@es .

qm:ProactiveSelfRegulation
    rdfs:comment "Usar las firmas somáticas como un sistema de alerta temprana para gestionar los estados internos emergentes antes de que se vuelvan abrumadores, permitiendo una intervención previa a la resolución."@es ;
    rdfs:label "Autorregulación Proactiva"@es ;
    skos:definition "La práctica de anticipar y gestionar los propios estados internos y comportamientos de antemano para alcanzar metas."@es .

qm:ProbabilisticField
    rdfs:comment "Un campo dinámico de múltiples posibilidades simultáneas en el que los estados mentales existen inicialmente antes de la atención enfocada y el procesamiento cognitivo."@es ;
    rdfs:label "Campo Probabilístico"@es .

qm:ProbabilisticMentalState
    rdfs:comment "El estado donde múltiples estados cognitivos, emocionales y perceptuales potenciales coexisten simultáneamente como posibilidades antes de que la atención consciente los enfoque en una experiencia definida."@es ;
    rdfs:label "Estado Mental Probabilístico"@es ;
    skos:altLabel "Función de Onda Mental"@es .

qm:ProjectedAnxietySystem
    rdfs:label "Sistema de Ansiedad Proyectada"@es .

qm:ProtectivePrinciple
    rdfs:comment "Un principio psicológico primordial encarnado por la Dimensión Psico-Protectora."@es ;
    rdfs:label "Principio Protector"@es .

qm:ProtoImpulse
    rdfs:comment "Impulsos internos sutiles que surgen del procesamiento inconsciente, la visión intuitiva, la inspiración creativa o la sensibilidad ética."@es ;
    rdfs:label "Proto-Impulso"@es .

qm:Proxy
    rdfs:comment "Cualquier representación indirecta, modelo, inferencia o descripción que proporciona acceso a fenómenos que no pueden ser captados directamente a través de medios empíricos convencionales."@es ;
    rdfs:label "Proxy"@es .

qm:PsychicArchitecture
    rdfs:comment "La estructura conceptual de la psique dentro del marco de Mindfulness Cuántico."@es ;
    rdfs:label "Arquitectura Psíquica"@es .

qm:PsychoAestheticDimension
    rdfs:comment "Un mecanismo cognitivo de equilibrio crucial que armoniza fuerzas aparentemente opuestas dentro de la psique, estableciendo una integración armoniosa entre fuerzas psicológicas opuestas. Funciona como un centro de integración, especializado en la síntesis armoniosa entre energías opuestas."@es ,
                 "Pd6: La dimensión del atractivo sensorial, la belleza y la atracción."@es ,
                 "La dimensión del atractivo sensorial, la belleza y la atracción. Funciona como un mecanismo cognitivo de equilibrio crucial que armoniza las fuerzas opuestas dentro de la psique, como la empatía y la protección, promoviendo así la integración y la madurez emocional."@es ,
                 "La sexta dimensión, que sirve como un modulador emocional, buscando un punto medio armonioso entre tendencias contradictorias como el cuidado y el límite."@es ,
                 "La fuerza integradora central de la psique, que equilibra las experiencias internas con la realidad externa, fomentando la armonía y la autenticidad del ser."@es ;
    rdfs:label "Dimensión Psico-Estética (Pd6)"@es .

# --- Section 8 ---

qm:PsychoConceptiveDimension
    rdfs:comment "Una función cognitiva dinámica y altamente intuitiva que facilita la visión espontánea y el reconocimiento de patrones. Representa el acto creativo inicial de la psique, donde el potencial abstracto y no formado comienza a unirse en conceptos nacientes, funcionando como la fuente subconsciente de sabiduría e intelecto."@es ,
                 "Una función dinámica e intuitiva para la visión espontánea, el reconocimiento de patrones y la aprehensión de relaciones complejas más allá del pensamiento lineal. Representa el acto creativo inicial de la psique donde el potencial abstracto se une en conceptos nacientes."@es ,
                 "Pd2: Pertenece a la intuición, la ideación y la 'chispa' de la nueva visión y la generación de significado. Contribuye a generar nuevas ideas durante el reencuadre activo."@es ,
                 "El umbral primordial donde el potencial mental indiferenciado se transforma en formas ideacionales reconocibles. Facilita la visión espontánea, el reconocimiento holístico de patrones y la síntesis no lineal, sirviendo como la fuente subconsciente de sabiduría e intelecto."@es ,
                 "El segundo estrato de la Modalidad Primaria, donde el potencial abstracto se une en ideas intuitivas y prelingüísticas."@es ,
                 "La capacidad para la visión rápida y pre-verbal, la ideación generativa y la formación inicial de conceptos brutos."@es ;
    rdfs:label "Dimensión Psico-Conceptiva (Pd2)"@es ;
    skos:altLabel "Procesamiento Psico-Conceptivo"@es .

qm:PsychoEmpathicDimension
    rdfs:comment "Un estado cognitivo expansivo que promueve la asociación creativa, la flexibilidad cognitiva y la apertura; la base para la empatía y la compasión. Es la fuente fundamental del amor y la compasión, impulsando la resonancia intersubjetiva."@es ,
                 "Pd4: La dimensión del afecto, el amor y la compasión."@es ,
                 "La dimensión del afecto, el amor y la compasión. Encarna la capacidad de conexión auténtica y resonancia emocional con los demás y sirve como base para la conexión humana."@es ,
                 "La cuarta dimensión y elemento inaugural de la Modalidad Secundaria, que representa el origen del amor, la compasión y la empatía, y proporciona inteligencia emocional."@es ,
                 "La dimensión de la conexión emocional expansiva, la capacidad de altruismo y el impulso compasivo para el crecimiento y la conexión con los demás."@es ;
    rdfs:label "Dimensión Psico-Empática (Pd4)"@es .

qm:PsychoFoundationalDimension
    rdfs:comment "Pd9: La dimensión de la familiaridad, los valores, la pertenencia y el anclaje moral."@es ,
                 "La dimensión de la familiaridad, los valores, la pertenencia y el anclaje moral. Es crucial para la consolidación del aprendizaje, la integración de la memoria y la traducción del conocimiento abstracto en inteligencia práctica y accionable, sirviendo como un vínculo crítico entre los reinos mental y físico."@es ,
                 "La función para la consolidación del aprendizaje, la integración de la memoria y la traducción del conocimiento abstracto en inteligencia práctica y accionable. Sirve como la base de la arquitectura emocional y el conducto principal para que los estados internos logren una expresión concreta."@es ,
                 "La novena dimensión, que integra específicamente el aprendizaje y ancla la conciencia en una inteligencia práctica y accionable."@es ,
                 "Las capas más profundas del subconsciente, los impulsos primarios, la libido energética y la base energética fundamental que estructura la personalidad."@es ;
    rdfs:label "Dimensión Psico-Fundacional (Pd9)"@es .

qm:PsychoFoundationalEncoding
    rdfs:comment "Una función cognitiva fundamental que consolida la memoria, codifica el aprendizaje experiencial y traduce el conocimiento abstracto en inteligencia práctica y accionable."@es ;
    rdfs:label "Codificación Psico-Fundacional"@es .

qm:PsychoMeditativeCollapse
    rdfs:comment "Una forma específica de Colapso Cognitivo en la que el potencial mental se transforma en Experiencia Actualizada a través del compromiso contemplativo, mediado por la Función del Observador."@es .

qm:PsychoMeditativeDimension
    rdfs:comment "Pd3: Abarca la cognición, la reflexión y el procesamiento interpretativo, facilitando el aprendizaje y la comprensión integradora. Ayuda a analizar situaciones desde nuevas perspectivas durante el reencuadre activo."@es ,
                 "Pd3: Abarca la cognición, la reflexión y el procesamiento interpretativo, facilitando el aprendizaje y la comprensión integradora. Ayuda a analizar situaciones desde nuevas perspectivas durante el reencuadre."@es ,
                 "La función cognitiva estructurada y analítica responsable de la categorización, la organización lógica y la estabilización conceptual. Transforma las intuiciones de Pd2 en una comprensión definida y coherente y es el locus principal del 'colapso cognitivo' y la intervención consciente."@es ,
                 "La función cognitiva estructurada y analítica responsable de la categorización, la organización lógica y la estabilización conceptual. Transforma las intuiciones en una comprensión coherente e integra el intelecto y el afecto. Es el locus explícito del colapso psico-meditativo."@es ,
                 "La función cognitiva estructurada y analítica responsable de la categorización, la organización lógica y la estabilización conceptual. Esta dimensión transforma las intuiciones en una comprensión coherente y es el dominio principal para la intervención consciente en el proceso de colapso psicodinámico."@es ,
                 "El tercer estrato de la Modalidad Principal, que sirve como el asiento principal de la razón, la estructuración y la comprensión analítica."@es ,
                 "La facultad para el pensamiento sistemático, la construcción lógica y la organización analítica de ideas en una comprensión coherente."@es ;
    rdfs:label "Dimensión Psico-Meditativa (Pd3)"@es .

qm:PsychoMotivationalDimension
    rdfs:comment "Energía cognitiva de proyección hacia el futuro responsable de sostener la motivación, fomentar la resistencia cognitiva y permitir el reconocimiento de patrones a largo plazo para alcanzar metas en períodos de tiempo extendidos."@es ,
                 "Pd7: La dimensión del propósito, el impulso y la ambición a largo plazo."@es ,
                 "La dimensión del propósito, el impulso y la ambición a largo plazo. Representa la energía cognitiva de proyección hacia el futuro para sostener la motivación, la resistencia cognitiva y lograr metas a largo plazo, traduciendo los valores internos en una acción externa consistente."@es ,
                 "La fuente de los impulsos instintivos, la fuerza de voluntad persistente y la fuerza energética que impulsa la acción y la perseverancia."@es ;
    rdfs:label "Dimensión Psico-Motivacional (Pd7)"@es .

qm:PsychoMotivationalMomentum
    rdfs:comment "Una forma especializada de energía cognitiva de proyección hacia el futuro responsable de sostener la motivación y la resistencia a través de los desafíos."@es ;
    rdfs:label "Impulso Psico-Motivacional"@es .

qm:PsychoProtectiveDimension
    rdfs:comment "Mecanismos cognitivos que regulan la toma de decisiones y mantienen la coherencia psicológica a través de la inhibición, la formación de límites y el enfoque selectivo. Encarna los principios de medida, límite y contención."@es ,
                 "Pd5: La dimensión del poder, el miedo y los límites."@es ,
                 "La dimensión del poder, el miedo y los límites. Regula la toma de decisiones y mantiene la coherencia psicológica a través de la inhibición y el enfoque selectivo, encarnando los principios de medida, límite y contención."@es ,
                 "La quinta dimensión, que encarna cualidades de discernimiento, límites apropiados, límites saludables y juicio protector."@es ,
                 "La capacidad para establecer y mantener límites, ejercer la autodisciplina y contener la energía o los impulsos psíquicos."@es ;
    rdfs:label "Dimensión Psico-Protectora (Pd5)"@es .

qm:PsychoReceptiveDimension
    rdfs:comment "Un sofisticado mecanismo de autocorrección cognitiva para refinar la percepción, reevaluar creencias y mejorar la precisión a través de la integración de retroalimentación. Funciona como un mecanismo esencial de autocorrección cognitiva, refinando continuamente la percepción e incitando a la reevaluación de creencias establecidas."@es ,
                 "Pd8: La dimensión de la realización, la claridad perceptual y la receptividad."@es ,
                 "La dimensión de la realización, la claridad perceptual y la receptividad. Funciona como un mecanismo de autocorrección cognitiva para refinar la percepción y reevaluar creencias a través de la integración de retroalimentación, uniendo los principios abstractos con la vida práctica."@es ,
                 "La octava dimensión, que refina la percepción, reevalúa creencias y mejora la precisión a través de la integración de retroalimentación."@es ,
                 "La capacidad de asimilación intelectual, comunicación estructurada y la expresión o recepción formal del pensamiento."@es ;
    rdfs:label "Dimensión Psico-Receptiva (Pd8)"@es .

qm:PsychoTranspersonalDimension
    rdfs:comment "Pd10: Esta dimensión pasiva actúa como un conducto para la influencia colectiva y la resonancia externa, permitiendo que el estado final de M2 se exprese a menos que sea negado por la dimensión Psico-Volitiva (Pd1)."@es ,
                 "Responsable de externalizar la conciencia internalizada en un comportamiento accionable y observable dentro del mundo físico. Representa la manifestación última del desarrollo de la conciencia dentro de la realidad temporal."@es ,
                 "La dimensión que representa la manifestación última del desarrollo de la conciencia en la realidad temporal. Es un conducto pasivo que recibe, integra y expresa las energías sintetizadas de las nueve dimensiones precedentes, sirviendo como la interfaz entre los sistemas psicodinámicos internos y la realidad externa."@es ,
                 "La décima dimensión, que representa la manifestación última del desarrollo de la conciencia dentro de la realidad temporal al externalizar la conciencia en un comportamiento observable."@es ,
                 "La interfaz con la realidad manifestada, la acción concreta y la experiencia del mundo físico."@es ;
    rdfs:label "Dimensión Psico-Transpersonal (Pd10)"@es .

qm:PsychoVolitionalDimension
    rdfs:comment "Encarna la conciencia unificada y la voluntad primigenia; sirve como el principio organizador, disuelve las limitaciones y gobierna la formación de la intención. Es la génesis absoluta de la actividad cognitiva y un estado de potencialidad pura, precognitivo y preemocional. Posee una propiedad 'aniquiladora' para disolver las limitaciones percibidas."@es ,
                 "Pd1: Encarna la voluntad, el impulso y la toma de decisiones, representando la acción intencional. Está específicamente involucrado en el proceso de reencuadre activo al cambiar la atención."@es ,
                 "La génesis absoluta de la actividad cognitiva y un estado de potencialidad pura. Encarna la conciencia pura y la voluntad primigenia, sirviendo como el principio organizador y la fuente última de todo pensamiento creativo. Posee propiedades 'aniquiladoras' para disolver las limitaciones percibidas y se considera el punto más alto en el 'mapa vertical de la conciencia'."@es ,
                 "El ápice de la arquitectura de la conciencia, que encarna la conciencia unificada y la voluntad primigenia. Es la fuente última de potencialidad pura, deseo, autodeterminación y pensamiento creativo, sirviendo como el principio organizador primario y la fuerza iniciadora de todos los fenómenos mentales posteriores. Posee una 'propiedad aniquiladora', disolviendo las limitaciones percibidas."@es ,
                 "El primer y más fundamental estrato de la Modalidad Principal, sirviendo como el origen absoluto de la voluntad y el potencial."@es ,
                 "Representa el origen fundamental de la energía psíquica, la intencionalidad primigenia y la fuente de la conciencia."@es ;
    rdfs:label "Dimensión Psico-Volitiva (Pd1)"@es .

qm:PsychoVolitionalField
    rdfs:label "Campo Psico-Volitivo"@es .

qm:PsychodynamicBalanceRestoration
    rdfs:comment "Metodologías enfocadas en lograr la Alineación Armónica entre las diez Dimensiones Psicodinámicas, basadas en la comprensión de que el malestar psicológico a menudo proviene de un desequilibrio dentro de esta red dimensional dinámica."@es ;
    rdfs:label "Restauración del Equilibrio Psicodinámico"@es .

qm:PsychodynamicCollapse
    rdfs:comment "La transición fundamental donde los fenómenos mentales preconscientes probabilísticos y multiestado (superposición cognitiva) se resuelven en resultados singulares, definidos y conscientemente experimentados, formando la realidad subjetiva. La atención consciente actúa como el catalizador principal."@es ,
                 "La transición fundamental mediante la cual un sistema mental o cognitivo pasa de un estado de indeterminación o superposición a un resultado singular, definido y conscientemente experimentado, desencadenado por la atención sostenida."@es ;
    skos:altLabel "Solidificación Cognitiva"@es ,
                  "Colapso Presente de la Percepción"@es ,
                  "Colapso Cognitivo"@es ,
                  "Colapso de la Función de Onda"@es .

qm:PsychodynamicDimension
    rdfs:comment "Los 'cuantos' elementales o bloques de construcción irreductibles de la vida mental y emocional. Se conceptualizan como sustratos energéticos fundamentales de los cuales emergen cogniciones, emociones y motivaciones, formando la sustancia de la conciencia y el fundamento estructural de la organización de la personalidad."@es ,
                 "Los 'cuantos' fundamentales, discretos y elementales de la vida mental y emocional. Estas son las unidades centrales irreductibles a partir de las cuales se construye todo el espectro de la experiencia subjetiva. Este es un modelo formal y conceptual, no un modelo de computación cerebral."@es ,
                 "Las unidades centrales irreductibles o 'cuantos' de la vida mental y emocional."@es ,
                 "Una categoría conceptual que representa diversos aspectos de la psique basados en la teoría psicodinámica."@es ;
    rdfs:label "Dimensión Psicodinámica (Pdj)"@es ,
               "Categoría de Dimensión Psicodinámica"@es ;
    skos:altLabel "Cuantos Cognitivos"@es .

qm:PsychodynamicDimensionsCategory
    rdfs:comment "Contenedor conceptual para las dimensiones psicodinámicas, que sirven como los 'cuantos' elementales de la vida mental."@es ;
    rdfs:label "Dimensiones Psicodinámicas (QM_Quantum / Cuantos Cognitivos)"@es .

qm:PsychodynamicFriction
    rdfs:label "Fricción Psicodinámica"@es .

qm:PsychodynamicHarmonicAlignment
    rdfs:comment "Un estado de funcionamiento psicológico óptimo caracterizado por la interacción armoniosa y la operación unificada de todas las capacidades dimensionales."@es ;
    rdfs:label "Alineación Armónica Psicodinámica"@es .

qm:PsychodynamicNavigation
    rdfs:comment "El proceso de guiarse a uno mismo a través de estructuras psicológicas multidimensionales, reconociendo que la experiencia se desarrolla a través de dominios cognitivos, emocionales, somáticos y relacionales."@es ;
    rdfs:label "Navegación Psicodinámica"@es .

qm:PsychodynamicWaveCollapse
    rdfs:comment "La transición fundamental mediante la cual un sistema mental o cognitivo pasa de un estado de indeterminación, superposición o fluctuación a un resultado singular, definido y conscientemente experimentado. Es el proceso pivotal donde el campo probabilístico de la mente se resuelve en una experiencia específica y actualizada."@es ,
                 "El proceso por el cual los estados psicodinámicos potenciales se resuelven en una experiencia consciente definitiva, análogo al colapso de la función de onda cuántica."@es ;
    rdfs:label "Colapso de la Onda Psicodinámica"@es ;
    skos:altLabel "Solidificación Cognitiva"@es ,
                  "Colapso Cognitivo"@es ,
                  "Colapso Experiencial"@es ,
                  "Colapso Presente de la Percepción"@es ,
                  "Proceso de Colapso Cuántico"@es ,
                  "Colapso de la Función de Onda"@es .

qm:PsychologicalDisharmony
    rdfs:comment "Una categoría general para dificultades psicológicas, sufrimiento emocional e ineficiencias cognitivas, vistas como 'configuraciones desalineadas' o 'patrones de interferencia o desarmonía'."@es ;
    rdfs:label "Desarmonía Psicológica"@es ;
    skos:altLabel "Configuración Desalineada"@es .

qm:PsychologicalDysfunctionAndImbalance
    rdfs:comment "Problemas de salud mental o falta de equilibrio que pueden abordarse o presentar desafíos."@es ,
                 "Estados que surgen de patrones específicos, desequilibrios o configuraciones desalineadas de las Dimensiones Psicodinámicas, que conducen a malestar, ineficiencia o expresiones patológicas en la psique de un individuo."@es ;
    rdfs:label "Disfunción y Desequilibrio Psicológico"@es .

qm:PsychologicalEntanglement
    rdfs:label "Entrelazamiento Psicológico"@es ;
    skos:altLabel "Entrelazamiento Interpersonal"@es ,
                  "Entrelazamiento Cognitivo"@es .

qm:PsychologicalHeart
    rdfs:comment "Un rol que cumple funciones reguladoras cruciales que mantienen la coherencia psicológica y previenen la fragmentación sistémica."@es ;
    rdfs:label "Corazón Psicológico"@es .

qm:PsychologicalPhenomenon
    rdfs:comment "Una categoría general para las manifestaciones experienciales y conductuales que son moldeadas por las Dimensiones Psicodinámicas."@es ;
    rdfs:label "Fenómeno Psicológico"@es .

qm:PsychologicalState
    rdfs:comment "Patrones emergentes complejos (p. ej., ansiedad, alegría) entendidos no como entidades monolíticas, sino como colapsos de campo multidimensionales que involucran combinaciones e interacciones específicas de las Dimensiones Psicodinámicas subyacentes."@es ;
    rdfs:label "Estado Psicológico"@es .

qm:PsychologicalStructure
    rdfs:comment "El orden y equilibrio general dentro del mundo interno de un individuo."@es ;
    rdfs:label "Estructura Psicológica"@es .

qm:PsychologicalTransformationViaOntologicalReassignment
    rdfs:comment "Un enfoque sistemático y fundamental para reestructurar la relación experiencial de un individuo tanto con la identidad como con la realidad misma."@es ;
    rdfs:label "Transformación Psicológica Vía Reasignación Ontológica"@es .

qm:PsychosocialEmotiveTriad
    rdfs:comment "Una tríada de dimensiones (Pd4, Pd5, Pd6) dentro de la Modalidad Secundaria que gobierna los estados afectivos, la dinámica relacional y la inteligencia socioemocional. También conocida como el 'Reino del Sentimiento'."@es ;
    rdfs:label "Tríada Psicosocial Emotiva"@es .

qm:PurePotentiality
    rdfs:label "Potencialidad Pura"@es .

qm:PurposeRedefinition
    rdfs:label "Redefinición del Propósito"@es .

qm:QuantumDiplomacy
    rdfs:label "Diplomacia Cuántica"@es .

# --- Section 9 ---

qm:QuantumMindfulnessApplication
    rdfs:comment "Una práctica transformadora o de reencuadre que tiene como objetivo generar activamente resultados positivos al cambiar el fundamento de la percepción y comprender la estructura de la conciencia. Su objetivo es la 'maestría activa' y la 'libertad perceptual'."@es ,
                 "Una práctica activa/transformadora que tiene como objetivo hacer positiva la Valoración Cognitiva alterando la Valencia(Ψ) a través de un reencuadre intencional y, más profundamente, alterando el Sesgo_M1 base con el tiempo. Es una práctica de generación de significado."@es ;
    rdfs:label "Mindfulness Cuántico (Activo)"@es ,
               "Aplicación de Mindfulness Cuántico"@es .

qm:QuantumObserver
    rdfs:comment "El aspecto consciente y autoconsciente de la conciencia individual, capaz de dirigir la atención deliberadamente y de un enfoque intencional, actuando como el catalizador principal en la transformación de estados potenciales en experiencias reales."@es ;
    rdfs:label "Observador Cuántico"@es .

qm:QuantumPerception
    rdfs:label "Percepción Cuántica"@es .

qm:QuantumPrinciple
    rdfs:comment "Un principio fundamental que guía la comprensión y aplicación del Mindfulness Cuántico, a menudo relacionado con el papel del observador o la naturaleza de la realidad."@es ,
                 "Se refiere al constituyente más granular y operacionalmente distinto de la arquitectura psíquica. Significa que la experiencia subjetiva no es un fenómeno continuo, sino que está constituida por dimensiones psicodinámicas identificables y discretas. El término se usa conceptualmente para describir configuraciones experienciales distintas."@es ;
    rdfs:label "QM_Quantum"@es ,
               "Principio Cuántico"@es .

qm:RawPerceptualImprint
    rdfs:comment "Representa la fuerza o saliencia inicial y no procesada de los datos sensoriales o internos. Es la 'fuerza de la señal bruta' del estímulo antes de que se haya aplicado cualquier procesamiento cognitivo significativo o capa interpretativa."@es ,
                 "Representa la fuerza o saliencia inicial y no procesada de los datos sensoriales o internos; la 'fuerza de la señal bruta'."@es ;
    rdfs:label "Huella Perceptual Bruta (α)"@es .

qm:RawSensoryData
    rdfs:label "Datos Sensoriales Brutos"@es .

qm:ReConvergence
    rdfs:label "Re-Convergencia"@es .

qm:RecognitionPhase
    rdfs:label "Fase 1: Reconocimiento y Distinción Perceptual"@es .

qm:RelationalConsciousness
    rdfs:comment "Conciencia de cómo los propios estados psicológicos son influenciados por otros y cómo los propios estados influyen en los que los rodean, crucial para navegar las sutiles influencias psicológicas inherentes a la experiencia de segunda mano."@es ;
    rdfs:label "Conciencia Relacional"@es .

qm:RelationalHealth
    rdfs:comment "La capacidad de formar relaciones caracterizadas por la confianza, la sintonía emocional y el apoyo mutuo."@es ;
    rdfs:label "Salud Relacional"@es .

qm:RelevanceFunction
    rdfs:comment "Una función que cuantifica cuán directamente se relaciona el contenido de una Observación (Ψ) con cada dimensión psicodinámica específica (Pd_j), determinando la fuerza de la Influencia de la Observación (I_Ψj) en la Activación Dimensional."@es ;
    rdfs:label "Función de Relevancia (Relevancia(Ψ, Pd_j))"@es .

qm:ReligiousFluidity
    rdfs:comment "La capacidad del marco QM para integrarse con diversas orientaciones espirituales y filosóficas sin requerir la adhesión a nuevas doctrinas."@es ;
    rdfs:label "Fluidez Religiosa"@es .

qm:Reputation
    rdfs:label "Reputación"@es .

qm:RequiredTrainingAndCapacity
    rdfs:label "Entrenamiento y Desarrollo de Capacidades Requeridos"@es .

qm:ResponseRePatterning
    rdfs:label "Re-patronaje de Respuesta"@es .

qm:ReverseEngineeringCollapsePatterns
    rdfs:label "Ingeniería Inversa de Patrones de Colapso"@es .

qm:SecondaryModality
    rdfs:comment "Comprende Pd4-Pd10 y articula los procesos complejos a través de los cuales las funciones cognitivas fundamentales se manifiestan e interactúan dentro de la experiencia vivida y el comportamiento observable, dando forma a la textura afectiva, social y relacional de la experiencia."@es ,
                 "Comprende Pd4-Pd10 y da forma a la textura afectiva, social y relacional de la experiencia. Está particularmente implicado en el mecanismo 'La Práctica se Convierte en Creencia'."@es ,
                 "Consiste en las siete Dimensiones Psicodinámicas (Pd4-Pd10) que son moduladas por la salida de la Modalidad Principal y son responsables de dar forma a la textura afectiva, social y relacional de la experiencia."@es ;
    rdfs:label "Modalidad Secundaria (M2)"@es .

qm:SecondaryModalityCategory
    rdfs:comment "Contenedor conceptual para las dimensiones de la Modalidad Secundaria, que dan forma a la experiencia afectiva, social y relacional."@es ;
    rdfs:label "Modalidad Secundaria (M2)"@es .

qm:SecondhandExperience
    rdfs:comment "Experiencias o información adquirida indirectamente, a través de relatos de otros, medios de comunicación o narrativas culturales, en lugar de un encuentro personal directo."@es ,
                 "La compleja red de información, narrativas e interpretaciones transmitidas a través de otros, que representa el conocimiento adquirido indirectamente más allá de la percepción sensorial personal inmediata."@es ;
    rdfs:label "Experiencia de Segunda Mano"@es .

qm:SelectivePermeability
    rdfs:comment "La capacidad de discernir qué información merece atención e integración, operando como un mecanismo de autocorrección cognitiva."@es ;
    rdfs:label "Permeabilidad Selectiva"@es .

qm:SelfAsDynamicObserverParticipant
    rdfs:comment "Un estado de ser evolucionado donde un individuo pasa de modos predominantemente reactivos a una postura proactiva y co-creadora hacia la experiencia, lo que implica el reconocimiento consciente del papel inherente de uno en la construcción de la realidad."@es ;
    rdfs:label "El Ser como Observador-Participante Dinámico"@es .

qm:SelfConceptConstruction
    rdfs:comment "La participación consciente en la formación de la identidad mediante la identificación, elección e integración de aspectos del yo en alineación con valores en evolución."@es ;
    rdfs:label "Construcción del Autoconcepto"@es .

qm:SelfIntegrity
    rdfs:comment "La preservación de las creencias, valores y estructuras de identidad fundamentales."@es ;
    rdfs:label "Integridad del Ser"@es .

qm:SharedReality
    rdfs:comment "Un marco de realidad negociado colectivamente que emerge a través del lenguaje, la cultura y la interacción social."@es ;
    rdfs:label "Realidad Compartida"@es .

qm:SomaticLiteracy
    rdfs:comment "La capacidad cultivada para leer y trabajar con las energías sutiles de la conciencia manifestadas en el cuerpo."@es ;
    rdfs:label "Alfabetización Somática"@es .

qm:SovereignArchitecture
    rdfs:comment "El locus de control interno de un individuo, su capacidad volitiva y su autodominio."@es ,
                 "El resultado positivo de la liberación de guiones, caracterizado por el autodominio interno, el control volitivo, la conciencia dimensional y el pensamiento y la acción auto-originados."@es ;
    rdfs:label "Arquitectura Soberana"@es .

qm:StandardizedProtocol
    rdfs:label "Protocolo Estandarizado"@es .

qm:StochasticInfluence
    rdfs:comment "Representa un elemento inherente de aleatoriedad, ruido o imprevisibilidad dentro de los procesos mentales para cada dimensión (εj), reconociendo que la conciencia no es perfectamente determinista."@es ,
                 "Representa un elemento inherente de aleatoriedad, ruido o imprevisibilidad dentro de los procesos mentales."@es ,
                 "Representa el elemento inherente de aleatoriedad, ruido o imprevisibilidad dentro de los procesos mentales para cada dimensión."@es ;
    rdfs:label "Influencia Estocástica (εj)"@es .

qm:StrategicAttentionManagement
    rdfs:label "Gestión Estratégica de la Atención"@es .

qm:StrategicWaveformArchitecture
    rdfs:label "Arquitectura Estratégica de la Forma de Onda"@es .

qm:StructuralAwareness
    rdfs:comment "La capacidad de discernir las intrincadas contribuciones de cada dimensión psicodinámica dentro de un sentimiento aparentemente monolítico, esencial para la influencia y transformación conscientes dentro del marco de Mindfulness Cuántico."@es ,
                 "La capacidad de discernir las intrincadas contribuciones de cada dimensión psicodinámica dentro de un sentimiento aparentemente monolítico, esencial para la influencia y transformación conscientes."@es ;
    rdfs:label "Conciencia Estructural"@es .

qm:StructuredUnderstanding
    rdfs:comment "Un modo de comprensión que abarca los principios organizativos profundos que subyacen a los fenómenos experienciales, combinando la visión intuitiva con la claridad analítica."@es ;
    rdfs:label "Comprensión Estructurada"@es .

qm:SubDynamicInterference
    rdfs:label "Interferencia Sub-dinámica"@es .

qm:SubconsciousInfrastructure
    rdfs:comment "La 'arquitectura oculta' que comprende respuestas emocionales profundamente arraigadas, patrones de comportamiento automáticos y suposiciones inconscientes."@es ;
    rdfs:label "Infraestructura Subconsciente"@es .

qm:SuperpositionCultivationMethod
    rdfs:comment "Una práctica para trabajar hábilmente con la Superposición Cognitiva, como la meditación o el desapego cognitivo."@es ;
    rdfs:label "Método de Cultivo de la Superposición"@es .

qm:SuperpositionalCognition
    rdfs:comment "Una capacidad cognitiva avanzada que implica el mantenimiento intencional de múltiples perspectivas y posibilidades sin un colapso prematuro."@es ;
    rdfs:label "Cognición Superposicional"@es .

qm:SuperpositionalCognitiveEngineering
    rdfs:comment "La intervención deliberada en el estado previo al colapso de múltiples posibilidades mentales coexistentes para influir en los resultados."@es ;
    rdfs:label "Ingeniería Cognitiva Superposicional"@es .

qm:SustainedAction
    rdfs:comment "Patrones de acción externa consistentes a lo largo del tiempo, traducidos de los sistemas de valores internos."@es ;
    rdfs:label "Acción Sostenida"@es .

qm:SustainedActionMechanism
    rdfs:comment "Un mecanismo psicológico específico que apoya el impulso sostenido de la Dimensión Psico-Motivacional."@es ;
    rdfs:label "Mecanismo de Acción Sostenida"@es .

qm:TherapeuticInterventionForDistress
    rdfs:comment "Aplicaciones de los principios de Mindfulness Cuántico para reencuadrar 'problemas' psicológicos percibidos como constructos maleables moldeados por marcos interpretativos, permitiendo intervenciones específicas y precisas."@es ;
    rdfs:label "Intervención Terapéutica para el Malestar y la Disfunción"@es .

qm:TherapeuticStrategy
    rdfs:comment "Un enfoque sistemático o conjunto de prácticas, métodos y técnicas empleadas dentro del marco de Mindfulness Cuántico para comprender, influir y transformar los estados psicológicos internos de un individuo y su manifestación en la realidad experimentada. Su objetivo es reequilibrar la arquitectura del sistema subyacente de la conciencia."@es ,
                 "Enfoques y métodos utilizados para la intervención terapéutica dentro del marco de Mindfulness Cuántico."@es ;
    rdfs:label "Estrategias Terapéuticas"@es ,
               "Estrategia Terapéutica"@es .

qm:TracingOriginsPhase
    rdfs:label "Fase 2: Rastreo de Orígenes"@es .

qm:TraitInfluence
    rdfs:comment "Incorpora la influencia del Rasgo de personalidad estable y a largo plazo de un individuo (Tj) asociado con una dimensión específica (ITj = wTj ⋅ Tj)."@es ,
                 "Incorpora la influencia del Rasgo de personalidad estable y a largo plazo de un individuo (Tj) asociado con esa dimensión específica (ITj = wTj ⋅ Tj). Aborda: '¿Cuánto influye mi personalidad fundamental en este sentimiento?'. Este es el locus del mecanismo 'la práctica se convierte en creencia'."@es ,
                 "Incorpora la influencia del Rasgo de personalidad estable y a largo plazo de un individuo (Tj) asociado con esa dimensión específica."@es ;
    rdfs:label "Influencia del Rasgo (ITj)"@es .

# --- Section 10 ---

qm:TraitVariable
    rdfs:comment "Una característica de personalidad estable y a largo plazo asociada con una Dimensión Psicodinámica. Puede ser alterada de forma duradera por estados mentales repetidos, formando efectivamente nuevas creencias."@es ,
                 "Un rasgo de personalidad subyacente y estable (Tj) asociado con una Dimensión Psicodinámica. El modelo afirma que 'la práctica se convierte en creencia', lo que significa que las activaciones dimensionales fuertes y repetidas pueden alterar de forma duradera estas variables de Rasgo fundamentales con el tiempo."@es ,
                 "Un rasgo de personalidad subyacente y estable asociado con una Dimensión Psicodinámica, que puede ser alterado de forma duradera por estados mentales repetidos impulsados por fuertes experiencias sociales o emocionales (el mecanismo de 'la práctica se convierte en creencia')."@es ;
    rdfs:label "Variable de Rasgo (Tj)"@es .

qm:TransitionalModalities
    rdfs:comment "Una agrupación de dimensiones (Pd7-9) que vinculan los estados psicológicos internos con la realidad externa."@es ;
    rdfs:label "Modalidades de Transición"@es .

qm:TranslationFatigue
    rdfs:label "Fatiga de Traducción"@es .

qm:UnconsciousReactiveCollapse
    rdfs:comment "Solidificación automática de un estado mental basada en patrones arraigados o influencias externas."@es ;
    rdfs:label "Colapso Reactivo Inconsciente"@es .

qm:UnresolvedSuperpositionConsequence
    rdfs:comment "Un resultado negativo resultante de la incapacidad de gestionar o resolver un estado de Superposición Cognitiva."@es ;
    rdfs:label "Consecuencia de Superposición no Resuelta"@es .

qm:ValueAlignment
    rdfs:comment "La práctica de identificar, clarificar e implementar consistentemente los valores personales en la vida diaria."@es ;
    rdfs:label "Alineación de Valores"@es .

qm:VectorizedAwareness
    rdfs:comment "Un modo operativo central de la conciencia y un instrumento activo para dar forma a la realidad interna, caracterizado por una atención que posee tanto intensidad como direccionalidad precisa. Es una herramienta especializada para navegar por terrenos psicológicos complejos e influir activamente en la emergencia de fenómenos mentales."@es ,
                 "Un modo de atención preciso y direccional para percibir y construir la realidad interna."@es ;
    rdfs:label "Conciencia Vectorizada"@es .

qm:ViewOfPerception
    rdfs:label "Visión de la Percepción"@es .

qm:VolitionalCommitment
    rdfs:comment "La decisión consciente y deliberada de adoptar y mantener la adhesión a una intención o meta específica. Es la piedra angular de un Anclaje Cognitivo efectivo."@es ;
    rdfs:label "Compromiso Volitivo"@es .

qm:VolitionalContinuity
    rdfs:comment "Una estructura psicológica que mantiene su integridad y forma psicológica incluso en medio de la incertidumbre o la disonancia cognitiva, representando la persistencia fundamental del compromiso intencional."@es ;
    rdfs:label "Continuidad Volitiva"@es .

qm:VolitionalImpulse
    rdfs:label "Impulso Volitivo"@es .

qm:VulnerabilityStructure
    rdfs:comment "Patrones profundamente codificados generados cuando las necesidades humanas fundamentales de seguridad emocional, conexión y validación no se satisfacen crónicamente."@es ;
    rdfs:label "Estructura de Vulnerabilidad"@es .

qm:Will
    rdfs:comment "La facultad de la conciencia por la cual uno elige o decide deliberadamente un curso de acción."@es ;
    rdfs:label "Voluntad"@es ;
    skos:definition "La facultad cognitiva de la elección consciente y deliberada."@es .

qm:WillToConnection
    rdfs:comment "Un impulso fundamental hacia el significado, la identidad y la interconexión, que opera con una fuerza direccional consistente."@es ;
    rdfs:label "Voluntad de Conexión"@es .

qm:WitnessConsciousness
    rdfs:comment "El cultivo de una conciencia desapegada y sin juicios que observa los fenómenos mentales sin alterar su curso natural."@es ;
    rdfs:label "Conciencia Testigo"@es .

qm:ZeigarnikEffect
    rdfs:comment "La tendencia psicológica a recordar mejor las tareas incompletas o interrumpidas que las tareas completadas."@es ;
    rdfs:label "Efecto Zeigarnik"@es ;
    skos:definition "El fenómeno por el cual las personas recuerdan mejor las tareas inacabadas que las terminadas."@es .

qm:M1
    rdfs:label "La Modalidad Principal (M1)"@es .

qm:Pd1
    rdfs:label "Dimensión Psico-Volitiva (Pd1)"@es ,
               "La Dimensión Psico-Volitiva (Pd1)"@es .

qm:Pd10
    rdfs:label "La Dimensión Psico-Transpersonal (Pd10)"@es .

qm:Pd2
    rdfs:label "Dimensión Psico-Conceptiva (Pd2)"@es ,
               "La Dimensión Psico-Conceptiva (Pd2)"@es .

qm:Pd3
    rdfs:label "Dimensión Psico-Meditativa (Pd3)"@es ,
           "La Dimensión Psico-Meditativa (Pd3)"@es .

qm:Pd4
    rdfs:label "La Dimensión Psico-Empática (Pd4)"@es .

qm:Pd5
    rdfs:label "La Dimensión Psico-Protectora (Pd5)"@es .

qm:Pd6
    rdfs:label "La Dimensión Psico-Estética (Pd6)"@es .

qm:Pd7
    rdfs:label "La Dimensión Psico-Motivacional (Pd7)"@es .

qm:Pd8
    rdfs:label "La Dimensión Psico-Receptiva (Pd8)"@es .

qm:Pd9
    rdfs:label "La Dimensión Psico-Fundacional (Pd9)"@es .

qm:RighteousAnger
    rdfs:comment "Un estado psicológico emergente que surge de la interacción de la identificación compasiva, el juicio de límites y el reconocimiento de una violación de la belleza moral."@es ;
    rdfs:label "Ira Justa"@es .

qm:TheTransitionalModalities
    rdfs:comment "Un grupo de dimensiones psicodinámicas (Pd7-9) que sirven como puente entre los estados psicológicos internos y su expresión en el mundo externo."@es ;
    rdfs:label "Las Modalidades de Transición (Pd7-9)"@es ;
    skos:definition "El conjunto de funciones psíquicas que median entre los mundos interno y externo."@es .

[ rdfs:comment "Ecuación Formal: Ψ = α(β + 1)(A + f)"@es ] .
[ rdfs:comment "La ecuación formal Kj = I_Sj + I_Cj + I_Tj + I_Ψj + εj significa que la activación total emerge de la confluencia de estas múltiples y distintas influencias."@es ] .
[ rdfs:comment "Ecuación Formal: Kj = I_Sj + I_Cj + I_Tj + I_Ψj + εj"@es ] .
[ rdfs:comment "Ecuación Formal: C = wΨ ⋅ Valencia(Ψ) + wS ⋅ ValenciaProm(S_t-1) + Sesgo_M1"@es ] .
[ rdfs:comment "Busca hacer activamente positiva la Valoración Cognitiva alterando la Valencia(Ψ) a través del reencuadre y, más profundamente, alterando el Sesgo_M1 base con el tiempo."@es ] .
[ rdfs:comment "Busca neutralizar una Influencia Cognitiva negativa reduciendo la reactividad (disminuyendo wΨ y wS) y observando sin juzgar (llevando la Valencia(Ψ) a cero)."@es ] .
[ rdfs:comment "Busca neutralizar una Valoración Cognitiva negativa reduciendo la reactividad (disminuyendo wΨ y wS) y observando sin juzgar (llevando la Valencia(Ψ) hacia cero)."@es ] .
[ rdfs:comment "La ecuación formal Ψ = α(β + 1)(A + f) subraya que estos componentes son interdependientes y contribuyen sinérgicamente a la fuerza general de la Observación."@es ] .
[ rdfs:comment "Ecuación Formal: S = Σ(xj * Pdj) para j=1 a 10. Representa el estado mental como un vector en el 'espacio' de las dimensiones psicodinámicas."@es ] .
[ rdfs:comment "La ecuación formal C = wΨ ⋅ Valencia(Ψ) + wS ⋅ ValenciaProm(S_t-1) + Sesgo_M1 encapsula la compleja interacción de estos factores."@es ] .
[ rdfs:comment "Busca asegurar activamente que la Influencia Cognitiva se vuelva positiva alterando la Valencia(Ψ) a través del reencuadre y, más profundamente, alterando el Sesgo_M1 base."@es ] .

:CognitiveSuperposition
    rdfs:comment "Esta clase describe el estado de potencial mental preconsciente. Es crucial distinguir esto del principio físico; aquí, es una herramienta conceptual para modelar la capacidad de la psique para mantener múltiples posibilidades no resueltas antes de un acto de atención consciente."@es ;
    skos:definition "El término 'superposición' se usa aquí en un sentido conceptual, derivado de sus raíces latinas 'super-' (sobre) y 'positio' (colocar), significando múltiples potenciales 'colocados' en el mismo espacio conceptual. Describe un estado preconsciente fundamental donde múltiples pensamientos o percepciones potenciales coexisten como un campo de probabilidad dinámico. El término se usa así como una analogía precisa para este estado de potencial mental no resuelto, que precede al 'colapso' en un único pensamiento consciente."@es .

:ConsciousnessWaveFunction
    rdfs:comment "Esta clase proporciona una etiqueta conceptual para el campo en el que existe el potencial mental. Este es un concepto psicológico abstracto, no una fórmula matemática en el sentido físico."@es ;
    skos:definition "Este término se construye a partir de sus partes constituyentes para formar una etiqueta conceptual. Una 'función' describe una relación entre entradas y salidas, y una 'onda' representa un estado de fluctuación y potencial. El marco combina estos para definir la 'Función de Onda de la Conciencia' como el espacio conceptual o campo probabilístico que contiene toda la gama de estados mentales potenciales antes de que se actualicen a través del colapso psicodinámico."@es .

:InterferencePatterns
    rdfs:comment "Esta clase describe los efectos emergentes de las dimensiones psicodinámicas combinadas, que pueden amplificarse o disminuirse mutuamente."@es ;
    skos:definition "El término 'interferencia' se usa en su sentido general de un proceso que afecta, modifica o cancela a otro. En esta ontología, describe cómo interactúan las 'ondas' de diferentes dimensiones psicodinámicas. Esto puede resultar en 'Interferencia Constructiva', donde las dimensiones se alinean para amplificar las cualidades positivas, o 'Interferencia Destructiva', donde entran en conflicto y crean disonancia interna."@es .

:PsychodynamicWaveCollapse
    rdfs:comment "Esta clase representa el proceso pivotal donde el campo probabilístico de la mente se resuelve en una experiencia específica y actualizada."@es ;
    skos:definition "Basado en el significado general de 'colapso' —caer juntos en un estado más compacto o definido— este término describe la transición psicológica fundamental del potencial a la actualidad. Dentro de este marco, es el proceso específico por el cual la 'onda' de múltiples posibilidades mentales (definida en qm:CognitiveSuperposition) se resuelve en un resultado singular, definido y conscientemente experimentado, desencadenado por un acto de atención."@es .

:PsychologicalEntanglement
    rdfs:comment "Esta clase modela el principio de interconexión profunda y persistente entre sistemas psicológicos, que puede no ser inmediatamente obvio o causal en un sentido lineal."@es ;
    skos:definition "A partir del significado general de 'entrelazamiento' —estar intrincadamente entrelazado o conectado— este marco utiliza el término para describir un estado de profunda interconexión psicológica. Por ejemplo, qm:EmotionalQuantumEntanglement se define como la interconexión persistente de los estados mentales y emocionales entre individuos. El término se utiliza como una poderosa metáfora para describir conexiones profundas y no locales que operan más allá de la percepción directa."@es .

:QM_Quantum
    rdfs:comment "El principio conceptual de que la experiencia subjetiva no es un fenómeno continuo, sino que está constituida por dimensiones psicodinámicas identificables y discretas. Este término se usa conceptualmente para describir configuraciones experienciales distintas, no un modelo de computación cerebral."@es ;
    skos:definition "Basado en su origen latino 'quantus' (que significa 'cuánto' o 'una cantidad'), un 'cuanto' en este marco es la cantidad discreta más pequeña o unidad fundamental de la arquitectura psíquica. Si bien se basa en esta definición primaria, el marco extiende este concepto creando una poderosa analogía psicológica con conceptos de la física cuántica. Utiliza principios relacionados como 'superposición' (qm:CognitiveSuperposition) y 'colapso' (qm:PsychodynamicCollapse) para construir un modelo novedoso de cómo funciona la mente, contrastándolo con los modelos continuos de mentación."@es .

qm:AnalyticalReasoning
    rdfs:comment "La capacidad de deconstruir información en categorías más pequeñas para sacar conclusiones."@es ;
    rdfs:label "Razonamiento Analítico y Dialéctico"@es ;
    skos:definition "Una forma de cognición que utiliza la lógica y el pensamiento sistemático para resolver problemas."@es .

qm:BalancingDimensionalEnergies
    rdfs:comment "La práctica de trabajar conscientemente para crear armonía y equilibrio entre las diferentes dimensiones psicodinámicas."@es ;
    rdfs:label "Equilibrio de Energías Dimensionales"@es ;
    skos:definition "Una práctica avanzada destinada a lograr el equilibrio entre las diversas dimensiones energéticas de la psique."@es .

qm:CalculatedTurbulence
    rdfs:comment "El estado óptimo de equilibrio, concebido como un equilibrio dinámico donde las dimensiones permanecen activamente comprometidas y receptivas dentro de umbrales productivos."@es ;
    rdfs:label "Turbulencia Calculada"@es .

qm:CognitiveAnchoringFailure
    rdfs:comment "La incapacidad de mantener un enfoque mental o intencional estable, lo que conduce a la distracción, la impulsividad o una sensación de estar a la deriva."@es ;
    rdfs:label "Fallo del Anclaje Cognitivo"@es ;
    skos:definition "El fallo en mantener un estado cognitivo o intencional estable."@es .

qm:CognitiveAppraisal
    rdfs:comment "El juicio o interpretación principal y de alto nivel de la mente sobre un fenómeno observado, realizado por la Modalidad Principal. Funciona como una 'señal de control maestra' o 'directiva principal' que proporciona el impulso direccional general para el posterior Colapso Psicodinámico. Es un proceso dinámico y potencialmente iterativo."@es ,
                 "El juicio o interpretación principal y de alto nivel de la mente sobre un fenómeno observado, realizado por la Modalidad Principal. Funciona como una 'señal de control maestra' que proporciona el impulso direccional general para el posterior Colapso Psicodinámico. Su valor es una suma ponderada de tres fuerzas distintas."@es ,
                 "La 'señal de control maestra' o 'directiva principal' pivotal que traduce una observación compleja en un único juicio de alto nivel, impulsando la activación de las diez Dimensiones Psicodinámicas."@es ,
                 "La 'señal de control maestra' o 'directiva principal' pivotal que traduce una observación compleja en un único juicio de alto nivel, impulsando la activación de las diez Dimensiones Psicodinámicas. Está determinada por la valencia de la observación, el estado mental previo y un sesgo inherente de la Modalidad Principal."@es ;
    rdfs:label "Valoración Cognitiva (C)"@es .

qm:CognitiveCapacity
    rdfs:comment "Una habilidad o potencial mental inherente que puede desarrollarse a través de la práctica."@es ;
    rdfs:label "Capacidad Cognitiva"@es ;
    skos:definition "La habilidad mental para realizar una tarea particular."@es .

qm:CognitiveInfluence
    rdfs:comment "Representa el impacto directo de la Valoración Cognitiva general (C) en la activación de una dimensión."@es ,
                 "Representa el impacto directo de la Valoración Cognitiva general (C) en la activación de una dimensión específica (ICj = wCj ⋅ C)."@es ,
                 "Representa el impacto directo de la Valoración Cognitiva general (C) en la activación de una dimensión específica (ICj = wCj ⋅ C). Aborda: '¿Cuánto influye mi juicio general sobre esta situación en este sentimiento específico?'. Este es un punto de intervención clave tanto para el Mindfulness Clásico como para el Cuántico."@es ;
    rdfs:label "Influencia Cognitiva (ICj)"@es .

qm:CognitiveMultiStateAwareness
    rdfs:comment "La capacidad de mantener en la mente múltiples ideas o perspectivas, incluso contradictorias, simultáneamente sin necesidad de resolverlas de inmediato."@es ;
    rdfs:label "Conciencia de Múltiples Estados Cognitivos"@es ;
    skos:definition "La capacidad de ser consciente y considerar múltiples estados mentales a la vez."@es .

qm:CollapseMode
    rdfs:comment "La manera en que un estado de superposición cognitiva se resuelve en una experiencia definida, que puede ser intencional o reactiva."@es ;
    rdfs:label "Modo de Colapso"@es ;
    skos:definition "Una forma específica en que un campo de posibilidades colapsa en una única realidad."@es .

qm:ConsensusReality
    rdfs:comment "Un conjunto compartido de creencias y percepciones sobre las que un grupo de personas está de acuerdo, que forma su comprensión común de la realidad."@es ;
    rdfs:label "Realidad de Consenso"@es ;
    skos:definition "Una realidad acordada basada en una comprensión compartida dentro de un grupo."@es .

qm:Contemplation
    rdfs:comment "Un proceso cognitivo activo y deliberado que implica un trabajo mental sostenido y riguroso para transformar el potencial en una Comprensión Estructurada. Es integral a la conciencia y fundamental para procesar toda experiencia consciente."@es ,
                              "Un proceso cognitivo activo y deliberado que implica un trabajo mental sostenido y riguroso para transformar el potencial cognitivo bruto en una comprensión estructurada. Es crucial para el colapso psico-meditativo y complementa el mindfulness fundamental."@es .

qm:CreativeGenesis
    rdfs:comment "El proceso de dar vida a nuevas ideas, conocimientos o creaciones, a menudo visto como emergente de un estado de potencial abierto."@es ;
    rdfs:label "Génesis Creativa"@es ;
    skos:definition "El origen o comienzo de un proceso creativo."@es .

qm:DecoherenceBacklog
    rdfs:comment "Una acumulación de superposiciones cognitivas no resueltas, que conduce a un estado de desorden mental y una eficiencia cognitiva reducida."@es ;
    rdfs:label "Atraso de Decoherencia"@es ;
    skos:definition "Una acumulación de estados mentales no resueltos que afecta la función cognitiva."@es .

qm:DecouplingPhase
    rdfs:comment "Una etapa en el proceso de liberación de los guiones heredados, donde uno comienza a des-identificarse y separarse de los patrones condicionados."@es ;
    rdfs:label "Fase 3: Desacoplamiento y Cultivo de la Arquitectura Soberana"@es ;
    skos:definition "La fase de separación de los patrones condicionados de pensamiento y comportamiento."@es .

qm:DimensionalLiteracy
    rdfs:comment "La capacidad de reconocer, comprender y navegar hábilmente las diversas dimensiones psicodinámicas de la experiencia."@es ;
    rdfs:label "Alfabetización Dimensional"@es ;
    skos:definition "La habilidad de comprender y trabajar con las diferentes dimensiones de la conciencia."@es .

qm:EmotionalResponse
    rdfs:comment "La reacción de un individuo a un evento o estímulo específico, que involucra activación fisiológica, conductas expresivas y experiencia consciente."@es ;
    rdfs:label "Respuesta Emocional"@es ;
    skos:definition "Una reacción psicológica y fisiológica a un estímulo."@es .

qm:EthicalBoundaries
    rdfs:comment "Los principios morales y estándares profesionales que restringen la aplicación de las prácticas de Mindfulness Cuántico."@es ;
    rdfs:label "Límites Éticos"@es ;
    skos:definition "Los límites éticos que gobiernan el uso de una práctica o técnica."@es .

qm:HumorAsCognitiveTechnology
    rdfs:comment "El uso del humor como una herramienta sofisticada para reencuadrar perspectivas, reducir la rigidez cognitiva y fomentar el bienestar psicológico."@es ;
    rdfs:label "Humor como Tecnología Cognitiva"@es ;
    skos:definition "Emplear el humor como una técnica deliberada para cambiar los estados cognitivos y emocionales."@es .

qm:ImposterSyndrome
    rdfs:comment "Un patrón psicológico en el que un individuo duda de sus habilidades, talentos o logros y tiene un miedo persistente e internalizado a ser expuesto como un 'fraude'."@es ;
    rdfs:label "Síndrome del Impostor"@es ;
    skos:definition "La experiencia de sentirse como un fraude, a pesar de la evidencia de éxito."@es .

qm:InstitutionalArchitectureImposition
    rdfs:comment "La influencia de las instituciones sociales y sus estructuras en las creencias, valores y comportamientos de un individuo."@es ;
    rdfs:label "Imposición de la Arquitectura Institucional"@es ;
    skos:definition "El moldeamiento de un individuo por las estructuras de las instituciones."@es .

qm:LearnedBehavioralRepertoire
    rdfs:comment "La colección de comportamientos y respuestas que un individuo ha aprendido de su entorno y experiencias."@es ;
    rdfs:label "Repertorio Conductual Aprendido"@es ;
    skos:definition "El conjunto de comportamientos que una persona ha adquirido a través del aprendizaje."@es .

qm:Memory
    rdfs:label "Memoria (Explícita e Implícita)"@es .

qm:MentalFlexibility
    rdfs:comment "La capacidad de adaptar las estrategias de procesamiento cognitivo para enfrentar condiciones nuevas e inesperadas en el entorno."@es ;
    rdfs:label "Flexibilidad Mental"@es ;
    skos:definition "La capacidad de cambiar entre diferentes conceptos o de pensar en múltiples conceptos simultáneamente."@es .

qm:MindfulnessBasedCognitiveTherapy
    rdfs:comment "Un enfoque terapéutico basado en la evidencia que combina técnicas de mindfulness con la terapia cognitivo-conductual para ayudar a prevenir la recaída de la depresión."@es ;
    rdfs:label "Terapia Cognitiva Basada en Mindfulness (TCBM)"@es ;
    skos:definition "Una intervención terapéutica que combina la meditación mindfulness con la terapia cognitiva."@es .

qm:NeurologicalEmbedding
    rdfs:comment "El proceso por el cual los pensamientos y comportamientos repetidos crean y fortalecen las vías neuronales en el cerebro, haciendo que esos patrones sean más automáticos."@es ;
    rdfs:label "Incrustación Neurológica por Repetición"@es ;
    skos:definition "El proceso físico de aprendizaje y formación de hábitos en el cerebro."@es .

qm:ObservationValence
    rdfs:comment "La coloración emocional subjetiva o la calificación numérica de positividad o negatividad que la mente asigna a una observación específica. Esta valencia es un resultado crucial del proceso perceptual e interpretativo y proporciona el componente del 'Impacto del Ahora' para la Valoración Cognitiva."@es ;
    rdfs:label "Valencia de la Observación (Valencia(Ψ))"@es .

qm:ObserverEffectParadox
    rdfs:comment "El desafío de observar un sistema sin alterarlo, particularmente en el contexto de la autoobservación, donde el acto de observar la propia mente inevitablemente la cambia."@es ;
    rdfs:label "Paradoja del Efecto Observador"@es ;
    skos:definition "La paradoja de que el acto de observación puede cambiar el fenómeno que se está observando."@es .

qm:ObserverRole
    rdfs:comment "La función y postura del observador en el proceso de percepción y construcción de la realidad."@es ;
    rdfs:label "Rol del Observador"@es ;
    skos:definition "El papel que desempeña el observador en un sistema."@es .

qm:OntologicalReassignment
    rdfs:comment "La práctica de cambiar la clasificación fundamental o 'ser-idad' de un fenómeno para alterar la relación que se tiene con él."@es ;
    rdfs:label "Reasignación Ontológica"@es ;
    skos:definition "El acto de cambiar la categoría ontológica de un concepto o experiencia."@es .

qm:OntologicalRestructuring
    rdfs:comment "La práctica avanzada de alterar fundamentalmente la propia comprensión del ser y la realidad."@es ;
    rdfs:label "Reestructuración Ontológica"@es ;
    skos:definition "El proceso de cambiar las creencias fundamentales sobre la existencia."@es .

qm:OsmoticIntegration
    rdfs:comment "La absorción gradual y a menudo inconsciente de creencias, actitudes y comportamientos del entorno social y cultural de uno."@es ;
    rdfs:label "Integración Osmótica"@es ;
    skos:definition "El proceso de absorber información y comportamientos del entorno circundante."@es .

qm:PerceptualMastery
    rdfs:comment "La habilidad avanzada para dar forma consciente y hábilmente a la propia experiencia perceptual."@es ;
    rdfs:label "Maestría Perceptual"@es ;
    skos:definition "Un alto nivel de habilidad para manejar y dirigir la propia percepción."@es .

qm:PersonalTendency_CognitiveResponsiveness
    rdfs:comment "El nivel característico de reactividad de un individuo a sus propias valoraciones cognitivas, que influye en la fuerza con que sus juicios afectan su estado mental posterior."@es ;
    rdfs:label "Tendencia Personal (Sensibilidad Cognitiva - wCj)"@es ;
    skos:definition "El grado en que los pensamientos y juicios de un individuo sobre una situación impactan su estado emocional y cognitivo posterior."@es .

qm:PersonalTendency_MoodPersistence
    rdfs:comment "La tendencia natural de un individuo a que un estado de ánimo o emocional continúe en el tiempo."@es ;
    rdfs:label "Tendencia Personal (Persistencia del Estado de Ánimo - wS)"@es ;
    skos:definition "El grado en que el estado de ánimo de una persona tiende a permanecer estable en el tiempo."@es .

qm:PersonalTendency_Persistence
    rdfs:comment "La tendencia de un individuo a mantener un estado mental o emocional particular a lo largo del tiempo."@es ;
    rdfs:label "Tendencia Personal (Persistencia Dimensional - wSj)"@es ;
    skos:definition "La disposición a continuar en un estado particular."@es .

qm:PersonalTendency_Reactivity
    rdfs:comment "El nivel característico de reactividad emocional y cognitiva de un individuo a los eventos externos y estímulos internos."@es ;
    rdfs:label "Tendencia Personal (Reactividad a Nuevos Eventos - wΨ)"@es ,
               "Tendencia Personal (Reactividad - wΨ)"@es ;
    skos:definition "El grado en que una persona reacciona a los estímulos."@es .

qm:PrincipleOfBalance
    rdfs:comment "Un principio fundamental relacionado con la armonía, el equilibrio y la integración de fuerzas opuestas dentro de la psique."@es ;
    rdfs:label "Principio de Equilibrio"@es ;
    skos:definition "El principio estético preocupado por lograr el equilibrio y la armonía."@es .

qm:PrincipleOfLimit
    rdfs:comment "El principio de establecer y mantener límites y restricciones saludables."@es ;
    rdfs:label "Principio de Límite"@es ;
    skos:definition "Una regla guía para establecer restricciones necesarias y saludables."@es .

qm:PrincipleOfMeasure
    rdfs:comment "El principio relacionado con el establecimiento de límites y fronteras apropiadas."@es ;
    rdfs:label "Principio de Medida"@es ;
    skos:definition "Una regla guía para establecer la proporción y los límites adecuados."@es .

qm:ProbabilisticSteering
    rdfs:comment "La práctica de influir conscientemente en la probabilidad de ciertos estados o resultados mentales dirigiendo la atención y la intención, sin forzar un resultado específico."@es ;
    rdfs:label "Dirección Probabilística"@es ;
    skos:definition "La guía consciente y sutil de la dirección mental y emocional mediante la gestión de las probabilidades de varios estados potenciales."@es .

qm:PsychoVolitionalDynamics
    rdfs:comment "La interacción de la voluntad, la intención y la energía psíquica que impulsa los procesos cognitivos y emocionales."@es ;
    rdfs:label "Dinámicas Psico-Volitivas"@es ;
    skos:definition "El estudio y la aplicación de las fuerzas de la voluntad y la intención dentro de la psique."@es .

qm:PsychologicalSelfSurgery
    rdfs:comment "Un concepto metafórico para la práctica avanzada y deliberada de identificar, analizar y reestructurar los propios patrones y creencias psicológicas profundas."@es ;
    rdfs:label "Autocirugía Psicológica"@es ;
    skos:definition "La práctica de aplicar una introspección y un autoanálisis profundos para cambiar fundamentalmente la propia composición psicológica."@es .

qm:RelationalMindfulness
    rdfs:comment "La aplicación de los principios del mindfulness a las relaciones interpersonales, centrándose en la conciencia de uno mismo y de los demás en las interacciones sociales."@es ;
    rdfs:label "Mindfulness Relacional"@es ;
    skos:definition "La práctica de ser conscientemente consciente en el contexto de las relaciones."@es .

qm:ResolutionFatigue
    rdfs:comment "Una forma profunda de tensión cognitiva donde la capacidad de la mente para formar estados mentales definidos a partir de posibilidades se ve comprometida, a menudo debido a que las entradas externas sobrescriben las señales internas."@es ;
    rdfs:label "Fatiga de Resolución"@es .

qm:ReverseEngineeringEmotionalStates
    rdfs:comment "La práctica de deconstruir un estado emocional para comprender sus partes constituyentes y sus fuentes dimensionales subyacentes."@es ;
    rdfs:label "Ingeniería Inversa de Estados Emocionales"@es ;
    skos:definition "Una práctica avanzada de analizar una emoción para comprender sus orígenes y estructura."@es .

qm:SigmoidFunction
    rdfs:comment "Una función matemática utilizada para transformar la Activación Dimensional bruta (Kj) en una Intensidad Final normalizada (xj) entre 0 y 1. Se elige por su no linealidad y su comportamiento similar a un umbral, que refleja los fenómenos psicológicos."@es ,
                 "Una función matemática utilizada para transformar la Activación Dimensional bruta (Kj) en una Intensidad Final normalizada (xj) entre 0 y 1. Se elige por sus propiedades de normalización, no linealidad y su comportamiento similar a un umbral, que modela con precisión cómo se manifiestan los fenómenos psicológicos."@es ;
    rdfs:label "Función Sigmoidea"@es .

qm:SocialInfluence
    rdfs:comment "El efecto que las palabras, acciones o la mera presencia de otras personas tienen en nuestros pensamientos, sentimientos, actitudes o comportamiento."@es ;
    rdfs:label "Influencia Social"@es ;
    skos:definition "El proceso por el cual las actitudes, creencias o comportamiento de los individuos son modificados por la presencia o acción de otros."@es .

qm:StrategicCognitiveTrajectoryManipulation
    rdfs:comment "El moldeamiento deliberado y estratégico de la propia trayectoria cognitiva y emocional a lo largo del tiempo."@es ;
    rdfs:label "Manipulación Estratégica de la Trayectoria Cognitiva"@es ;
    skos:definition "La práctica de guiar intencionalmente la dirección de los propios pensamientos y sentimientos."@es .

qm:StructuralIntrospection
    rdfs:comment "Una forma disciplinada de autoexamen centrada en comprender las estructuras subyacentes de la propia conciencia y los patrones psicológicos."@es ;
    rdfs:label "Introspección Estructural"@es ;
    skos:definition "La práctica de mirar hacia adentro para comprender la arquitectura de la propia mente."@es .

qm:SystemDeconstruction
    rdfs:comment "La práctica de descomponer sistemas psicológicos complejos en sus componentes fundamentales para comprender su funcionamiento."@es ;
    rdfs:label "Deconstrucción de Sistemas"@es ;
    skos:definition "Una práctica analítica de desmontar un sistema para ver cómo funciona."@es .

qm:TacitKnowledge
    rdfs:comment "Conocimiento que es difícil de expresar o articular, a menudo adquirido a través de la experiencia y la práctica en lugar de la instrucción formal."@es ;
    rdfs:label "Conocimiento Tácito"@es ;
    skos:definition "Comprensión o saber hacer implícito que no se verbaliza fácilmente."@es .

qm:TranslationChallengeInPsychology
    rdfs:comment "La dificultad de traducir experiencias psicológicas subjetivas a un lenguaje científico y objetivo sin perder el significado esencial."@es ;
    rdfs:label "Desafío de la Traducción en Psicología"@es ;
    skos:definition "El problema de transmitir con precisión conceptos psicológicos subjetivos."@es .

qm:TraumaticCollapse
    rdfs:comment "Una resolución rápida y abrumadora de una superposición cognitiva desencadenada por un evento traumático, que conduce a un estado mental rígido y a menudo disfuncional."@es ;
    rdfs:label "Colapso Traumático"@es ;
    skos:definition "El colapso del potencial mental en un estado fijo como resultado de un trauma."@es .
