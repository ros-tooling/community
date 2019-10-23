# Working Group Governance

(note - most of this is adapted from the Kubernetes governance documents)

This document proposes an **opt-in** (i.e. non-mandatory) governance model for ROS 2 working groups. An example of working group following this governance model is the [ROS 2 Tooling Working Group](https://quip-amazon.com/a5poAx4jFDX0/ROS-2-Tooling-Working-Group-Proposal).

# Working Groups

The ROS 2 project is organized into Working Groups. Each working group is composed of members from multiple companies and organizations, with a common purpose of advancing the project with respect to a specific topic, such as Security or Navigation. Our goal is to enable a distributed decision structure and code ownership, as well as providing focused forums for getting work done, making decisions, and onboarding new contributors. Every identifiable subpart of the project (e.g., github org, repository, subdirectory, API, test, issue, PR) is intended to be owned by some working group.

Areas covered by working groups may be vertically focused on particular components or functions, cross-cutting/horizontal, spanning many/all functional areas of the project, or in support of the project itself. Examples:

* Vertical: Localization, Perception, Motion Planning, Control, Tooling
* Horizontal: Security, Performance, Real-Time, Safety
* Project: Testing, Release, Docs, PM, Contributor Experience

Working Groups must have at least one and ideally two Working Groups chairs at any given time. Working Group chairs are intended to be organizers and facilitators, responsible for the operation of the Working Group and for communication and coordination with the other Working Groups, the Steering Committee, and the broader community.

Each Working Group must have a charter that specifies its scope (topics, subsystems, code repos and directories), responsibilities, areas of authority, how members and roles of authority/leadership are selected/granted, how decisions are made, and how conflicts are resolved. See the Working Group charter process for details on how charters are managed. Working Groups should be relatively free to customize or change how they operate, within some broad guidelines and constraints imposed by cross-Working Group processes (e.g., the release process) and assets (e.g., the ros2 organization).

A primary reason that Working Groups exist is as forums for collaboration. Much of the work in a Working Group should stay local within that Working Group. However, Working Groups must communicate in the open, ensure other Working Groups and community members can find notes of meetings, discussions, designs, and decisions, and periodically communicate a high-level summary of the Working Group work to the community.
See Working Group governance for more details about current Working Group operating mechanics, such as communication channels, meeting times, etc.

### Subprojects

Specific work efforts within WG are divided into subprojects. Every part of the ROS2 code and documentation should be owned by some subproject. Some WGs may have a single subproject, but WG can also have multiple significant subprojects with distinct (though sometimes overlapping) sets of contributors and [owners](https://github.com/kubernetes/community/blob/master/community-membership.md#subproject-owner), who act as subproject’s technical leaders: responsible for vision and direction and overall design, choose/approve change proposal (REP) approvers, field technical escalations, etc.

Example subprojects for a few WGs:

* WG Security: sros2
* WG Navigation: navigation2
* FIXME: add more once WGs have been established.

Subprojects for each WG are documented in working groups README pages.

# Working Group Roles and Organizational Governance

In order to standardize working group efforts, create maximum transparency, and route contributors to the appropriate WG, WGs should follow these guidelines:

* Create a charter and have it approved according to the [WG charter process](https://quip-amazon.com/F3IUAzfpEzh5/Working-Group-Governance-wg-governance#bUU9CAmzib7)
* Meet regularly, at least for 30 minutes every month, except November and December
* Keep up-to-date meeting notes, linked from the WG's page in the community repo
* Record meetings and make them publicly available on a YouTube playlist
* Ensure related work happens in a project-owned github org and repository, with code and tests explicitly owned and supported by the WG, including issue triage, PR reviews, test-failure response, bug fixes, etc.
* Use the WG forums as the primary means of working, communicating, and collaborating, as opposed to private emails and meetings

## Roles

### Notes on Roles

Within this section "member" refers to a member of a Chair, Tech Lead or Subproject Owner Role.

* Initial members are defined at the founding of the WG or Subproject as part of the acceptance of that WG or Subproject.

* Members *SHOULD* remain active and responsive in their Roles.
* Members *MUST* be [community members] to be eligible to hold a leadership role within a WG.

* Members taking an extended leave of 1 or more months *SHOULD* coordinate with other members to ensure the role is adequately staffed during the leave.

* Members going on leave for 1-3 months *MAY* work with other members to identify a temporary replacement.

* Members of a role *SHOULD* remove any other members that have not communicated a leave of absence and either cannot be reached for more than 1 month or are not fulfilling their documented responsibilities for more than 1 month. This may be done through a [super-majority](https://en.wikipedia.org/wiki/Supermajority#Two-thirds_vote) vote of members.

* Membership disagreements may be escalated to the WG Chairs.  WG Chair membership disagreements may be escalated to the Steering Committee.

* Members *MAY* decide to step down at anytime and propose a replacement.  Use [lazy consensus](http://en.osswiki.info/concepts/lazy_consensus) amongst other members with fallback on majority vote to accept proposal. The candidate *SHOULD* be supported by a majority of WG Members or subproject contributors.

* Members *MAY* select additional members through a  [super-majority](https://en.wikipedia.org/wiki/Supermajority#Two-thirds_vote) vote amongst members. This *SHOULD* be supported by a majority of WG Members.

### Chair

* Chair
    * Run operations and processes governing the WG
    * Establish new subprojects
    * Decommission existing subprojects
    * Resolve cross-Subproject technical issues and decisions
    * Escalation points for all WG subprojects
    * Number: 2-3
    * Membership tracked in the WG README

### Subproject Owner

* Subproject Owners
    * Scoped to a subproject defined in the WG README page
    * Seed members established at subproject founding
    * *SHOULD* be an escalation point for technical discussions and decisions in the subproject
    * *SHOULD* set milestone priorities or delegate this responsibility
    * Number: 2-3 per subproject
    * Membership tracked in the WG README page

### Member

* Members
    * *SHOULD* maintain health of at least one subproject or the health of the WG
    * *SHOULD* show sustained contributions to at least one subproject or to the WG
    * *SHOULD* hold some documented role or responsibility in the WG (e.g. reviewer, approver, etc - see community membership below)

    * *MAY* build new functionality for subprojects
    * *MAY* participate in decision making for the subprojects they hold roles in
    * Includes all reviewers and approvers in WG subprojects repositories
    * Membership tracked in the WG README

## Organizational Management

* WG meets monthly with agenda in meeting notes
* *SHOULD* be facilitated by chairs unless delegated to specific Members

## Subproject Creation

* Subprojects may be created by [REP](https://www.ros.org/reps/rep-0000.html) proposal and accepted by [lazy consensus](http://en.osswiki.info/concepts/lazy_consensus) with fallback on majority vote of subproject owners in the WG.  The result *SHOULD* be supported by the majority of members.
* WG README *MUST* be updated to include project information

Projects SHOULD create repos under *github.com/ros2-wgs* through [lazy consensus](http://en.osswiki.info/concepts/lazy_consensus) of WG members.

* Projects must define how releases are performed and milestones are set.  Example:

>  - Release milestones
  - Follows the ROS 2 release milestones and schedule
  - Priorities for upcoming release are discussed during the WG meeting following the preceding release and
    shared through a PR. Priorities are finalized before feature freeze.
- Code and artifacts are published as a Bloom package



### Technical processes

Subprojects of the WG *MUST* use the following processes unless explicitly following alternatives
they have defined.

* Proposing and making decisions
    * Proposals sent as [REP](https://www.ros.org/reps/rep-0000.html) PRs and published to Discourse as announcement
    * Follow [REP](https://www.ros.org/reps/rep-0000.html) decision making process
* Test health
    * Canonical health of code published to <link to dashboard>
    * Consistently broken tests automatically send an alert to <link to google group>
    * WG members are responsible for responding to broken tests alert. PRs that break tests should be rolled back     if not fixed within 24 hours (business hours).

    * Test dashboard checked and reviewed at start of each WG meeting.  Owners assigned for any broken tests and followed up during the next WG meeting.

Issues impacting multiple subprojects in the WG should be resolved by WG Chairs.

### WG Retirement

* In the event that the WG is unable to regularly establish consistent quorum or otherwise fulfill its Organizational Management responsibilities

    * after 3 or more months it *SHOULD* be retired
    * after 6 or more months it *MUST* be retired

# Working Group Charter Guide


All ROS2 Working Groups must define a charter defining the scope and governance of the Working Group.

* The scope must define what areas the Working Group is responsible for directing and maintaining.
* The governance must outline the responsibilities within the Working Group as well as the roles owning those responsibilities.

### Steps to create a WG charter

1. Copy the working group main page template (see below) into a new file under `community/wg-*YOURWG*/README.md`
2. Copy the template (see below) into a new file under `community/wg-*YOURWG*/charter.md`
3. Read the [Recommendations and requirements](https://quip-amazon.com/F3IUAzfpEzh5/Working-Group-Governance-wg-governance#bUU9CAdZ0Eo) so you have context for the template
4. Fill out the templates for your WG
5. Create a pull request with a draft of your changes. Communicate it within your WG and get feedback as needed.
6. Send the WG Charter out for review to [info@openrobotics.org](mailto:info%40openrobotics.org). Include the subject "WG Charter Proposal: YOURWG“   and a link to the PR in the body.
7. Typically expect feedback within a week of sending your draft. Make any necessary changes.
8. Once accepted, the steering committee will ratify the PR by merging it.

### Steps to update an existing WG charter

* For significant changes, or any changes that could impact other WGs, such as the scope, create a PR and send it to the steering committee for review with the subject: "WG Charter Update: YOURWG“

* For minor updates to that only impact issues or areas within the scope of the WG the WG Chairs should facilitate the change.

### WG Charter approval process

When introducing a WG charter or modification of a charter the following process should be used.
As part of this we will define roles for the [OARP](https://stumblingabout.com/tag/oarp/) process (Owners, Approvers, Reviewers, Participants)

* Identify a small set of Owners from the WG to drive the changes. Most typically this will be the WG chairs.
* Work with the rest of the WG in question (Reviewers) to craft the changes.

  Make sure to keep the WG in the loop as discussions progress with the Steering Committee (next step).
  Including the WG mailing list in communications with the steering committee would work for this.

* Work with the steering committee (Approvers) to gain approval. This can simply be submitting a PR and sending mail to [info@openrobotics.org](mailto:info%40openrobotics.org). If more substantial changes are desired it is advisable to socialize those before drafting a PR.

    * The steering committee will be looking to ensure the scope of the WG as represented in the charter is reasonable (and within the scope of ROS2) and that processes are fair.
* For large changes alert the rest of the ROS2 community (Participants) as the scope of the changes becomes clear.

  Sending an announce on Discourse and/or announcing at the community meeting are good ways to do this.

If there are questions about this process please reach out to the steering committee at [info@openrobotics.org](mailto:info%40openrobotics.org).

### How to use the templates

WGs should use the template (see below) as a starting point. This document links to the recommended WG Governance but WGs may optionally record deviations from these defaults in their charter.

### Goals

The primary goal of the charters is to define the scope of the WG within ROS2 and how the WG leaders exercise ownership of these areas by taking care of their responsibilities. A majority of the effort should be spent on these concerns.

### WG README Template

```
# <working group> Working Group

<working group description>

The [charter](charter.md) defines the scope and governance of the <working group>.

## Meetings
* Regular WG Meeting: [Thursdays at 19:00 UTC](https://docs.google.com/document/d/FIXME/edit) (monthly). [Convert to your timezone](http://www.thetimezoneconverter.com/?t=19:00&tz=UTC).
  * [Meeting notes and Agenda](https://docs.google.com/document/d/FIXME/edit).
  * [Meeting recordings](https://www.youtube.com/playlist?list=FIXME).

## Leadership

### Chairs
The Chairs of the WG run operations and processes governing the WG.

* <first> <last> (**[@<GH Username>](https://github.com/<GH username>)**), <company>

## Contact
- Matrix: [#wg-<working group>](fixme)
- [Discourse Category](fixme)
- [Open Community Issues/PRs](https://github.com/ros2-wgs/community/labels/sig%2F<wg>)
- GitHub Teams:
    - [@ros2-wgs/wg-<working group>-api-reviews](https://github.com/orgs/ros2-wgs/teams/wg-<working group>-all) - Working Group Members

# Details about WG-<working group>

<add any additional information about the working group here>
```

### WG Charter Template

```
# WG YOURWG Charter

This charter adheres to the conventions described in the [ROS2 Charter README] and uses
the Roles and Organization Management outlined in [wg-governance].

## Scope

Include a 2-3 sentence summary of what work WG TODO does. Imagine trying to
explain your work to a colleague who is familiar with ROS2 but not
necessarily all of the internals.

### In scope

#### Code, Binaries and Nodes

- list of what qualifies a piece of code, binary or nodes
- as falling into the scope of this WG
- e.g. *ROS2 localization node*, 
- *CI for ROS2 repos*, etc
- **This is NOT** a list of specific code locations,

#### Cross-cutting and Externally Facing Processes

- list of the non-internal processes
- that are owned by this WG
- e.g. qualifying and cutting a ROS2 release,
- organizing mentorship programs, etc

### Out of scope

Outline of things that could be confused as falling into this WG
but don't or don't right now.

## Roles and Organization Management

This WG follows adheres to the Roles and Organization Management
outlined in [wg-governance]
and opts-in to updates and modifications to [wg-governance].

### Additional responsibilities of Chairs

- list of any additional responsibilities
- of Chairs

### Additional responsibilities of Tech Leads

- list of any additional responsibilities
- of Tech Leads

### Deviations from [wg-governance]

list of other ways this WG's roles and governance differ from the outline
```



# Working Group Governance Requirements

## Working Group Governance Requirements

### Goals

This document outlines the recommendations and requirements for defining WG governance.
This doc uses [rfc2119](https://www.ietf.org/rfc/rfc2119.txt) to indicate keyword requirement levels.
Sub elements of a list inherit the requirements of the parent by default unless overridden.

### Checklist

Following is the checklist of items that should be considered as part of defining governance for
any subarea of the ROS2 project.

**Roles**

* *MUST* enumerate any roles within the WG and the responsibilities of each
* *MUST* define process for changing the membership of roles
    * When and how new members are chosen / added to each role
    * When and how existing members are retired from each role
* *SHOULD* define restrictions / requirements for membership of roles
* *MAY* define target staffing numbers of roles

**Organizational Management**

* *MUST* define when and how collaboration between members of the WG is organized
* *SHOULD* define how periodic video conference meetings are arranged and run
* *SHOULD* define how conference / summit sessions are arranged
* *MAY* define periodic office hours on slack or video conference
* *MAY* define process for new community members to contribute to the area
    * e.g. read a contributing guide, show up at WG meeting, message the google group
* *MUST* define roles (and membership) within WGs

**Project Management**

The following checklist applies to WGs:

* *MUST* define how milestones / releases are set
    * How target dates for milestones / releases are proposed and accepted
    * What priorities are targeted for milestones
    * The process for publishing a release
* *SHOULD* define how priorities / commitments are managed
    * How priorities are determined
    * How priorities are staffed


**Technical Processes**

All technical assets *MUST* be owned by exactly 1 WG. The following checklist applies to WGs:

* *MUST* define how technical decisions are communicated and made within the WG or project
    * Process for proposal, where and how it is published and discussed, when and how a decision is made (e.g. [REP](https://www.ros.org/reps/rep-0000.html) process)

    * Who are the decision makers on proposals (e.g. anyone in the world can block, just reviewers on the PR, just approvers in OWNERs, etc)

    * How disagreements are resolved within the area (e.g. discussion, fallback on voting, escalation, etc)
    * How and when disagreements may be escalated
    * *SHOULD* define expectations and recommendations for proposal process (e.g. escalate if not progress towards resolution in 2 weeks)

    * *SHOULD* define a level of commitment for decisions that have gone through the formal process (e.g. when is a decision revisited or reversed)

* *MUST* define how technical assets of project remain healthy and can be released
    * Publicly published signals used to determine if code is in a healthy and releasable state
    * Commitment and process to *only* release when signals say code is releasable
    * Commitment and process to ensure assets are in a releasable state for milestones / releases coordinated across multiple areas (e.g. the ROS2 OSS release)

    * *SHOULD* define target metrics for health signal (e.g. broken tests fixed within N days)
    * *SHOULD* define process for meeting target metrics (e.g. all tests run as presubmit, build cop, etc)

# Community Membership

This document outlines the various responsibilities of contributor roles in ROS2. The ROS2 project is subdivided into subprojects under WGs. Responsibilities for most roles are scoped to these subprojects.


|Role	|Responsibilities	|Requirements	|Defined by	|
|---	|---	|---	|---	|
|member	|active contributor in the community	|sponsored by 2 reviewers.  multiple contributions to the project.	|ros2-wgs GitHub org member	|
|reviewer	|review contributions from other members	|history of review and authorship in a subproject	|WG README page	|
|approver	|approve accepting contributions	|highly experienced and active reviewer + contributor to a subproject	|WG README page	|
|subproject owner	|set direction and priorities for a subproject	|demonstrated responsibility and excellent technical judgement for the subproject	|WG README page	|
|	|	|	|	|

## New contributors

New contributors should be welcomed to the community by existing members,
helped with PR workflow, and directed to relevant documentation and
communication channels.

## Established community members

Established community members are expected to demonstrate their adherence to the
principles in this document, familiarity with project organization, roles,
policies, procedures, conventions, etc., and technical and/or writing ability.
Role-specific expectations, responsibilities, and requirements are enumerated
below.

## Member

Members are continuously active contributors in the community.  They can have
issues and PRs assigned to them, participate in SIGs through GitHub teams, and
pre-submit tests are automatically run for their PRs. Members are expected to
remain active contributors to the community.

**Defined by:** Member of the ros2-wgs GitHub organization


### Requirements

* Enabled [two-factor authentication](https://help.github.com/en/articles/about-two-factor-authentication) on their GitHub account
* Have made multiple contributions to the project or community.  Contribution may include, but is not limited to:
    * Authoring or reviewing PRs on GitHub
    * Filing or commenting on issues on GitHub
    * Contributing to WG, subproject, or community discussions (e.g. meetings, ROS Answers, Discourse)
* Have read [the contributor guide](https://index.ros.org/doc/ros2/Contributing/)
* Actively contributing to 1 or more subprojects.
* Sponsored by 2 reviewers. **Note the following requirements for sponsors**:
    * Sponsors must have close interactions with the prospective member - e.g. code/design/proposal review, coordinating on issues, etc.

    * Sponsors must be reviewers or approvers in at least 1 repository either in any ros2-wgs repo, or the org they are sponsoring for.

    * Sponsors SHOULD be from multiple member companies to demonstrate integration across community.
* **[Open an issue][membership request] against the ros2-wgs/community repo**
* Ensure your sponsors are @mentioned on the issue
* Complete every item on the checklist (see membership template below)
* Make sure that the list of contributions included is representative of your work on the project.
* Have your sponsoring reviewers reply confirmation of sponsorship: `+1`
* Once your sponsors have responded, your request will be reviewed by the ros2-wg GitHub Admin team, in accordance with their SLO. Any missing information will be requested.



```
---
name: Organization Membership Request
about: Request membership in a ros2-wgs Org
title: 'REQUEST: New membership for <your-GH-handle>'
labels: area/github-membership
assignees: ''
---

### GitHub Username
e.g. (at)example_user

### Organization you are requesting membership in
e.g. (at)ros2-wgs

### Requirements
- [ ] I have reviewed the community membership guidelines (https://git.k8s.io/community/community-membership.md)
- [ ] I have enabled 2FA on my GitHub account (https://github.com/settings/security)
- [ ] I have subscribed to the kubernetes-dev e-mail list (https://groups.google.com/forum/#!forum/kubernetes-dev)
- [ ] I am actively contributing to 1 or more ROS2 subprojects
- [ ] I have two sponsors that meet the sponsor requirements listed in the community membership guidelines
- [ ] I have spoken to my sponsors ahead of this application, and they have agreed to sponsor my application

### Sponsors
- (at)sponsor-1
- (at)sponsor-2

### List of contributions to the Kubernetes project
- PRs reviewed / authored
- Issues responded to
- WGs projects I am involved with
```

### Responsibilities and privileges

* Responsive to issues and PRs assigned to them
* Responsive to mentions of WGs teams they are members of
* Active owner of code they have contributed (unless ownership is explicitly transferred)
* Code is well tested
* Tests consistently pass
* Addresses bugs or issues discovered after code 

## Reviewer

Reviewers are able to review code for quality and correctness on some part of a subproject. They are knowledgeable about both the codebase and software engineering principles.

**Defined by:** *reviewers* entry in an WG README file in a repo owned by the project. Reviewer status is scoped to a part of the codebase.

**Note:** Acceptance of code contributions requires at least one approver in addition to the assigned reviewers.

### Requirements

The following apply to the part of codebase for which one would be a reviewer:

* member for at least 3 months
* Primary reviewer for at least 5 PRs to the codebase
* Reviewed or merged at least 20 substantial PRs to the codebase
* Knowledgeable about the codebase
* Sponsored by a subproject approver
* With no objections from other approvers
* Done through PR to update the WG README file
* May either self-nominate or be nominated by an approver in this subproject.

### Responsibilities and privileges

The following apply to the part of codebase for which one would be a reviewer:

* Tests are automatically run for PullRequests from members of the ros2-wgs GitHub organization
* Code reviewer status may be a precondition to accepting large code contributions
* Responsible for project quality control via code reviews
* Focus on code quality and correctness, including testing and factoring
* May also review for more holistic issues, but not a requirement
* Expected to be responsive to review requests as per community expectations (TBD)
* Assigned PRs to review related to subproject of expertise
* Assigned test bugs related to subproject of expertise
* May get a badge on PR and issue comments

## Approver

Code approvers are able to both review and approve code contributions.  While code review is focused on code quality and correctness, approval is focused on holistic acceptance of a contribution including: backwards / forwards compatibility, adhering to API and flag conventions, subtle performance and correctness issues, interactions with other parts of the system, etc.

**Defined by:** *approvers* entry in an WG README file.

Approver status is scoped to a part of the codebase.

### Requirements

The following apply to the part of codebase for which one would be an approver:

* Reviewer of the codebase for at least 3 months
* Primary reviewer for at least 10 substantial PRs to the codebase
* Reviewed or merged at least 30 PRs to the codebase
* Nominated by a subproject owner
* With no objections from other subproject owners
* Done through PR to update the WG README file

### Responsibilities and privileges

The following apply to the part of codebase for which one would be an approver:

* Approver status may be a precondition to accepting large code contributions
* Demonstrate sound technical judgement
* Responsible for project quality control via code reviews
* Focus on holistic acceptance of contribution such as dependencies with other features, backwards / forwards compatibility, API and flag definitions, etc

* Expected to be responsive to review requests as per community expectations (TBD)
* Mentor contributors and reviewers
* May approve code contributions for acceptance

## Subproject Owner

**Note:** This is a generalized high-level description of the role, and the
specifics of the subproject owner role's responsibilities and related
processes *MUST* be defined for individual WGs or subprojects.

Subproject Owners are the technical authority for a subproject in the ROS2
project.  They *MUST* have demonstrated both good judgement and responsibility
towards the health of that subproject.  Subproject Owners *MUST* set technical
direction and make or approve design decisions for their subproject - either
directly or through delegation of these responsibilities.

**Defined by:** *owners* entry in WG README page


### Requirements

The process for becoming an subproject Owner should be defined in the WG
charter of the WG owning the subproject.  Unlike the roles outlined above, the
Owners of a subproject are typically limited to a relatively small group of
decision makers and updated as fits the needs of the subproject.

The following apply to the subproject for which one would be an owner.


* Deep understanding of the technical goals and direction of the subproject
* Deep understanding of the technical domain of the subproject
* Sustained contributions to design and direction by doing all of:
* Authoring and reviewing proposals
* Initiating, contributing and resolving discussions (emails, GitHub issues, meetings)

* Identifying subtle or complex issues in designs and implementation PRs
* Directly contributed to the subproject through implementation and / or review

### Responsibilities and privileges

The following apply to the subproject for which one would be an owner:

* Make and approve technical design decisions for the subproject.
* Set technical direction and priorities for the subproject.
* Define milestones and releases.
* Mentor and guide approvers, reviewers, and contributors to the subproject.
* Ensure continued health of subproject
* Adequate test coverage to confidently release
* Tests are passing reliably (i.e. not flaky) and are fixed when they fail
* Ensure a healthy process for discussion and decision making is in place.
* Work with other subproject owners to maintain the project's overall health and success holistically

# References

[1] [Open Source Guides: Leadership and Governance](https://opensource.guide/leadership-and-governance/)
[2] [Projects that make their rules explicit would see more participation](https://opensource.com/open-organization/18/4/new-governance-model-research)
[3] [Apache Forret Project Guidelines](http://forrest.apache.org/guidelines.html)
[4] [How the ASF (Apache Software Foundation) works?](http://www.apache.org/foundation/how-it-works.html)
[5] [Governance Models (OSS Watch)](http://oss-watch.ac.uk/resources/governancemodels)
[6] [Node.JS Project Governance](https://github.com/nodejs/node/blob/master/GOVERNANCE.md)
[7] [Kubernetes Governance Model](https://github.com/kubernetes/community/blob/master/governance.md)

