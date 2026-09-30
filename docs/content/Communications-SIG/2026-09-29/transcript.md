SIG: Communications SIG
Date: 2026-09-29
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Julia Furst Morgado (Dash0)** 00:26 Hello?
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 00:30 Hi, Julia, how are you?
**Julia Furst Morgado (Dash0)** 00:32 I'm good, how are you?
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 00:34 I'm okay, thank you.
**Julia Furst Morgado (Dash0)** 00:38 Okay.
So about those, the maximum number of PRs, you said that's something new.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 00:47 It is. We've been getting a lot of drive by AI contributions, and.
**Julia Furst Morgado (Dash0)** 00:53 Yeah, I can…
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 00:54 overwhelming us. So we are trying out some restrictions. I just came back from a hiatus, so I'm still getting caught up on the news.
**Julia Furst Morgado (Dash0)** 01:04 How was it?
Your hiatus.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 01:07 It was, it was, I was taking care of a family member.
**Julia Furst Morgado (Dash0)** 01:10 Oh, okay, okay, sorry, yeah, I thought it was a vacation.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 01:14 No, no.
**Julia Furst Morgado (Dash0)** 01:15 Okay.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 01:17 So we had started with a restriction of one PR.
**Vivek Anandaraman** 01:23 school.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 01:24 For anyone who doesn't have, write access.
**Vivek Anandaraman** 01:27 and.
**Julia Furst Morgado (Dash0)** 01:28 Bye.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 01:30 After we saw a few instances of people within the community having the same issue you did, we've increased that to 3.
Sounds good. So.
I'm not sure if it's retroactive. It should be, but we're going to stick with three for now and see how that goes.
**Julia Furst Morgado (Dash0)** 01:47 I think I have… I probably have more than 3, so that's why it blocked me, because I.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 01:53 Okay.
**Julia Furst Morgado (Dash0)** 01:53 a few, localization ones that I'm waiting on, probably Marilia or Vitor to… to review, but that's fine, so we'll wait on that, and then once they review it, I'll… I'll move that out of the draft mode.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 02:09 Perfect.
**Julia Furst Morgado (Dash0)** 02:10 Thank you.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 02:10 Perfect, yeah, and thank you for doing the update.
**Julia Furst Morgado (Dash0)** 02:13 valuable one. Yeah, of course.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 02:15 Hi, Vivek, how are you?
**Vivek Anandaraman** 02:18 Pretty good.
Hey, how are you guys?
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 02:22 Yeah, we are good. I will probably be the only maintainer here today from Communications SIG.
**Vivek Anandaraman** 02:30 Okay.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 02:31 Everyone else has time off.
or business reasons for not being able to join today. So, I am pulling up the notes doc to see… One second… It's on the browser window that's behind my Zoom window.
Okay.
Let's see.
there.
Okay.
So does everyone have the notes, Doc?
**Julia Furst Morgado (Dash0)** 03:07 Yep.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 03:08 Okay.
So let's get the attendance here. If you have anything, that you'd like recorded.
as a topic, feel free to Add it to the topics.
And… Got it. And… 0… and you can also add your name here if.
You want… I'll try typing the right ones, but… Oh… I'm just going to type first names in if you want to add the rest of your… names in the doc feel free.
Okay, Julia, I see you've added getting started. Hello, Leandro and Sophia, long time no see. It's good to be back. Hope you're all doing well.
**Julia Furst Morgado (Dash0)** 03:59 Yeah, mine.
**Sophia Solomon** 04:00 Same to you.
Thank you.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 04:02 Thank you, thank you, yeah.
**Leandro Caracciolo** 04:04 Fine, thanks.
**Julia Furst Morgado (Dash0)** 04:09 Yeah, about the Getting Started project, I was hoping Severin would be here. Last time we… at the last call, I said that I had interested in helping, you know, move that project forward, so I took a look at all the links he shared with me. There is a pull request closed, there is a.
a page on the documentation. Vitor also shared a few things with me, so I just wanted a little bit more direction, but I also have a call with Vitor, about that, and about, some localization projects we've been talking. So I can… I can talk with him and maybe update here on the… on the meetings notes, whatever, you know, if I decide something, because… let me share here this, link.
I'm gonna put it, here on the… on the notes, so this is something that Vitor had started in April.
For the Getting Started application, and I think it didn't move after that, it's stale, but we're gonna see, we're gonna try to, you know, get that going, and I know we need, you know, people from each SDK to also, jump in, and… because each one of them they're going to, do the implementation. Yeah, so that's it. I just wanted to… to see if I'm on the right direction, like, starting out. I'm… for now, I'm… I'm by myself, but we're open to more people helping with this project.
And yeah, if you have any ideas or comments, I'm always open.
Yeah.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 06:05 Okay, great, thank you. I do agree that it's going… the project is mostly going to require a lot of coordination across the different SDKs and SIGs. It's gonna be a bit of herding cats to get it all done, but, hopefully.
If we have someone like you who's willing to… spearhead that effort, then we'll actually make progress on it, because I know that, Severin has been trying to get this off the ground, and then Vitor stepped in to try and help, but To be honest, the comms maintainers are spread very, very thin right now.
**Julia Furst Morgado (Dash0)** 06:45 -H.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 06:45 So it's been a rough few months for the SIG, but we are… doing what we can to keep things moving, and we need people like you, Julia, to step up and help us out, so… I don't have any further details to shed light on whatever progress has been made.
**Julia Furst Morgado (Dash0)** 07:05 Okay.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 07:07 So I think your meeting with Vitor is probably the good first step.
I do know that, Severin discussed the Getting Started project with, one of the, oh, we lost Yuan.
Severin discussed the Getting Started project with Dan Gomez Blanco.
**Julia Furst Morgado (Dash0)** 07:33 Yeah,
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 07:34 see if it dovetailed with the Blueprints project.
**Julia Furst Morgado (Dash0)** 07:37 but.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 07:37 But, the consensus was that They don't actually mix very well because blueprints is more of an advanced use case. Like you're already kind of in the weeds, you have this setup.
And you you want to know exactly how to configure open telemetry for your specific observability stack.
getting started is meant to be truly.
**Julia Furst Morgado (Dash0)** 08:02 Yeah.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 08:02 You know nothing about OpenText.
**Julia Furst Morgado (Dash0)** 08:04 Exactly.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 08:04 And this is going to dip you and just let you dip your foot in. Does anyone else have any thoughts about the Getting Started project or interest in helping Julia get it off the ground?
**Vivek Anandaraman** 08:20 Yeah, I'd be willing to, help Juliana. Yeah, like, I haven't… I don't have, like, a lot of experience in open source itself. Like, I have experience in the IT field, I have been in, you know, like, other IT fields, but… Not as a maintainer, you know, like, got a whole lot of experience in open source, but I am willing to volunteer, you know, just so it's an FYI, so…
**Julia Furst Morgado (Dash0)** 08:43 Okay.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 08:44 You don't need experience.
We are, in a lot of cases, all beginners here every day. It's a new thing.
And I can tell you that AI has changed the landscape considerably for us.
We are absolutely a group of people who like to just.
learn on the go. So if that sounds like you, then we absolutely welcome.
**Vivek Anandaraman** 09:11 Yeah, I am pretty curious. Yeah, I am curious by nature and I will, you know, pursue things. So yeah.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 09:16 Yeah. And I will say, I've said it before and I'll say it again, Docs is a great place to get started because not only are you helping the project, but you're also learning at the same time by reading the docs, by creating them.
you're… you're learning about the project.
If you have specific questions about contributing to open source in general, or contributing to open telemetry.
We can, you can ask them here. There are.
**Vivek Anandaraman** 09:42 some.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 09:42 channels to are you in the CNCF Slack?
**Vivek Anandaraman** 09:46 Yeah, I am.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 09:47 Okay.
**Vivek Anandaraman** 09:48 Cool.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 09:49 I don't mean to pressure you, but if you have questions, you can always bring them to the SIG… to the COMSIG meeting. We… like to, dovetail with the contributor experience sake as much as we can, because we know that Docs is the on-ramp for a lot of new contributors, so happy to answer.
**Vivek Anandaraman** 10:08 Yeah.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 10:08 Any questions you have?
**Vivek Anandaraman** 10:10 Yep.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 10:14 Okay.
So Julia, I'll leave it up to you to get in touch with Vivek and.
**Julia Furst Morgado (Dash0)** 10:19 configure.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 10:20 out how you want to coordinate that. If you… need resources from COMPS, you can ask Vitor or come to us.
**Julia Furst Morgado (Dash0)** 10:31 Yeah.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 10:31 We'll figure out.
**Julia Furst Morgado (Dash0)** 10:32 also.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 10:33 to help.
And then you can just report back on whatever progress you've made because I know you're going to make progress.
**Julia Furst Morgado (Dash0)** 10:40 Yeah.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 10:41 the.
Okay, I don't have anything myself for the agenda because I am literally just getting back into open telemetry. So if anyone else has anything else they'd like to discuss, please.
You have the floor.
**Julia Furst Morgado (Dash0)** 11:08 Nothing besides that.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 11:11 Okay.
Sophia.
I don't want to spend a lot of time on this because I literally haven't looked at it at all. But I know that you were interested in helping me with the collector docs project.
**Sophia Solomon** 11:26 I really want to help. My build was way too out of date.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 11:31 Yeah.
**Sophia Solomon** 11:31 Severin closed it out, but I, I still like, I think.
I mean, cucumbers around the corner. I would love to really, like, lock in and help with that.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 11:41 Yeah, it needs to be done.
**Sophia Solomon** 11:43 I'm so sorry that, like, it's just fallen to the wayside.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 11:47 No, no, it's not you, it's me.
**Sophia Solomon** 11:49 No, not yet.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 11:50 This was, like, one of those projects that I took on, and then life got in the way, right? So, excuse me.
I just wanted to tell you I don't have any updates, just that It's still on my radar. I've already communicated to the comms folks that it is my top priority once I get fully ramped back up.
**Sophia Solomon** 12:12 Yeah.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 12:12 So I will reach out to you again once I have.
spend some time looking at it and figuring out what needs to be done. I have a feeling even the pages have changed since I, you know, PRs have been merged, and I'm…
**Sophia Solomon** 12:25 And they haven't.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 12:26 know.
**Sophia Solomon** 12:27 But yeah, no, no, I'd love to like be more involved. I'm like more balanced with my roles right now, like within my job and open telemetry. So I feel I have a lot more time than I did, I think, the beginning of the year to help you.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 12:44 Great. So that's awesome.
**Sophia Solomon** 12:46 run this.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 12:46 will need the help. Yeah. Leandra, it's good to see you. Do you have any updates?
**Leandro Caracciolo** 12:55 Yeah, it's good to see you, too. No, I have not updated, just to say that if you need something related to design, and just… I'll be here to help, and… Just ping me on the Slack channel.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 13:09 Okay, great. Yeah, for those of you who don't know, Leandro, is a… graphic designer? I'm not really sure what the proper term is, but he's come up with a lot of our… Our new artifacts that we're using for, like, LinkedIn and the website and all of that kind of stuff, so…
**Julia Furst Morgado (Dash0)** 13:27 I've heard a lot about you, Leandro. You work at Olive Garden?
**Leandro Caracciolo** 13:32 Yep, yep.
**Julia Furst Morgado (Dash0)** 13:33 Yeah, nice to meet you.
**Leandro Caracciolo** 13:34 enjoy.
**Julia Furst Morgado (Dash0)** 13:34 Cool. I'm Brazilian as well.
**Leandro Caracciolo** 13:36 Very great. Yes.
Nice to meet you, nice to meet you. If you need something related to design, or something that I can help, just… just ping me.
And talk about it. Thank you, thank you very much, all.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 13:51 Yeah, yeah.
Vivek, is this your first SIG meeting?
been.
**Vivek Anandaraman** 14:01 I, I was in the last week, the last, the week before, you know, that, two weeks ago, right? Okay. I think. Okay.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 14:08 Okay, great. Yeah, I had to take a few months off from the project. So I've been. This is literally my first SIG meeting since.
I don't even know when it's been. It's been months.
But if there… I'll just reiterate, if there's anything that you need, you can find us in otel-coms, in Slack. Or you can even ping me directly if you have questions. I'm… I'm on Slack.
called.
**Vivek Anandaraman** 14:36 Cool. Okay. Yeah. Thanks, Stephanie. Yeah.
**Julia Furst Morgado (Dash0)** 14:39 Okay.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 14:41 If there's nothing else, and I think we can get some time back in our day.
**Julia Furst Morgado (Dash0)** 14:47 Sounds good.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 14:49 Okay.
**Vivek Anandaraman** 14:49 Yes.
**Julia Furst Morgado (Dash0)** 14:50 Thank you. Bye, everyone.
**Vivek Anandaraman** 14:51 Yeah.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 14:52 Hopefully there will be more maintainers next meeting, so everybody will know.
**Sophia Solomon** 14:55 It's.
**Julia Furst Morgado (Dash0)** 14:56 Okay. Bye-bye.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 14:58 You all. Thank you. Bye.
**Leandro Caracciolo** 14:59 Bye bye.
