@prefix : <http://tuos.org/qm#> .
@prefix dc: <http://purl.org/dc/elements/1.1/> .
@prefix qm: <https://tuos.org/qm#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix xml: <http://www.w3.org/XML/1998/namespace> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@base <http://tuos.org/qm> .

<http://tuos.org/qm> rdf:type owl:Ontology ;
                         dc:creator "The University of Ontological Science" ;
                         dc:title "Quantum Mindfulness - Power of Perception and Psychodynamic Dimensions Ontology" ;
                         rdfs:comment "A formal ontology of the Quantum Mindfulness framework's Prime Modality. This version uses OWL restrictions to define relationships at the class level, ensuring a robust and machine-readable structure."@en ,
                                      "A formal ontology of the psychodynamic architecture of consciousness as detailed in the Quantum Mindfulness source material. This model defines the sequential process from Observation to the emergence of a final Mental State, and the mechanism of Belief Formation."@en ,
                                      "An ontology of the Quantum Mindfulness framework. Note: While some source texts refer to eleven dimensions, the detailed enumeration consistently lists ten (Pd1-Pd10). The concept of 'eleven' may allude to a foundational 'Psycho-Volitional core' that underpins the ten enumerable dimensions."@en .

#################################################################
#    Annotation properties
#################################################################

###  http://purl.org/dc/elements/1.1/creator
dc:creator rdf:type owl:AnnotationProperty .


###  http://purl.org/dc/elements/1.1/title
dc:title rdf:type owl:AnnotationProperty .


###  http://www.w3.org/2000/01/rdf-schema#subClassOf
rdfs:subClassOf rdf:type owl:AnnotationProperty .


###  http://www.w3.org/2004/02/skos/core#altLabel
skos:altLabel rdf:type owl:AnnotationProperty .


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
                 rdfs:label "constituent of"@en .


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
                 rdfs:label "contributes to"@en .


###  https://tuos.org/qm#definesRoleOfObserverAs
qm:definesRoleOfObserverAs rdf:type owl:ObjectProperty ;
                           rdfs:comment "Defines the conceptual role of the conscious observer within a specific mindfulness paradigm."@en ;
                           rdfs:label "defines role of observer as"@en .


###  https://tuos.org/qm#dependsOn
qm:dependsOn rdf:type owl:ObjectProperty ;
             owl:inverseOf qm:providesFoundationFor ;
             rdfs:domain qm:PsychodynamicDimension ;
             rdfs:range qm:PsychodynamicDimension ;
             rdfs:label "depends on"@en .


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
              rdfs:label "harmonizes"@en .


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
                  rdfs:label "has primacy over"@en .


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
                     rdfs:label "is achieved through"@en .


###  https://tuos.org/qm#isAlteredBy
qm:isAlteredBy rdf:type owl:ObjectProperty ;
               rdfs:label "is altered by"@en .


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
                    rdfs:label "is calculated from"@en .


###  https://tuos.org/qm#isConfirmedBy
qm:isConfirmedBy rdf:type owl:ObjectProperty ;
                 rdfs:comment "Indicates that the existence of a phenomenon is known through its consistent influence or discernible patterns, rather than direct observation."@en ;
                 rdfs:label "is confirmed by"@en .


###  https://tuos.org/qm#isConstrainedBy
qm:isConstrainedBy rdf:type owl:ObjectProperty ;
                   rdfs:label "is constrained by"@en .


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
                 rdfs:label "is developed by"@en .


###  https://tuos.org/qm#isEngagedBy
qm:isEngagedBy rdf:type owl:ObjectProperty ;
               rdfs:label "is engaged by"@en .


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
             rdfs:label "is input to"@en .


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
             rdfs:label "is locus of"@en .


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
              rdfs:label "is output of"@en .


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
              rdfs:label "is source of"@en .


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
             rdfs:label "leverages"@en .


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
              rdfs:label "operates as"@en .


