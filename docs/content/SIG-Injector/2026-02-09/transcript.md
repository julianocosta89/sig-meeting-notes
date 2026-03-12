SIG: SIG Injector
Date: 2026-02-09
Duration: 50 minutes
Zoom Recording URL: https://zoom.us/rec/share/mqP8u954O5eqSIcTf_JUfC22YRbQp_lR1i4iiV3MXI0yJtbMM4EMfbNuJQN70FKR.Zg3ETr6yltJfu-hQ
============================================================

## Zoom Recording Transcript

**atoulme** 01:07 Hello.
**Bastian Krol** 01:11 Hey there!
How are you doing?
**atoulme** 01:15 Good.
I was, how was this week?
**Bastian Krol** 01:21 You mean Otelandflagt?
**atoulme** 01:24 Yeah.
**Bastian Krol** 01:24 Yeah, what's good.
Good fun!
**Ted Young** 01:32 Hey, hey!
**Bastian Krol** 01:33 Hey, hey, Ted. Hey, Nicola.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 01:36 Okay.
**atoulme** 01:43 Okay, so… Are we good with our release at this point?
**Bastian Krol** 01:50 With the release, yeah.
**atoulme** 01:52 Reese is good, right? We're good, okay.
**Bastian Krol** 01:53 The release is, the best release ever.
**atoulme** 01:57 So, the next one, yes?
**Bastian Krol** 01:58 Exactly. No, actually, maybe I can… oh, I didn't put that on the agenda, but I can give a quick update on that. So, I already incorporated that release into the zero operator, and… just today, we released, an early version with Python also instrumentation, so for now.
**atoulme** 02:20 the, the actual…
**Bastian Krol** 02:22 Python instrumentations, and which ones are still in our repository, but… That could also be upstreamed later on. It's, for now.
opt-in, so all the other auto transformations are always on by default. Python for now is opt-in, and we are looking for some… customers who are willing to give it a try, so I maybe have more use in one or two weeks if first ones have tested. I mean, you of course have tested this quite extensively.
And, yeah, looks, looks good so far.
**atoulme** 03:01 Thanks.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 03:02 Yeah, I put an update around that as well. One of our engineers, Gregor, followed up with a SIG for the Python, and he proposed some PR, and then there was a bench and forth, back and forth, and it seemed like they all came to a conclusion that there should be like, a proto-Sea kind of, like, generation approach.
Added, so… That would help with, the proto, protobuf, I guess,
**Bastian Krol** 03:31 Yeah, absolutely. I was following that quite closely. I've also put the… put the new PR in… into your, agenda.
bullet item, so that would… as far as I understand that PR, that would only be the serialization for now, not the actual exporter yet, maybe, but… I mean, it's a draft payer for now, so let's see what comes out of it. But, I mean, there have been, like, I guess, 5 or 6 attempts of doing that over the last year, but this looks really promising.
I think.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 04:08 Dick.
**Bastian Krol** 04:09 No, that's the ticket behind it. So, awesome. Good.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 04:12 No.
**Bastian Krol** 04:13 That your colleague is doing that.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 04:17 Yeah.
**atoulme** 04:24 Okay, I got a digit up, sorry.
I had one item for today.
Let me take notes Make sure we have two things. So, Ted, you want to go first?
**Ted Young** 04:41 Sure. Just, raise awareness about, you know, the new proposal, for packaging SIG, to start coordinating everything.
there's nothing in there, I think, that's surprising, to this group, but please have a look at it. My main question… was really around staffing as a thing that we have to sort out ahead of time, because I think Jack Berg has a good comment in there around, you know, we do need to coordinate with the 4 or 5 language SIGs.
On this one.
**Bastian Krol** 05:22 Hmm. So…
**Ted Young** 05:24 that was the main thing, and one thing that got proposed as a way to track that would be to add a new column to the OpenTelemetry support matrix. Right now, it's, you know, tracing metrics, logs. How stable is that?
You know, is it present? Is it beta? Is it stable?
You know, we could potentially add another column there.
And use that as a way to kind of, like, track and coordinate it, because otherwise, I don't know, it'll feel kind of hard to do sort of behind the scenes, because there's a lot of decision-making that has to get done.
That's part of that.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 05:58 What would the new column be exactly? So what would the title be?
**Ted Young** 06:03 That's my question, right? You know, is this new column Linux, right? Is that what we're saying, right? We don't want to say packaging, because that's… right, we aren't talking about that in a generic way.
**Bastian Krol** 06:17 Hmm.
**Ted Young** 06:18 you know, you could have Kubernetes or the operator or something as one column, and Linux package management, Linux something or other as, like, another one.
**atoulme** 06:28 Yeah, we can do that. That's fine.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 06:32 That could just exist for other platforms, like macOS.
**atoulme** 06:36 No, not aware.
Anyway… I've had requests from people recently to ask a, what is it, a homebrew tap just for this, but…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 06:47 No.
**atoulme** 06:48 I've been… I've been passively resisting doing that, because I just don't want to.
**Ted Young** 06:52 I think we should get Linux sorted out first.
**atoulme** 06:55 Yeah, yeah, yeah. I think…
**Ted Young** 06:56 We get… because Mac, the other thing that's weird about Mac is, like, when people say they want, you know, hotel for Mac, I think so.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 07:04 Most of the time, they want a development environment. Yeah.
**Ted Young** 07:08 And so, like.
**atoulme** 07:09 That's exactly what this is.
**Ted Young** 07:10 Let's just get Linux sorted out, and then maybe Windows next, yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 07:16 MSI or something.
**atoulme** 07:18 Whoever wants to touch that.
**Bastian Krol** 07:20 Exactly.
**atoulme** 07:21 we have an issue open for max support for the injector, and I think Bestie commented that, it's like, I don't think that's that… That's nowhere near the top 10 things we need to do, right? Something like that.
**Ted Young** 07:31 If we do anything on Mac, I would suggest us have a look at Docker for Mac, and maybe have, like… I mean, I mean, honestly, I think the answer is just paste, you know, app install OTel into your Docker file.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 07:46 Okay, excellent.
**Ted Young** 07:47 Okay. Sounds good.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 07:48 I don't know, I'll be devil's advocate here a little bit for the Mac, because of Python, perhaps. Since this new Gen AI, people may want to know stuff about how frequently they use the external services and whatnot. It's primarily a Python thing.
a play. But the…
**Bastian Krol** 08:04 don't run that on Mac in production, even the Python. No.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 08:09 No, but they would… developers would know, like, internally, like, the APIs that VS Code is making to my GenAI, or people are now crazy about this, whatever the claw thing is, like… So this runs everything automatically, so they could track internally on their dev machine for their own purposes, like, how much did I spend, which models am I hitting, and all these things. And it's impossible to track without it, unless… You have telemetry in the built-in tools, so…
**atoulme** 08:37 No, we're definitely getting some pressure from our own IT team. They wanted to deploy the collector for Mac, because actually the collector has better monitoring support with the host metrics receivers than most other tools out there, including Telegraph.
**Ted Young** 08:50 Yeah. But…
**atoulme** 08:51 this is just so way out of our priorities, and I pushed back multiple times on that.
**Bastian Krol** 08:58 Yeah.
**atoulme** 08:58 What we like is people to be up in arms about it, and tell us exactly what they want to see, instead of just getting this very diffuse image.
So I wouldn't do it, no.
**Ted Young** 09:07 I would love to see the community, sort of.
lead the way on Mac, and kind of show us like, the different kinds of things they want to be doing, you know? Other people can package OpenTelemetry up and be like, brew install, not something we will slap a trademark violation on, you know, level thing, but, like, people can make their own thingies for, you know…
**atoulme** 09:34 It's a solvable problem.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 09:35 It's mostly for developers, I think it's… if I look at it that way. I still think there's an opportunity, it's just not for the businesses we're in, perhaps. Like.
you want to monitor your employees', you know, usage of AI tools and stuff like that. I don't think you can do it. Like, there's a… I read a blog where somebody was talking about how to add OpenTelevitry to VS Code. He was adding it to his agent under the covers that was talking.
And it was complicated.
I mean, it was a lot of work that they had to go and manually add this all-vis SDK, make their own agent that wrap things around, and I'm like… I don't know, it might be possible to enjoy all those.
**Bastian Krol** 10:14 It can certainly be improved, but I mean, the fact of the matter is it's also still complicated for the vast majority of use cases where you just want to run the server workload on a Linux box, so that.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 10:26 Yeah, yeah, yeah, let's fix that first, I agree, I agree, yeah.
**Bastian Krol** 10:29 Yeah, I think we are all in agreement on that, and then coming back to that new column, it could be… I mean, it's maybe a little bit wordy, but installable via package manager on Linux, that's what we want to express, kind of, with less words, probably.
**Ted Young** 10:44 Yeah. I'm hoping we can boil it down to just Linux, with maybe a little asterisk, and then, you know, at the bottom, under the ingredients list, it says… You know, we mean package management when we say Linux.
**atoulme** 10:57 I like it. So, would you like that to be somehow each… Where would you want this information? Where is that table?
**Ted Young** 11:06 So this is on the… on the website right now.
**atoulme** 11:08 On the website itself, okay.
**Ted Young** 11:10 Yeah, if you go to, like, OpenTelemetry.io, and go to Status.
That's just, like, the status of everything at the highest level.
**atoulme** 11:26 I see, okay.
**Ted Young** 11:27 We want to, like, keep this as, like, a cons… I mean, we need to improve what's here, but…
**atoulme** 11:32 But there needs to be…
**Ted Young** 11:34 if we just add another column to, you know, the language APIs and SDKs called, you know.
**atoulme** 11:41 Yeah, that's fair enough.
**Ted Young** 11:41 And then another one, maybe, like, operator, Kubernetes.
Operator might be the right word there.
**atoulme** 11:52 We also have home charts that we should… anyway, we…
**Ted Young** 11:56 Anyways, we can sort out what that means, but we just need to figure out what it means for Linux package management, and I think it's totally fine to add a column there.
So that it's super clear what actually gets installed. The other way would be to just add another section here. The same way we have Kubernetes operator, we could add another section called Linux Package Management.
And I would only do that if it turns out What we're trying to say is too hard to fit into.
Fit into that part up above.
**atoulme** 12:31 the other thing that would be meaningful to me is, if you can have Learn More, if you go back to the main page of the website, because right now it says Learn More, try the demo, and it should be a download button right there.
**Ted Young** 12:44 Download… yeah. Well, this is the… I'm putting my product hat on. I wanted… I go to OpenTelemetry, and the first thing I just see is, like, you know, Linux, Mac, Windows, right? And it's just, like, you click and… and it's more about, how do I instantly get started with OTEL?
Like, regardless of how you do it in production, but… but… We'll figure so much out through this packaging SIG, because there's so many common questions around, like, dependency management, and, you know, what gets installed, and what if you want to… pin something on a certain version because you don't want your telemetry to break, or something like that. I think there's… There's a lot of stuff that has to get sorted.
So I'd kind of like us to get started with that SIG sooner rather than later, basically.
And not buried under too many other things.
I guess my last question on that before we move on is, like, do we feel like we have a contact at all of those different language SIGs?
**Bastian Krol** 14:07 I don't think so.
**atoulme** 14:11 Nope.
I mean, that's… to me, that's the thing that's going to happen, is that this… this packaging SIG is going to get the brunt of all bugs reported.
And we should be ready to… to be the triaging org of Open Telemetry moving forward.
**Bastian Krol** 14:34 Question is probably also how we should… like, on a tactical level, prepare that communication. We should probably make all of them aware what we are doing here around now, basically, so they are… in the know already. They might ignore that for a while, but at least we have made that aware, and we should probably figure out which communication channels we want to use for that, if we just want to open issues in the relevant repositories, talk to them on Slack, or get into their Meetings, or, something like that, and then also who, does that communication.
Fuck.
Just for making them aware, for now, that we are having that packaging initiative, and that it will also, at some point, require Contributions on their end, probably.
or collaboration.
I should say.
**atoulme** 15:38 Yep.
**Bastian Krol** 15:41 So, what… what do you folks think how this should be approached?
**Ted Young** 15:51 I, I think…
**atoulme** 15:52 everywhere.
**Ted Young** 15:53 I can open, commun… well, we have to figure the ordering of it out, but I think we can open a community issue around adding this as, like, a new column, and trying to get… I mean, maybe it's just a matter of, like, just getting a point of contact from each SIG.
I think I could go around to each language SIG and do that, so I can take that as an action item.
**Bastian Krol** 16:18 That sounds awesome, yep.
**atoulme** 16:21 Thank you.
Worst case, Opening a bunch of tickets across all SIGs also.
They can play the TPM route, which is… Something that I see done in organizations like this is you just open a bunch of tickets, link them to each other, and copy them to each of the SIGs one by one.
Yeah. But, you know, if you want a soft touch first. I think we're still in the good phase of the packaging sync proposal, where we need to talk, we don't need to talk.
**Ted Young** 16:51 What… one language that's not listed here that I wanted to mention is Go, Nicola.
like, that would be the… you know, we've been talking about the injector, obviously, and that's why we've been listing these four languages, but if we're talking about the packaging SIG now, this is also an opportunity to include Go. Do you feel like that's… Ready to go.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 17:14 Well, based on the last discussion we had in the OB SIG, it would have to be OB, not GO Auto Experimentation. Yes.
And, as long as the platform is BPF-enabled, I think yes, so Linux would be.
And, yeah, I think we should be good to go. One thing I can think of is… Yeah, I mean, if we want to use the same approach per executable.
Yeah, this is the only kind of thing I have in my mind, because operator asked for OB, or somebody asked the operator for adding OB as a sidecar.
when we can do that, that's definitely one of the modes we support. It's not optimized for that. That's the only, sort of.
downside is, like, some of the internal constants we use are meant to, you know, instrument multiple applications, so… I mean, there could be some… memory overhead if you just launch 500 of them, but for a Linux package, I think it'll be fine. It'll just sit in the background, and we'll tell it which applications to instrument.
It should be fine.
**Ted Young** 18:19 I think there's something to be said for, yeah, the Kubernetes version of this.
running things as daemon sets and trying to figure all of that out, but… Yeah. I almost would want to push for… Go and Obi being part of this early on, just because it might open up more design concerns? Yeah. Right? That we might overlook.
by presuming one technology stack, right? Like.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 18:47 Okay. You listed a couple of things there. Yeah, I will actually… there is a feature, request open, and I'll work on it then, this week, hopefully, because, to… choose the language technology to instrument. So you… right now, you have to… you can choose by port, you can choose by name, executable name, and all this, but if we want to just Go, instrument all my Go applications, we can just… you can specify in your selection criteria, instrument everything that's Go.
And… Yeah, that doesn't exist right now, but we're gonna add it, so it's easy to add.
**Ted Young** 19:22 Awesome.
Okay.
Alright, we should probably move on so we can actually get all the agenda items.
**atoulme** 19:37 Yeah, what's the next one? Python sig updates on the HTTP JSN export. Was that brought up?
I think we… did we discuss this?
**Ted Young** 19:47 -
**atoulme** 19:49 Okay, who brought that up? There's no name.
Is it Westy, or…
**Bastian Krol** 19:54 I think Nikola, Bronx.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 19:55 I already mentioned it. Yeah, so there's just an update we talked about. Sorry, I didn't put my name. Yeah, that's the thing I mentioned. It seems like they're moving forward with solving the issue with, HTTP, I wrote in JSON, it's Protob, right?
**Bastian Krol** 20:12 No, no, no, it's actually, I mean, they already have an HTTP proto-exporter, which has a protobuf dependency, so this… should become an HTP JSON exporter at the end. Okay, okay, alright. They're basing the JSON export conversion on the custom proto-Buff plugin? It's weird, but, maybe…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 20:32 Oh, God.
**Bastian Krol** 20:32 Yeah. Okay.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 20:34 Cool, yeah.
**atoulme** 20:39 dis…
**Bastian Krol** 20:41 dedicated.
**atoulme** 20:44 Good.
**Bastian Krol** 20:46 Yeah, I'm not sure. Is there more to discuss on that? Probably, probably not right now. Yeah, okay. Okay, then we can move on to Antoine's release cycle.
**atoulme** 20:56 to open a PR, and, you know, this is for discussion among us about how we want to, now that we've done a couple releases.
We should probably have some idea of a release cycle, just to set some expectations with the community, to also be able to catch new releases from instrumentation, because what's going to happen is, even if we don't have changes ourselves.
there's a good chance that it's going to be a .NET release, a Java release, or Node.js, what have you.
**Michele Mancioppi** 21:27 Yeah, but this is, this point is moot in a world where the SIG packaging actually happens.
Because we are not going to ship any longer the packages in our releases.
**atoulme** 21:39 Okay.
**Bastian Krol** 21:40 Yeah, but we're not there yet, so…
**atoulme** 21:42 That's true. No, but I mean, if there's any reason to skip a release, maybe we should just skip a release. Also, just that, right? So, every two weeks, we look at where we are. No changes to the code, no vulnerabilities being reported, no changes from any of our dependencies that we currently have. We can… we can say, hey, we're going to skip release XYZ, there's no point, we don't need to do that, and keep using what you have.
We shouldn't make faces just for the sake of it, but… I think we should have a checkpoint every two weeks, at least, and to check whether it's a time for Make a release or not.
**Bastian Krol** 22:17 Okay. Yeah, my main point against that would… would have been, like, yeah, I'm… I think we can just release whenever we have a new feature, and I'll…
**atoulme** 22:28 Oh, okay.
**Bastian Krol** 22:29 from my gut feeling is that we often have stretches of weeks where we don't add a lot of new features, but I didn't think about the new auto-transplantation agents, or the new SDK versions, which is a very good point. And I think… with that in mind, the release schedule makes more sense to me. Once, and that is one agenda item that I push up.
Once we fix the renovate update, because for now, we don't get updates, and we need to fix that, renovate stuff, because we are still on very old, or by now, quite old.
SDK versions.
**atoulme** 23:10 Yeah, you're right, you're right.
Yeah, okay, so now I can see also Miki's point, is like, if we start to set the expectation that we're going to care so much about upstream dependencies, we may set a vicious cycle where… People are like, you don't really need… we don't really need to help you and do unpackaging, because look, you filled the void, and you're doing a release every two weeks. So… And I like also the idea you're having of, like, making a release when it's significant, like, having Python support, for example, is worth having a release for.
So, one thing we could do is just kick the can down the road 3 months and talk about it in the quarter, and see where we are.
**Bastian Krol** 23:47 Okay, yup.
**atoulme** 23:49 If things change, you know… Cause there's… there's no… I mean… as long as you're okay if we make releases on the go, right? So, what's going to happen is, if we don't have a release cycle where we set someone up for release, that means that it's kind of free for all, meaning that whoever's made the last release is the person who knows how to make a release the most.
And after a little while, it's gonna be… Bastion?
**Michele Mancioppi** 24:18 I mean, I feel strongly that.
**atoulme** 24:21 Yeah.
**Michele Mancioppi** 24:21 For me, the release should be as simple as starting manually a job from the UI.
Who's true.
**atoulme** 24:27 True. You're right.
**Michele Mancioppi** 24:29 I feel very strongly about it, Antoine. No other release process makes any sense.
**atoulme** 24:34 I completely agree with that. We… we've had two releases. The first one was, like, okay, it's brand new, not everything works. We had a second one with someone else, so we bumped into different types of furniture elements, we found… we found eventually the light bulb, everything worked.
it would be great to just have yet another person run the next release, whatever it is, just so we get one more piece of feedback from that, so we can keep making it better. That's all I want, really, because,
**Bastian Krol** 25:05 Sounds fair.
**atoulme** 25:06 If it's just Basty running every release, he's gonna get really, really good at it.
And then we're going to be like, hey, you know, we can't possibly make a release, he's on vacation.
Right?
**Bastian Krol** 25:18 Yeah, I mean, we have made, to be fair, we have made some quite good progress on automating it and making it not one click in the GitHub UI, but maybe, like, three or four.
**atoulme** 25:29 4, yeah. Yeah, it's getting there.
**Michele Mancioppi** 25:30 It's…
**Bastian Krol** 25:32 Yeah, with the exception of that one issue that you found in the last release, where, that one… the tag wouldn't kick off the other, GitHub.
**atoulme** 25:42 Oh my god, that was… That was a GitHub thing, right? This wasn't even us, but…
**Bastian Krol** 25:46 Yeah, I think it was… it was us in the end, and I think what you brought up in the end with the GitHub app, AutelBot, we should definitely do that and try that out with the next release. So, of course, we can only test these things when we actually do a release, that's a little bit… a bummer, but I think we should at least prepare that before the next release, that, that works, because I think that the job didn't kick off was not a GitHub problem, that was, actually the, Thing that it doesn't kick off a new, new job if it's done by another Look, whatever.
**atoulme** 26:28 Okay.
**Bastian Krol** 26:30 I can, I can open a GitHub issue for the… for adding the auto-bought GitHub app.
**atoulme** 26:35 Yeah, yeah, yeah, yeah, we talked about that on Slack, so I think.
**Bastian Krol** 26:38 Right.
**atoulme** 26:38 me to put it on GitHub.
Yeah, yeah, I mean, this is exactly this type of learning, it's so important, because then you can make your release cycle better, and this is also you retain people, so you can make it easy for people to continue to support the project. And I completely agree with you, it should be just a click away, it should not be complex, it should be very automated, and we should be able to make a release at any point in time from Maine.
Without any trouble. What else?
Yeah, I mean, what you're saying about we only get to touch this… to learn about this during release, maybe we could do a… I'll… I'll regret saying this, but we could do it nightly, if you want.
Don't know.
**Bastian Krol** 27:23 I think it's…
**Michele Mancioppi** 27:24 Likely.
The nightly idea is not a bad idea, because that is also where we would, when we fix renovate, we would push packages with the latest, latest thing, right?
**atoulme** 27:37 So it's the middle-of-the-world solution for the existing current compromise we have.
**Michele Mancioppi** 27:42 Yeah. And we would not say that this is an official release. It's a nightly, you get the latest agents.
And good luck with that. And eventually, when the packaging SIG is on the road, then we yank The dev releases, and we release only the binary.
But there is in, in the district, perhaps.
**atoulme** 28:03 I like that. So the packagingSig repo would start with some code that we currently have, you know, repo.
I mean, we probably would not take over the FPM code, because as you mentioned.
**Michele Mancioppi** 28:14 I, already have a PR against our repo with what I think could be the release process. Have a look.
**atoulme** 28:22 Okay.
Oh, sure, if you, feel free to drop in.
**Michele Mancioppi** 28:26 Yeah, it's an FPR.
**atoulme** 28:28 It's an PR on, on, injector SIG.
**Michele Mancioppi** 28:31 I think so.
Yeah, because we don't have a repo for the packaging, I mean, we don't have yet the SIG, technically.
**atoulme** 28:37 No, we don't. It's gonna take a little bit more.
**Michele Mancioppi** 28:40 It's, PR239.
**atoulme** 28:43 Yeah, okay, I see. Okay, so… Alright, I'll take a look at that, I think.
I didn't get a chance.
Nice. So, definitely, right? So, we could do a nightly release, and that would probably also… fix this, so just, put some notes on what we discussed, because I'm gonna forget.
So, in the notes doc, I'm saying… We can formalize a release process, a dictator.
Just want to make sure we don't have to make sure… We don't have… Just one person.
Know how to release…
**Michele Mancioppi** 29:25 Also, I do not want to curse it, but my expectation is that The moment you have the packaging seek, the releases of the injector are going to be few and far in between.
I mean, it's gonna be new languages, or fixing some bugs.
Maybe changing the configuration, the configuration format, but the injector is rather feature-complete.
Despite being relatively young.
**atoulme** 29:53 No, that's… that's lovely.
I don't have any feature in mind, maybe supporting declarative config would be a big one.
**Michele Mancioppi** 30:03 That is not for the injector to implement. I mean, the only thing would be to make sure that…
**atoulme** 30:09 It tastes a good step, that's all.
**Michele Mancioppi** 30:10 He added it… maybe in the system package, it goes and looks for the… for the right places, but it didn't… doesn't need to do anything itself.
**atoulme** 30:19 That's true.
**Michele Mancioppi** 30:19 I was thinking more checking and changing the places where it goes and check for… for the tracers, that's it.
**atoulme** 30:28 Any… any notion of agent management you'd like to splice into… splice into the, injector down the road?
**Michele Mancioppi** 30:36 Ethan, no, I don't think so.
The, both in, both in the operators.
And in the system packages, the delivery of the agents are separate.
And they should stay separate.
**atoulme** 30:52 No, I mean, what I mean by that would be… So, there was… there was actually an issue from, I think Jack, on the repository, which was kind of entertaining, the idea that the injector should be able to report status.
Even if it's, so, process inventory tool. On its own, it's a little interesting, but I'm not sure, like, I'm stretching a little bit what he's wanting to do.
**Michele Mancioppi** 31:17 I'm getting flashbacks of the instant agent.
I, I'm not sure.
**atoulme** 31:24 Yeah, I mean, you do, right? What I'm saying is, if we had these type of things in place, You could apply some level of agent management also, where you could say, you know, exclude that particular process from the injector.
Or include only that 3…
**Michele Mancioppi** 31:42 We have that in the configuration file, so the exclusion-inclusion paths, those we have already.
**atoulme** 31:47 Yeah, so we're just changing the file, And that should be good enough. Okay, so the agent management would just be interacting with the injector by changing the config file of the injector.
**Michele Mancioppi** 31:58 Correct. Yeah, because, I mean, the injector is not a standalone process. It's an addition to other processes.
**atoulme** 32:05 Yeah, yeah. I mean, I think this story could be… honed using the existing op-amp tooling of OpenTeometry to kind of show, also.
Some of the things that we can do with that.
Does that make sense?
**Michele Mancioppi** 32:23 Sorry to repeat, I got distracted by somebody talking to me.
**atoulme** 32:27 No, it's… so, I'm just saying… saying that even if we don't need to do anything, I think it needs to be showcased somewhere, so you would be…
**Michele Mancioppi** 32:35 yet.
**atoulme** 32:35 Showing what is possible down the road.
**Michele Mancioppi** 32:40 Yeah, I mean, that's, configuration files, that's documentation. And maybe the system packages Can have a better documentation there, but…
**atoulme** 32:50 Yeah, that's exactly what I'm going for, yeah.
Okay, package in Sea will eventually build… SDKs, and there will be no need.
Or regular radio studios.
And, blocker, anyway, renovate.
Okay, I think I'm done with my item. Anything else we should talk about on that?
**Michele Mancioppi** 33:18 Is there appetite to support Ruby?
**atoulme** 33:22 Yeah, there is appetite for me to support Ruby, it's just, I mentioned, right, the hardest part for me was to get a Ruby maintainer to come out and tell us how to test against So…
**Michele Mancioppi** 33:36 Yeah, I mean, that's the Spotify people mostly, right?
**atoulme** 33:41 I don't even know.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 33:42 Shopify.
**atoulme** 33:42 I have no links whatsoever to them. Does anybody here know a…
**Ted Young** 33:47 I think there might not be a lot of bandwidth on the Ruby side, that's my main concern. I haven't checked in with them a bit, but I will check in with them.
Report back to you guys.
**atoulme** 33:58 Thanks. Yeah, let's see.
**Michele Mancioppi** 34:00 Jack in, in my DMs, suggested to… I suggested, but he was, was, agreeing to, try and make the support in the injector, part of the, compliance metrics of language 6.
To give a strong signal that that is something that languages should do when viable.
**atoulme** 34:24 Yeah, Ted would… so…
**Ted Young** 34:26 We were talking about that earlier, actually, yeah.
**Michele Mancioppi** 34:29 Yeah. I mean, the way I see it, there should be also, like, the same way that traces are stable, and logs are stable, metrics are stable, injector support or auto-instrumentation is something that is either stable or not, right?
**atoulme** 34:41 Yeah. Yep.
**Michele Mancioppi** 34:42 That's.
**Ted Young** 34:45 Yeah, we discussed adding maybe operator as a column, and, like, Linux package management as a column.
**Michele Mancioppi** 34:52 Yes.
**Ted Young** 34:53 Or operator or Kubernetes, it wasn't quite clear what… what the column name was for that one, since there's Helm charts and other things.
**Michele Mancioppi** 35:01 I would assume Open Telemetry Operator.
**atoulme** 35:04 Yes.
**Ted Young** 35:05 That's reasonable.
**Bastian Krol** 35:08 No.
**atoulme** 35:09 Okay, perfect. I'm putting notes in the doc as we talk. Feel free to edit them as you see best.
Okay.
**Michele Mancioppi** 35:19 By the way, speaking of the packaging SIG, Ted, I need guidance on what to do now. I mean, a bunch of people are commenting on the community PR, but I don't know what are the next steps.
**Ted Young** 35:32 Well, the main section that seems empty right now is staffing, right? I think that was something that Jack brought up as well.
We need to get a liaison from every SIG that we intend to ship with as part of this initial batch.
I offered, as an action item, to… Figure out who those liaisons should be.
**Michele Mancioppi** 36:00 Please.
**Ted Young** 36:00 If you already know, if anyone here already knows, just… just DM me. But yeah, I'll… I'll try to figure that out.
I'm talking.
**Michele Mancioppi** 36:08 Can you get JSON for Java?
**atoulme** 36:12 Mr. Plum?
**Michele Mancioppi** 36:13 Yeah.
**atoulme** 36:17 I mean, let me talk to him.
**Ted Young** 36:18 Yeah, I'm not too worried about Java, I don't know who the, who are people talking to over in .NET already? Is there someone already?
Interested in this project over time?
**atoulme** 36:31 I also have people in that I can ask.
Let me ask.
I… we will need to kind of marshal people into the open on that one, because… yes.
**Ted Young** 36:41 Yeah.
**Michele Mancioppi** 36:42 If anything, I'm pleasantly surprised by the fact that A whole bunch of people volunteered to do work for the packages.
I think we'.
**Ted Young** 36:51 We're getting closer to, like, stuff that end users care about, and also, like, feel like they have some expertise in, so I'm actually not… I actually think we'll start to see more end-user interactions with OpenTelemetry through SIGs like this.
**Bastian Krol** 37:07 And if you, say, volunteered, you basically just took a photo of everyone that was in the room and said you now Yet.
**Michele Mancioppi** 37:14 Yeah, that, of course, those were voluntold. But, there was also people that I not… had not spoken with, that actually volunteered. Like, Denny's from Grafana Labs.
that, we didn't meet him in, in, Brussel.
I think also another… a second one.
And the name I don't have in my head.
**Ted Young** 37:37 And, you know, also, like, Red Hat, there are Red Hat people involved in OpenTelemetry, right?
**Michele Mancioppi** 37:45 Yes.
**Ted Young** 37:45 Could be able to get some interest from over there, certainly.
**Michele Mancioppi** 37:48 We are waiting for Pavel to show up, right?
**Ted Young** 37:51 Right? Yeah.
**Michele Mancioppi** 37:54 Why am I talking to them?
**atoulme** 37:57 I'm talking to them… tomorrow? Tomorrow.
Oh… I got a conflict. Okay, we'll figure it out. But yeah, I'm trying to talk to them tomorrow. Hopefully that works.
**Michele Mancioppi** 38:11 So, by the way, action item, can you please try out the PR for the packaging?
And test it and tried to break it.
There is an easy way documented on creating a local APT project, and unless I'm entirely off the mark, I mean, besides the code being mostly clawed, human-proofed.
The biggest item that would be… would be missing is the GPG signing.
the packages.
**atoulme** 38:44 Do you need a key for that?
**Michele Mancioppi** 38:46 Yes, we would need a key, but it's, mostly, I'm honestly torn on whether it makes sense to put it on GH pages, or is there a better alternative?
**atoulme** 38:57 Emil Helm charts on Jewish pages.
**Michele Mancioppi** 39:01 Yes, but that's on GPG, and it's not used for APT, right?
**atoulme** 39:06 Yeah, no, it's not the same, it's not the exact same delivery. I… also, APT seems to be a bit more… okay, I don't know.
**Michele Mancioppi** 39:15 I mean, there is an entire thing done by Canonical called Launchpad to raise APTs, but I would not touch that with a 10 feet pull.
**atoulme** 39:23 Also, it would probably just put us back to the starting point when it comes to RPMs next, because we would need to come up with our own solution again.
So if you had a thing that works for both, that would be better.
**Michele Mancioppi** 39:36 I agree.
**atoulme** 39:37 a free JFrog server.
**Michele Mancioppi** 39:38 Yeah, it's mostly the hosting and the signing that I honestly do not have strong enough opinions.
**atoulme** 39:45 So, does GitHub have, GitHub packages? Don't they host…
**Michele Mancioppi** 39:49 I do not believe it supports DBM Falls. I believe it supports NPM.
I know it supports binaries, Docker images, but I don't remember it to support system packages now.
**Bastian Krol** 40:06 So… your question was who has time to take a look at that, and I would very much not be engaged there too much, so…
**Michele Mancioppi** 40:20 Yeah, I'm such a coward.
**Bastian Krol** 40:22 Yes, yes, no, I mean, that is absolutely… I have no idea about packaging, so… One actually raised their hand, and…
**Michele Mancioppi** 40:31 I'm not asking for people to look into the code, I'm asking people to try the packages.
To get a line exposed and break it.
**atoulme** 40:42 Yeah, no, that's fine.
Yeah, we can… we can take a look. I'm asking internally for the Java.net person. Meanwhile, so GitHub packages… Another thing to consider, Nikla, is maybe we also want to ship this stuff as a RGZ for what it's worth.
I know, so…
**Michele Mancioppi** 41:05 Oh boy, why would you do that?
**atoulme** 41:08 Because.
**Bastian Krol** 41:13 What was that? Come again?
Ship, yeah.
**Michele Mancioppi** 41:16 I make a tarball.
**Bastian Krol** 41:17 That's okay.
**atoulme** 41:18 Oh… Yes.
**Michele Mancioppi** 41:21 But I'm having, I'm having issues… Thinking, why would… in which use case we would use that?
**atoulme** 41:30 Well, vendors want to take it, that's one. Another one… would be to have a way to make it work on other platforms, like Mac, down the road.
**Michele Mancioppi** 41:45 Yeah, but the entire… the entire layout of the… of the configuration files and the location is all gonna be fucked up.
**atoulme** 41:51 On things that there's not finance. As long as you publish the binary, it's fine, right? People will do their own thing.
Okay, so GitHub packages seems to be hosting RPM and Debian packages.
No, shit, no, it does not.
Oh, it's so confusing. Yeah, you can just drop them as release assets on your GitHub release page.
That's what we do.
I won't like it.
Okay.
One problem at a time. If you want, we can open an issue with the Infrasig, so there's a number of people who are dedicated to the project's infrastructure.
I think it's time to ask them how to help us with that.
Does that make sense?
**Bastian Krol** 42:46 Michaela just dropped, for whatever reason.
**atoulme** 42:49 Okay, that's okay.
**Bastian Krol** 42:51 Yep.
But I guess that's a good idea.
**Michele Mancioppi** 42:55 There it is again.
Oh, Zoom crashed. Let's go.
**atoulme** 43:00 Make it so… Well, Craig, right, so there is a SIG, for Pentimeter responsible for project infrastructure, and we could ask them for Debian RPM package support. If they can't find a way to help us.
We're going to go with GitHub pages for now, until we know better.
That works.
**Michele Mancioppi** 43:22 Are you sure it's a good idea?
**atoulme** 43:27 I have no idea. Actually, I'd like it to be wrong, and then we can fix it, rather than not doing anything.
**Michele Mancioppi** 43:34 Hmm.
Because, is it the same sick that took, like.
two months to find out which Google account to use for the certification of the OpenTerm Operator on GK Autopilot.
**atoulme** 43:46 It's the same thing that also is taking 6 months to get us IBM support, because IBM and CNCF have to sign papers, and there is a contract there. There's some inertia, but it's not caused by their own ability to execute, but by the fact that everything they do As long… as soon as there is a vendor or some other third party involved.
gets 10x more complex than it should be. But the Trask and the people running in that SIG, they have good intentions around GitHub Actions, for the most part, as they've done a wonderful job of teleforming everything that we have in our repositories, so it's easier to manage at scale.
Helping, helping Trask.
bus-based task in Austin.
Yeah, you can pingtransky, Tamila, yes.
**Michele Mancioppi** 44:37 Yeah, fantastic.
**atoulme** 44:38 official, so it's not just team, but yeah, feel free to… Okay.
Cool. Bessie… Bessie, you wanna talk about the next step?
**Bastian Krol** 44:53 Yeah, we kind of mentioned both of them already, and it's mostly really just two items that we should take care of in the next weeks, I would say, and it's me asking who can wear cycles to look into that.
So one is the release with the GitHub Autobot app. I can…
**atoulme** 45:16 Yes.
**Bastian Krol** 45:17 Inquisite, or what?
**atoulme** 45:20 Yeah, makes sense. Yeah.
I can assign that to me, and the other one is, the renovate updates for the auto-instementation agents, which are broken since… since I think they never worked, and I would love if someone could take a look soon.
This is pretty bad, and frankly, he told me.
So, I'm guessing I'm really psychiat. I don't seem to be taking the time to read the docs properly. For someone who's an actual engineering degree.
wants to look into that, that'd be great. I can also ask for help outside.
**Bastian Krol** 45:57 Okay, that would be awesome, because I haven't used RenoH.
**atoulme** 46:02 Yeah, it's pretty… I mean.
Eric, but you need to pay attention for more than 5 minutes, and I seem to be unable to do that.
**Bastian Krol** 46:09 I don't know.
**atoulme** 46:12 The other thing is, like, it's a little tricky to make sure that it's working the right way, so, I think… I've tried twice with, like, best effort attempts. I was like, I'm just going to copy and paste what I see is working also there, and I'm like, it didn't work. Okay, maybe…
**Bastian Krol** 46:28 And it's also kind of really hard to debug or even see why no job is starting or stuff, so that is kind of… Pain fluid.
Yeah.
**atoulme** 46:41 I mean… Yeah, again, like, these are… these are jobs that… Anyone… on a project can take, I'm happy to ask around for help on Renovate.
I'll do that internally to my company,
**Bastian Krol** 46:56 Yeah, thank you very much, that's much appreciated.
**atoulme** 47:03 Hmm.
**Bastian Krol** 47:03 Unless we want to strategically ship outdated… SDKs to not set any expectations, but that came up before, but I think that's not really…
**Michele Mancioppi** 47:15 I like dressing our deficiencies as a deliberate strategist.
**Bastian Krol** 47:20 Yeah, exactly. I think we should get that fixed.
**Michele Mancioppi** 47:24 Speaking of deficiencies, Ted, Jack told me that his plate is pretty full in terms of technical committee sponsorship for the SIG packaging. Do you have a sacrifice of honor you could point me at?
**Ted Young** 47:43 So, I think we should just bring it to the TC as to who wants to be a sponsor, right? That's what you're missing? Just the TC?
**Michele Mancioppi** 47:52 Yes. Pretty much, I would say we're at that stage, yeah.
**Ted Young** 47:56 Yeah, and I would say for this one, it doesn't necessarily have to be a TC. It could get delegated to somebody, but that would be if, I would say, someone like Pavel or somebody who showed up with a lot of, like, packaging experience.
Who also knows OpenTelectricity really well.
So, just throwing that out there. If there's someone who isn't a TC member, but you think knows both.
enough about OpenTelemetry and package management. We could add them as a sponsor.
**Michele Mancioppi** 48:25 Luke, there's wrong with you, please.
**Ted Young** 48:30 Thank you.
**Bastian Krol** 48:30 And what exactly is the role of a sponsor in that regard? I'm not sure…
**Ted Young** 48:35 So, I think of this as, like, the sourdough, like, starter.
starter yeast. We find, like, when we analyze, like, why SIGs do really well versus why SIGs, will go make a design and then struggle to, like, get it accepted, a lot of it is just… how much of, like, open telemetry design feedback it gets, because usually with these SIGs, the subject matter experts are no longer, like.
You know, the people who were subject matter experts in, like, tracing or something.
**Bastian Krol** 49:12 Back in the day.
**Ted Young** 49:14 But you need to talk to those people, because that's how your stuff is gonna fit in with everything else. So just making sure that there's… ideally at least, like, two TC members, or someone the TC has delegated as saying, like, yeah, as long as, like, this person is hanging around the SIG, The chances that the design that comes out of this SIG will be one where we're like, what? This doesn't, like, work well with anything else we're doing. It's, like, much lower.
**Bastian Krol** 49:43 Okay, understood, thanks.
**Ted Young** 49:45 nip.
**atoulme** 49:57 I think we covered everything. Anything else?
Okay.
**Michele Mancioppi** 50:07 Alright, I need to drop by folks.
**atoulme** 50:10 Bye, take care. Cheers.
