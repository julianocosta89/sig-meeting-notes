SIG: OpAMP SIG
Date: 2026-03-31
Duration: 46 minutes
============================================================

## Zoom Recording Transcript

**Tigran Najaryan** 05:11 Hi, everyone.
**Andy Keller** 05:13 Blue.
I'm pretty sick, apparently I got something at KubeCon.
Brought it home with me from Amsterdam.
Tends to happen when you travel abroad.
Yes.
**Tigran Najaryan** 05:31 Yeah.
**Andy Keller** 05:32 Probably sound pretty funny. I definitely feel… Really bad. So…
**Tigran Najaryan** 05:38 Do you… do you normally work from home, Andy?
**Andy Keller** 05:42 You know, it's a mix. I would say, like, one or two days a week, but because I'm sick, I'm not going to the office.
**Tigran Najaryan** 05:48 Yeah, yeah. It's a special bet for people who work from home. You… I guess you lose your immunity or something, so as soon as you're somewhere out there with a lot of people, you catch something.
**Andy Keller** 06:02 Yeah.
**Tigran Najaryan** 06:02 Yes, yeah.
**Andy Keller** 06:03 I'm fortunate I have an 11 and 14-year-old in school, so they bring it all back.
**Tigran Najaryan** 06:07 Yeah.
**Andy Keller** 06:08 So, even if I didn't leave the house, I'd get it. But… But no, I, I, I get out, I get to the office pretty regularly, and… I always, even when I'm at home, I'm really intentional about Going out to get coffee, or doing something.
Socializing in some… Even if it's in a small way.
We had a very good, SIG meeting in… at KubeCon. There was probably about 16 or 17 people there.
**Tigran Najaryan** 06:41 Yes, I'd love to hear what you guys did. Maybe, maybe, maybe let's start with that, I guess? It would be very interesting to hear.
**Andy Keller** 06:48 Let's wait a second, I'm not sure where he is. I don't know if anybody else is planning on… Joining.
No, he says he's in it, so I think he's not in the right one.
You know, we… I wonder if he's using a link?
At the top of the document. Is that this, or… I used the one from the calendar invite. I know we have.
**Aunsh Chaudhari** 07:36 I mean, the one as a doctor.
**Andy Keller** 07:37 A couple of weeks ago, because there was.
**Aunsh Chaudhari** 07:39 The one in the dock is right, yeah. I use that anymore.
**Tigran Najaryan** 07:42 It's the same link, I think. I don't see… it's in the invite and the doc, they are the same link, as far as I can see.
**Aunsh Chaudhari** 07:51 Correct, yeah.
**Andy Keller** 07:57 Okay.
I just noticed there's also some other people who say they're here and they're not, so…
**Dakota Paasman** 08:05 Hey, thanks for that, we're just sitting in that other one.
**Andy Keller** 08:09 Oh, okay.
**Tigran Najaryan** 08:10 What's the other one? Where did you get that link from?
**Dakota Paasman** 08:13 I got it from the, Google Calendar, the Google Calendar meeting.
**Tigran Najaryan** 08:20 Okay.
Because I'm… okay, on my calendar, I'm seeing the old one.
Somehow, okay, we'll need to look at it after this call. Somebody probably updated the calendar, and…
**Andy Keller** 08:36 See, I don't know if you were here that time, but there was… once we moved the meeting, we, like, conflicted with another group.
Yes. I had a meeting at the same time, and…
**Tigran Najaryan** 08:46 Yeah. Okay, I'll take a look at it after the call. I'll fix it.
Okay, Yeah, so like I was saying, it would be very interesting to hear what you guys did at KubeCon, if… A few… if anybody wants to maybe give a 5-minute Maybe a summary of what interesting things happened there, it would be great to know.
**Andy Keller** 09:12 Yeah, so we had an in-person meeting, on Wednesday at 4 local time in Amsterdam, and… We logged notes, so they're, below today's, the time is wrong, it looks like, but the date, I think, is right. So, we had a lot of people join, a lot of people that don't regularly join, And, talked about, you know, stabilization. That was kind of where I started, just updating everyone that that's kind of the major goal over the next… 6 to 12 months.
We shared the vision roadmap doc.
Talked about different components, including the bridge.
There's some good notes in here.
Highlighted that, partial reload issue, I have to click through to remember his name from Elastic.
Blake… Made sure everybody looked at that.
Oh, I forgot, what was this issue with PERC? I forget now, the hotel call UI?
**Aunsh Chaudhari** 10:28 Yeah, it was actually a nice demo that he had put together of an application.
**Andy Keller** 10:32 Oh, yeah, that's right. Yeah, go ahead.
**Aunsh Chaudhari** 10:34 Yeah, so I think that's just, he was able to basically show off, like, how we can use the op-amp server and supervisor as well, but being able to show even data flowing through the collector, through the CLI, through a nice, like, UI, right? I think that was something that he demoed. So he's planning to put in somewhat work into it, and also open source that. That's the… feedback that he shared, but it was very interesting to look at that. He was able to whip that out and demo it out to all of us, yeah.
**Douglas Camata** 11:03 Yeah.
**Tigran Najaryan** 11:04 There's no link to that, do you guys have a link, maybe?
**Andy Keller** 11:07 No, there's… it's not a public repo yet, he just gave a demo of…
**Tigran Najaryan** 11:11 Working on us.
**Michel Laterman** 11:12 I'll make sure to… ask for a publicly available demo for… we're really moving forward with our off-band stuff internally, too, so…
**Andy Keller** 11:23 Sorry, what was that?
**Tigran Najaryan** 11:24 Okay.
**Michel Laterman** 11:25 We're really moving forward with our op-amp stuff internally, so… We're gonna be flagging all sorts of stuff, Yeah, we're… right now, we're targeting monitoring like, a monitoring-only all-pamp support for our next minor release?
The feet, which should be… released to the public in a month or two. The feature freeze is, like, next week or something, so…
**Andy Keller** 11:52 Oh, great. Awesome.
**Aunsh Chaudhari** 11:55 Awesome.
**Tigran Najaryan** 11:58 Okay, I guess regarding the discussions that you had at KubeCon, if you guys made any decisions on anything, or if you, I guess, came close to a decision on anything, it would be great to make sure that these are recorded.
Somewhere, maybe in the form of issues in the… if it's a spec in spec repo, or somewhere, if its supervisor can be the collector, contribute repo, just to make sure that we have a record of those decisions somewhere.
And, I mean, I see the notes there, but… I'm not sure I'm… it tells me whether… I guess, we need to do about any… anything about any of this, right? So, if there's anything actionable there, it would be good to have those as issues.
**Aunsh Chaudhari** 12:48 Yeah.
Yeah, I think there was one discussion around… Go ahead.
**Douglas Camata** 12:53 Yeah, sorry, Anush.
**Aunsh Chaudhari** 12:55 Perfect.
**Douglas Camata** 12:56 I think mostly… What we talked regarding supervisor there was… We were thinking about… What in supervisors should be part of the… of the push towards stable?
And I think we agreed, About package management, and… There was even a conversation regarding the PR that Dakota has been moving forward recently that will be split for the collector upgrades, and… some other things that we already have, we already have issues and even BRs for.
Like, configuration validation using the collector's own binary Validate command, and some other things.
I don't know if it was exactly this that you were gonna say, Anush, but if you have anything to compliment.
**Aunsh Chaudhari** 13:54 No, no, yeah, I think that was, just the discussion around some of the issues that are put into that doc, right? I think, Jacob also agreed that he's going to review that doc and add a few other things that are on his mind. I think we agreed also that we'd want to take this in a sequence, right? There was a question around, do we plan to also focus on the bridge as well as the extension in terms of the stability for those components? So the discussion was, let's start with the spec.
go to the implementation in OPAM, go, then go to the supervisor, and then follow with bridge and, extension use cases, right? So that… that was the sequence that we discussed.
And there was also a brief discussion that I was hoping to bring on this call also on the interest of bringing in Kubernetes management.
Right, beyond what we already have with the Opam Bridge.
more focused on being able to modify a config map directly. So, again, there was no decision made, but the outcome was let's discuss this further. Jacob also agreed that he'll want to discuss that further with Dimitri and create an issue, and then we can engage on that further and get other people's opinions. So, that was another topic that we brainstormed over.
**Douglas Camata** 15:08 Yeah, and and I saw that Dmitry even already opened the issue.
Regarding the… this… this brain thing that he was talking about at the… at the meeting there in person, so I will try to find the link for it and put it here in the… in the doc for today's agenda.
I was wondering, maybe… maybe we should think about start tagging issues and or PRs that we already have, or that will be open for, like, a supervisor, stable.
release, and for anything else, of course, that we want to include in that. Maybe we can have a nice, like, project, GitHub project.
**Tigran Najaryan** 15:55 Yes. Boris.
**Douglas Camata** 15:56 of everything.
**Tigran Najaryan** 15:57 Yeah, yeah, I think that's a good idea. So, what I would suggest to do is that it seems like we have most or all of the topics collected in this Google Doc with the roadmap.
I don't know if we want to keep it just in the Google Doc, maybe… maybe let's do this… do the… do the final round of the review, and… Once we consider the dock to be Out of what we commit to doing.
we should probably go ahead and create the corresponding GitHub issues, and have that project board that you were talking about, and label the issues that we create as the I don't know, 1.0 or whatever it is, right? We will figure out what the right labeling is for that.
So that we can track the progress towards the roadmap. Or maybe it's a milestone, I don't know. Whatever it is, it's something that allows us to make it easier to track. The doc… I don't think the dock is the best way to keep track of the progress of what's happening.
So, my suggestion is that let's take the final look at the doc, and I guess before the next, maybe, SIG, let's make sure we finalize that and begin populating the GitHub issues and GitHub project board.
**Aunsh Chaudhari** 17:25 Sounds good, yeah.
**Tigran Najaryan** 17:27 We're going to need the issues anyway, because that's all we, I guess, assign and track work, so it needs to be in GitHub, either way.
**Douglas Camata** 17:36 Yeah, and if we need any help in setting up this project or these other things, Pablo did this already for the collector's SIG, so we could ask him for some help, if we need.
**Tigran Najaryan** 17:52 What exactly did Pablo do?
**Douglas Camata** 17:55 He, set up…
**Tigran Najaryan** 17:57 corridor?
**Douglas Camata** 17:57 Yeah, yeah, he set up the project board for tracking work on stability for the collector, and he often shares it in the collector's SQL, and it looks quite cool if we… want something like that, and we cannot set it up ourselves. We could ask for his help, too.
To set up.
**Tigran Najaryan** 18:19 Okay, okay, sounds good. So let's do this. Let's do the final pass on the doc, on the Google Doc.
Once we're happy with that, let's begin creating the project boards, or maybe one board will need to decide, because it's multiple repositories that are involved.
And and we'll take it from there. We'll take a look what Collector is doing, and maybe we can borrow some of the processes from there.
**Aunsh Chaudhari** 18:44 Sounds good. Maybe if folks are okay, I probably just want to take a minute so that people have a high-level understanding of how the doc is put together and what it's broken down into, and then feel free to review online, right? So I'll just take a minute so that everyone's mapping it out appropriately. Let me share my screen.
So… Yeah, I think overall, based on the discussion that the maintainers had, there were three goals, right, that were defined around the op-amp spec, going 1.0, being able to Then implement those table features, and then the supervisor, right? Initially, there was a draft list of issues that were basically created down below, right? That we had just pulled in from different repositories and broken it down just on high-level themes.
Like, after these goals were determined.
What few of us have done is that you've just taken those issues and sort of broken it down by those three goals, and then called out what was out of scope, right? So… so things like additional features, additional auth methods, or hot reload, or even the extension, since the extension is a different space other than these three goals, I think we've just called that out as being out of scope, so… yeah, just want to walk you through that. Feel free to… add comments, add, edit new goals as well, and edit new issues if needed. I think we had done a first pass of these issues A week or week and a half before, so if there are new ones that need to be added, please add them here.
**Tigran Najaryan** 20:12 What do the Y's mean on that table?
If it's a.
**Aunsh Chaudhari** 20:16 Why are you holding?
**Tigran Najaryan** 20:16 Included, and if not, it's out.
Is that the.
**Aunsh Chaudhari** 20:20 Yeah, if it's a… yeah, so it's a Y. Basically, this means that for spec going 1.0, these are the two issues that based on the review should be considered, right? Similarly, for basically the Go implementations, once they're in the spec, if they need to be implemented in the GO, like, OPAM Go implementation, these need to be implemented appropriately. So, this just means this issue should be bucketed in the milestone The spec 1.2. That's what it means. The Y means that.
**Tigran Najaryan** 20:51 Okay.
**Andy Keller** 20:55 And I just wanted to clarify the, the extension… this bullet point, adding support for remote config to the extension is definitely out of scope, but the extension itself is… essential because of its usage by the supervisor. I think that's obvious to everyone, I just want to make sure that…
**Tigran Najaryan** 21:14 Yes, yeah.
Yes.
**Aunsh Chaudhari** 21:17 Makes sense.
**Tigran Najaryan** 21:21 Okay, I think we can work on that offline. Maybe let's use this time for the agenda items. We have a few, so let's… let's go ahead. Dakota, you have the first one.
**Dakota Paasman** 21:33 Yeah, so we're just now talking about the roadmap and vision for stabilizing the supervisor.
I've opened up a new issue that I've linked in the… in the meeting notes. This issue is kind of like a… a relaunch, I suppose, of the package upgrades.
Feature. That original PR, I'm planning on having closed.
And then, kind of, from that PR, from those changes, you know, create several smaller PRs that gradually implement this feature. Just to allow review to be more streamlined, and not needing to review a massive 3,000-line PR.
So yeah, this issue is just kind of outlining that in some of the… The key… the key points.
Related to that PR.
**Tigran Najaryan** 22:26 Yeah, I like that. Can you also maybe break it down into multiple sub-issues, so that when you close the PR, it closes the issue, we can see the progress of what is being done?
**Dakota Paasman** 22:38 Yeah, yeah, I can definitely do that.
**Tigran Najaryan** 22:40 Yeah.
**Dakota Paasman** 22:40 Yeah, the, so yeah, this was just kind of, announcing that to everybody,
**Andy Keller** 22:46 Yeah, and this was a decision we made at the SIG meeting last week.
**Tigran Najaryan** 22:50 Yeah, yeah.
Makes sense, yeah, I like that.
**Dakota Paasman** 22:54 So yeah, I'm hoping to have the first PR up later this afternoon.
So, I'll message in the Slack channel about that when it's ready.
**Tigran Najaryan** 23:04 Yeah, yeah. I think that's good. One of the reasons what that… we weren't able to merge the PR was exactly what you said, it was just too big to do, I guess, to… to be reviewed in one go, so I like your approach here. Let's do that.
**Dakota Paasman** 23:22 Yeah, that's all I had for this.
**Tigran Najaryan** 23:27 Okay, I have the next one. I… I made a spec change PR. This is something that we discussed a while back, I think it was. When was that? Let me take a look at that. A year ago, essentially. It's about… whether capabilities of the agent can change after it is started. And at the time when we were discussing it, we decided that It is possible, but we are not… Saying that any capability can change, but there's a limited set of capabilities that we allow.
To be changed after the start, essentially after the first message is exchanged between the client and the server.
However, we have not followed up on that, and the spec remained as it is, and this is… essentially trying to capture that decision in the spec and make the implementation of that restriction in the… in the OPAM, though. Today.
essentially, you can change any of the capabilities, and I do not think that we understand well the consequences of allowing that.
So, this is essentially limiting it to… A safe subset of capabilities that is okay to change after… after the agent has started.
I would like… you guys to take a look at it. I want some more opinions, especially. Maybe Evan is not here.
from Evan to make sure that the supervisor operation is not conflicting with this idea in any way.
As far as I can tell, it should be okay. I looked at the implementation, it seems like we're not changing capabilities in the supervisor after the start.
But I would like… I guess, independent confirmation that Nothing is wrong with this. I have a spec change PR and the implementation of that change in Go as well. I linked the PRs there.
And I guess, Andya's… you as well, would be great if you could take a look at it.
**Andy Keller** 25:42 Yeah, I looked at it, the… I'm gonna try to suggest a slightly different language. It reads to me… like, almost like the second sentence contradicts the first one, and I know what you're trying to say is… like, I don't know if we should even say currently, or something, but, like.
Currently, only the following capabilities may be updated.
Because the first one is kind of general, that just says some of its capabilities.
**Tigran Najaryan** 26:15 Yeah, help me with the language there.
**Andy Keller** 26:19 I'll propose something, and I'll put it in here.
Okay.
**Tigran Najaryan** 26:23 Sounds good. But also with the idea of the restriction, if you're… if you think that it's the right approach here, whether we should be doing that or no.
**Andy Keller** 26:33 I'm not… yeah, I'm not sure. My… my… If we leave it unrestricted, that it… it says immediately that, sort of, OPGO… the Opie AppGo implementation has a limitation.
as we're moving to 1.0, I don't love saying that, you know, we don't fully support spec, because we only allowed certain things to be changed.
But I… it does feel like an implementation detail, and not a…
**Tigran Najaryan** 27:04 The reason… yeah, the reason I want to restrict it like this is also because I do not think we understand well enough what can happen if you allow the capabilities to change, to flip-flop at runtime, and what sort of… Complicated state changes can… can be the outcome of that… that capability change, and… it may require… I guess it complicates the states, right, on the client and on the server side.
And… There may be weird, unexpected consequences of that, oscillations in the capabilities, and in the… if you're in the middle of an exchange that requires a certain capability, and suddenly that… that bit capability bit switches during the exchange, what happens then? It's just… I… I think that allowing that blanket change for anything, anytime.
It's an unnecessary complication, and you don't.
**Andy Keller** 28:07 Although… although I would say that these two are probably the ones to be the mo… that would be the most… Complex, in that case, because of… You know, you're sending a remote config.
Which implies it accepts it, and then… You're gonna require it to report the remote config to see if it's been… Excellent.
**Tigran Najaryan** 28:26 And that's a good call-out. Maybe we should look at it very carefully, of what we allow with these two things. But at least with those, if we… if we analyze all the possible combinations of the behaviors and qualify it, then… then maybe we can be confident that it's fine. But we have… what, 15, 20 other capabilities? I don't want to subscribe to doing that same analysis for every possible combination of those.
**Andy Keller** 28:53 Right.
That makes sense. Could… could somebody remind me, if the… I think it's possible that the collector would… Could change.
**Tigran Najaryan** 29:06 We don't do that in the collector, as far as I can tell. In the supervisor.
**Andy Keller** 29:10 But does a supervisor get its capabilities from the collector?
**Tigran Najaryan** 29:15 I don't think so.
**Douglas Camata** 29:17 No, no, the supervisor gets them from its own config file.
**Tigran Najaryan** 29:22 From config file, yes. From its own config file, and sets it once, and it doesn't change as far as I can tell after that.
**Andy Keller** 29:29 I just wanted to make sure it wasn't possible that.
**Tigran Najaryan** 29:31 So, I guess, the soup…
**Andy Keller** 29:32 Received new configuration that changed that, and the supervisor would effectively… Board that.
**Tigran Najaryan** 29:38 As far as I can tell, with the current implementation, it doesn't.
**Andy Keller** 29:41 It's fixed, right? Okay.
**Tigran Najaryan** 29:43 Yeah, yeah.
**Douglas Camata** 29:45 And we don't even have, like, a hot config reload, so there is really no way in which a running supervisor would change.
**Andy Keller** 29:53 Couple times.
Yeah, it would only be if we were delegating from the collector, which it sounds like we're not, so that… yeah.
**Tigran Najaryan** 30:03 Okay.
Okay, I think we're good with that for now. Take a look at it offline, Andy, if you have a different wording for the… for the spec change, I'm happy to make the change. Okay. And also, if… You can think of… any weirdnesses that may happen as a result of the config capability flag changes, we should address that, make sure that it's covered in the implementation and the spec, if we need the spec to have an opinion on that as well.
Okay.
Let's move to the next one.
Rhonda, you want to.
**JM Juande Manjon** 30:42 Yes, this is Juan de, and yeah, I would like to offer my sponsorship for a new open country space.
Where a user like me, sorry, can contribute and share a PAM-based application. If we go in that road, the first thing that we'd like to do is to port the OpenGo example.
Consequently reuse, the server in the open, excuse me, they'll tell them.
**Tigran Najaryan** 31:11 So, with the example we discussed, and I think you talked to the demo people, you guys decided that it will be in the demo repository, right?
**JM Juande Manjon** 31:19 Right, so that was my first initial, thought, but, I think it's not a good idea, because we will lose the control, on that repo, because we don't owe that repo.
And somehow, if we have our own country, we can, modify or control who is changing, what changes go into the example.
somehow.
And I think it's not the right page on the demo. The demo, basically, is just linking to external repo to grab the code, or maybe grab an image and integrate the image in the example, but the code itself is not in the open screen.el demo.
**Tigran Najaryan** 32:09 So you… you're saying you don't want the actual example implementation that demo uses to be in the demo repository, you want it somewhere else.
**JM Juande Manjon** 32:19 Right, to keep the ownership on the outside.
**Tigran Najaryan** 32:22 that the MO maintainers suggested, or have you discussed it with them? Maybe they're happy to…
**JM Juande Manjon** 32:28 I mentioned this in the previous meeting here.
Maybe you were not present?
Not sure about that, but Yes, I think it spread my concerns about losing the control of the example code if we move offside the OPAN Space.
**Tigran Najaryan** 32:50 My concern with that is the following. If it lives in a different repository, let's say your opam-contrib, right, you need to make it a public package then. You have to publish it so that you can then import it In the… in the demo, right? Somehow.
And…
**JM Juande Manjon** 33:10 Right.
**Tigran Najaryan** 33:11 that… that is what I would like to avoid doing, because once you publish it.
people may start depending on it. Right now, it's internal.
There's no way to… to depend on it.
**JM Juande Manjon** 33:22 Right, so…
**Tigran Najaryan** 33:23 That's what worries me a bit.
**JM Juande Manjon** 33:25 That's exactly the goal of the contrib repo, where a user can share What they are doing, and others can use it.
So the idea is not to block people using it, it's the opposite. It's to help people share open-based application.
**Tigran Najaryan** 33:44 I hear you. I… It comes with the maintenance responsibilities, though. That's the.
**JM Juande Manjon** 33:50 Right, this one offered my sponsorship.
**Tigran Najaryan** 33:54 Okay, then… what I… one maintainer is not enough.
With OpenTelemetry, we always require multiple maintenance of repositories.
so that the repo is healthy. I would need to see at least one more person So that we can go ahead with that idea of additional repository, or pump-related repository. I'm… let me be clear, I'm very glad that you're offering your help.
But I don't want you to alone be, I guess.
**JM Juande Manjon** 34:28 Yeah, we would not…
**Tigran Najaryan** 34:29 The burden of maintaining that repository on your own.
If you can find one more person, and typically we have the requirement that it needs to be from a different company.
If we can have two maintainers, then we can go and make the request.
for a new repository and explain what we're doing there. But those are the typical rules. We need more than one maintainer, and the maintainers need to be from different companies. If we do that, I would still be very careful about what we're publishing as Go packages.
So that perhaps you do… you still keep it as an internal package, but you build it maybe as a Docker image that can be used in the demo, so that the containers are public, but the Go code It's not importable, unless you make a… An explicit decision that you want to make it important.
**JM Juande Manjon** 35:22 That sounds good as well.
**Tigran Najaryan** 35:26 Okay, so let's do that. If you can find one more person… let's then discuss. We should still get the, the GCs approval on creating the repository, but I think then, if that happens, we can have a case and explain why we want a separate repository, why we want it to be a different place, and we will also show that we have staffing necessary with two maintainers.
To go ahead with that, we can go and create a community reply issue for creation of the new repository.
**JM Juande Manjon** 35:59 Okay, great. I would like to find someone else. Thank you.
**Tigran Najaryan** 36:02 Oh, wow.
Thank you.
Okay, Anish, you have the next one?
**Aunsh Chaudhari** 36:08 Yeah, I think this was in line with the discussion that Douglas and I were bringing up, right? We started this discussion, Dimitri was, bringing up the topic that we at Splunk were interested in.
remote configuration capabilities in Kubernetes beyond what's already available with the op-amp bridge, right? And… I think that's the issue that's already been created by Dimitri. The goal was just for folks to take a look, offer feedback, share any reviews as well, thoughts there, right? I don't… Jacob and Dimitri have already been discussing their thoughts there, but yeah, feel free to basically review what's being proposed there, and if folks have any questions there, that'll be great to discuss on the next SIG if needed.
**Tigran Najaryan** 36:53 I don't see Jacob's comments on that issue. Did they discuss it in person at KubeCon?
**Aunsh Chaudhari** 36:58 Yeah.
**Tigran Najaryan** 36:59 Okay, okay.
Okay, we should ask Jacob to post his thoughts on the issue as well, so that we… We have a public record of that as well.
And I'll take a look at it myself.
**Andy Keller** 37:13 Yeah, and I don't… I don't see it mentioned here, but it was… it was an interesting conversation.
Basically, this operator was conflicting with another operator.
And it created some extra complexity, and they'd like to just keep Their own management of… Kuberry's workloads separate, and let AppyUp manage the config maps.
But the conflicts, the… Which makes sense, you can have that happen.
**Aunsh Chaudhari** 37:47 Yeah.
Yeah, I think we discussed that we'll need to basically be careful that it doesn't land up being very close to the operator or the offline bridge itself. If we're going down this route, yeah, there needs to be… need to make sure that there are no conflicts in terms of the two channels that are available, right? Yeah, so I think that needs to be cleared, yeah.
Okay.
So I think the next one… yeah, I just wanted to basically just raise a question around If there are any questions, like, if there are any changes in terms of the spec for SDK itself, right? I know some of the Java, or… implementations of the op-amp client within each of those SDKs have been… started to be built, right? I think we had… I think I had certain comments that we want to make on the identifying or non-identifying attributes, so… I just wanted to clarify whether this is the spec, the OPAM spec.
is the best place here itself to make any comments around SDKs as well. I know right now there's been A discussion on identifying non-identifying attributes focused on the selector.
**Tigran Najaryan** 39:06 Yeah.
So, I think, Ash, what… what we should do is… Keep the OPAMP spec document, generic.
So that it doesn't have… I mean… Too much specifics about the specific agent types that we want to support.
And I know we already have those types of specifics for Rotel Collector in the spec. I think what we should do is have, sort of a supplementary guidelines or something like that, a separate document that can live next to the spec, which says.
okay, how can I use the OPAM spec with AutoCollector, or with Auto SDKs, that can be in the… in the same repository as OPAMP spec repo.
or maybe even can be in the hotel spec repo. We can decide where exactly we want to place that, but I would like to have that clear boundary between the generic OPAM spec and how we apply it to OpenTelemetry assets.
the wording that we have right now in the spec about hotel collectors, I would like that to move to that separate document as well, and then in that same document, we can add the guidance for the OPL SDKs. So we will have, essentially.
the spec doc as it is now, which is the generic OPAMP protocol specification, and another separate document which says, here's how you apply Opamp spec for OpenTelemetry Collector, OpenTelemetry SDKs, and stuff like that. We have the… We have similar things elsewhere in the spec, where there's that, like, the… the generic spec, and then there's supplementary guidelines that give additional clarifications about how you use the spec and all that stuff. I think that that fits.
the exact place, we can decide where is the right place for it. The same repo, or maybe the spec, the big spec repo as well. We can do that. But I think that's what I would like to do, so that We don't… we don't pollute the generic protocol specification with the narrow concerns of each individual type of the agent that you want to handle using… using Copart.
Then… then… and then we will be free to add more if we'd like. Like, maybe Kubernetes concerns, other… other types of agents, maybe, maybe. There's a variety of… ways you can apply the generic op-amp spec to these different environments and use cases, so those we can capture. I think it's fine for us to have an opinion about those.
And the fact that we have so many questions, I guess, is a clear indicator that we need, somehow, the clarifications somewhere. But I would prefer them to be outside of the protocol spec, which is… which is the generic functionality you get inside the hotel. Essentially, the spec should be what you have in OpumpGo as a generic implementation, and OpamGo has no opinion about the collector behavior or the SDK behaviors. It's a protocol implementation, it's a client and server implementation.
The rest is how you apply the protocol for your particular agent type. That, I think we should capture in the separate doc.
**Aunsh Chaudhari** 42:36 Okay.
**Tigran Najaryan** 42:38 But I think, yes, we can capture it. We still… it's okay for us to have an opinion about those things, and and say that this is how we think OPAMP is best to be implemented for SDKs.
**Aunsh Chaudhari** 42:52 For other… yeah, for other.
**Tigran Najaryan** 42:53 Yeah, and for, yeah, for any other use case that we have for hotel assets.
**Aunsh Chaudhari** 43:00 Okay.
Okay, we'll start there, and then we can determine the location, as we discussed. Sounds good.
**Tigran Najaryan** 43:06 Yeah, yeah.
And if you want, you can maybe start with filing a… to request which extracts the existing wording for Autel Collector into a separate document, which will be the place where we add the others.
**Aunsh Chaudhari** 43:25 Will do. Thanks.
**Tigran Najaryan** 43:26 Yeah.
Okay.
What do you think, Andy? Do you think that works for you?
**Andy Keller** 43:33 Yeah, I think that makes sense, and I agree that the spec should be generic and not really… really targeted on the protocol. I will say that, the word agent has become problematic.
When discussing this kind of stuff with people, because people only think agents are AI these days.
So, I don't…
**Tigran Najaryan** 43:54 Yeah.
I don't know what to do about that.
**Andy Keller** 43:57 I know, it's a little late, it's a little late.
**Tigran Najaryan** 43:59 I mean, it's.
**Andy Keller** 44:00 an acronym.
But people think, you know, they hear Agent Management Protocol and… Yeah.
Got some interesting, interesting discussions with KubeCon related.
**Tigran Najaryan** 44:10 We should have some disclaimers, maybe non-AI agents.
**Andy Keller** 44:14 Exactly.
telemetry agents, I mean, it is…
**Tigran Najaryan** 44:18 Yeah.
**Andy Keller** 44:19 I wasn't…
**Tigran Najaryan** 44:23 Okay.
**Andy Keller** 44:24 I'm trying to find a link to it. I don't know if, I think it was in my LinkedIn, It just reminded me that somebody's working on a, A fluent bit.
op amp.
Implementation?
And I don't remember who it was.
And I don't think it's public yet.
But I wasn't sure if anybody else had come across that.
But it would be cool if that happened.
**Tigran Najaryan** 44:52 No.
Yeah.
**Andy Keller** 45:00 Alright, well, that's…
**Tigran Najaryan** 45:01 Okay, I think that's all we have in the agenda.
Anything else, anyone?
All right, thank you all.
See ya.
**JM Juande Manjon** 45:17 Bye.