###  https://tuos.org/qm#operatesThrough
qm:operatesThrough rdf:type owl:ObjectProperty ;
                   rdfs:domain qm:PsychodynamicDimension ;
                   rdfs:range qm:ProcessingMechanism ;
                   rdfs:label "operates through"@en .


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
             rdfs:label "practices"@en .


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
                         rdfs:label "provides foundation for"@en .


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
                              rdfs:subClassOf qm:Uncategorized ;
                              rdfs:comment "Internal states such as insights, principles, values, and intuitive understandings."@en ;
                              rdfs:label "Abstract Internal Experience"@en .


###  https://tuos.org/qm#ActionableIntelligence
qm:ActionableIntelligence rdf:type owl:Class ;
                          rdfs:subClassOf qm:Uncategorized ;
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
                       rdfs:subClassOf qm:ProcessingMechanism ;
                       rdfs:label "Analytical and Dialectical Reasoning"@en .


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
                   rdfs:label "Assigned Meaning"@en .


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
                                rdfs:subClassOf qm:PracticesCategory ;
                                rdfs:label "Balancing Dimensional Energies"@en .


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
                                             qm:UnresolvedSuperpositionConsequence ;
                             rdfs:label "Cognitive Anchoring Failure"@en .


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
                     rdfs:subClassOf qm:GoalsCategory ;
                     rdfs:label "Cognitive Capacity"@en .


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
                      rdfs:subClassOf qm:Uncategorized ;
                      rdfs:comment "The capacity to sustain motivation and enable long-term pattern recognition essential for achieving goals across extended time periods."@en ;
                      rdfs:label "Cognitive Endurance"@en .


###  https://tuos.org/qm#CognitiveEnhancement
qm:CognitiveEnhancement rdf:type owl:Class ;
                        rdfs:subClassOf owl:Thing ,
                                        qm:MainStrategiesCategory ,
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
                                rdfs:subClassOf qm:CognitiveCapacity ;
                                rdfs:label "Cognitive Multi-State Awareness"@en .


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
                rdfs:subClassOf qm:CognitiveSuperposition ;
                rdfs:label "Collapse Mode"@en .


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
                    rdfs:subClassOf qm:SharedReality ;
                    rdfs:label "Consensus Reality"@en .


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
                            rdfs:subClassOf qm:Uncategorized ;
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
                   rdfs:subClassOf qm:Phenomenon ;
                   rdfs:label "Creative Genesis"@en .


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
                                      qm:UnresolvedSuperpositionConsequence ;
                      rdfs:label "Decoherence Backlog"@en .


###  https://tuos.org/qm#DecouplingPhase
qm:DecouplingPhase rdf:type owl:Class ;
                   rdfs:subClassOf qm:LiberationProcess ;
                   rdfs:label "Phase 3: Decoupling & Cultivating Sovereign Architecture"@en .


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
                       rdfs:subClassOf qm:CognitiveCapacity ;
                       rdfs:label "Dimensional Literacy"@en .


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
                       rdfs:subClassOf owl:Thing ;
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
                                     ] ;
                     rdfs:label "Emotional Response"@en .


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
                     rdfs:subClassOf qm:PracticalLimitationsOfQMApplication ;
                     rdfs:label "Ethical Boundaries"@en .


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
                               rdfs:subClassOf qm:Uncategorized ;
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
                                 rdfs:subClassOf qm:Uncategorized ;
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
                              rdfs:subClassOf qm:IntegratedTherapeuticApproaches ;
                              rdfs:label "Humor as Cognitive Technology"@en .


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
                    rdfs:subClassOf qm:PsychologicalDysfunctionAndImbalance ;
                    rdfs:label "Imposter Syndrome"@en .


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
                   rdfs:subClassOf qm:CoreConceptsCategory ,
                                   qm:EpistemologicalChallenges ,
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
                                       rdfs:subClassOf qm:ExternalInfluence ;
                                       rdfs:label "Institutional Architecture Imposition"@en .


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
                       rdfs:label "Internal Cartography"@en .


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
                               rdfs:subClassOf qm:ExternalInfluence ;
                               rdfs:label "Learned Behavioral Repertoire"@en .


