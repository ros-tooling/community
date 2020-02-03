# ROS 2 Tooling Working Group

The Tooling Working Group's mission is to provide ROS 2 users with simple, robust and easy to use tools for recording, debugging, visualization and introspection.

This document defines the scope and governance of the ROS 2 Tooling Working Group.

## Meetings

* Regular WG Meeting: Every other Friday at 9:00 AM Pacific Time (biweekly)
  * The meeting reminder will be posted on discourse.ros.org in the week leading up to the meeting
  * After the meeting we will post:
    * Video recording
    * Notes from the meeting

## Subprojects

The following subprojects are owned by Tooling WG:
* ros-cross-compile
  * Description: A tool to build ROS/ROS2 workspaces for various target platforms.
  * Owners
    * @emersonknapp
    * @prajakta-gokhale
  * Repositories
    * https://github.com/ros-tooling/cross_compile
* rosbag2
  * Description: A tool to record and play back ROS2 communications
  * Owners
    * @Karsten1987
  * Repositories
    * https://github.com/ros2/rosbag2
* System Metrics Collector
  * Description: a set of composable nodes that collect a set of host system metrics and publish them to the ROS system for analysis
  * Owners
    * @dabonnie
    * @mm318
  * Repositories
    * https://github.com/ros-tooling/system_metrics_collector.git

### Adding new subprojects

To request introduction of a new subproject, use the "Add Project Request" issue template in this repository.

To resolve the created ticket, a PR must be merged by a working group admin, which edits the "Subprojects" section of this document.
The PR will be merged on a 1/2 vote (see "Voting")

### Standards for subprojects

When adopting a subproject, the WG agrees that a specific set of criteria will be maintained by the WG.

These criteria are:
* Build passes against ROS 2 master
* The ROS 2 standard linter set is enabled and adhered to
* Builds have 0 warnings
* Quality builds are green (address sanitizer, thread sanitizer, clang thread safety analysis)
* Test suite passes
* Code coverage is measured, and non-decreasing level is enforced in PRs
* Issues are responded to promptly
* Releases go out regularly when bugfixes or new features are introduced

### Deprecating subprojects

Sometimes, project may cease to be useful, or their maintainers may leave.
We do not want to commit to maintaining every project that has ever been added here forever.
To request removal of a subproject, use the "Remove Project Request" issue template in this repository.

To resolve the created ticket, a PR must be merged by a working group admin, which edits the "Subprojects" section of this document.
Additionally, if the repository lives in the `ros-tooling` organization, it will be transferred or deleted out of the organization.
The PR will be merged on a 2/3 vote (see "Voting")

## Scope

WG Tooling’s mission is to provide ROS 2 users with simple, robust and easy to use tools for recording, debugging, visualization and introspection purposes.

### In scope

* Subprojects owned by the WG

### Out of scope

* Middleware/communications

## Membership, Roles and Organization Management

The roles of the WG are reflected in its Teams

* Members
    * Issue triage privileges
* Reviewers
    * Code review privileges for a subproject
* Approvers
    * Code review approval and merge privileges for a subproject
* Subproject owner
    * Admin on a specific subproject
* Admin
    * Admin on organization and all its repositories

To become a member or change role, use the "Organization Membership Request" issue template on this repository.
* `Member` will be granted automatically on request
* `Reviewer` will be granted with approval of Subproject Owner for the relevant project
* `Approver` will be granted with approval of Subproject Owner for the relevant project
* `Subproject Owner` requests will be granted on adding a subproject (see "Adding New Subprojects")
  * Transfer of ownership of a subproject will be granted on approval of the existing Subproject Owner, it uses the same membership issue template.
* `Admin` requests will be granted on a 2/3 vote (see "Voting")

## Modifying this governance document

Changes to this document will be made via Pull Request.
The PR will be merged on a 1/2 vote (see "Voting")

## Voting

In this document, any call for a X/Y vote means the following:

At the next meeting of the working group, the Members in attendance will vote, and if >= X/Y of the voters vote in favor, the motion passes.
