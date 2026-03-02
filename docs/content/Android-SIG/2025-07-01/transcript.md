SIG: Android SIG
Date: 2025-07-01
Duration: 29 minutes
============================================================

## Zoom Recording Transcript

**Jason Plumb** 01:03 Hello!
**Cesar Munoz** 01:08 Hey Jason.
**Jason Plumb** 01:10 How are you doing.
**Cesar Munoz** 01:12 I'm doing good. Thanks. How about you?
**Jason Plumb** 01:15 Are you back from vacay? Is that what I'm remembering.
**Cesar Munoz** 01:18 Yeah, it was really just 2 days off.
Nice that I, you know, put it together with a great, a long weekend.
**Jason Plumb** 01:28 Cool.
**Cesar Munoz** 01:31 But I usually I usually don't take vacations during summer, which
I know it kind of sounds strange.
but I kind of prefer them in in Christmas.
**Jason Plumb** 01:41 Yeah.
**Cesar Munoz** 01:42 You know.
**Jason Plumb** 01:43 I get it? It only sounds strange because you're a Spaniard.
Otherwise I totally get it. I I like both. I mean, especially up here. People like to take vacation to where it's warm.
**Cesar Munoz** 01:57 Got him?
Can I see.
**Jason Plumb** 01:59 But the other way around.
**Cesar Munoz** 02:02 I see.
Well, I would.
**Jason Plumb** 02:05 But we have no agenda. So
it's pretty light today. I think so.
**Cesar Munoz** 02:09 That's fine. Did I miss anything last week?
**Jason Plumb** 02:12 Or at least anything.
**Cesar Munoz** 02:15 Really important, or.
**Jason Plumb** 02:18 You know there has been a huge snafu with Sonotype. I don't know how closely you've been following it, but
You know, yesterday was the last day that Sonotype supported the Oss Re.
**Cesar Munoz** 02:31 Legacy. Yeah.
**Jason Plumb** 02:32 Yeah, their legacy stuff. So you know, we were trying to get ahead of that curve. But there were some. There are some challenges around that specifically they took down the
snapshot browser. So here's the old snapshot browser right?
And just for an example, if you go into here.
there's nothing past June 25, th or really nothing past like June 5, th because that's we made a change right? We switched over on the 20, I think on the 25th
**Cesar Munoz** 03:05 Got it.
**Jason Plumb** 03:06 And then the new. The new snapshot is
here is where it's supposed to be.
And you know, I've emailed them about this. I opened a support ticket, and the the long and the short is they've intentionally taken this down because they have some problem in the back end.
So the the snapshots
are working. Those artifacts are actually in the repository, and publishing is succeeding. They've just taken down the browser portion of it, so you can't
actually see your artifacts, or confirm that the snapshots are working.
**Cesar Munoz** 03:42 See.
**Jason Plumb** 03:42 So that's, you know, a little bit troubling. So we talked some about that, because I think clever check and others were like, well, we know the view. Click instrumentation got merged, but we can't find the snapshot.
And there was a lot of talk around that there was also time.
**Cesar Munoz** 03:59 The snatch.
**Jason Plumb** 04:01 It's the.
**Cesar Munoz** 04:02 It's.
**Jason Plumb** 04:03 You for instrumentation. All there's an issue on that. Now.
**Cesar Munoz** 04:10 Oh, I think I saw that it actually sounds like a pretty good idea to be honest.
**Jason Plumb** 04:13 I think so too. I think the main challenge is for anybody who wants
specific kinds of build time instrument in instrumentation, but not all of them.
But anyway, there's an issue on it. Now. That was a follow up
After that discussion. I think it's a really good idea. It's for people that maybe don't, for whatever reason want to use. Well, even if they do want to use the agent, maybe they want additional instrumentation at the
opinionated agent doesn't yet include. So they can just get all right.
**Cesar Munoz** 04:48 Yeah, everything that we have.
**Jason Plumb** 04:49 Yeah.
Seems like a pretty low impact change.
**Cesar Munoz** 04:56 That I think that sounds like a good idea.
I will guess that probably. Well, this
probably more than one way of doing that, and
from a 1st glance to me it seems like the
probably the best approach will be
by creating a greater plugin, because
a greater plugin can add other plugins on on a project.
and part of adding the all instrumentations is that at some point you will have to add instrumentations that do by code weaving which need
the by body, Plugin. So I don't know if if it's a matter of
convenience, that's probably, you know, kind of like a single line to add everything way to do it.
Otherwise I'm guessing.
Yeah, I guess we'll we can just add, as part of the read me, just, you know, add this 5 body, Plugin, and then
these, these other dependencies.
**Jason Plumb** 06:12 Right, right.
**Cesar Munoz** 06:14 So, yeah.
**Jason Plumb** 06:15 So I think I think we did a little code inspection. We determined that right now, if if we had an instrumentation, all module and you include it. You would get all of the build time instrumentation, which maybe, you know you could. I think I've convinced myself that that's what you want right. If you've included the All, then you.
**Cesar Munoz** 06:33 Yeah, if you don't.
**Jason Plumb** 06:34 Time and runtime. So, yeah.
**Cesar Munoz** 06:38 Definitely.
**Jason Plumb** 06:42 Hanson talks a little bit about the Colin Api, and he's out today because it's Canada day.
**Cesar Munoz** 06:50 I saw that message.
**Jason Plumb** 06:51 Assuming Hira already knew that. But
How's it going? Hyro?
**Jairo Mendoza** 06:58 Going good. How are y'all doing.
**Jason Plumb** 07:00 I'm pretty. Okay.
**Cesar Munoz** 07:01 All good. I know.
**Jason Plumb** 07:02 If you have any specific topics, we're really light today, so feel free to add them.
**Jairo Mendoza** 07:07 Yeah, I don't really have anything. I'm usually a fly on the wall for these meetings.
**Jason Plumb** 07:11 Yeah, that's cool. I mean, you're welcome to do that, or you're welcome to help out as much or as little as you want, I mean, and by help out, I just mean, you know, contribute to the conversation, ask questions, review
and submit. Prs. All of that is very helpful to the project.
**Jairo Mendoza** 07:29 Got it.
**Cesar Munoz** 07:30 Definitely
also, coming back to the Maven Central stuff, I'm confused because I saw I I could swear that I saw this
snapshot website working at some point a couple of days ago.
**Jason Plumb** 07:46 It was always, yeah,
**Cesar Munoz** 07:48 Then I get a 4 0, 4. Today.
**Jason Plumb** 07:50 Yeah.
**Cesar Munoz** 07:51 Same link.
**Jason Plumb** 07:52 I know they've taken it down.
**Cesar Munoz** 07:55 But it's like going up and down all the time, or is it? They just took it down
for good until.
**Jason Plumb** 08:00 15 until they can fix the bug. Let me find the.
**Cesar Munoz** 08:05 Got it.
**Jason Plumb** 08:08 Let's see, I will. I'll show you this this issue that I opened one sec.
**Cesar Munoz** 08:15 Got it. Thank you.
**Jason Plumb** 08:17 Yeah.
**Cesar Munoz** 08:17 I haven't been chewing the loop with this issue. I thought it was, you know, all working well.
**Jason Plumb** 08:22 You can see my email now, right.
**Cesar Munoz** 08:25 Yeah, because they did go, you know, forward with the the with the sunset date.
**Jason Plumb** 08:34 That's right.
Yeah. So I asked, and I said I couldn't browse snapshots, and it took them a week, but they got back to me, and they said, due to a bug with the underlying service, we cannot provide
browse access.
but you should still be able to publish and consume them, but you can't browse them in the ui.
which I was like. That's cool. But is there any other way to verify that one worked and is available
other than consuming it, which I you know I I recommended to a colleague
yesterday that they build a toy project, and just like consume a snapshot and see what version they get.
But and are you gonna fix it? And the answer was, There's no other way, and once the bug is fixed. We we hope to have the browser support again soon. So it's you know. It's probably
a week or a month or something. I you know that's unfortunate, but that's the way it goes.
**Cesar Munoz** 09:29 Thanks him.
Okay, but it then. Okay. But I didn't understand that part that you mentioned. That's still snapshot snapshots are still working for projects.
**Jason Plumb** 09:39 That's right.
**Cesar Munoz** 09:39 At least. Okay.
**Jason Plumb** 09:41 Yeah. So do you think we should talk about the release?
Yeah. So we should still be on merge domain. We're still publishing like, what's the last thing that we merged like this is code. Ql, it doesn't count. Stale doesn't count this one. No, that's a no, it's not main. Here's main management issue issue. Here's 1. Okay. So yesterday we merged this dependency update. And if we look at
this Nope, that's the branch I'm I'm still waking up.
If we look at this well, why did it go here?
That's the oss. Oh, it's the scorecard we just want to build. Here's a build. Okay?
So if we look at this
and we drill down into published snapshot
should work.
Yeah. So it's doing all the different phases, and then
publish to Sonotype, published a sonotype. Right? This. This is all related to publishing.
and it's a snapshot because we're not doing a release and seems to have worked right.
**Cesar Munoz** 10:59 Yeah.
**Jason Plumb** 11:00 So there's no, there's no build fail failure. So every indication is that it worked
the way to test it would be to like fire up the demo app, and instead of taking the dependency on the module, on the on the local module, you can take a dependency on the snapshot.
but we are due for a release. I was hoping to get it started yesterday, and didn't get around to it so apologies on that. But we, now that upstream has released so instrumentation
has released a oh, they still haven't.
They're they're trying to get a 17 wall. I think the goal is to get a 17 one out.
**Cesar Munoz** 11:43 Probably gonna be this week.
**Jason Plumb** 11:48 Maybe I'm wrong about that. Maybe.
**Cesar Munoz** 11:51 The one I think waiting for the most is a country and I think.
**Jason Plumb** 12:00 Yeah.
**Cesar Munoz** 12:00 They also haven't twitter, release.
**Jason Plumb** 12:07 It's true
we are pretty behind, unfortunately, is the is the thing I would love for us to get one out, but.
**Cesar Munoz** 12:18 Alright. We can create one.
**Jason Plumb** 12:19 Yeah.
**Cesar Munoz** 12:20 It's just not gonna get the
**Jason Plumb** 12:24 It won't have that in trip. Fix is the problem
Trask is out the rest of this week.
I can ask Lori, but it seems unlikely. It's gonna happen this week, you know. Friday is a holiday in the Us. So it's a
short week.
but I will. I will go ahead and ask and see what that's about, and maybe we'll just punt on doing a release until next week.
I hate to.
**Cesar Munoz** 12:59 I, yeah, I get it. But it's like.
without the country stuff. It's you know. I mean, we we can still create it.
I I. It's not like I'm against creating it this week, but it's just that really the country stuff. I think it's the
bigger piece here.
**Jason Plumb** 13:15 I think what I should be.
**Cesar Munoz** 13:16 That's good.
**Jason Plumb** 13:17 Do. I have the ability to do a release? I've never done one in contrib.
I bet you I don't.
Let's see.
Prepare the release branch workflow.
It looks like I I do have that ability. That's good.
A patch release. No, I think that's all. It is right.
**Cesar Munoz** 13:52 If you scroll to the bottom, there's a making the release. Yeah. Can can you
click there? Can you run that.
**Jason Plumb** 14:00 I can.
**Cesar Munoz** 14:01 It's like.
**Jason Plumb** 14:01 So.
**Cesar Munoz** 14:02 Yeah.
**Jason Plumb** 14:03 I think, as a Maintainer I can do a release, but I want to run it by people
I mean, I think it'd be fine, and since it's been so long, I'll just ask. And and if people say yes, I'll just try it.
Okay, I'll try and I'll try and release contribute today. That'll be that'll be one of the things I get done hopefully unless they get, unless they say no, in which case I'll let you know.
**Cesar Munoz** 14:27 That that's fine, and if there's anything I can do to help, please let me know.
**Jason Plumb** 14:34 Sounds good.
Okay. Do you wanna take a few minutes and look at the pull open pull requests.
**Cesar Munoz** 14:44 Let's go ahead.
**Jason Plumb** 14:46 If we start at the bottom it'll go fast. So this person just has not come back around, I think.
Okay, so yeah, there it sounded like they were still around, but they haven't come back back to it.
**Cesar Munoz** 15:06 Yeah.
**Jason Plumb** 15:07 This one.
February.
Oh, yeah, this was a weird one.
**Cesar Munoz** 15:17 I think we kind of decided that it's not needed.
I don't know why kind of remember that. But.
**Jason Plumb** 15:23 Yeah, it's true. We're like, 2 months.
**Cesar Munoz** 15:29 Or maybe we're just waiting for them to come back.
**Jason Plumb** 15:34 Let's see what they say. So how did I leave this? Did you have another use case? I have a question. So
let me just tag them real quick.
Okay?
Cause it was. It did end with a question. Just want to see if it just I wanted to ping them and see if they'll come back around
this one survey has basically abandoned. It looks like, so I I'm inclined to close this. But
let's close it. You asked her a long time ago.
Well, over a month ago.
**Cesar Munoz** 16:23 Yeah.
**Jason Plumb** 16:24 And I labeled it, okay, so let's just close it.
**Cesar Munoz** 16:30 And probably what she wanted to do there, it's already there.
Maybe that's what I was mentioning in the comment.
**Jason Plumb** 16:39 I think that's fine.
9, 47 was.
Oh, yeah, the config for disk buffering, which is cool. Where are we on this one?
Where do we leave this one?
Okay, they were busy.
Okay, we'll be patient on that one.
Oh, yes, we talked about this one, didn't we?
This is an automatic update. It's a huge version jump.
We kind of know why.
And there was an issue that we got created to support this right? Yeah, integration testing. Okay?
Oh, and it's assigned to clever check. Okay, cool.
We can just move on from that one.
This is new.
That's just a dependency update.
**Cesar Munoz** 17:53 I'm looking at this now, and I'm realizing it's a it's a patch version.
**Jason Plumb** 17:58 And in some of the other repos
and some of the other Java repos. We're now grouping the patch patch.
The renovate patch updates are all grouped together, and they do them like, I think, once a week.
so that they don't get so so we're not thrashing so much on that we could consider that if if you think there's a lot of thrashing, I don't think it's that bad
like. I don't mind just coming in and merging this right? It's pretty fast.
But I think there was an I think, in the other repos. The dependency lists are so big, especially in instrumentation
that, having patch updates all week is a hassle.
**Cesar Munoz** 18:40 Sounds like it. So far I haven't. It hasn't been an issue for me, and, to be honest, I haven't even checked
which ones are patches.
**Jason Plumb** 18:50 Okay.
**Cesar Munoz** 18:51 Ones are just minor stuff.
I just see I bear some bumping it, merge it.
**Jason Plumb** 18:58 Okay.
**Cesar Munoz** 18:58 So.
**Jason Plumb** 18:59 Yeah, I think we. I think we can wait on that. I don't think it's super important. So what is okay, this is interesting.
Please check the spirit carefully and watch out for any permission related. Workshop workflow failures after merging it so open telemetry.
**Cesar Munoz** 19:14 But yeah, it's why. But I saw that. It's it's ceasing, Trask. And I don't know. It's yeah.
**Jason Plumb** 19:26 So they're locking stuff down a little bit. Our build no longer has the ability to create issues.
But the workflow notification gets a new permission.
**Cesar Munoz** 19:42 To create them.
**Jason Plumb** 19:43 That can create. So it's moving right? It's explicitly adding, read, and then, I mean, this seems fine to me.
**Cesar Munoz** 19:51 Like making the writing permissions.
**Jason Plumb** 19:54 Yes.
**Cesar Munoz** 19:55 More specifics.
**Jason Plumb** 19:55 To the workflow that needs it. Yeah, I think this is fine.
**Cesar Munoz** 20:05 For me. We can merge it just not, you know, haven't been in the loop of this Ci changes that I know trust has
carried over.
**Jason Plumb** 20:20 Oh, that's interesting. So they're making the Github Token permissions read only.
But then in this one, maybe, that
if the I don't know how the I'm unclear on how the token is used
in that context, because it's not mentioned explicitly.
Okay, so it's just more granular. I guess. Okay.
**Cesar Munoz** 20:55 So it's like, yeah. Because, he he added, there the word default. So it's it's only gonna be. So we will get right
permissions with the same Github Token, when you know.
**Jason Plumb** 21:07 The steps that need it.
Okay, I I think that's I think this is no brainer. Then I think I think we're good.
Are you? Are you good with this.
**Cesar Munoz** 21:16 Yeah, that sounds good.
**Jason Plumb** 21:17 Okay.
okay, so yeah, we just need to keep our eye open for any, any actions that might fail after that.
But I think we're good. Okay? Well, that that chips that down a little bit.
I don't have any.
That's not true. I don't.
I was gonna say, I don't have any real work in progress that I'm actively pursuing an android. But it's not true. I'm still trying to figure out how to do.
I'm still investigating how to do a proper
session based sampler that samples both spans and logs.
So there's spans and events, and I haven't. I haven't touched it. In a week or so. We you know, we had the open source summit last week.
Yeah. So I'm just I'm behind on that and working.
**Cesar Munoz** 22:11 But it sounds like.
**Jason Plumb** 22:12 And working on a hundred other things, too.
**Cesar Munoz** 22:15 I I see what you mean. It's kind of similar situation for me I've been thinking
about because I was checking the instrumentations that we have the automatic instrumentations
and notice that some of them don't have instructions on how to install them.
So I was able to just create a Pr. To add those changes to the readme files.
**Jason Plumb** 22:43 Yeah, on how to install them. That's a good question, like what one is specifically.
**Cesar Munoz** 22:49 So the logs, for example. Android lock.
**Jason Plumb** 22:56 This one.
Yeah, it has. It says what it generates, but not how to use it.
**Cesar Munoz** 23:02 Yeah.
**Jason Plumb** 23:02 Okay.
**Cesar Munoz** 23:03 Things like that should be straightforward.
I'm actually gonna create an issue. There.
**Jason Plumb** 23:21 And would it be possible for you to be specific on which ones need it which re which modules which instrumentations need it.
**Cesar Munoz** 23:29 In the issue. Yeah, yeah, it's fine.
**Jason Plumb** 23:33 Okay.
**Cesar Munoz** 23:34 I'll have to check after the call. But yeah.
**Jason Plumb** 23:36 Sure, but some of them like don't really need instructions right? Some of them are straightforward, I think.
**Cesar Munoz** 23:43 I mean at least you it, I think, for all of them. You at least have to have one dependency. So you need to have the dependency, Uri.
There.
**Jason Plumb** 23:54 Or or use agent for a lot of them.
**Cesar Munoz** 23:59 The agents.
**Jason Plumb** 24:03 Right. If you depend on the or
depend on the agent and use the initializer.
then you get all those for free, because.
**Cesar Munoz** 24:12 The ones that are in the dependencies of it.
Yeah, those.
**Jason Plumb** 24:17 Yeah.
**Cesar Munoz** 24:20 But you know, these are.
these are independent, too. So if you're not using the agent you might.
It's like just having the coordinates. What should I ask? The dependent.
**Jason Plumb** 24:32 Yeah, that's cool. I think that's a good idea. I think that's helpful. Did we? Did we finish adding.
the readmes to all of the instrumentations. You know we there was an issue on that.
**Cesar Munoz** 24:46 I'm not aware of it.
**Jason Plumb** 24:48 This one.
So we're about half so fragment is missing. Oh, let's see.
**Cesar Munoz** 24:56 So maybe we can reuse that issue.
**Jason Plumb** 24:59 Well, let's see, what is it specific?
This, this was intended. My my goal of this was to like what telemetry is provided by it.
But if you wanted to piggyback on that, it'd be fine. It's just we've already completed half of these.
so I think a new issue would be better.
**Cesar Munoz** 25:19 Okay.
**Jason Plumb** 25:19 So fragment.
It has been done. We have fragment right? Why is that not checked? Fragment is good.
Http. URL. Connection.
**Cesar Munoz** 25:31 Yeah, that's on that actually has the instructions to install it.
**Jason Plumb** 25:34 Didn't have the telemetry.
It does.
**Cesar Munoz** 25:37 Oh, what what it! Oh, I see! I see!
**Jason Plumb** 25:40 Let's leave that one. And then network.
I think you can just tell right now. It's already been.
It's already been done. I just probably didn't come back and click it.
Yeah. So that's cool.
Assuming it's still correct.
And then, okay.
still missing, I'm gonna add, Okay, http, let's see if that has it the websocket one.
No. So I'm gonna edit this and add, Okay, Http, websocket, yeah.
And what was the last couple here? Startup and volley.
**Cesar Munoz** 26:42 Volley. I think we have to.
I think volley is the one
I think it's the one that is still not usable.
**Jason Plumb** 26:54 I mean the idea.
**Cesar Munoz** 26:55 The injection, the installation.
**Jason Plumb** 26:59 The build time, or at all like it doesn't happen.
Yeah, it's only hybrid, right?
**Cesar Munoz** 27:09 I think it needs everything to to.
Yeah. And it's an instrumentation
implementation. And if it needs to get.
you know, in injected with biocode instrumentation, then it also needs the the plugin. There.
**Jason Plumb** 27:27 Yeah. So we have an issue on build time. But we don't have
okay.
**Cesar Munoz** 27:35 It needs real time stuff. Then.
**Jason Plumb** 27:37 Yeah, yeah. And no one's expressed interest in volley lately that I've heard of. So maybe
I'm I'm fine just letting it sit there. I don't think anybody's using it.
Okay, well, so this is coming along. There's there's some low hanging fruit. If people
yeah, I have help wanted on there, let's put good 1st issue.
If people want to help out with that, maybe they can find it that way.
Okay.
**Cesar Munoz** 28:04 Sounds good.
**Jason Plumb** 28:11 Okay, cool anything else. I'll just I'll I'll I'll mention
this issue since we talked about it in the Sig. That's not what I meant to do. That's
what I meant to do.
Okay.
**Cesar Munoz** 28:39 Nice.
**Jason Plumb** 28:40 That's all I got.
We both have an action item.
Hiro, do you want an item.
**Jairo Mendoza** 28:49 Yeah, I mean, sure, if there's like a
an an issue, I could start working on.
**Jason Plumb** 28:54 I mean, if you want to pick up one of these, it would be awesome. So this is to document what type of telemetry is created for each of these instrumentations, and we have examples of previous prs that add these. But really there's like a few that are left. The easy ones are probably startup is probably the easiest.
The Http ones
generate spans. It's based on the upstream instrumentation. So you can pick through that. And just, you know, indicate that it's client spans, and, like whatever attributes go on there, or just, you could just point to the Http semantic conventions honestly.
**Jairo Mendoza** 29:30 Okay for?
Okay, I'll look into them.
**Jason Plumb** 29:34 Okay, cool. Thanks. Appreciate the help. Always. Always.
**Cesar Munoz** 29:38 Thank you.
**Jason Plumb** 29:38 Yeah, cool.
**Cesar Munoz** 29:41 I think that's it for today. Then.
**Jason Plumb** 29:43 Sounds like it
alright. Well, I'll see you see you next week, and I'll let you know about the contribute. Release.
**Cesar Munoz** 29:51 Thank you. Talk to you later.
**Jason Plumb** 29:53 Take care!
**Cesar Munoz** 29:55 Twig.
**Jason Plumb** 29:55 Bye.