###  https://tuos.org/qm#LiberationFromInheritedScripts
qm:LiberationFromInheritedScripts rdf:type owl:Class ;
                                  rdfs:subClassOf qm:MainStrategiesCategory ;
                                  rdfs:comment "A specific pathway focused on transcending pervasive external conditioning (Inherited Scripts) to foster genuine Authentic Self-Origination."@en ;
                                  rdfs:label "Liberation from Inherited Scripts"@en .


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
          rdfs:subClassOf qm:Uncategorized .


###  https://tuos.org/qm#MentalFilesystemOrganization
qm:MentalFilesystemOrganization rdf:type owl:Class ;
                                rdfs:subClassOf qm:CognitiveStructuringApproaches ;
                                rdfs:label "Mental Filesystem Organization"@en .


###  https://tuos.org/qm#MentalFlexibility
qm:MentalFlexibility rdf:type owl:Class ;
                     rdfs:subClassOf qm:CognitiveCapacity ;
                     rdfs:label "Mental Flexibility"@en .


###  https://tuos.org/qm#MentalPhysicalInterface
qm:MentalPhysicalInterface rdf:type owl:Class ;
                           rdfs:subClassOf qm:Uncategorized ;
                           rdfs:comment "A function facilitating the bidirectional flow and embodiment of psychological states and somatic awareness."@en ;
                           rdfs:label "Mental-Physical Interface"@en .


###  https://tuos.org/qm#MentalQuanta
qm:MentalQuanta rdf:type owl:Class ;
                rdfs:subClassOf qm:Uncategorized ;
                rdfs:comment "Fundamental units of cognitive or experiential possibility that compose the state of Cognitive Superposition."@en ;
                rdfs:label "Mental Quanta"@en .


###  https://tuos.org/qm#MentalState
qm:MentalState rdf:type owl:Class ;
               rdfs:subClassOf qm:Uncategorized ;
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
                                    rdfs:subClassOf qm:StandardizedProtocol ;
                                    rdfs:label "Mindfulness-Based Cognitive Therapy (MBCT)"@en .


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
                      rdfs:subClassOf qm:Uncategorized ;
                      rdfs:comment "The authentic, self-originated unfolding of an individual's potential."@en ;
                      rdfs:label "Natural Development"@en .


###  https://tuos.org/qm#NeurologicalEmbedding
qm:NeurologicalEmbedding rdf:type owl:Class ;
                         rdfs:subClassOf qm:ConditioningMechanism ;
                         rdfs:label "Repetition and Neurological Embedding"@en .


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
                         rdfs:subClassOf qm:EpistemologicalChallenges ;
                         rdfs:label "Observer Effect Paradox"@en .


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
                rdfs:subClassOf qm:ObserverParticipantDynamic ;
                rdfs:label "Observer Role"@en .


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
                           rdfs:subClassOf qm:CollapseInfluencePractice ;
                           rdfs:label "Ontological Reassignment"@en .


###  https://tuos.org/qm#OntologicalRestructuring
qm:OntologicalRestructuring rdf:type owl:Class ;
                            rdfs:subClassOf qm:PracticesCategory ;
                            rdfs:label "Ontological Restructuring"@en .


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
                      rdfs:subClassOf qm:ConditioningMechanism ;
                      rdfs:label "Osmotic Integration"@en .


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
                     rdfs:subClassOf qm:PerceptualGoal ;
                     rdfs:label "Perceptual Mastery"@en .


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
                                                            qm:PersonalTendency ;
                                            rdfs:label "Personal Tendency (Cognitive Responsiveness - wCj)"@en .


