# Prompting chain: from ideated indicators to specific examples

# Prompt

The following lists are objective signs of degrading and improving bilateral relations.

Your tasks are as follows:

1) Reformat each list as a markdown table  
2) Within each lsit, divide the indicators into three categories: low, moderate, high. The severity ranks how significant that indicator is to the overall worsening or improving of bilateral ties.

Here are the lists:

## **Signs Indicating Degrading Bilateral Relations**
- Imposition of sanctions or trade embargoes by one country on another.
- Recall of ambassadors or diplomatic staff.
- Public accusations or hostile rhetoric by government officials.
- Military confrontations or increased military presence near shared borders or contested regions.
- Withdrawal from bilateral agreements or treaties.
- Suspension of cultural, educational, or scientific exchange programs.
- Restrictions on visas for citizens of the other country.
- Cyberattacks attributed to the other country.
- Reduction in trade volumes due to deliberate policies.
- Closure of consulates or embassies.

## **Signs Indicating Warming Bilateral Relations**
- Establishment or restoration of formal diplomatic ties.
- High-level state visits between heads of state or senior officials.
- Signing new bilateral agreements, such as trade deals, defense pacts, or cooperation frameworks.
- Launching joint cultural, educational, or scientific initiatives.
- Increased trade volumes and investment flows between the two countries.
- Mutual reduction in tariffs and other trade barriers.
- Opening new embassies, consulates, or cultural centers in each other's territories.
- Joint military exercises or security collaborations.
- Public statements emphasizing mutual respect and shared goals.
- Participation in multilateral forums with coordinated positions. 

# Output

### **Signs Indicating Degrading Bilateral Relations**

| **Severity** | **Indicators**                                                                                     |
|--------------|---------------------------------------------------------------------------------------------------|
| **High**     | - Imposition of sanctions or trade embargoes by one country on another                            |
|              | - Military confrontations or increased military presence near shared borders or contested regions |
|              | - Cyberattacks attributed to the other country                                                    |
|              | - Closure of consulates or embassies                                                              |
| **Moderate** | - Recall of ambassadors or diplomatic staff                                                       |
|              | - Public accusations or hostile rhetoric by government officials                                  |
|              | - Withdrawal from bilateral agreements or treaties                                               |
|              | - Restrictions on visas for citizens of the other country                                        |
|              | - Reduction in trade volumes due to deliberate policies                                          |
| **Low**      | - Suspension of cultural, educational, or scientific exchange programs                            |

---

### **Signs Indicating Warming Bilateral Relations**

| **Severity** | **Indicators**                                                                                     |
|--------------|---------------------------------------------------------------------------------------------------|
| **High**     | - Establishment or restoration of formal diplomatic ties                                          |
|              | - High-level state visits between heads of state or senior officials                              |
|              | - Signing new bilateral agreements, such as trade deals, defense pacts, or cooperation frameworks |
|              | - Increased trade volumes and investment flows between the two countries                         |
|              | - Public statements emphasizing mutual respect and shared goals                                   |
| **Moderate** | - Launching joint cultural, educational, or scientific initiatives                                |
|              | - Mutual reduction in tariffs and other trade barriers                                           |
|              | - Opening new embassies, consulates, or cultural centers in each other's territories             |
|              | - Joint military exercises or security collaborations                                            |
|              | - Participation in multilateral forums with coordinated positions                                |
| **Low**      | *(No indicators listed)*                                                                         |

 # Prompt

 The following tables lists signs of warming or degrading bilateral ties and rates them by severity.

 Your task:

 Find examples of such incidents from the international relations of the State of Israel from Jan 1st 2023 through to the present.

 For each example:

 - Describe the incident
 - State which country (or countries) were affected, citing both their names and ISO-3166 alpha 2 identifiers  
 - State the "ranking" of the incident according to the reference grid.

Here's the reference grid:

| **Severity** | **Indicators**                                                                                     |
|--------------|---------------------------------------------------------------------------------------------------|
| **High**     | - Imposition of sanctions or trade embargoes by one country on another                            |
|              | - Military confrontations or increased military presence near shared borders or contested regions |
|              | - Cyberattacks attributed to the other country                                                    |
|              | - Closure of consulates or embassies                                                              |
| **Moderate** | - Recall of ambassadors or diplomatic staff                                                       |
|              | - Public accusations or hostile rhetoric by government officials                                  |
|              | - Withdrawal from bilateral agreements or treaties                                               |
|              | - Restrictions on visas for citizens of the other country                                        |
|              | - Reduction in trade volumes due to deliberate policies                                          |
| **Low**      | - Suspension of cultural, educational, or scientific exchange programs                            |

---

### **Signs Indicating Warming Bilateral Relations**

| **Severity** | **Indicators**                                                                                     |
|--------------|---------------------------------------------------------------------------------------------------|
| **High**     | - Establishment or restoration of formal diplomatic ties                                          |
|              | - High-level state visits between heads of state or senior officials                              |
|              | - Signing new bilateral agreements, such as trade deals, defense pacts, or cooperation frameworks |
|              | - Increased trade volumes and investment flows between the two countries                         |
|              | - Public statements emphasizing mutual respect and shared goals                                   |
| **Moderate** | - Launching joint cultural, educational, or scientific initiatives                                |
|              | - Mutual reduction in tariffs and other trade barriers                                           |
|              | - Opening new embassies, consulates, or cultural centers in each other's territories             |
|              | - Joint military exercises or security collaborations                                            |
|              | - Participation in multilateral forums with coordinated positions                                |
| **Low**      | *(No indicators listed)*                                                                         |

# Output

## Degrading indicators, examples:

| **Incident Description**                                                                 | **Affected Countries**                            | **Severity** |
|------------------------------------------------------------------------------------------|--------------------------------------------------|--------------|
| Hamas's coordinated attack on Israel on October 7, 2023                                 | Israel (IL), Palestine (PS)                      | High         |
| Strained relations with Russia over Israel-Gaza war                                     | Israel (IL), Russia (RU)                         | High         |
| Strained relations with China over Palestine support                                    | Israel (IL), China (CN), Palestine (PS)          | High         |
| Strained relations with Turkey over Gaza conflict                                       | Israel (IL), Turkey (TR)                         | High         |
| Strained relations with Egypt due to Gaza conflict and displacement concerns            | Israel (IL), Egypt (EG)                          | High         |
| Strained relations with Iran over multiple attacks                                      | Israel (IL), Iran (IR), Lebanon (LB), Syria (SY) | High         |

## Warming indicators, examples:

| **Incident Description**                                                                                 | **Affected Countries**                            | **Severity** |
|----------------------------------------------------------------------------------------------------------|--------------------------------------------------|--------------|
| The UAE reaffirmed its commitment to the Abraham Accords despite regional tensions over the Gaza conflict. | Israel (IL), United Arab Emirates (AE)           | High         |
| Signing of a free trade agreement between Israel and the UAE, strengthening economic ties.               | Israel (IL), United Arab Emirates (AE)           | High         |
| UAE's reliance on Israeli air defense systems to protect against Houthi missile threats.                 | Israel (IL), United Arab Emirates (AE)           | High         |
| China acknowledged Israel's "reasonable security concerns" in a shift toward balanced rhetoric.          | Israel (IL), China (CN)                          | Moderate     |
| Continued U.S.-Israel cooperation under a 10-year military aid agreement, including joint missile defense programs. | Israel (IL), United States (US)                  | High         |
| Ongoing normalization efforts under the Abraham Accords with countries like Bahrain and Morocco.         | Israel (IL), Bahrain (BH), Morocco (MA)          | High         |