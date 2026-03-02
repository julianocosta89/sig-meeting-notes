SIG: eBPF instrumentation
Date: 2025-08-13
Duration: 61 minutes
Zoom Recording URL: https://zoom.us/rec/share/Wn1sh50rtsa9ph3eZk6iU-u99-FJQoPvK1vzk4lYAWY9V-CEiUS8CwRRuHapvttL.tJ6jlFfvpDi_T9Ro
============================================================

## Zoom Recording Transcript

Tyler Yahn 00:00:27 Hey.
Mattia Meleleo 00:00:27 Hello?
Tyler Yahn 00:00:29 How's it going?
Mattia Meleleo 00:00:31 Good, good.
A little bit warm here, and I don't have air conditioner.
Tyler Yahn 00:00:37 Oh, no.
Mattia Meleleo 00:00:39 32 degrees right now.
Tyler Yahn 00:00:41 Ugh. Where are you based out of, Mattia?
Mattia Meleleo 00:00:44 Well, I'm in South Italy, but right now I'm in Albania. I'm having a road trip.
Tyler Yahn 00:00:52 Okay, yeah. Wow, that's pretty warm. I didn't expect it to get that warm there, but yeah.
Mattia Meleleo 00:00:57 Yeah, it's pretty cool, man.
Tyler Yahn 00:01:00 Florence.
Mattia Meleleo 00:01:01 tolerance.
Florian Lehner 00:01:02 Right?
Tyler Yahn 00:01:15 Hey, Nicola.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:01:18 Hey, just got a little bit more water.
Where's this morning?
Tyler Yahn 00:01:25 And then, Rob.
Nimrod Avni 00:01:26 Hey, man.
Tyler Yahn 00:01:29 How's it going? Where are you based out of, actually? I didn't ask.
Nimrod Avni 00:01:32 I'm in Israel.
Tyler Yahn 00:01:34 Oh, in Israel, yeah, okay. What's the temperature there? Is 32 hot, even?
Nimrod Avni 00:01:38 30… I think it's more, I think it's….
Tyler Yahn 00:01:41 I know, I think it's about, like, a 30… 36 thunderstorm. Oh, I don't know how you do it, man.
Nimrod Avni 00:01:48 Staying at home, full AC on, not leaving.
Tyler Yahn 00:01:53 Yeah, that's… that's, I guess, the way to do it.
Nimrod Avni 00:01:55 Cool.
Tyler Yahn 00:01:59 Cool, we can probably jump in here in just a second. I see there's a few things, on the docs. I'm guessing Nikola added the first one as well, but, we'll… we'll jump in. If you have agenda items you want to talk about.
Go ahead and add them there. If you haven't yet, go ahead and also add your name to the attendees list, and I will start sharing my screen.
Cool. Alright, we can jump in here. Nicola, I'm pretty sure you added this, because it relates to this, but just a heads up, I guess, that the hotel docs for Obi are now, up and published and ready, which is…
Exciting. Yeah, which is a big milestone.
I think the next thing that you wanted to talk about, though, is, …
For the remaining dock items, for Milestone 2.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:03:19 Yeah, sorry, I made 001, I think it was 010. Yeah, I was just wondering if, I think we added a bunch of new dock items, but they're ongoing stuff, none of the major things, so I was just wondering, should we…
R.
Keep them in this milestone, or…
We are ready to maybe make 0.1 release with the existing docs as we had them.
….
Tyler Yahn 00:03:48 Yeah, I mean…
I think it… I think having a foundation of what we do is fine. I mean, obviously, it's always going to be a moving target, because things are always going to be updated, so yeah, I think that that seems…
Reasonable to me, if there's any opposition.
Let me know. Move those.
Nimrod Avni 00:04:07 I think that I just looked at the, Helm chart PR, and someone gave a comment there of, …
That it's probably best, if we set the image tag to be something stable.
So if we're doing a release, then we'll probably need to add some, like, …
Another action to, like, tag the new image with the new release, so we can have a stable image.
And I don't know, how do we even, like, if we are planning to…
have, like, … this is, like, a minor version, but if we, like, will release, like, patch versions, or, like, how… if we want to, you know, make, like, smaller releases.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:04:51 Yeah, so, I mean, I was thinking if we have V010, I think that's great, and then we can actually make progress on the Helm chart.
We get that out of the way as well.
And then minor patches as we go forward, maybe we find bugs, erases, and so on.
We can maybe branch off, if you'd like. Like, can we make release… dash 010 branch.
Nimrod Avni 00:05:16 And then… or, release….
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:05:19 I guess, 0.1 branch.
And then we just… if we wanted to patch that with bug fixes that we discover I want to keep stable, but for now, I think, since we're still in active development, may not be needed, but just to have one so we can move progress on that.
Helm chart, and….
Nimrod Avni 00:05:38 Yeah, sure. Sounds, … sounds like a plan.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:05:41 Yeah, what do you think, Tyler?
When we make a pre-release, we can… we don't have to say it's stable or anything, we can mark it as just an initial release.
Tyler Yahn 00:05:50 Oh, I… I mean, that's communicated in the V0.
you know, major, yeah, version. I, yeah. I mean, I think you actually are kind of making a good point. It's like, I think we should have a task to define, like, what we mean by stability here. We do that in almost all the hotel, … Oh, okay.
repositories, and saying, like, you know, like, here's our versioning scheme, we're using, semantic versioning, here's our, you know, release policies around, like, backwards compatibility,
we don't make any guarantees prior to, like, 1.0, like, that kind of stuff. Like, I think it…
I, I, I think…
You bring up a good point, because, like, that's just in my mind, but it's easier to point to people in the repository, like, no, no, no, this is documented, like, let's… let's go with this.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:06:35 Yes.
Tyler Yahn 00:06:35 So… Yeah, that's a… that's probably something we can include, …
in the V2, I guess, is a good idea.
… Let me start sharing again.
Yeah, I think… Yeah, let's… let's add that.
Baby.
Yeah, that sounds good to me. …
I think this is just, …
One thing that I did want to ask, because it looks like, you know, this is… we're done with this milestone, …
But we should probably review this, but one of the things I wanted to ask is, like, right now we have a lot of…
Exported packages?
Right now, nothing's hidden, or it's all… it's all a public API, essentially.
This means that, like, our dev docs are going to include all of these at, like, the Go package site. Like, obviously, we're not trying to deliver, like, a Go library.
And so, one of the things that is kind of problematic in this situation is that if somebody does kind of interpret this as a programmatic library, then…
the versioning stability guarantees that we are going to have to come up with are going to have to be around, like, the Go library itself, so breaking API changes to whatever we have in these packages becomes prohibited at that point, which is pretty restrictive, in ways that we probably don't want.
So, I was wondering, you know, before we do make this, like, tagged release, did we want to move…
the directory structure is to an internal. This is generally how you… it's not generally… it's impossible for people to actually depend on packages in this internal using the Go tooling, is the idea. So things like in this package, or in these tests, or all of the things that we're not actually trying to export externally.
I, yeah, I was wondering what people's thoughts on this are.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:09:04 Yeah, so I think a lot of that stuff wasn't internal, to be honest. I think we… when we ported a code in the between state, between, Bela…
and vendoring, Obi, and all those things. I think we need to take a careful look to see what should be an exported interface from OBI.
So we can still keep our…
Backwards compatibility until we make a major release, remove some of the stuff that we have.
… Yeah, I mean… A lot of that…
Package components, was it package internal as well?
In the past.
Tyler Yahn 00:09:44 So….
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:09:44 book.
Tyler Yahn 00:09:46 I guess that's the question, it's like, so you're… you're… you're vending this right now into… to Bela, like, what is… what is needed there for that?
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:09:54 Yeah, we have a couple of touchpoints, and to be honest, I think a lot of it is too open right now, because we had a lot of intermediate states, because if, you know, like, we started moving the code…
We moved all the code here, but then we started cannibalizing the code in Bayless, so we don't actually have
a duplicate.
Tyler Yahn 00:10:13 And then, during that phase.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:10:16 Of… but we couldn't… Technically, it was too much work to do all in just one go.
and remove everything, so we started moving package by package. We sort of slowly started taking out packages out of Bela, and doing GoMod import, from OB.
But now that we're done with that, it's mostly done. There's no… there's no code in Bela other than stuff that deals with, translational environment, variable names, or Grafana Cloud connectivity.
So now we have to take a careful look at what do we actually need as touchpoints, and only expose those and move everything internal.
Tyler Yahn 00:10:59 Yeah.
That seems, … Doesn't seem too hard, especially since you have an example of that.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:11:09 Yeah, I think we…
We just need to do a survey now to see which packages do we really import.
Right. And from all the, all the code.
See if you see… yeah… Yeah.
…
You know, so some of these may still need to be kind of considered, but… and maybe we can also refactor some of the code to make this better.
You know?
Tyler Yahn 00:11:43 Yeah, no, I… well…
Yeah, there's not a… there's not a doubt in my mind that, like, if this stuff is being used external, then it needs to be exported, right? Like, that definitely needs to happen.
So this is, this is actually really good to help in that answer. It's just that, like, what, …
Yeah, I think it's just going through this and just trying to find the things that aren't covered by this, and looking at what we can obfuscate. Like, I definitely think there's some easy wins here, right? Like, this test directory, there's….
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:12:12 Yeah.
Tyler Yahn 00:12:13 There's no way that….
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:12:14 Yeah. I'd be surprised if you're depending on that, but, like, …
I… no, we're not. No. No, we're not.
Tyler Yahn 00:12:22 I do also think that, like, this configs thing… I was thinking about this this morning, like, we probably want something like this offsets tooling… I mean, we want it shared across this and the auto insertation project, to be honest. And so, like, we need some sort of external face of that, so, like, having something like that seems fine.
…
Yeah, but I mean, we can… we can take a look at the, I think, the rest, and maybe just… just try to clean it, because, like.
The hard part is, is, like, if you don't do this, from the start, things can get really messy. …
Let me tell you how I know, ….
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:12:59 So, you know, you see things like this, where you have, like, an exporter package and an exporters package, because….
Tyler Yahn 00:13:06 People still find these things.
Even though they haven't worked for, I don't know, since, yeah, V02, right? So, like….
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:13:16 Yep.
Tyler Yahn 00:13:17 it's kind of like, it's nice to think about it beforehand. There's ways to try to, like, deprecate them, but, like, they still sometimes will show up in the logs like this, and people will get confused, about, like, what is…
you know.
what they should use and what they shouldn't use. It's not, I think, as important in this situation, because this isn't really meant to be a library, except for cases like what you're talking about, where, like, I guess you're wrapping this, so…
Yeah, I think it's more just, like, maybe we can spend a little bit of time thinking about it to take the obvious ones. Like, this test function, I think, is a good one to move internal…
Obviously that's not, like, trivial, because you need to update all the tooling and all the other things, but, like, I think that that's something we could take a look at, though.
I'm trying to think anything else, like, obviously, like, we saw a lot of things in this package, directory here.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:14:06 Yeah.
Tyler Yahn 00:14:07 In fact, I think… Just that quick look, I don't think there was much…
I mean, maybe his build info was the only thing that I didn't see, but I mean, I'm… who knows, like…
I didn't look that closely.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:14:21 Yeah, we had to.
Tyler Yahn 00:14:22 So… I think that maybe this….
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:14:25 Yeah.
Tyler Yahn 00:14:25 Yeah.
So true.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:14:28 bad. Some of the stuff can be made internal, what we have here, also, I think, yeah. It used to be much better, but then we… we sort of…
Completely messed this up.
….
Tyler Yahn 00:14:41 Well, I kinda get it, though, you need to, like, get…
you need access, and you don't know what access you need, so it's easier just to make everything. But, ….
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:14:50 Yeah, I mean, we have to do it slowly, make sure we don't break anything, learn from the process, and as we make versions, people do pick up the Bela main image, it can be broken 100%. Not many people do, but some…
That's what I'll do.
Tyler Yahn 00:15:06 Yeah.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:15:06 And when that is done, we can actually… we need to go back and We've, …
Hide a bunch of these packages.
Yeah, a lot of them were exposed because of the intermediate state, I have to say.
Because a lot of the stuff, like, we went bit by bit.
Okay. Otherwise, it was impossible to do. Both were moving targets.
At some point.
Tyler Yahn 00:15:40 No, I think, like, the way that we did it was probably the right way, yeah.
But otherwise, I don't think there's, … maybe that's… maybe we can ask now, like, if there's anything else that we need to get done that's, like, it's going to cause a problem if we don't get this in the first release, I guess, is kind of how I'm looking at it, because I don't think there's too much or more of that.
But I'm asking, I guess, maybe anyone on the call if they know of, …
Anything blocking this release.
Yeah.
This'll be cool. Let's put this in… Second milestone.
… Nimrod, are you a CNCF member?
Nimrod Avni 00:17:01 I'm pretty sure not.
Tyler Yahn 00:17:03 Oh,
Nimrod Avni 00:17:04 be included.
Tyler Yahn 00:17:08 Alright. Well, if you wanted to be, I'm happy to sponsor you, by the way, just to add up, yeah.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:17:15 Me too.
Nimrod Avni 00:17:17 Nice.
I'll see how I do that.
Tyler Yahn 00:17:21 Oh, it's pretty easy. You just go to the community repository, and you create an issue.
And you need two sponsors, so it sounds like Nicola and I are… you can put us down, or plus other… whoever else you find, but yeah.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:17:33 Yep. ….
Tyler Yahn 00:17:34 But yeah, also to others on the call, if you are not a CNCF hotel member.
Feel free to reach out to me in Slack, and yeah, happy to… I would help.
… it just makes it easier, because I… well, I've got…
I don't know, in theory, I can add you as an owner at that point, but I've also been told that's not the case anymore, so, …
You do get a cool badge on your GitHub repo, which is, I think, important. You should… you should have that.
Nimrod Avni 00:18:04 What's important for them.
Tyler Yahn 00:18:06 Yeah, that's the important.
Okay, cool. Alright, so, on the…
One thing I did want to…
know is, when we do publish this, is this, like, how do we tag the Docker image?
I guess to verify or to show that it's, a V, like, it's a tagged version, have we already gone through this process somewhere?
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:18:29 Hmm.
I don't think we have to make sure it still works at… I mean…
I mean, with Baylor, we had the CI jobs that did that, and built based on… once we made a…
tag.
But….
Nimrod Avni 00:18:45 Just tag main, but we can… I guess we can, like, rely on… like, every time there's a release, just tag it with the release.
Tyler Yahn 00:18:54 Yeah, I mean, I know that's what we do for the Go stuff as well, like, whatever… you know, any tag should work, it's just whether or not, like, the publish, I think.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:19:04 Yeah, publish Docker Hub.
I know when I merge a bunch of stuff, like, sometimes this fails for me, or I get a notification I couldn't push the image, but…
Usually does work, so… I don't know.
Tyler Yahn 00:19:17 Yeah, okay.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:19:18 I think we… we just try it, and…
work through these issues. I mean, most of the stuff was done by Mario, so I… I don't know, I'm not that good at this.
Tyler Yahn 00:19:28 Okay.
Yeah, I mean, it does look like it's got the tags listed, so… …
Yeah, alright, well, I guess, we'll find out on the first release.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:19:39 But yeah.
Tyler Yahn 00:19:39 Yeah. Okay.
Okay, next up, I think on the agenda, I wanted to just go through the open PRs really quick. I'm pretty sure a lot of them are just updates to, yeah, we don't have to talk about those, but, yeah, maybe we could talk about this, so…
The bump, for the test server 117, still haven't looked into the, excluding this, so still a work in progress. I, I'm… it's on my, list of things to do, so, yeah, just, no, no update on that one.
This BPF infer packet type based on server port. This is something that's been opened, I think, for, yeah, for like a week. Mattia, how's this going?
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:20:18 I think that's.
Mattia Meleleo 00:20:18 Yeah, I think it's, it's ready. Yeah, sorry for delaying it a little bit, but I was, working on something different, and yesterday I checked, I did the last request from Rafael and Nicola.
And, yeah, thanks for the help, Nicola. I think it's, it's ready now.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:20:38 Yeah, well, it's on my to-do today. Hopefully both Raphael and I can review and merge.
Tyler Yahn 00:20:46 Okay, perfect. Awesome. Alright, sounds good.
Add license headers to all C files. This is, on my agenda as well, so this is something to just, like, that was called out in the last meeting, that we don't actually have headers for any of these. I did a nice, …
just find and replace, and it was pointed out, Mattia, that this BPF core, we don't actually, like, change this, it's just synced from, you know, the upstream
libraries themselves, so I have to update this to exclude this, and …
One of the things, I guess, also, I want to… yeah, go ahead.
Rafael Roquetto 00:21:19 Sorry, I think we should add the headers on those. I mean, I don't know, just my opinion, because we actually generate those, like, VM, Linux, all those things. I mean, some are, you're right, Mathie's right, some are from Swing, some are not, but we do modify them a bit, like, we apply explained
I mean, … playing format to them. I don't know, I mean, if this makes sense or not.
What do you guys think?
Mattia Meleleo 00:21:47 I just wanted to point it out, I'm not, I'm not, like, legal or something like that, so….
Rafael Roquetto 00:21:53 Yeah, me, me neither, yeah, yeah, it's a good…
Yeah, good thing you pointed out, though, yeah.
Tyler Yahn 00:21:58 Yeah, I don't, … if we are modifying it in any way, like, those modifications can be licensed in a different way. Like, they don't, like, they obviously need to support the, …
I think it's GPLv2, license, right? Like, that still needs to exist. It's just that any of the changes that we submit on top of those can then be licensed with our Apache 2 license, is the idea.
… That being said, like.
you know, like, I don't know how much we're changing this. Like, I was interpreting from what Mati was saying, that we aren't, but Rafael, if you're saying that, like, we are, like, even linting them, that seems like something that we can, you know, include here.
We can include it even if we don't make any changes, just to, like, say that there is an additional, like, copyright on top of this, if there is going to be changes. We obviously cannot change, like, or we cannot change the copyright of the original source material, but, like, yeah, like, I mean, I… there's nothing saying that we can't…
just add this, header as well, and it doesn't really… it won't modify that, I guess is the thing.
Rafael Roquetto 00:23:07 Yeah, so the VM Linux ones, we can definitely either copyright, because they are generated by ourselves. The BPF underscore ones.
I'm not sure. Yeah, I think… do you know? Do you know, Nikola, how… where they're coming from originally?
Mattia Meleleo 00:23:24 These come from LibPF, and some others come from the Silum-Cilium project.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:23:31 I don't think we can, in my personal opinion, and I, like.
I'm not a lawyer either, but we cannot add an Apache license to these, in my opinion, because they're licensed under LGPL and BSD.
So we cannot actually say that we are now distributing these with this license. That's my take on it, but….
Tyler Yahn 00:23:53 So, I… yeah, we're not… I don't think that's what we're saying here, because, like, we are including the original copyright, right, and we're distributing with the original copyright, and so what we're saying is that, like, the original copyright, like, obviously we can't… yeah, you are 100% right, we cannot change the original copyright on the code that is copied over here.
But what we can say is that, like, there are changes and modifications to this file that also are from us, and those changes and modifications we can copyright in our own way.
But yeah, like, as long as, like, we don't try to modify the original copyright in saying that, like, the source of this, like, cannot, …
you know, and we are complying as well, like, with the GPL v2, right? Like, because we are distributing the changes that come on top of whatever we are building from, right? Like, so I think that that's… that's still fine, as long as, like, that still persists. I don't think that the actual code itself
Well, I know that the code itself is still going to be a GPL2 copyright, it's just our changes on top of it, I guess, are the only thing that we can copyright, yeah.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:24:53 Yeah, we lint them. We for sure lint them, and I think there might have been changes in the past to fix typos and stuff like that.
Tyler Yahn 00:24:59 Yeah.
I don't think it's, like, that…
important, given our top-level copyright, or our top-level license for the whole project, but I… yeah, like, I'm…
I'm happy to go with whatever way people want to go, is the idea.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:25:17 I mean, the other thing is, like, this also is licensed to everything here with DSD2, which… Hey, my…
I think as far as I know is you can do whatever you like with it.
Tyler Yahn 00:25:26 Well, it's a… it's a… it's an OR, right? So I think… I think this is exactly the… the whole thing that we're running into as well, because I'm pretty sure this is the… the Silium license. They based it off of the… the Linux kernel license, which is the GPLv2, right? And so, that's, like.
The whole thing that comes in here is, like, this is a combination of two licenses, and so we're adding in a third license, is what's going on.
But that's… I'm also not a lawyer, so that's just based on, like, training and reading I've done in the past, but that's… I don't know.
I've always seen that you can add, your own copyright license, because it's just… it makes sure that it's clear, stating that what you're copywriting is the changes you've made.
But yeah.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:26:10 Right.
Tyler Yahn 00:26:11 As long as we also comply with the original copyright, but we're in an open source project that is distributing
distributing the code, which is one of the big things from the GPLV2. You know, warranties and all that kind of stuff are still…
Yeah.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:26:26 Okay.
Tyler Yahn 00:26:27 Well, if that's said, then I don't think this actually needs any modification. This is… this should be…
Good to go.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:26:33 Are good for review.
I think so. I think you have an approver, I think you're just… there might have been, like, a conflict or something with,
Tyler Yahn 00:26:44 … Yeah, oh, there's just a makefile. So, yeah, I can update that then. …
And I'll… I'll try to put this in the notes, our conversation here.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:26:55 Cool. Okay.
Tyler Yahn 00:26:58 Other than that, we've got updates…
These updates are failing for some reason. Oh, yeah, maybe we.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:27:04 It's license sometimes. It's a license.
Tyler Yahn 00:27:06 Yeah, it's this James Path thing.
… so… This is annoying.
I spent way too much time looking at this. This is Apache 2 licensed, so, like, just to be clear to anybody who's listening, like, this is not, like, a, you know, permissive, or a license that's gonna cause us problems. Yeah, yeah.
It's just that, like, the tooling that we use, for some reason, is not able to figure this one out. And so, …
I was trying to… I was trying to figure this out in a different project, and, like, what I came to realize is, like, this is actually getting deprecated in this next release, this EC2, detector, because it uses the V1 AWS, SDK, which is already deprecated.
So, our… our solution here really is to just start using the V2 version of this.
it hasn't been released yet. I'm hoping it gets released this week, and then we can depend on, like, a tag version, but we could even just upgrade right now to depend on a commit dependency, which I can put a PR in for that, actually. It gets a little annoying, sometimes it tries to, like, renovate every time there's a new commit to contribute, it's gonna try to open up and update this.
Which is not needed, but it's just annoying. But, like, we can also wait for the tag version, and then just do an upgrade in this package here.
And it will resolve this and allow this to move forward. I don't know why, like…
For some reason, it fails…
here, but, like, in other PRs, it doesn't fail, so I'm not exactly sure what's going on with the verified license thing, so, …
Yeah, I can look a little further into it, but yeah, that's one thing that we can do to solve this.
So I'll try to open a PR for that as well.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:28:48 Okay.
Tyler Yahn 00:28:51 … other than that, it looks like, Mattia, you've just opened this one a little while ago, we can talk about this one as well.
Mattia Meleleo 00:28:59 Yeah, it's just some, spam logs which, which should be… should have been debugged from the start, and not worn or errors.
Tyler Yahn 00:29:09 Yeah, okay. Looks like you already had a review on this. Yeah, it looks good, so… Yeah.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:29:16 Yeah, there might be, like, a need to restart a test. I was gonna mention something like that, something related to that, that we've had a lot of failures recently with, ….
Tyler Yahn 00:29:26 One particular test.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:29:28 I'm not sure, I did restart your integration test, Aaron, I don't know what happened there.
Mattia Meleleo 00:29:34 Oh, it's the JSON RPC, I think.
Yeah. It's, it's failing pretty often.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:29:39 Yeah, it's not… it's actually a test bug. This oats, I'm not sure about. This we need to look into. I can… I can take a look.
This seems maybe related.
Maybe. I don't know, although it shouldn't be, but…
It's touching the SQL, which is what… yeah.
These usually are more stable, …
The… the other one… the other one, I… we found a test bug. I was looking with Mark this morning, …
We… we found a test bug.
where… Essentially, we depend… once we find a certain path.
In our tests, we depend on finding all components of a trace, and once in a while, one of the… one of the traces reported is delayed.
So we don't pick it up, and we fail the test.
So, I think the fix is easy, we just need to move the whole code that detects that all traces are correct into the… under the eventually.
So that the thing retries.
And pulls the right trace. It just… one span will miss, but we see it later come out in the log, but I think at the time the test runs, it's not there.
And fails the test.
I thought it was an actual bug, but then we looked at it, and I see all traces are fine. It's just, unfortunately, the test is broken.
So this should help quite a bit with CI issues.
Tyler Yahn 00:31:10 Nikola, I was kind of wondering, …
about the logging for these tests? Because I was looking at it recently as well. We log it off to, like, this file. Is there any reason… well, I can think of a few, but, like, did we look into just trying to log this to standard out, and then have it in the test output of, like, the action logs itself?
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:31:32 No, I think it's been like that from the beginning. Mario set it up.
Alright.
I think it might be.
Tyler Yahn 00:31:39 I mean, the only thing is, like, I think it's gonna be, like, they're already pretty long, it's just gonna… it's gonna add a lot of logs to that, but, …
Yeah, it just seems like it'd be nicer when it fails that you could just read the….
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:31:51 Like….
Tyler Yahn 00:31:52 The message of why it failed, in the logs, because, like…
… do a lot of stupid things, and, like, they're pretty obvious once I see the logs, but it just takes a little bit to get to it, yeah.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:32:01 Yeah.
Tyler Yahn 00:32:02 Yeah. Yeah, it's so, like, a two-step thing, right? You see the failure, then you open the logs, and you look in the logs, and you're like, okay, this is why I failed. Yeah, yeah. And it's a little bit harder when they're, like, flaky, right? Because, like, sometimes you're just like, well, maybe it was just a flake, I'll just kick it off and let's try it again, where it's like, no, like, you literally had a syntax error or something like that, right? So, yeah.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:32:21 No, I agree.
And especially the Kubernetes ones, those are the hardest, because…
the Kubernetes ones, you have, like…
These ones, at least, the Docker YAML, they all… we all… it's kind of obvious which file it goes to, and even the test says which file it goes to, but the Kubernetes, I find, it's like, you have to look at the pod log, and you're never sure which one did it run. Did it run…
The demon set, or did they run the sidecar, and it's like, you know… That's a good idea.
Yeah, okay.
Tyler Yahn 00:32:55 Alright, I… I will… I'll keep that in my queue of things that I'll take a look at. I just didn't know if, like, it's already been discussed, and so I just wanted to double check.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:33:03 No, it's been like that from the beginning. I think we just picked something and went with it.
it might be good to be in both places, sometimes the GitHub thing is slow to render and all this.
Tyler Yahn 00:33:13 That's a good point, yeah. Yeah. That, yeah, that actually is a good point.
It also…
It goes away after a few weeks, too, so it's nice to have docs on that kind of thing.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:33:23 I think so, yeah.
Tyler Yahn 00:33:24 Okay.
Well, cool. Alright, that's the last, …
PR, it looks like, we're just, I think, waiting on tests on that one, because it's already been reviewed, so, yeah.
Next up, Florin, you wanted to talk about the hotel collector integration.
Florian Lehner 00:33:41 Yes, I'm talking about this, white word. I wanted to ask, how the idea is for the EVPF instrumentation to integrate with the hotel collector.
When I look into documentation, I see Docker, Kubernetes, and the standalone option, but nothing like, hey, this fits into the hotel collector…
environment, I would say, or ecosystem. …
I'm asking this in particular because, I think it would be interesting to get out, from the EVPF
instrumentation, traces, traces and metrics, for example, then, maybe call some, some processors, like Kubernetes Attribute Processor that enrich data, or any other processor you can think of.
And then, use also the existing exporters to, write them wherever you want.
And, so I'm… so I was wondering if… if you have already some kind of integration, or is there an example config that you could share?
Tyler Yahn 00:34:48 So, yeah, it's, it doesn't exist yet, but it's a thought. Like, you're not alone, like, we've definitely thought about this. We have an issue tracking this as well. It's not… it's definitely not a goal for our initial release right now, but we can… yeah, I can find it for you as well, ….
Florian Lehner 00:35:04 It would be super interesting. And, maybe as a follow-up question.
I'm from the profiler side, so we have profiler, and we are also deployed as a daemon center on the systems.
And I was wondering how you solve the issue, if you're deployed as a daemon set, that you account, that your account
specific traces or metrics, to a specific APM service.
And, and tell the system, hey, you are a daemon set, you see the complete system, and this is specific to this, APM service, for example.
Right. Doing a hazard.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:35:46 Yeah, I can answer maybe on both questions.
Okay, so for the collector, we have done this before with the Grafana version of it. Unfortunately, not with the auto collector, but we will do it. That's one of the commitments we had when we donated the project, and so…
So I think there's a way forward. I think the Grafana version alloy is not that different. I think for two things we need is, one is…
like, the collector to supply the metrics exporter in one way to us, and the other one is their traces exporter, so we can touch it, and as long as they're configured, and they're passed down to our
OB, as… as objects, I think we'll…
it should be just fine. And I think collector will be even easier, in my opinion, because both syntaxes use YAML. With the final version, we have this river language that needs conversions and all this, so… We've done it before, there's, like, integration, so I think…
once we get to it, that should be okay. And we did all the work related to
it being a reloadable component, it can be embedded so that it can just, if you change the config, we can hot reload, and it will disappear and restart again. All that work is done, so…
It should work.
Now, about the correlation, in daemon sets of…
how these things map to what particular service, right? … So, for that, we… have…
We subscribe to the Kubernetes API ourselves, and so technically we do two…
The approach is, like, twofold.
The first thing that happens is that we discover all processes based on their process ID,
People have supplied various rules, what processes they want to instrument, but on one side, on the eBPS side, we see the process ID. When we see the process ID, we dig through the proc metadata to find the container ID.
If it's in a container or not, right? So, once we find the container ID, we keep it in memory as a mapping process ID to container ID.
And so that's one collection.
On the other side, we subscribe to the Kubernetes API, and it supplies us with the pod information, and in the pod information, we have the container IDs.
So, …
with this information, then, we're able to distinguish, so at that point, this information is merged based on the container ID as a unique key.
And then, when the signals come through the eBPF side, for which process it is, we map it to the… to the right container, and then for the right container, we can map it to the correct metadata, whatever it was for that. So, service name and so on, service ID.
So we technically annotate our Kubernetes ourselves. We don't have to, we can just use it for the matching, we can just look without the Kubernetes attributes and let the collector annotate after.
…
But that's the generic way, we use. Now, the process tracking is also, you probably know, because you're experiencing the same things, …
certain process IDs, depending on the namespaces, so we do collect all that information on eBPF sites, so we collect the host PID, if it's available, but also the namespace bid and the namespace, and then we match based on that.
Because, depending on which level you're inserted and what permissions are given to the OB process, you may not see the actual
Depend… like, you see some levels, maybe, of…
Of the PID information, but not all PIDs.
Florian Lehner 00:39:50 Yeah, I'm asking, as we're facing similar issues on the profiler side, we also extract, PID and container ID. We don't, or not, we don't, we no longer, fetch Kubernetes information, because we were asked to remove it.
to reduce dependencies, and as there is a hotel collector processor.
for attaching Kubernetes attributes, then this is done in a later stage.
But what we noticed is that, …
that the gRPC data is blown up quite significantly if you put the container ID into the resource definition of the respective protocols, so metrics, traces, logs, or profiles.
And, yeah, I was wondering if… if you… how you deal with this, other than… Yeah, just….
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:40:43 Yeah, okay, so… It's not great, it's not great. But I'll explain. So, you're absolutely right, and one of the main performance hogs in a startup is this Kubernetes thing.
To alleviate some of it, Mario built this Kubernetes cache service, which we deploy, but it's… that cache service gets hit.
But essentially, we tried to create… we created, like, sort of, like, a proxy for this Kubernetes information to make it more efficient to be served. So, especially since,
I don't know if it's the same for the profiling, probably not, but, we…
Wanna be able to create Correct information about service graphs, no matter what the node is.
And for that reason, we capture the cluster-wide information from Kubernetes, so that if you're hitting an IP on an outgoing trace, we want to find out what the name of that service is. So we need to know if this IP belongs to a service on another node.
And then what the service… hotel service name for that is.
And, … To alleviate some of this.
because we were too demanding on the Kubernetes API, we created this Kubernetes cache service, we'd get launched, and then OB just hits that service. So, it's less overhead, from the service… from OB to that service, because we kind of, like, handcrafted some of those gRPCs and whatnot.
But then that service just, also, …
goes, like, to the Kubernetes API, and once it hits that information, there's still a lot of memory overhead on that service. But if you deploy in one cluster, you can have one.
Florian Lehner 00:42:28 Nope.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:42:29 And at least you're not blowing up every daemon set with this information.
Florian Lehner 00:42:34 Yeah, I see the point. I'm just more wondering about the gRPC messages that, the hotel, exporters will send out. So, the metrics exporter, traces exporter, metrics exporter, as they, oh, as you…
Do we put, for every…
container ID, or for every Kubernetes entity, do you create a dedicated resource entity in each.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:43:04 Yeah, okay, so container ID is not something we, use in our Kubernetes implementation.
We do not export the container ID, because it blows up cardinality and everything, so…
We tend to kind of go down to the service level.
… When we report the outgoing trace data, or metrics data.
Florian Lehner 00:43:35 But as you see multiple different service entities, you probably have to then also create a resource definition for each one, and then attach respective traces or metrics to it.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:43:48 But, yeah, I was just chopping on the question, so I don't want to hijack the meeting. No, this is good. It's a good conversation. I can explain how we do this. So, …
So, assuming we get the Kubernetes data, from… we have a default set of Kubernetes attributes that we associate with each process, based on the container ID matching.
And they typically contain a cluster name, service name.
They do not contain the container name because it's high cardinality, and we don't… we don't put that in.
So then what happens is that we keep, sort of an internal database of
Metadata for each bid, if you will.
as traces come, as spams, or whatever you call them, come from the eBPF side.
This information is then enriched in this pipeline internally in OB, and then passed down to be serialized as metrics or traces, whatever.
So, … different things happen. For traces, what we do is we… …
everything in Obey, kind of, on the ring buffer, when it comes, comes in number of events. So, for example, the ring buffer can contain, like, 100 events. They all come at the same time, and once it fills up, or there's a timeout, it just senses the whole batch.
We take these batches, and then we first group the, … prefers group… dumb.
Traces, or if you will, if we're exporting traces, we group
Each individual of those elements by the resource attribute.
Then we create one resource attributes and embedded spans, and we ship them out to the exported endpoint.
For metrics, different things happen. So, for metrics, we have an internal cache of reporter per…
With the resource attributes for it.
sort of, like, each bid knows which recorder it uses, and then those resources actually get attached by the old telemetric SDK, and they go out
… Whenever we, say, record a new route, or whatever it is.
And Prometheus export is the simplest that one. Just, we consult the metadata, say, this is the process ID, okay, find me the metadata, attach it to this. Is that kind of the answer you were looking for?
Florian Lehner 00:46:21 Yep, yep, sounds good. Yeah, so….
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:46:25 So we did have a bug initially that we were sending resource attribute to every trace. That caused, like, collector to reject requests because they were too large and things like that, so that… that's the reason why that's fixed in this kind of grouping first and then send.
And then the metrics, we do have a memory consumption issue. Unfortunately, for the hotel side that we're trying to… we haven't found a way how to resolve it, it's just how the SDK wants the data to be sent to it, so we need to have a reporter per service that we monitor.
Which…
Because it's only about the resource attributes, but you need to create a separate metrics reporter for each individual service, and then as the events come through the pipeline, we hit the map, what's my reporter?
Get all the data and export it, yeah.
Florian Lehner 00:47:18 Cool, yeah, thanks. Makes sense, yeah, we are facing similar issues as we have the similar view on the system, and we noticed that,
Yeah, messages that are sent out just exploding.
And, the more container environments, or the more containers you have, the bigger the sizes will. And, auto collector, if you send it to an auto collector in the backend, they will face,
Significant issue if multiple, sources are sending data.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:47:55 Send it.
Florian Lehner 00:47:55 And they're running out of memory.
So, dormant.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:47:58 memory, and sometimes, because of the size, I would outright reject a request. It's too large for accessory, no, no can do.
Yeah. For us, batching for the traces helped quite a bit.
Yeah.
But, it's sort of like, you… you have to rely on that, well.
You'll have some way to common, like.
usually it works out. Like, if you have your ring buffer big enough, the events that go through when we get the batch, usually there's quite a bit of commonality between… that we can compact and create one trace per service.
When we send them out.
Florian Lehner 00:48:40 Yeah, cool. Okay, cool, thank you.
Tyler Yahn 00:48:44 Okay, yeah, thanks for answering that, Nicola. That was actually pretty insightful. So, yeah, next up, Mattia, you wanted to ask a question about network-level degradation with and without context propagation?
Mattia Meleleo 00:48:56 Yes, this is a bit of a big question, because we have this, we have one customer which is testing the obi.
And, is experiencing some, cluster-level network degradation. So, Kafka is going on timeout and stuff like that.
And, as far as we could tell, this is happening both with and without context propagation, so…
Even without the TC tracer, I think it's called.
and the TP injector programs, this is still happening. So I was wondering if you guys, mostly, I think, Nicola and Rafael, if you have some experience with, with this kind of issues, and how did you troubleshoot it in the past?
And, yeah, some ideas in general.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:49:48 Okay, so, I guess, so network-level degradation means the network is just becoming slower, because we're doing something to it.
….
Mattia Meleleo 00:49:58 Yes, yes.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:50:03 Hmm.
Florian Lehner 00:50:06 profile it.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:50:09 That's my….
Florian Lehner 00:50:11 I'm opinionated, sorry.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:50:12 Yes.
Yeah, so, … Yeah, I would personally try with BPF Top.
… I know, so you can kind of try to find out…
which of the BPF programs may be running too hot, or spending a lot of time?
…
there's also internal OB metrics that do this information. I think they're on by default, so you… we do report latency for, like, if you enable internal metrics.
you'll see a bunch of metrics spit out in OB that will tell you how slow or how frequently certain programs run, so that will be valuable feedback.
It likely is interrupting things too much somewhere.
I don't know, … or interrupting too frequently. Are you running with the larger buffers, by default?
Nimrod Avni 00:51:13 I think so.
Mattia Meleleo 00:51:14 Mmm, yes, I guess we are.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:51:17 So try to reduce it. That's one of the things that I hit as soon as I enabled larger buffers, first time in a long time in Bela, and then I removed them because people were, like, complaining about the impact it had on their system, and then we…
remove them, so… I couldn't… Yeah.
Mattia Meleleo 00:51:39 We need to check which databases the customer is using, because we don't even have that kind of information. But yeah, we'll.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:51:47 Yeah, so enable… tell them to enable bail… oh, sorry, OB internal metrics, and you should see BPF…
programs in there. Raphael, do you remember if we finished the work that we have the full name of the BPF program? Because we had some limitation with the psyllium library. Do you remember, like, you found a better way, or did we do that work?
Rafael Roquetto 00:52:09 like, the full name? What was it again? Remind me again.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:52:13 So…
So, our internal metrics, we scrape and try to figure out what is the latency for each of the BPF programs, but we had some limitation with the Silium library, and we extracted the name of the BPF program that did that. It was, like, chopped up to, like.
Mattia Meleleo 00:52:31 15 bytes, I think, I guess?
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:52:33 16….
Rafael Roquetto 00:52:33 Yes, it's still the same, it's still the same.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:52:36 It's still the same, I think….
Rafael Roquetto 00:52:38 Mark might have done something in that prompt.
I gotta double-check, but I think it's still the same.
Sorry, yeah.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:52:46 Yeah, so that's, … that might be a little bit about DPFTOP maybe helps. Now, like, our… every probe we have is prefixed with OB, but OB is shorter, so you're gonna see some…
maybe you'll see some of it, and it'll give you an indication of what it might be. I'm hoping that, that it's… there's enough for you to see, which…
But one of the things, try reducing that buffer to, like, maybe a lower value, and see if that actually helps.
It would be good feedback.
Mattia Meleleo 00:53:15 We will… we will check and report back.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:53:18 Yeah. Thank you. That'll be alright. Thanks.
Tyler Yahn 00:53:22 Awesome. Okay, we're running pretty close on time, but I think we got a little bit left. Niman, do you want to talk about contextual propagation in cgroups if you want? I can start sharing my screen again here.
Nimrod Avni 00:53:32 Yeah, I think we… we talked about it a bit, last time, with all the, like, …
OpenTelemetry demo presentation, but we had a deeper look because
Also, a customer, kind of asked about it, and then I viewed the logs, and I saw this exact log. Then we kind of tried to explore, … I even looked at some old beta commits, and I dug around for some documentation, and I saw that, like.
the message is, like, intentional, because the SOCOps-type programs can't be, attached to CGroupv1.
… and from what I look, like, from when me and Mattel, we kind of dug there, it's like the… there's, like, the SOC message program, which kind of listens to the, the SOC ops, like, populates some map, and then that listens to it for every…
packet, it, like, injects the context, so…
I, like, we try to dig around and think if there's…
either a way to populate that map without, like, from another program that is not a SOCOps program.
Or how, like, another approach?
That can, like, that the context propagation can work without the… the way we do it now. Or, or, like, you know, worst case, we can, like,
specified some place officially in the docs, because we, like, we already have, like, some…
places, you know, we have some limitations for stuff like kernel version and whatever, but we can even, like, specify that in a more deliberate way.
Rafael Roquetto 00:55:18 So.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:55:18 Okay, so….
Rafael Roquetto 00:55:19 Sorry, go ahead, Nikla, go ahead.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:55:22 Yeah, so it's kind of interesting. Okay, so, based on what you found, correct me if I'm wrong, but it seems what you found is that the SOC message program is the one that we really need.
can run without these cgroups we run.
But the software….
Nimrod Avni 00:55:37 Sweet.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:55:37 Ops 1, the one that actually does populate that map, cannot.
Nimrod Avni 00:55:42 Yeah.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:55:43 So technically, then, we can let this SOC message load, so there's two things.
If the traffic control is active, it will try to populate that map. You can find the code.
It just skips a beat, because it cannot detect that a new socket's been added, but if he sees a message coming through the socket that he doesn't know of, and it's not in the map, it will go and add it.
So you kind of miss one request, but you get the next one. Now, unfortunately, if it's, like, you make one request and you get the response, you can't see it. The other way would be, …
with what, Mattia had done in the past, which is, like, iterator. You can iterate over the live sockets and just add it to that map.
But it needs to be somehow on demand. Now, if you look at the who can touch that map.
… I think there's a list of programs in there.
And maybe… and TC was one, so TC can modify that map.
…
Maybe we get lucky, maybe it's possible to modify from a Krobe, so then we can do it in Accept, or in Connect, and we just….
Nimrod Avni 00:56:55 I think he looked at that, right?
Mattia Meleleo 00:56:57 The issue is that, that, the value that, that Mapu wants is not a normal SOC, but a BPF SOC.
So, we have to try and do something ugly, like constructing a BPF SOC from a normal SOC. I think that's doable, and maybe it works, but it's a bit ugly, I don't know if it really works.
Rafael Roquetto 00:57:19 Oh.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:57:19 Let me have this code.
Rafael Roquetto 00:57:20 just let me interject a bit. The… are we sure it doesn't work with CGRPV1? I know that we don't attach to cgroup V1. I don't remember why that patch was.
But… Is it just a matter of… Are attachment code being broken?
I use that program type.
Nimrod Avni 00:57:40 is not support… from what I read, both in the Bela PR, the… and I think I linked some, like, Red Hat link somewhere, so I think it just, like, CGroupv1, doesn't support the SOCUP,
Mattia Meleleo 00:57:55 Also, the Silium library explicitly mentioned cgroupv2. I can put a link in the chat here.
Rafael Roquetto 00:58:04 Because all we need to… okay, so the CDM eBPF does not attach to C group, like, V1, it cannot pass the cgroup V1, ….
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:58:13 Yeah. Beth, okay.
So, I was gonna mention the code exists, the code exists in this, TC… TC Tracer has this track sock.
So, given, like, in here, it doesn't actually need anything else, but it needs to create this tuple.
And then after you've created this tuple, which is our, like, it's not that…
Hard to make. If you have the right information.
We do this lookup sock from Tuple.
And then you find the BPF SOC, and then we just go BPF updateElement.
Nimrod Avni 00:58:53 Where do we search this?
the BPF…
So the question, if that doesn't search it in the place that the, … that the SOCUP program populates it?
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:59:07 Yeah, so maybe in Kprobes, this can be done. You can see what this one does. It does this BPF-SK lookup TCP, so I don't know where is this available?
Nimrod Avni 00:59:19 So… Oh, it's not in the map, it's… okay.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:59:23 Yeah, so you have this helper that you can find the BPF SOC from this tuple
structure, which… it's pretty simple, it just has the IP address and the ports.
Mattia Meleleo 00:59:36 We can do?
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:59:36 It's the….
Nimrod Avni 00:59:37 Yeah. Oh, that's.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:59:39 Amazon
and then you can, you can look it up, as long as this helper is available from a K-Probe. I don't know, I… I mean, we did it in TC, serve as a backup path, because sometimes the socket is established before we load OB.
So then, we don't see the socket. Like, let's take a long-running connection, something that's doing TCP keep alive. They keep sending messages, so then TC, in traffic control, we see a socket, we hit the map and say it's not there, and then we do this…
To find as the, … And this code here gets the tuple from, like, an SKB.
….
Nimrod Avni 01:00:24 No.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 01:00:24 That… There's a couple of places you can do it, maybe if it's available in a SOC filter?
the SOC filter can do this for you, because it also parses SK buff, although a slightly different version of it.
Yeah, see which programs have that helper available, and maybe you'll find one that… You can… Inject.
Rafael Roquetto 01:00:47 Real quickly, I just want to mention, it might be possible to attach to Group V1, but we need to do it, the system code directly, and not use the CLEO API. Just something we can discuss later. I know we are out of time.
Tyler Yahn 01:00:59 So yeah, let's pause on this. So, if you have more feedback, please go ahead and comment on the issue to keep the conversation going asynchronously. We are definitely over time. So, yeah, I want to thank everyone for joining. I will see you all in a week's time, or after you get back from vacation.
Nimrod Avni 01:01:13 Thank you, guys.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 01:01:14 Thank you.
Mattia Meleleo 01:01:14 Bye-bye.
Thank you.