###  https://tuos.org/qm#PersonalTendency_MoodPersistence
qm:PersonalTendency_MoodPersistence rdf:type owl:Class ;
                                    rdfs:subClassOf qm:PersonalTendency ;
                                    rdfs:label "Personal Tendency (Mood Persistence - wS)"@en ,
                                               "Personal Tendency (Mood Persistence - wS)" .


###  https://tuos.org/qm#PersonalTendency_ObservationReactivity
qm:PersonalTendency_ObservationReactivity rdf:type owl:Class ;
                                          rdfs:subClassOf qm:DimensionalActivationInfluencesCategory ,
                                                          qm:PersonalTendency ;
                                          rdfs:label "Personal Tendency (Observation Reactivity - wΨj)"@en .


###  https://tuos.org/qm#PersonalTendency_Persistence
qm:PersonalTendency_Persistence rdf:type owl:Class ;
                                rdfs:subClassOf qm:DimensionalActivationInfluencesCategory ,
                                                qm:PersonalTendency ;
                                rdfs:label "Personal Tendency (Dimensional Persistence - wSj)"@en .


###  https://tuos.org/qm#PersonalTendency_Reactivity
qm:PersonalTendency_Reactivity rdf:type owl:Class ;
                               rdfs:subClassOf qm:PersonalTendency ;
                               rdfs:label "Personal Tendency (Reactivity to New Events - wΨ)"@en ,
                                          "Personal Tendency (Reactivity - wΨ)" .


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
                      rdfs:subClassOf qm:AestheticPrinciple ;
                      rdfs:label "Principle of Balance"@en .


###  https://tuos.org/qm#PrincipleOfLimit
qm:PrincipleOfLimit rdf:type owl:Class ;
                    rdfs:subClassOf qm:ProtectivePrinciple ;
                    rdfs:label "Principle of Limit"@en .


###  https://tuos.org/qm#PrincipleOfMeasure
qm:PrincipleOfMeasure rdf:type owl:Class ;
                      rdfs:subClassOf qm:ProtectivePrinciple ;
                      rdfs:label "Principle of Measure"@en .


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
                           rdfs:label "Proactive Self-Regulation"@en .


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
                         rdfs:subClassOf qm:PerceptualShapingTechnique ;
                         rdfs:label "Probabilistic Steering"@en .


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
                       rdfs:subClassOf qm:Uncategorized ;
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
                            rdfs:subClassOf qm:Phenomenon ;
                            rdfs:label "Psycho-Volitional Dynamics"@en .


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
                      rdfs:subClassOf qm:Uncategorized ;
                      rdfs:comment "A role serving crucial regulatory functions that maintain psychological coherence and prevent systemic fragmentation."@en ;
                      rdfs:label "Psychological Heart"@en .


###  https://tuos.org/qm#PsychologicalPhenomenon
qm:PsychologicalPhenomenon rdf:type owl:Class ;
                           rdfs:subClassOf qm:OtherKeyConcepts ;
                           rdfs:comment "A general category for the experiential and behavioral manifestations that are shaped by Psychodynamic Dimensions."@en ;
                           rdfs:label "Psychological Phenomenon"@en .


###  https://tuos.org/qm#PsychologicalSelfSurgery
qm:PsychologicalSelfSurgery rdf:type owl:Class ;
                            rdfs:subClassOf qm:PracticesCategory ;
                            rdfs:label "Psychological Self-Surgery"@en .


###  https://tuos.org/qm#PsychologicalState
qm:PsychologicalState rdf:type owl:Class ;
                      rdfs:subClassOf qm:Uncategorized ;
                      rdfs:comment "Complex emergent patterns (e.g., anxiety, joy) understood not as monolithic entities but as multi-dimensional field collapses involving specific combinations and interactions of underlying Psychodynamic Dimensions."@en ;
                      rdfs:label "Psychological State"@en .


###  https://tuos.org/qm#PsychologicalStructure
qm:PsychologicalStructure rdf:type owl:Class ;
                          rdfs:subClassOf qm:Uncategorized ;
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
                    rdfs:subClassOf qm:Uncategorized ;
                    rdfs:comment "The capacity to form relationships characterized by trust, emotional attunement, and mutual support."@en ;
                    rdfs:label "Relational Health"@en .


