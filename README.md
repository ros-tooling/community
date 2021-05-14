# ROS 2 Tooling Working Group

The Tooling Working Group's mission is to provide ROS 2 users with simple, robust and easy to use tools for recording, debugging, visualization and introspection.

This document defines the scope and governance of the ROS 2 Tooling Working Group.

NOTE: The `scripts` directory in this repository contains scripts used to manage this organization and keep it up to date with any settings/permissions laid out in this document.


## Subprojects

This Working Group owns and maintains the following Subprojects.
Its meetings and membership are largely focused on the direction, design, and work on the projects.


### Subproject list

The following subprojects are owned by Tooling WG:
* Tooling WG Management Infrastructure
  * Description: Set of repositories used to manage the working group itself, not a released product
  * Repositories
    * https://github.com/ros-tooling/repo-configs
* ros-cross-compile
  * Description: A tool to build ROS/ROS2 workspaces for various target platforms.
  * Repositories
    * https://github.com/ros-tooling/cross_compile
* rosbag2
  * Description: A tool to record and play back ROS2 communications
  * Repositories
    * https://github.com/ros2/rosbag2
    * https://github.com/ros2/rosbag2_bag_v2
* System Metrics Collector
  * Description: a set of composable nodes that collect a set of host system metrics and publish them to the ROS system for analysis
  * Repositories
    * https://github.com/ros-tooling/system_metrics_collector.git
* Github CI Actions
  * Description: A set of Github Actions for ROS/ROS2 packages and tooling that automatically test Pull Requests
  * Repositories
    * https://github.com/ros-tooling/action-ros-ci
    * https://github.com/ros-tooling/action-ros-ci-template
    * https://github.com/ros-tooling/action-ros-lint
    * https://github.com/ros-tooling/setup-ros
    * https://github.com/ros-tooling/action-pypi
* launch_ros_sandbox
  * Description: A ROS 2 `launch` extension that starts Nodes in their own containers
  * Repositories
    * https://github.com/ros-tooling/launch_ros_sandbox
* ros-github-scripts
  * Description: Collection of scripts for easier management of ROS projects on GitHub - including generating reports of contributions for TSC members, and starting Jenkins ci_launcher jobs for pull requests.
  * Repositories
    * https://github.com/ros-tooling/ros-github-scripts
* `topic_tools`
  * Description: Package containing tools for manipulating ROS topics - such as multiplexing, relaying, and throttling
  * Repositories:
    * https://github.com/ros-tooling/topic_tools 


### Adding new subprojects

To request introduction of a new subproject, add a list item to the "Subprojects" section and open a Pull Request to this repository, using the default Pull Request Template to populate the text of the PR.

PR will be merged on unanimous approval from Approvers.

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


### Subproject changes

Modify the relevant list item in the "Subprojects" section and open a Pull Request to this repository, following instructions in the Pull Request Template to populate the text of the PR.

PR will be merged on unanimous approval from Approvers.


### Deprecating subprojects

Sometimes, project may cease to be useful, or their maintainers may leave.
We do not want to commit to maintaining every project that has ever been added here forever.

To request removal of a subproject, remove the relevant list item in the "Subprojects" section and open a Pull Request in this repository, following instructions in the Pull Request Template to populate the text of the PR.

PR will be merged on unanimous approval from Approvers.

If the repositories of the subproject are in the `ros-tooling` organization, they will be transferred out of the organization or deleted at this time.


## Governance

### Meetings

* Regular WG Meeting: Every other Friday at 9:00 AM Pacific Time (biweekly)
  * The meeting reminder will be posted on discourse.ros.org in the week leading up to the meeting
  * After the meeting we will post:
    * Video recording
    * Notes from the meeting


### Communication Channels

The WG hosts a Matrix channel for text based chat at https://matrix.to/#/!IQcVAivBdnSuEniBZa:matrix.org?via=matrix.org

Some users use the Riot clients to connect to this chat room.


### Backlog Management

The WG backlog is tracked on a [ZenHub](https://www.zenhub.com/) board.
ZenHub connects to GitHub to add extra metadata to issues for more detailed project management than GitHub projects provide.
* The ZenHub board can be viewed in GitHub by [installing its browser extension](https://www.zenhub.com/extension) - [Board on GitHub](https://github.com/ros-tooling/community#zenhub).
* Members who do not wish to install a browser extension can [view the board directly on ZenHub](https://app.zenhub.com/workspaces/ros-2-tooling-working-group-5dc4f36af1b75b0001fb7c8d/board)


### Membership, Roles and Organization Management

Working Group members may act in one or more of the following roles:

* **Member**
  * Attend at least one out of the last three Working Group meetings
  * Responsible for triaging issues
* **Reviewer**
  * All reviewers are members
  * Prerequisite: Proven track record of high-quality reviews to WG subprojects
  * Responsible for reviewing pull requests
* **Approver**
  * All approvers are reviewers
  * Prerequisite: Proven track record of high-quality contributions and reviews to WG Subprojects
  * Responsible for approving and merging pull requests
  * Responsible for vetting and accepting new projects into the Working Group
* **Lead**
  * TSC member or their delegate
  * Responsible for organizing and moderating working group meetings
  * Responsible for posting meeting materials (minutes, recordings, etc.)
  * Responsible for breaking ties

To become a member or change role, use the "Organization Membership Request" issue template on this repository.
Such applications are accepted upon unanimous agreement from Approvers, and are typically based on the applicant's history with the subprojects of the Working Group.
The Lead role cannot be applied for, as it is an appointee of the ROS 2 TSC.


### Modifying this governance document

Changes to this document will be made via Pull Request.
The PR will be merged on WG approval.
