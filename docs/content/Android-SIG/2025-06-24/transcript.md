SIG: Android SIG
Date: 2025-06-24
Duration: 55 minutes
============================================================

## Zoom Recording Transcript

**Hanson Ho** 00:34 Hmm!
Good morning.
**Jason Plumb** 00:51 Hello!
**Hanson Ho** 00:55 How's it going.
**Jason Plumb** 00:58 Just waking up.
**Hanson Ho** 01:01 Are you actually on Pto right now, Jason.
**Jason Plumb** 01:03 No, which is why I'm here.
**Hanson Ho** 01:07 We said, you're a terrible Pto, so I thought you're like,
**Jason Plumb** 01:12 That's why. Yeah, I'll be around.
Oh, I'm not sharing my screen.
That would help.
Okay.
alright. We are at 2 after. So I think we should go ahead and get started. I think Cesar and Manuel both said that they were not going to be able to make it today, so
we'll jump right in, and clever Chuck has an idea.
and he is not here yet.
**Hanson Ho** 02:09 Hmm.
**Jason Plumb** 02:10 But we could talk about it. It's I think it's a pretty straightforward idea.
So as things are laid out right now in the repo. We have
a set of instrumentations right? And these are what we support currently, and not all of them are included in the agent, the agent being kind of the top. Hey, clever Chuck, we're talking about your idea already.
The agent, the agent here is the top level.
construct that we expect that most users will want to use it should be. It's intended to provide the simplest setup and the most common instrumentations, but it does not include everything from the Instrumentation Directory. And so I think the idea here is that we could make a new module that would sit parallel to the agent, and would be called instrumentation. All and all it would do is just take all of these right, so you could include
one dependency and then source all of the instrumentation.
Right? Did I get that right?
**CleverChuk** 03:21 Okay, yeah.
But I'm starting to think about it a little.
it might have an issue with the ones that have, like the agent stuff like where you have to like use like the bite body to like. Do do some stuff so those ones you can't really like
Use them all from that package. That module, if we like, created it.
**Jason Plumb** 03:51 Right.
I mean, it would be purely to ease dependencies like it doesn't necessarily mean that the instrumentation is initialized right.
**CleverChuk** 04:02 Right.
**Jason Plumb** 04:05 So you're saying that if someone needs the the bite, buddy build time instrumentation, that, depending on the all instrumentation, all would not allow them to apply the plugin, or what? Where's the shortcoming?
**CleverChuk** 04:20 Yeah, it does is essentially what I'm saying.
**Jason Plumb** 04:22 Okay.
**Hanson Ho** 04:26 Well, where where the instrumentation lives. Really, you know, if it's part of the project whether it's a separate module or the same module. It doesn't really matter a ton. If you build it and you're not using it. I think our 8 will strip it out. I think the more interesting would be to pull out
instrumentation. That doesn't depend on anything that is offered by the agent so similar to Ktp. Where you could use this theoretically anywhere if you could actually pull those instrumentation out to separate modules and eventually, maybe even to a to a different project altogether. I think that would be interesting.
consolidating existing dependencies.
I think I think it's I mean it's it. I think there's some utility, but it it more becomes kind of organization rather than
providing like a
something, you know, very specific to the end user. is the reason why you want to do this clever check to just ease the number of modules that are included? In in an app, or or is there some other kind of you know modulization reason that you wanna you wanna do this.
**CleverChuk** 05:42 Yeah, basically to is like, if you wanted to like, use all of them
a school in the ones that like ride bike body.
then it will be like easy to just
include that one so like going to like. Get them all individually.
**Jason Plumb** 05:59 Yep.
yeah, I can definitely understand that for someone that doesn't want to use the agent necessarily, but they do want at least to be able to easily pick and choose instrumentations to install. Then it's 1 dependency, instead of having to go hunt down coordinates for all of them, and I
I don't know that we publish a
well, I I don't think we publish a bomb yet, do we? The
yeah. So that makes harder. I think there's an issue.
**Hanson Ho** 06:30 We don't, really. We only have one version for our modules. Right? So it's not like we have. At least, I don't think that we have, we? We release different versions of the instrumentation modules. I thought everything under the android android is is just one version.
or am I wrong?
**Jason Plumb** 06:53 No, they're all version together.
**Hanson Ho** 06:54 Okay. Okay.
**Jason Plumb** 06:57 Bye.
**CleverChuk** 06:57 Ups.
**Jason Plumb** 06:58 But still needing the coordinates like being able to to tell Gradle to use this top level bomb to source the versions, for everything is nuts.
**Hanson Ho** 07:09 Yeah. And and I, I think having a a project that basically includes all the other projects as as a I think that makes sense as well. We don't necessarily have to move it all and actually literally put them all in the same project. We just have a an overarching project that basically points to all the instrumentation. So we get that updated so folks will can just include the open telemetry android instrumentation module, and they get everything.
**CleverChuk** 07:36 Yeah. And another utility for that, I'm thinking, is like, so I'm making the SDK for the Solomons one, and I don't wanna depend on the agent so, but I still want users. If they use like the following SDK, they should be able to like, just pull the dependencies from the upstream one. So having this one, this instrumentation dash, or also like, make it a little bit more easier for them to like, add them
as well.
**Hanson Ho** 08:08 So so that that's when we have to make sure the instrumentation doesn't depend on things that are that are
that are in in the agent, and I well, hold on when you say agent, you don't. You don't just mean the agent right? You don't. You mean you don't mean core like, you're you're gonna have to use core like sessions. Okay? Okay? Got it? Got it.
**CleverChuk** 08:29 Yeah. Yeah. The agent package.
**Hanson Ho** 08:32 Okay. All right.
**Jason Plumb** 08:37 What would. Yeah. So if if you just wanted to get everything, or if there's stuff in that agent does not include, then you have to go track it down. But if we had an all package, then it's more easy to to find.
since since I'm looking out here.
what happened with our bomb like it it apparently. We published the bomb for a little bit, and then we stopped.
**Hanson Ho** 08:57 Oh, oh, I guess our bomb includes the Http version.
**Jason Plumb** 09:02 Did it? Did it change coordinates or something like, so we're up to? Oh, maybe that's maybe the I'm sorry. Maybe that is our version, right? Maybe we're just so far behind here. Okay, yeah, our version is really low. Okay, so we do publish a bomb. Now is the is the takeaway.
**Hanson Ho** 09:17 Oh, cool!
**Jason Plumb** 09:18 These do declare
everything right, so you could at least get your version information from the bomb, and that should help.
But it doesn't necessarily tell you every instrumentation. Right? You'd you'd still have to
declare in your gradle or tomil each of these instrumentations that you care about.
**Hanson Ho** 09:41 Yeah, I I think having an overall package makes sense then, especially for for that use. Case. Clever chat.
**Jason Plumb** 09:46 So can we think of any ways to mitigate? This right. This is the shortcoming that if these coordinates were inst instrumentation, all.
Then you can't tell Byte Buddy specifically which one to apply. There's something in
the module itself that tells it something. I don't understand how this works well enough to say.
**Hanson Ho** 10:09 You could. I mean, it's it's cradle. So you could.
Do you want a specific byte buddy version, or or an android open to entry Android version.
**Jason Plumb** 10:24 Bye.
I think the challenge is that when you want to use build time instrumentation, you declare it like this.
And if if the coordinates for this were instrumentation all.
and then, whatever the version is, that's fine. But then, Byte, Buddy, I think in inspecting that package. It's looking for something probably implement like probably in spi.
and there would be multiple. There could be multiples from different modules. And so you
necessarily be able to say which one to apply is that the challenge there clever chuck.
**CleverChuk** 10:59 Oh, actually no!
**Jason Plumb** 11:01 Okay.
**CleverChuk** 11:01 It's not. It's not a challenge. I'm thinking about it right now. So basically, if I'm thinking, if we do that, Bibles would just like. Apply all of them, which is kind of what you want for like including all right.
**Jason Plumb** 11:15 Okay, I could. I could be convinced, like we could make that a documentation problem.
Yeah.
**Hanson Ho** 11:23 Another way is to dynamically like, write, write a little plugin script that basically runs and picks up the projects that that
require this and basically manually put this in integrate all
But then that means you're you're writing
cradle code and plug in code. So
whether you want to do that is is, is a different question.
**Jason Plumb** 11:46 Yeah.
**CleverChuk** 11:50 So the question is, does that by body, Plugin? Is it gonna be able to like search the whole thing?
But does it? Will it still work.
**Jason Plumb** 12:04 Yeah, that's a Tbd, we would have to do some testing to find that out, because I don't. I don't know specifically it. I don't remember what the what it looks like.
**Hanson Ho** 12:14 It's it's gradle, right? So it should just be finding the appropriate gradle class. Yeah.
**Jason Plumb** 12:20 This is what tells it. So there's a
there's a resource that says which ones to apply. That's what it is. Okay.
So if we built the all package, we would either need to go out of our way to exclude these
and force people to if if they want build time, instrumentation, they would have to depend on them individually, or they get everything.
**CleverChuk** 12:42 Bye.
**Jason Plumb** 12:43 Yeah, okay.
**Hanson Ho** 12:47 What? What do you mean? They get everything like like.
**Jason Plumb** 12:50 If we built this all module, then all, then we would have. We would presumably we would merge all of the resources for all of the instrumentation, and there would be Buddy build plugins that contains
all of the not just the okay Htp ones, but all of the build time dependencies. And so when they declare
I think I already lost the line, but when they declare in their build gradle that they want bite Buddy to apply, it would apply all of them.
**Hanson Ho** 13:21 I need it.
**Jason Plumb** 13:22 Maybe what they want right?
**Hanson Ho** 13:24 If you're including a module that says all, then.
**Jason Plumb** 13:28 Original point. Yeah, if you're including all, you probably do want everything. Then.
**Hanson Ho** 13:34 And I think I think already is smart enough. If you're not referencing it at runtime, I think it'll it'll remove the the classes you know, from the built artif artifact. If it's if it's done in a way where you know, the build can figure out so
And if you don't, if you don't run, release and and and you know, do do all the the obfuscation and the you know, shrinking down thing then. Well, it's your problem.
**Jason Plumb** 14:18 That was weird.
Okay, I hadn't seen this little suggestion before. Okay.
okay, so I think that I think it's worth looking at for me. I think I think this is a good idea. I think there will definitely be a subset of users that will use this. We just need to make sure the documentation is clear about a couple of behaviors, and I think this is a welcome addition. Do you wanna make an issue for this.
**CleverChuk** 14:43 Yeah, I can.
**Jason Plumb** 14:44 Cool. Yeah, I think this would be welcome.
**CleverChuk** 14:48 Okay, cool. One question is, I haven't seen the view dash, click.
package like deployed. I don't see it when I check the maybe and stuff.
**Jason Plumb** 15:01 Cause it got merged right.
**CleverChuk** 15:04 No, no, not the not the composed one. The other one.
**Jason Plumb** 15:08 Did it get merged.
**CleverChuk** 15:10 Yeah, like a long time ago.
**Jason Plumb** 15:15 So you haven't seen the compose so.
**CleverChuk** 15:17 No, not the proposed view view. Dash, click!
You haven't seen the view click. Okay, so, and that.
**Jason Plumb** 15:23 Merged after the last release release which we're behind on.
So it was merged after 0. Dot 11 got published back in April.
so we would need to go look in snapshots. And there there is an absolute snafu happening right now with Sona type.
So I'm gonna 1st try and pull up.
Yeah, the old snapshots, which I think are here, android, and then it says, Click.
**Hanson Ho** 16:03 Do you click.
**Jason Plumb** 16:05 No, okay, so I don't see it here at all.
**Hanson Ho** 16:07 Well, this the last time it was April 16.th So this is also quite old.
**Jason Plumb** 16:13 April, June.
**Hanson Ho** 16:15 Oh, oh, the instrument. Okay. Oh, okay.
Boom!
**Jason Plumb** 16:21 But.
**Hanson Ho** 16:21 Dated.
**Jason Plumb** 16:22 We've definitely had stuff that merged since then. So let's check in the new place I was. I was. This is the last thing I was looking at last night before I had to walk away. But,
I will. I will explain what's a little bit about what I know what's going on, and it is
quite exciting. So I think that this is not the new one. It's a central. So this one
I did hit that snapshots.
It doesn't like that. You'd have to put a slash. And then I/O slash! No, you do browse.
**Hanson Ho** 16:58 This is the new hotness. Org Nope, I/O.
**Jason Plumb** 17:05 And open telemetry is not showing up in here at all.
So it was, I promise you. It was at some point
**CleverChuk** 17:15 Okay.
**Jason Plumb** 17:16 The snapshots look to be not really currently working with Sonatype.
They
had an issue yesterday that was pretty bad, and it lasted like, you know, it's like it's they're they're struggling right now. Okay, so their sonotype is coming up on a self imposed deadline of June 30, th which is one week away to shut down the open source. The ossrh repo. I think, Greg, or you've done this for some some repositories and move them over and stuff I'm assuming you're experiencing the same problem.
**GZ Gregor Zeitlinger** 17:53 We have the same problem.
And, Java agent, I'm i i'm not doing.
I release myself right now.
**Jason Plumb** 18:06 Okay?
So in this snapshot, let's just see for comparison.
Sona, type, central. Yeah, this is like supposed to be the new thing. So com.
Do we have signal effects in here? Com splunk? I mean, we do. So. This.
when was this last published? This looks like the 19.th So a few days ago.
Maybe we've definitely had commits since then. So I mean, I say, definitely, let's make sure.
just look at actions. Probably.
Yeah. So 9 h ago we had had a nightly build that should have published a snapshot which is not showing up in this. I at least I don't see it.
and I'll see the 24, th or the 25, th or the 23rd in here.
So I think snapshots are weirdly broken, like stuff might be going into a weird
state. I will also say that in Android, if we go to the same thing, actions. You know we had a merge to main. This is, this is sorry. These are different actions. But if we had
see.
okay, well, this is complicated. So this is what I was looking at yesterday. This one failed the Markdown link check
ironically, because our read me calls out where we publish now.
and we've updated it to the new location. So
what I attempted to do to resolve that was to
did it get merged? No, this one. So I could use a rubber stamp on this stupid pr, because I just wanna ignore that. So our build start passing so that we've got this catch. 22 where, like, our build doesn't pass because the link is failing, and the link is failing because our build doesn't pass. So I think if we get this one rubber stamped we can try it again, and hopefully, it'll it'll show up in the snapshots. But based on
the fact that we're doing the same thing in our splunk distro. And we're not seeing snapshots. And we're doing the same thing in Java core and the instrumentation repo. All of the other repos are doing the same thing, and none of them are showing up in snapshots seems to indicate a bigger problem. And I know that there are open issues that Trask is actively chasing down.
**Hanson Ho** 20:33 I've rubber stamped it.
**Jason Plumb** 20:34 Thank you.
**Hanson Ho** 20:35 I know I know the the non snapshots are fine, so we may be able to publish something. If we do it to the non snapshot boat.
**Jason Plumb** 20:45 One hopes. Yeah, one hopes. But we're also still waiting on upstream. First, st like, we want to be depending on the new version of upstream which has not dropped yet, because mostly because of can I?
that's not true. That's because of core. There's that fix in core to that that disk buffering and PE related problem. And so we we need to get the new core, which I think
we get through instrumentation right? We depend on the we. We depend on the instrumentation alpha bomb. So we gotta wait for that to Rev before we depend on everything new
and sometimes using snapshots is like a cool stopgap measure. But we can't even do that right now because of snapshots being snafu.
So I apologize for this. I wish we had more
more insight. I'm sure that they are just overwhelmed with people trying to migrate before the deadline and stuff is not.
you know, it's not. It's not robust.
**GZ Gregor Zeitlinger** 21:42 I'm wondering if there's a different way to publish snapshots.
Maybe on Github.
I've read that it should be possible, but I haven't tried.
**Jason Plumb** 21:56 I I believe you. I mean we, you know, should be able to. I think there's I think, that there are.
or there is, a way to do maven packages. But yeah, I'm not. It's it's it's something that that we need to be thinking about in case this
goes really badly. We need an alternative way to publish. And
the Ghcr is definitely an option.
**Hanson Ho** 22:18 I guess folks could always build from source like
he published a local maven. And and and basically, you know, build out of there like like they were, Cci, and and building us
not great. But you know, if if we're talking about
grabbing the binaries, and you know, pushing it into your workflow. It's it's 6 of the one half of them, the other.
**Jason Plumb** 22:43 Yeah, I mean, I I'm assuming things are gonna be a little chaotic for the next week, and hopefully they settle back down. So I'm not trying to lose sleep over this yet, but
it is still a a pretty significant concern, but at least they've acknowledged it right like, at least,
at least, you know, they're continuing this today. So people are looking at it. The way that the way that it manifests is always through search, which is not what what we experience, but that's how it manifests so
hopefully. It'll come back sometime.
**Hanson Ho** 23:16 Yeah, if you just browse the the web ui and and search for you know our package, it's it's it's just it's there, but not the snapshots. I can't even get to the snapshots from the the main.
**Jason Plumb** 23:27 Yeah.
Yup.
**Hanson Ho** 23:33 So clever tech if you're worried about it. Not publishing, you can always just publish the local maven and see if it's if it makes it to your thing that if it if it does, then it's probably gonna work. Once we actually get the the build going properly.
**CleverChuk** 23:49 Yeah. Sounds good. No worried about it.
Just wanted to know why it hasn't been published, because I assume it would have with the
0 dot 11.
**Hanson Ho** 24:02 When did you.
**Jason Plumb** 24:05 That's a while ago.
**CleverChuk** 24:08 Yeah.
Don't remember the exact date.
**Hanson Ho** 24:13 I mean, it'd be very, very weird if if it merged before 11 was cut, and it wasn't in 11. I don't even know how that would be possible.
Unless unless there's a some sort of dependency kind of weirdness.
**Jason Plumb** 24:31 I mean, yeah, there, there should be a 0 dot 12 snapshot out there. And
I'm I'm 94% sure that when I did all of these changes over to the new sonotype. That Android
was one of the 1st to to actually get an artifact published in the new snapshots. Location
like I saw that happen.
And it's it's been unraveling ever since. So
**Hanson Ho** 24:59 It's weird. That's on the old place, though.
**Jason Plumb** 25:01 Let's go find that that. Pr.
No, it's view, probably view.
Oh, I'm in the wrong repo.
Keep me honest. Y'all, that's still the wrong repo.
I'm still waking up.
So view this one, right?
May 6.
So yeah, a month and a half ago there absolutely should be 0 dot.
In fact this was be. This is before we switched it over. So the old snapshot location should have
published. So that is a little bit concerning for a new module to not be out there.
and we looked in here.
**Hanson Ho** 25:57 Yeah, those directories are created in on June. Right? So.
**Jason Plumb** 26:03 So this was merged in May May 6.th
And they're there is some. Yeah, there's some June stuff interesting.
**Hanson Ho** 26:18 Leaves it in the bong. There you go!
**Jason Plumb** 26:20 Think the bomb has it.
It is called view, right?
**CleverChuk** 26:28 Yeah, you guys, good.
**Hanson Ho** 26:30 But tomorrow.
**Jason Plumb** 26:31 It's in the bomb. So view click.
So I think I think what I'm doing wrong
is I need to go into.
**Hanson Ho** 26:42 Instrumentation.
**Jason Plumb** 26:43 Here.
**Hanson Ho** 26:44 Yeah.
**Jason Plumb** 26:45 Yeah.
**Hanson Ho** 26:45 There you go!
**Jason Plumb** 26:46 There it is! Clever! Chuck.
**Hanson Ho** 26:51 Some instrumentation, have the instrumentation in their name, and they live up there. Is it because.
**Jason Plumb** 26:58 We changed.
That's it.
**Hanson Ho** 26:59 Yeah, okay.
**Jason Plumb** 27:00 Yeah, we changed it.
**Hanson Ho** 27:02 Got it. Those are just those are just old then. So you're not gonna find you shouldn't find like 12 artifacts dot 12 snapshot artifacts in there. Right? I guess.
**Jason Plumb** 27:12 Sorry, Hanson. Say one more time.
**Hanson Ho** 27:14 Oh, so the if you click into instrumentation, dash whatever! You should only find old artifacts because they don't.
**Jason Plumb** 27:22 Yeah, we changed the name right? So the the group now includes the word instrumentation. The modules do not. So these are all old.
**Hanson Ho** 27:31 Perfect. Yeah, yeah.
**Jason Plumb** 27:32 They're all under this. The group contains the name instrumentation now. And so these are all the current stuff. This is funny. Okay.
we've we've flopped at some at some point we flip flopped in the past. But whatever but yeah, like all of these, like, if we just pick fragment that that has 12 alpha snapshot
startup, 12 alpha snapshots. So this is this is the new way of organizing, which I think is the same way we do it for Java.
**CleverChuk** 28:02 No.
**Jason Plumb** 28:07 Yeah, they love trailing slashes. By the way, make sure you always have a trailing slash.
**Hanson Ho** 28:12 It's like one redirect rule. Come on.
**Jason Plumb** 28:16 So it's it's it's similar. We just have the word android in there, right? So none of these packages
have the word instrumentation in there, and they're within a group called I/O, open telemetry instrumentation.
So we're trying to. We're trying to like, you know, do the same thing with Android here.
**Hanson Ho** 28:36 Edit. Rx. Chat.
**Jason Plumb** 28:41 In in Java.
**Hanson Ho** 28:44 No, no, sorry I saw there's Rx Java instrumentation. I'm like, I I guess you use Rx Java on the back end as well.
**Jason Plumb** 28:51 It's everywhere. Man.
**Hanson Ho** 28:52 Oh God oof!
**Jason Plumb** 28:56 And you know, we instrument everything. So
okay.
So I think you wanted to talk a little bit about Kotlin Api.
**Hanson Ho** 29:09 Yeah. So so the plan to, you know, create a cotton. Api is well underway. We're gonna probably ship a version of embrace that uses it internally, but not expose it externally, because obviously, it's still, you know.
work in progress. And obviously, I don't expect, you know, potentially android to use it right away. But I kind of want to talk about when we have this Api, and when eventually we'll have some parts of the Sda, build out what criteria we want to use to to consider using it. Certainly we don't ever want to expose the Api until it's been like.
you know, accepted, donated, and and official in in some capacity. And we may not want we I mean, we could decide whether we want to do it side by side. You know, have, like the Javan and the and the and the Kotlin one so kind of just want to talk about how everybody's feeling is like, do we want to wait until the SDK is actually out? That you can just move everything over? You know, after it's, you know, proven in production. Or do we want to? Incrementally
consume? This is
obviously I'm not going to put my finger or thumb on the scale. This is kind of like you know how everybody else feels.
**Jason Plumb** 30:28 Yeah, I think this would also be a good discussion to have like when Manuel and Cesar around. But I think for me.
I'm of the opinion. And this this may not be nice to users to say this, but I'm of the opinion that we should align strongly with Kotlin, because that's what Android itself has done. And that's the way that the the
project seems to be going. I think clever Chuck, or someone has made the point in the past, though, that there are still plenty of apps that are written in Java that have not caught up yet, and they may still need observability. So I would. I mean, I'm leaning toward the side of the new hotness in this case, instead of the backwards compatibility.
and I would love, for
I would love for us one option to make it less confusing to users like if if someone is adopting open telemetry, and they say, I've got this android app, and I don't know which one to pick. There's the. There's the Java, one of the Kotlin one. What are the pros and cons. Now they're like they're thinking about all this language specific stuff that they shouldn't have to care about.
And if they're writing an android app they're probably using Kotlin in 2025. But, like, you know, may maybe maybe not. There's still people writing Java apps Java programs in Java. 8. So
that's that's my 2 cents. I would be inclined to say it would be nice to only support Collin Api when it's available.
There, that'll that's gonna take a while, anyway, like that process of getting it donated and adopted will take some time.
but it will really clean a bunch of things up like it'll be really really nice.
**Hanson Ho** 32:11 So I tried migrating open to android to it. And it works okay, for the.
**Jason Plumb** 32:18 We have. Ja. We have Java classes on our main Api, like our main Api returns Java classes.
**Hanson Ho** 32:24 Oh, oh, yeah, no, for sure. So so this is more like internally, so so externally, it's still Java, everything, but internally using it just to see how it works, you know. And there's certainly some migration help that's necessary to deal with things like scopes and things like that. So you know, it's it's informative doing the migration and seeing you know what kinds of things pop out. But.
**Jason Plumb** 32:49 Totally.
**Hanson Ho** 32:50 The main thing really is about creating a model that works on Kotlin and Android most of all, but also allows folks to use it in Java. So it's similar to how Android works where Kotlin is first, st Java still works. So whatever Kotlin SDK is out, there should be usable in Java.
even if you don't. Even if the syntax is kind of like, you know, not fantastic, and you have to specify every parameter and all that. But you should still be able to work.
but yeah, okay, it's it's good to hear that. you know, there's some some
will not some desire to to get this in so.
**GZ Gregor Zeitlinger** 33:37 Have a complete Kotlin SDK.
**Hanson Ho** 33:40 Yes.
**Jason Plumb** 33:41 And and Api, yeah.
**Hanson Ho** 33:42 Yes, an ecosystem and instrumentation. I'll be talking about this on Thursday, and learning why so Android is is part of it. But it's not the entirety of it. I know it's ambitious. I'm going to go ahead and say that. But they had to do this for Swift to get it, and the fact that Android got it without having to build SDK is a good
accelerator for adoption. But at the end of the day it's still
as I will highlight in my presentation. There's still a bunch of ill-fitting things, not just the syntactic Api, but just the the model of of, you know, a current span. For instance, the lack of resilience.
**GZ Gregor Zeitlinger** 34:25 Then do you want to like Clone? The entire source code of the Java SDK.
**Hanson Ho** 34:31 No rebuilt from scratch from the ground up the SDK.
**GZ Gregor Zeitlinger** 34:36 In other words, do you want to replicate the entire functionality, or without reusing anything from the Java SDK, that's actually what I mean.
**Hanson Ho** 34:45 Correct with adapters built out so that you can pull in pieces if you're if you're able to. But one of the key use cases is Kotlin multi-platform, and you could only write Kotlin in there, so you can't have any Jvm classes at all. So in that way it has to be pure Kotlin, so that you could basically have a multi platform app and have the core instrumentation and
and SDK, be at the column layer. So if you have like an app that generates or targets android ios and web. You don't have to include the Javascript SDK, swift, SDK, and Java SDK in the native layers just to send a simple span and have to deal with the various platform level. Yeah, it's not something that's going to ship
next week next month. This is a. This is an investment into the ecosystem, and we know it's hard, and we know it's gonna be a long road. But you know, we got to start somewhere. So.
**GZ Gregor Zeitlinger** 35:50 Yeah, I'm I'm just asking, because I know how complicated the Java SDK already is.
Have you checked? If there are ways
that code generation can help, for example, so that you don't have to.
I copy, paste. The functionality.
**Hanson Ho** 36:12 Oh, we're not! We're not.
**GZ Gregor Zeitlinger** 36:13 Huge.
**Hanson Ho** 36:14 So I think a lot of the complexity is in metrics. And metrics is the last one we're gonna attempt to to do the port over, I think spans and logs is relatively straightforward and frankly spans is is, I think, the most important thing. So we're gonna basically incrementally build out spans and logs. And then metrics
is probably 80% of the effort. If not more
and much less than 80% of the value. So that's the one we're going to skip past initially. But there's probably ways of doing code generation. Frankly, I'd sooner use an Llm. To get the scaffolding going first, st but I don't think it's necessary. I think it's
we can start building it and and see where it gets to us, which is, which is why I don't think, you know, open technology should use this even when it's out until somebody has gone in there and and actually productionized it. So we at embrace is willing and ready to be the guinea pigs. Here.
**GZ Gregor Zeitlinger** 37:25 I'm not worried about the scaffolding. The long tail is huge. I'm currently working on declarative configuration, which is
a completely new topic. And
it's currently only working in Java and by splitting the SDK.
Now, we don't only have to implement it for other languages, but we have to again implement it for a very similar language again. But,
I'm inviting you to join the the configuration sake, and then
we can do some brainstorming on how we could reuse work, or the Java SDK or the Java Sig.
just to explore possibilities before we take on a huge
amount of work. Slash technical depth.
I'm not sure what it is, but it
I would hope that this can be avoided.
**Hanson Ho** 38:31 So so so we've been thinking about this for a while.
And I also would like for this to be avoided.
But Kotlin is a separate language, and it's so close to Java that it's very tempting to just say, Let's just use Java, and I think up to a certain point it works, and it's fine. But I think there gets to a certain point where there are
certain reasons that makes it less viable. And I wouldn't call technical debt. I would definitely call it additional overhead for the community. But I also don't think that we're expecting the folks working on Java to have to spend time on the Kotland side. I'm expecting hopefully to pull in new folks to help with with this and make this a net. New concern so similar to.
you know, other languages. Just because there's there's a there's a path to to compilation. I think there is. There's a bunch of reasons why I think we've we've arrived at this technically, most of all having things run natively in Kotlin, and and
you could run content, multi-platform, and generate no Java code.
So you know
it. It's it's effectively a nonstarter. Unless the native platform has a hotel SDK, and when you start talking about, you know Cross platform it, you know.
But yeah.
**Jason Plumb** 40:05 So, Gregor, in defense of this idea, I mean, I think I understand where you're coming from, and the concerns are, I think, are really valid, but in defense of it you could also claim that opentelemetry has repeated this effort many times, like there's opentelemetry, python, and there's opentelemetry go and there's opentelemetry ruby, and there's opentelemetry. Erlang, like we have reimplemented this Api many, many.
**GZ Gregor Zeitlinger** 40:30 It's a nightmare. Yes, it's a nightmare, so nothing
avoiding to make it even worse is worth a lot of investigation. In my opinion.
**Jason Plumb** 40:44 I I mean, I think I think the I think the party line would say, we are trying to support a diverse broad number of contemporary programming languages, and maybe even some non-contemporary. And you know, if if people are actively developing in Kotlin, there's a there's a gap for them right now, especially if they're targeting multi-platform.
Whatever, Hansen, I remember.
**GZ Gregor Zeitlinger** 41:10 I'm just inviting you to have a collaborative discussion with the Java folks so that we can explore if there is any way
that is not splitting.
**Jason Plumb** 41:24 Make it easier, you know.
**GZ Gregor Zeitlinger** 41:25 Like honestly.
**Jason Plumb** 41:27 Totally.
**Hanson Ho** 41:27 I don't it it so so I I'm definitely open to to have it, because I know the complexity like I don't even know half of of of the complexity of the metrics, and all the ancillary things that are spinning up. So I I appreciate what it means.
But working on this for a year and a half, initially wanting to do this and convincing myself that I shouldn't do this.
It's it's it's been a year, and
maybe it will not be as robust as a Java ecosystem. So we're always going to have a way to basically use the Api of Kotlin and then basically defer to the Java SDK, to do. Everything like this is the 1st step is what we're doing is simply the Api. But there's still some things that we kind of have to do a mapping of, and maybe the Kotlin SDK will never, you know, implement metrics. It will be a subset of functionality, but
I think there's utility there. And I think if we do it right, it's not going to be
considered a fork or debt. It is. It is going to look and smell very similar, but with enough differences that when you drill in it becomes a think of it as an alternate implementation of an SDK like. Theoretically, there's the Api and SDK. The idea is that there could be multiple SDK, this is just a slightly different way of approaching things. But I definitely do not
enter this lightly. I've been doing this for 20 years.
**Jason Plumb** 43:04 I want to jump in and ask you something. I've been meaning to ask you for a while, and that is rewinding back to a conversation that you and me and Trask had about this idea and starting with an Api implementation first, st like a pure Kotlin Api implementation. And you're you're talking a lot right now about an SDK implementation which kind of implies that you've got a Kotlin Api somewhere, but I haven't seen. I haven't seen it, is it? Is it published?
**Hanson Ho** 43:33 Oh, yes, it's it's published. And and we I can. Actually, I can actually share the my private branch of where I use it.
**Jason Plumb** 43:40 Do you mind putting that in the Doc? I think it would be helpful for people to refer to.
**Hanson Ho** 43:43 Yeah.
**Jason Plumb** 43:44 And then
the the description there was like the Api surface is much smaller than like the SDK implementation. So like starting with the Api would be kind of the logical thing to do, and then you could provide an an SDK
that has Kotlin implementations that wrap the Java implementations, and then, one by one, you could go and replace those I think that was, that's my recollection at 8 o'clock in the morning, about the conversation we had months ago. But is that still the approach that that you've gone down.
**Hanson Ho** 44:15 Definitely the first.st The 1st release is gonna be an Api with a bunch of wrappers and adapters that are transparent to the consumer. So you call like, you know.
Kotlin, get tracer provider, get tracer, and then you get hey? I got a Kotlin tracer, but you you debug in there, and it's all. It's Java all the way down, including the threat, local current span and all that. So warts and all. And that's going to be independently useful, I think, without the SDK implementation. I kind of jump forward, because that's you know.
That's what I do. I jump forward, but very discreetly. The 1st thing I want to propose and donate is simply the Api. This is, I think, that part of it is fairly non-controversial, having an Api that that surfaces idiomatic Kotlin.
what is more is, is the the further down, and you know there are.
**Jason Plumb** 45:10 Let's let's do it as as collaboratively as we can, because, like to Gregor's point, there, there may be some ways that we could leverage existing art and not have as much heavy lifting. But let's let's try and get the collaboration aspect explored earlier rather than later, if possible.
**Hanson Ho** 45:26 Yeah, like, I think the the architecture that we have in mind
things could be used piecemeal. It's it's how piecemeal. And because obviously, if you stick a certain level of wrapper, you have to support that use case, and we want to start from the very top. But you know, if if things don't work out we can, we can. We can wrap further down.
**Jason Plumb** 45:48 Okay.
we have, just about 10 min left. And I wanna make sure that we have time to go over Leonardo's thing. Are we ready? Are we okay with with this?
Are we? Are we ready to move on.
**Hanson Ho** 46:00 Yep.
**Jason Plumb** 46:01 Cool.
I still think it's an exciting and fun idea, Hanson. I think you're also a little bit batty.
**Hanson Ho** 46:08 Yeah. Oh, oh, yeah, no, no, this is. It was insane. I didn't.
I didn't want to do this.
**Jason Plumb** 46:14 Alright, Leonardo, welcome. You've got some interest or concerns about span events.
**Leonardo Serrano** 46:20 Yep, yep, I can. I can explain a little more. So
yeah, I know there is a a wider effort to deprecate span events.
I know we still use in in open telemetry, android. We still use span events for
there's a couple of places where we use it. I believe. Activity, lifecycle.
a handful of places. My question is.
**Jason Plumb** 46:49 Go ahead!
**Leonardo Serrano** 46:51 Is anyone working on deprecating these in opentelemetry android instrumentation?
**Jason Plumb** 46:59 No. And I think it's a problem.
So yeah, like.
Oh, man, look at this documentation. We have read me that even mentions that we make span events. It's so good. Okay? So yeah, activity, for example, does create span events. So when an activity goes through a state change, we generate a span as one of these names.
and then, in addition to the name, we generate span events. So these are intended to be
points in time, indicating when things happened on a span. That's the original kind of design there, and if you looked at the span with its start and end for the state change. You could see it going through these various lifecycle stages. I haven't done that in a while. I'm not actually sure how what that looks like or how useful that is. But that's the that's the original intent. That's how the instrumentation was created. Originally.
As far as I know, no one is doing work to change this. And by change, I think the we can go back. I linked to I linked to the spec change pr, but I think the intention is to instead of creating span events, generate events separately that have span context.
**Leonardo Serrano** 48:15 Yes, yes.
**Jason Plumb** 48:16 Okay.
I don't think anyone's working on that right now in in Android. In fact, we don't have an issue yet for it. I don't think.
**Leonardo Serrano** 48:24 Oh, okay.
yeah, I can create that. And I can maybe take a stab at that myself. My follow up question would going to be? Is anything preventing us from
moving away from span events?
**Jason Plumb** 48:36 I mean, it's in the spec, and we're not stable. I think we should align with the spec. That's my 2 cents.
**Hanson Ho** 48:43 I will also add that if a span can generate 10 span events, you're you're increasing overhead number of signals by an order by, you know one span there, how many span events on Mobile? It's a pretty. It's
the calculus becomes different in terms of usefulness and overhead. So while I agree that the hotel modeling basically is saying, use events and link it with span context, the actual instrumentation. We should start thinking whether these are actually useful. If we had to incur a
hotel log for each of these. I would argue, it's not useful. If it's or rather the the cost benefit doesn't. Doesn't work out if we had to like make those separate events.
smad eventsa whatever
So for this specific instrumentation, I think I think we should think carefully about it. But if there's other usages span events where it is, you know just one or 2 I think it's reasonable to to port over.
**Jason Plumb** 49:58 We? Yeah. I mean, the concerns around the concerns around optimization. Continue to come up prematurely when anybody talks about events, I think. I think we should 1st build them, and then find ways of making them smaller, or more or more efficient.
I think.
Go ahead.
**Hanson Ho** 50:17 Oh, I think the problem is, is not only the the actually over the wire efficiency. I mean that that's obviously part of it. I don't think a particular on pre create event should live and be viewed independently from the span, that it's part of it, it is, it is not.
**Jason Plumb** 50:39 And that's up to your back end to decide. Then, right like some back ends. Want to throw those out completely. They don't care about those those state changes.
That's true.
**Hanson Ho** 50:48 Yeah, th, this gets into the granularity of the hotel data model, and it's that's not a debate for here. But if if we do port it to events, I think we should definitely have a way of or to regular events. I think we should definitely have a way of turning them off. So you can actually have the the view instrumentation without incurring the the
10 X number of signals.
**Jason Plumb** 51:14 Yeah, that's legit.
Yeah, Leonardo, have you looked at this in Java already like, have you seen what what changes are happening up there?
**Leonardo Serrano** 51:24 Yeah, sort of. I mean they they don't upstream. Java does not seem to, at least not from what I could tell. Make big use of span events, anyway.
**Jason Plumb** 51:33 Right, it's true.
But we I mean getting ahead of it in Android is good, because at some point, you know, this method will no longer exist
like some some future. Well, that's not true because of stabilization. So they will probably keep this.
The reality is, they'll probably keep this method around for a really long time, and it will be bridged so rather than having a span event that shows up in the data model as a component of span under the covers, the SDK will be creating a separate event.
**Hanson Ho** 52:06 I thought only the Api was deprecated, and that the span event thing inside Otlp still exists, or and not deprecated.
**Jason Plumb** 52:14 In otlp.
**Hanson Ho** 52:16 Yeah, like, I thought.
**Jason Plumb** 52:17 I think they I think they have to keep it there for back backwards compatibility. Let's go check this thing.
**Hanson Ho** 52:23 Or is there a way to deprecate elements within the protocol?
Yeah, it's Api deprecation.
**Jason Plumb** 52:32 Yeah, yeah, it's right there. So that's that's what it is. Okay. So it's deprecated.
not removed, you know. It'll it'll it will be around for a while because the Api is stable, but when it revs like that will at some point in the future go away.
And so I think, getting ahead of that is smart.
**Leonardo Serrano** 52:55 Cool. Thank you.
**Jason Plumb** 52:57 Yeah, no thanks for bringing it up. It's it's something that I think we have not covered here. So it's a gap.
and we love the help. Thanks for offering
anything else that people wanna people wanna bring up or mention in the last remaining couple of minutes
we have. Oh, that's the wrong repo. That is right. Repo.
hey? So let's let's check this out real quick. Then, while we were talking, is this the build?
Think this is the build? It hasn't. Has it finished? No, it still hasn't finished 32 min still building.
Yeah. Well, this will. This will be our test, though, to see
if the snapshots are publishing, which I think they're not. I think there's still a problem.
**CleverChuk** 54:03 When are we shipping the 0 dot 12.
**Jason Plumb** 54:07 Yeah, like a month ago that would be awesome, wouldn't it? Yeah, no, I appreciate your question. I think it's as soon as upstream gets their release out, because we want to depend on the new alpha bomb from instrumentation.
So as soon as that happens, we can rev ours and do a release.
**CleverChuk** 54:29 Roger.
**Jason Plumb** 54:31 And I expect things with sonotype to still be chaotic for a little bit. But hopefully another week.
I don't know.
Look, it's it's doing maven stuff right now. It's great.
**Hanson Ho** 54:46 My God.
**Jason Plumb** 54:48 It takes a while, but hopefully we can get through it. And yeah.
I also want that dot 12 release. You're you're not alone in thinking about that. So
well, thanks everyone for being here and showing up and appreciate you, and see you next week.
**Hanson Ho** 55:10 Yep.
**Jason Plumb** 55:11 If not tomorrow. Actually Hanson.
**Hanson Ho** 55:14 Yes. Oh, yeah, let's figure it out. It's tomorrow. Oh, wow! It is tomorrow.
**Jason Plumb** 55:20 All right.
Alright, bye.
**Hanson Ho** 55:23 Bye.