###  https://tuos.org/qm#RelationalMindfulness
qm:RelationalMindfulness rdf:type owl:Class ;
                         rdfs:subClassOf qm:CollapseInfluencePractice ;
                         rdfs:label "Relational Mindfulness"@en .


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
                                     rdfs:subClassOf qm:CognitiveOptimization ;
                                     rdfs:label "Reverse Engineering Emotional States"@en .


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
                         rdfs:subClassOf qm:Uncategorized ;
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
                 rdfs:subClassOf qm:Uncategorized ;
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
                   rdfs:subClassOf qm:InfluentialFactor ;
                   rdfs:label "Social Influence"@en .


###  https://tuos.org/qm#SomaticLiteracy
qm:SomaticLiteracy rdf:type owl:Class ;
                   rdfs:subClassOf qm:PerceptualGoal ;
                   rdfs:comment "The cultivated capacity to read and work with the subtle energies of consciousness as manifested in the body."@en ;
                   rdfs:label "Somatic Literacy"@en .


###  https://tuos.org/qm#SovereignArchitecture
qm:SovereignArchitecture rdf:type owl:Class ;
                         rdfs:subClassOf qm:Uncategorized ;
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
                                            rdfs:subClassOf qm:CognitiveOptimization ;
                                            rdfs:label "Strategic Cognitive Trajectory Manipulation"@en .


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
                           rdfs:subClassOf qm:PracticesCategory ;
                           rdfs:label "Structural Introspection"@en .


###  https://tuos.org/qm#StructuredUnderstanding
qm:StructuredUnderstanding rdf:type owl:Class ;
                           rdfs:subClassOf qm:Uncategorized ,
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
                        rdfs:subClassOf qm:PracticesCategory ;
                        rdfs:label "System Deconstruction"@en .


###  https://tuos.org/qm#TacitKnowledge
qm:TacitKnowledge rdf:type owl:Class ;
                  rdfs:subClassOf qm:Phenomenon ;
                  rdfs:label "Tacit Knowledge"@en .


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
                                    rdfs:subClassOf qm:EpistemologicalChallenges ;
                                    rdfs:label "Translation Challenge in Psychology"@en .


###  https://tuos.org/qm#TranslationFatigue
qm:TranslationFatigue rdf:type owl:Class ;
                      rdfs:subClassOf qm:CognitiveStrainAndDysfunction ;
                      rdfs:label "Translation Fatigue"@en .


###  https://tuos.org/qm#TraumaticCollapse
qm:TraumaticCollapse rdf:type owl:Class ;
                     rdfs:subClassOf qm:UnconsciousReactiveCollapse ;
                     rdfs:label "Traumatic Collapse"@en .


###  https://tuos.org/qm#Uncategorized
qm:Uncategorized rdf:type owl:Class .


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
        rdfs:subClassOf qm:PsychoVolitionalDimension ;
        rdfs:label "Will"@en .


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
                   rdfs:subClassOf qm:InfluentialFactor ;
                   rdfs:label "Zeigarnik Effect"@en .


#################################################################
#    Individuals
#################################################################

###  https://tuos.org/qm#CalculatedTurbulence
qm:CalculatedTurbulence rdf:type owl:NamedIndividual .


###  https://tuos.org/qm#CognitiveAppraisal
qm:CognitiveAppraisal rdf:type owl:NamedIndividual .


###  https://tuos.org/qm#CognitiveInfluence
qm:CognitiveInfluence rdf:type owl:NamedIndividual .


###  https://tuos.org/qm#Contemplation
qm:Contemplation rdf:type owl:NamedIndividual .


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


###  https://tuos.org/qm#ObservationValence
qm:ObservationValence rdf:type owl:NamedIndividual .


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


###  https://tuos.org/qm#QM_Quantum
qm:QM_Quantum rdf:type owl:NamedIndividual .


###  https://tuos.org/qm#ResolutionFatigue
qm:ResolutionFatigue rdf:type owl:NamedIndividual .


###  https://tuos.org/qm#RighteousAnger
qm:RighteousAnger rdf:type owl:NamedIndividual ;
                  qm:emergesFromInteractionOf qm:Pd4 ,
                                              qm:Pd5 ,
                                              qm:Pd6 ;
                  rdfs:comment "An emergent psychological state arising from the interaction of compassionate identification, boundary judgment, and the recognition of a violation of moral beauty."@en ;
                  rdfs:label "Righteous Anger"@en .


###  https://tuos.org/qm#SigmoidFunction
qm:SigmoidFunction rdf:type owl:NamedIndividual .


###  https://tuos.org/qm#TheTransitionalModalities
qm:TheTransitionalModalities rdf:type owl:NamedIndividual ,
                                      qm:TransitionalModalities ;
                             qm:composedOf qm:Pd7 ,
                                           qm:Pd8 ,
                                           qm:Pd9 ;
                             rdfs:label "The Transitional Modalities (Pd7-9)"@en .


[ rdfs:comment "Formal Equation: C = wΨ ⋅ Valence(Ψ) + wS ⋅ AvgValence(S_t-1) + Bias_M1"@en
] .

[ rdfs:comment "Formal Equation: Kj = I_Sj + I_Cj + I_Tj + I_Ψj + εj"@en
 ] .

[ rdfs:comment "The formal equation Kj = I_Sj + I_Cj + I_Tj + I_Ψj + εj signifies that the total activation emerges from the confluence of these multiple, distinct influences."@en
 ] .

[ rdfs:comment "Formal Equation: Ψ = α(β + 1)(A + f)"@en
 ] .

[ rdfs:comment "The formal equation Ψ = α(β + 1)(A + f) underscores that these components are interdependent and contribute synergistically to the overall strength of the Observation."@en
 ] .

[ rdfs:comment "Aims to neutralize a negative Cognitive Appraisal by reducing reactivity (lowering wΨ and wS) and observing without judgment (pushing Valence(Ψ) toward zero)."@en
 ] .

[ rdfs:comment "Aims to neutralize a negative Cognitive Influence by reducing reactivity (lowering wΨ and wS) and observing without judgment (pushing Valence(Ψ) to zero)."@en
 ] .

[ rdfs:comment "Aims to actively make the Cognitive Appraisal positive by altering Valence(Ψ) through reframing and, more profoundly, by altering the baseline Bias_M1 over time."@en
 ] .

[ rdfs:comment "Formal Equation: S = Σ(xj * Pdj) for j=1 to 10. Represents the mental state as a vector in the 'space' of psychodynamic dimensions."@en
 ] .

[ rdfs:comment "Formal Equation: S = Σ(xj * Pdj) for j=1 to 10. This represents the mental state as a vector in the 'space' of psychodynamic dimensions."@en
 ] .

[ rdfs:comment "The formal equation C = wΨ ⋅ Valence(Ψ) + wS ⋅ AvgValence(S_t-1) + Bias_M1 encapsulates the complex interplay of these factors."@en
 ] .

[ rdfs:comment "Aims to actively ensure the Cognitive Influence becomes positive by altering Valence(Ψ) through reframing and, more profoundly, by altering the baseline Bias_M1."@en
 ] .

#################################################################
#    Annotations
#################################################################

qm:CalculatedTurbulence rdfs:comment "The optimal state of balance, conceived as a dynamic equilibrium where the dimensions remain actively engaged and responsive within productive thresholds."@en ;
                         rdfs:label "Calculated Turbulence"@en .


qm:CognitiveAppraisal rdfs:comment "The mind's primary, high-level judgment or interpretation of an observed phenomenon, undertaken by the Prime Modality. It functions as a 'master control signal' or 'prime directive' that provides the overarching directional impetus for the subsequent Psychodynamic Collapse. It is a dynamic, potentially iterative process."@en ,
                                   "The mind's primary, high-level judgment or interpretation of an observed phenomenon, undertaken by the Prime Modality. It functions as a 'master control signal' that provides the overarching directional impetus for the subsequent Psychodynamic Collapse. Its value is a weighted sum of three distinct forces."@en ,
                                   "The pivotal 'master control signal' or 'prime directive' that translates a complex observation into a single, high-level judgment, driving the activation of the ten Psychodynamic Dimensions."@en ,
                                   "The pivotal 'master control signal' or 'prime directive' that translates a complex observation into a single, high-level judgment, driving the activation of the ten Psychodynamic Dimensions. It is determined by the observation's valence, the previous mental state, and an inherent bias from the Prime Modality."@en ;
                      rdfs:label "Cognitive Appraisal (C)"@en ,
                                 "Cognitive Appraisal (C)" ;
                      rdfs:subClassOf "Psychodynamic Model"@en ,
                                      "Psychodynamic Model, Cognitive Influence Model"@en .


qm:CognitiveInfluence rdfs:comment "Represents the direct impact of the overall Cognitive Appraisal (C) on the activation of a dimension."@en ,
                                   "Represents the direct impact of the overall Cognitive Appraisal (C) on the activation of a specific dimension (ICj = wCj ⋅ C)."@en ,
                                   "Represents the direct impact of the overall Cognitive Appraisal (C) on the activation of a specific dimension (ICj = wCj ⋅ C). It addresses: 'How much does my overall judgment of this situation influence this specific feeling?'. This is a key intervention point for both Classical and Quantum Mindfulness."@en ;
                      rdfs:label "Cognitive Influence (ICj)"@en ,
                                 "Cognitive Influence (ICj)" .


qm:Contemplation rdfs:comment "An active, deliberate cognitive process involving sustained, rigorous mental work to transform potential into Structured Understanding. It is integral to conscious awareness and instrumental in processing all conscious experience."@en ,
                              "An active, deliberate cognitive process involving sustained, rigorous mental work to transform raw cognitive potential into structured understanding. It is crucial for psycho-meditative collapse and complements foundational mindfulness."@en .


qm:Memory rdfs:label "Memory (Explicit and Implicit)"@en .


qm:ObservationValence rdfs:comment "The subjective emotional coloring or the numeric rating of positivity or negativity that the mind assigns to a specific observation. This valence is a crucial output of the perceptual and interpretive process and provides the 'Impact of the Now' component for the Cognitive Appraisal."@en ;
                      rdfs:label "Observation Valence (Valence(Ψ))"@en ,
                                 "Observation Valence (Valence(Ψ))" .


qm:ResolutionFatigue rdfs:comment "A profound form of cognitive strain where the mind's capacity to form definite mental states from possibilities is compromised, often due to external inputs overwriting internal signals."@en ;
                     rdfs:label "Resolution Fatigue"@en .


qm:SigmoidFunction rdfs:comment "A mathematical function used to transform the raw Dimensional Activation (Kj) into a normalized Final Intensity (xj) between 0 and 1. It is chosen for its non-linearity and threshold-like behavior, which mirrors psychological phenomena."@en ,
                                "A mathematical function used to transform the raw Dimensional Activation (Kj) into a normalized Final Intensity (xj) between 0 and 1. It is chosen for its properties of normalization, non-linearity, and its threshold-like behavior, which accurately model how psychological phenomena manifest."@en ;
                   rdfs:label "Sigmoid Function"@en ,
                              "Sigmoid Function" ;
                   rdfs:subClassOf "Psychodynamic Model"@en .

#################################################################
#    Additional Annotations for Conceptual Clarification
#################################################################

###  Annotations for qm:CognitiveSuperposition
<https://tuos.org/qm#CognitiveSuperposition>
    rdfs:comment """This class describes the state of pre-conscious mental potential. It is crucial to distinguish this from the physical principle; here, it is a conceptual tool to model the psyche's capacity to hold multiple, unresolved possibilities before an act of conscious attention."""@en ;
    skos:definition """The term 'superposition' is used here in a conceptual sense, derived from its Latin roots 'super-' (above) and 'positio' (to place), signifying multiple potentials being 'placed' in the same conceptual space. It describes a foundational pre-conscious state where multiple potential thoughts or perceptions coexist as a dynamic probability field. The term is thus used as a precise analogy for this state of unresolved mental potential, which precedes the 'collapse' into a single conscious thought."""@en .


###  Annotations for qm:PsychodynamicWaveCollapse
<https://tuos.org/qm#PsychodynamicWaveCollapse>
    rdfs:comment """This class represents the pivotal process where the mind's probabilistic field resolves into a specific, actualized experience."""@en ;
    skos:definition """Grounded in the general meaning of 'collapse'—to fall together into a more compact or definite state—this term describes the fundamental psychological transition from potential to actuality. Within this framework, it is the specific process by which the 'wave' of multiple mental possibilities (defined in qm:CognitiveSuperposition) resolves into a singular, definite, and consciously experienced outcome, triggered by an act of attention."""@en .


###  Annotations for qm:ConsciousnessWaveFunction
<https://tuos.org/qm#ConsciousnessWaveFunction>
    rdfs:comment """This class provides a conceptual label for the field in which mental potential exists. This is an abstract psychological concept, not a mathematical formula in the physical sense."""@en ;
    skos:definition """This term is constructed from its constituent parts to form a conceptual label. A 'function' describes a relationship between inputs and outputs, and a 'wave' represents a state of fluctuation and potential. The framework combines these to define the 'Consciousness Wave Function' as the conceptual space or probabilistic field  that contains the full range of potential mental states before they are actualized through psychodynamic collapse."""@en .


###  Annotations for qm:PsychologicalEntanglement
<https://tuos.org/qm#PsychologicalEntanglement>
    rdfs:comment """This class models the principle of deep and persistent interconnectedness between psychological systems, which may not be immediately obvious or causal in a linear sense."""@en ;
    skos:definition """Drawing from the general meaning of 'entanglement'—to be intricately intertwined or connected—this framework uses the term to describe a state of deep psychological interconnection. For example, qm:EmotionalQuantumEntanglement is defined as the persistent interconnectedness of mental and emotional states between individuals. The term is used as a powerful metaphor to describe profound, non-local connections that operate beyond direct perception."""@en .


###  Annotations for qm:InterferencePatterns
<https://tuos.org/qm#InterferencePatterns>
    rdfs:comment """This class describes the emergent effects of combined psychodynamic dimensions, which can either amplify or diminish each other."""@en ;
    skos:definition """The term 'interference' is used in its general sense of one process affecting, modifying, or canceling another. In this ontology, it describes how the 'waves' of different psychodynamic dimensions interact. This can result in 'Constructive Interference,' where dimensions align to amplify positive qualities , or 'Destructive Interference,' where they conflict and create internal dissonance."""@en .

<https://tuos.org/qm#QM_Quantum>
    rdfs:comment """The conceptual principle that subjective experience is not a continuous phenomenon, but is constituted by identifiable, discrete psychodynamic dimensions. This term is used conceptually to describe distinct experiential configurations, not a model of brain computation."""@en ;
    skos:definition """Grounded in its Latin origin 'quantus' (meaning 'how much' or 'an amount'), a 'quantum' in this framework is the smallest discrete amount or fundamental unit of the psychic architecture. While rooted in this primary definition, the framework extends this concept by creating a powerful psychological analogy with concepts from quantum physics. It uses related principles like 'superposition' (qm:CognitiveSuperposition) and 'collapse' (qm:PsychodynamicCollapse) to build a novel model of how the mind works, contrasting it with continuous models of mentation."""@en .