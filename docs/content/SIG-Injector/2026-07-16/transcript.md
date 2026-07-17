SIG: SIG Injector
Date: 2026-07-16
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**atoulme** 03:10 All right, so.
Got one more.
No sticker here.
**Bastian Krol** 03:18 Oh, no, yeah, it's… he's back every week, and I don't even know who Joey is.
**atoulme** 03:24 We'll never meet that person.
**Bastian Krol** 03:27 Probably not.
**atoulme** 03:28 Otter, Zoom…
**diego** 03:32 Hey, what's going on?
**Bastian Krol** 03:34 Okay.
**diego** 03:36 Hey, J Thank you.
**jberg** 03:38 There you go.
Hi, everyone.
**diego** 03:40 Okay.
**atoulme** 03:41 And it's gone.
**Bastian Krol** 03:44 Maybe we'll get rid of it once we switch over to the other Zoom meeting.
**atoulme** 03:47 That's,
**Bastian Krol** 03:48 Yeah, it's a good outcome.
**atoulme** 03:51 I actually think this might be the reason, right?
**diego** 03:56 I wonder what… It's in those notes.
**atoulme** 04:01 You know, a move that I heard was pretty cool, is that if you meet a boat like that that's recording notes on Zoom, just start to talk about the Titanic, or you copy the Wikipedia page of Titanic, and you use your Mac to say it. You know, there's a say command on Mac.
And so, you can have it record everything about the Titanic, and then summarize it back to the author that there is a boat out there in grave danger that they go to take action to save all the passengers.
Oh.
Which is cool.
So, got the agenda up here.
Do we have an agenda today? Thanks, Jack.
Oh.
Thank you.
Okay.
Yeah,
**Bastian Krol** 05:11 I don't see anything on the agenda. Antoine, do you want to talk about these weird… Additional architecture, if you want to add.
**atoulme** 05:21 Yeah, I was wondering that it's… It's not urgent, Okay, so, I had a discussion with the operator SEEK folks, and they said, hey, your stuff from the injector actually works pretty well, and… We were playing with it, and we, you know, we really had it work. Well, here's the… sorry about the noise. We just had a little bit of an issue. It doesn't support all the architectures that the operator supports.
**Bastian Krol** 05:50 That's where it's coming from, that's good information, yeah.
Okay.
**atoulme** 05:54 So, I thought, okay, you know what, I haven't dipped my toes into coding for Injector just in a little while, let's just give it a shot, right? How far can I get.
**Bastian Krol** 06:05 Of course.
**atoulme** 06:06 And I just used, like, basic inference, like, every time I see AMD and ARM, let's add more options and see how far I can get with the matrix build. And now I'm realizing that I think there is an issue in Zig, where some of the POSIX libraries are missing.
I'm just reading from the build output, right? That S390X and PPC6480 just don't have the same level of POSIX implementation as the others.
I mean, that's what the build seems to tell me.
Did you look at that?
**Bastian Krol** 06:37 I did, I did not look into it, it's in draft, I, but… So, what do you mean? The operating system doesn't offer the same system calls, so Zig can't do…
**atoulme** 06:50 Oh, maybe I'm.
**Bastian Krol** 06:51 What it wants to do there, or…
**atoulme** 06:54 Yeah, okay, so I rebased and missed something up. Initially, yes, there were some POSIX, calls that were missing. Let me see that… Yeah, here is in the former commit… I think I messed up something else… the… the actual…
**Bastian Krol** 07:16 Do you mean to share your screen or what?
**atoulme** 07:19 Yeah, but it's gonna be mostly upsetting for me, because I think I can't remember exactly, and I don't have it.
**Bastian Krol** 07:25 Okay.
**atoulme** 07:26 So, anyway, yeah, bear with me, I'm gonna keep working on it in some, like, limited capacity, and I don't think this is urgent.
But I wanted to see what we could get for free, and I don't think we had a… A very crisp thing.
Yeah, okay.
**Bastian Krol** 07:46 Okay.
**atoulme** 07:46 I don't see it here, but I was able to see it on my laptop. It's like the build. I will post the message with more information. There is a comment here by Michele, which I think is relevant, which says, I personally do not feel comfortable in distributing binaries. We can neither test nor troubleshoot. That's a fair point.
**Michele Mancioppi** 08:05 I think that method is prophetic, Antoine. It's not only accurate, it's prophetic.
**Bastian Krol** 08:11 How does the operator project handle that? Do they also run their stuff on GitHub Actions, or do they have separate CI, or…
**atoulme** 08:24 Well, so, of course, with GitHub Actions, you have the ability to run with external runners that could be based on some other architectures, and the GitHub Actions runners work on S390X, no problem.
Same for PPC 64. I don't know if you know this, we've been trying to get with IBM for a while to get S390X partners, and this has gone from, okay, we just need this to work for OpenTelemetry, to it needs to work with CNCF, to it needs to work with Linux Foundation.
to the two legal departments of IBM and the LLM.
**Bastian Krol** 08:57 We can work together.
Gods.
**atoulme** 09:01 So that's been a year. So I think it'.
**Bastian Krol** 09:03 Yes.
**atoulme** 09:03 Sure.
Once we do that, we will be able to have S390X GitHub Actions runners.
**Michele Mancioppi** 09:10 I'm going to say, I'm going to Google in the record to say something that may come across as toxic.
But until IBM puts in the work, I don't care about PPC or S390X.
**atoulme** 09:23 Okay, fair enough. That might be a fine line in the sand to drive, if we want that. Or if a vendor out there, like, you know… my company's affiliation, decides that they want to put, a fair amount of resources into that, that's fair as well. But yeah, otherwise, we can… so the way, the way this is done with the collector, by the way, is that there are some guardrails and some expectations that are built in.
Are you familiar with the the support tiers in the collector?
I could try to get away with it.
For free. Okay, so let me, let me just,
**Michele Mancioppi** 10:02 Yeah, but there you can piggyback on the fact that Go has pretty spectacular support for those architectures. That's not the case for other languages.
**atoulme** 10:12 That's.
**Bastian Krol** 10:13 I would assume it's not too bad in, in ZIC probably, but that's really just, just a guess, I think. But I think you can cross compile to that as well, probably.
**atoulme** 10:23 Yeah, we can cross-compile on Z for what I can tell, but.
**Michele Mancioppi** 10:26 Absolutely right.
**Nikola Grcevski @ Grafana / OpenTelemetry** 10:29 There might be an emulator like, why are we not considering that?
Fine.
Hearing you, or…
**Bastian Krol** 10:39 Yeah, that would also be an option. I mean, slow, but… Nikola Grcevski @ Grafana / OpenTelemetry 10:41 Exactly.
**Bastian Krol** 10:42 thing.
Yeah. It's better than not testing, for sure.
**Nikola Grcevski @ Grafana / OpenTelemetry** 10:48 I was gonna say, I also have an old PS. 3. That's power. PC. I can try to run Linux on it and put it up.
**atoulme** 10:58 You sure you don't want to play, like, Assassin's Just.
Okay.
**Bastian Krol** 11:03 CI runs under Nicola's desk.
**Nikola Grcevski @ Grafana / OpenTelemetry** 11:06 That's awesome.
**Bastian Krol** 11:07 Right.
**atoulme** 11:07 Yeah.
**jberg** 11:10 We should get an issue open for this, just so, we can sort of talk about centrally what the desired architectures are and what the trade-offs are for supporting them. I'm trying to find… where the operator, documents its supported architectures, and I don't see anything in, like, written documentation. The closest thing I see is, like, There's a just in one of their part of their build, you know, I see the list of platforms supported and to the extent I can tell that's like how they how they're expressing which platforms they support.
**atoulme** 11:46 Yeah, so that's actually my first question back to the operator. It's like, who's using this stuff? You know?
**jberg** 11:52 How did you come to support these?
**Michele Mancioppi** 11:57 Ali, who's using this stuff? Yeah, it's OpenShift.
The, actually, in Thunder Zero, I mean, we are talking to people that are running the OpenTelemetry operator on OpenShift on exotic architectures.
**atoulme** 12:12 That's Yeah, yeah, but I mean.
Is it really used directly? Like, what's the download number? Is it 10 a month? Is it, what are we talking about here, right? Are we… and so maybe there's a discussion we're not having yet about whether the operator in the first place should be supporting that, which maybe is the first step.
And if it's supporting that, then what are the guarantees?
So I think, to Jack's point, that might be a bit of a discussion to have with your operators to push back on them and say, look, we need you to document what you expect here.
That's fine.
**Michele Mancioppi** 12:50 Also, I would, I would argue that I mean, even if… I mean, in a world in which the operator adopts the injector, which is great.
There will still be the manual, the manual backward support, so making the, the injector-based approach work only on AMD64 and ARM64.
As a way to get started, I don't think it's the end of the world. And that will actually provide incentives for Big Blue and Red Hat to come and, you know, do their bit.
**Bastian Krol** 13:22 From a quick scan, also in the operator repo, they publish images for the four architectures, so what two we have and the two new ones, but they don't actually run any tests.
On these other architectures, so… I'm not sure if that's an example that we want to copy, but yeah.
What you said, Michaela, sounds okay, but that would mean that the operator needs to have different behaviors, depending on the architecture. That's maybe… Not sure if they are cool with that.
**atoulme** 14:00 They won't be cool with that, but… So, anyway, I… That's a Draft PR. It's just hanging out.
Trying to drive some… learning, and I'm noticing that I need to do a bit better and make sure that I actually pinpoint exactly what doesn't work.
Besides the fact that I messed up some bash groups.
So, I'm gonna go and do that, and this is not urgent, and can be in here for another 3 months.
And we can keep talking.
And that was it.
**jberg** 14:45 Well, so I guess from an urgency standpoint, if it's the thing blocking the injector's integration with the operator, it arguably is urgent, at least to reach a resolution with those maintainers about which architectures and why.
**atoulme** 15:01 Yep.
Let me try to build it then.
But yeah, The discussion that happened here was more like a private discussion.
**jberg** 15:18 And.
**atoulme** 15:18 Because this is just Mikolaj from one of the operator leads just trying things out.
I know this is very different from the… well, it's not different, but it was, like, a clean room POC that he was doing that I think is different from what Mikkeli had offered with the draft PR for the operator back when. So, for what it's worth, that might be,
**Michele Mancioppi** 15:42 Yes, my PR was, when I closed it, it was a broke off, broke concept, and that the last cube came down to them. The city said, oh, we're gonna start over, and then Jacob said, yeah, I want to go and redesign the instrumentation service, and they're on, yes.
Still very much ongoing.
**atoulme** 16:07 Mmm.
**jberg** 16:08 Well, it's a positive signal that, you know, some of their leads are picking it up and trying it for themselves, so, you know, I think what we can do is, you know, capture whatever feedback they have and issues and try our best to resolve them, because that's where we all want to get to, is where the operator is using the injector.
**atoulme** 16:28 That's fair.
Yeah, I think I messed up somewhere.
So, yeah, I would say, don't look too much at that PR, work on it.
Okay.
**jberg** 16:42 I messed up, and maybe it's easy, and it's just a matter of, expanding our test matrix.
**atoulme** 16:47 Yeah, exactly. This sounds like… I need to continue to work on it. So, let's… Yep.
We'll let you know as I go through this.
**jberg** 16:59 Cool.
**atoulme** 17:02 All right. What else?
Yeah, that's… Is there anything else on the agenda?
Alright, clean up packages with draft release of system package SIG.
Well, yeah, so just 20 minutes ago.
We merged the first PR for the packaging SIG, and then we're on the verge of merging the second one, where we're going to be able to make a draft release of the packages, and that is going to supersede whatever we have had for the injector, and I think that's what this is about.
This line implies that eventually we would want to just… the injector seek should just be… showing a dot so far or whatever it is that we're building from Zig and not concern itself with bundling instrumentation SDKs and doing a bunch of like extra work and then therefore move towards packages being the source of truth for distribution.
Am I getting this right? I'm not sure who put that line, but I think it might have been me today.
**Michele Mancioppi** 18:10 And we must continue making GitHub releases with the binaries, because that is what is being used by the system packages pipeline. But we can clean up.
most of the stuff in terms of creating DAB and RPM archives, just keep the integration tests here.
And there is a second interesting opportunity.
The system packages, thanks to Diego.
have, now inside the System Packages repository.
2 exporters for python, one for acp protobuf and one for Grpc. That have exactly 0 dependencies.
And through those, since those exist and we can point people at it to use them, I feel we could graduate the support for Python.
Yeah, but no, otherwise the name, yeah.
**jberg** 19:02 I mean, yeah, that's great. So what's the status of those PRs, Diego? Or I don't know if they're PRs. Did that work? I saw you showing that a couple of weeks ago. Did that… How did the Python SIG react to that?
**diego** 19:16 Actually, the… Well, I don't think there was much of, of a reaction. It's a… it's something I… Actually, I have the Python 6 is happening in 10 minutes, so I can — Pretty much, ask again, you know.
**jberg** 19:40 Yeah.
**diego** 19:41 Yep.
**jberg** 19:42 So are they just — I assume you went and talked to them about this. You're saying there wasn't much reaction. Does that mean it's still in a PR format? Or what's the status?
**diego** 19:54 No, I mean, well, I, I also probably introduced it, as something that was very prototypical then, and, And, I don't know, maybe people were, oh, there's Diego being crazy again? I don't know, but… I'll try again.
I'll try again in 10 minutes, and I'll… I'll tell them, this is the… this is the solution. This is what we need, you know?
Nothing works today, but… Mercy is, everything works.
**jberg** 20:29 Yeah, is… so do you have a proper PR open? Because, I think… I think there's a number of people outside the Python SIG that are sort of looking around at Python and saying, like, look, this this is a problematic dependency. And, you know, Python is is a problem for the OTel ecosystem right now. And so, like, if you have a PR open that links back to the issue that talks about the the the protobuf dependency as, like, a a toxic dependency, then, you know, that's an opportunity for Other folks that have expressed an interest, this group, I know Ludmilla, another TC member has also liked expressing this. We can go and talk about our support for this PR and get behind it and encourage the Python maintainers to take a hard look at it.
**diego** 21:16 Totally. Just, a word of warning. This is, And all the can of worms. Yeah.
In the sense that the problem that we're trying to solve here is actually structurally a problem with Python itself. So this is something that has been a problem for us for years.
all the parts of the project, like the Bootstrap project for Python, have had… have faced this problem.
All the time, like when we install dependencies and so on. So yeah, implementing a dependency ourselves is a solution.
of a common problem that we have all over the place. For example, file configuration.
uses PyYAML and JSON schema, which are also third-party dependencies. And we also go to great lengths to only install them when it's absolutely necessary, and so on. So, yeah, I can present it today.
And yeah, hopefully people like it.
And and we can get this, how did… I… I do expect people to have questions about, say.
So we're going to have our custom Python protobuf implementation who's going to support that if things change and so on. But yeah, I'll give it a try and let you know.
**jberg** 22:55 So the historic problem that you're talking about is Python has problems with dependency conflicts.
Right.
**diego** 23:03 But to be more specific, the problem is that Python can only support One.
dependency per package, right? So, in… it's not like Node.js, where package A has its own dependencies, and package B has its own dependencies, and so both of them have… can have different versions of the same dependency, and work together.
In Python, you can only have one dependency.
For example, Protobuf, and that has to work for… everyone. So, if the application code was using Protobuf, and they wanted to use a specific version, and then comes the injector, and they want, Then comes an exporter added by the injector and that exporter wants to use a different version.
They crash the doesn't work right. So yeah.
**jberg** 23:53 Is it any version conflict or is it a version?
discrepancy that, you know, that has like a breaking change on it where like, you know, application wants to use feature a of the YAML library and the library wants to use feature B of the YAML library. And there was a breaking change between, you know, version one and two where A and B are introduced.
**diego** 24:17 I mean, it doesn't…
**Michele Mancioppi** 24:18 Yes.
**jberg** 24:19 Yeah. It's breaking changes. Right. So that that's no different than, like, you know, an ecosystem And so what makes a dependency toxic is if it's very popular and it has breaking changes. Because if it's very popular alone, that's not a problem if it's very stable. So it's the popular and breaking changes. And so the protobuf library in Java is like that. And we booted that because that's a toxic dependency.
And so, like, you mentioned a couple of other dependencies, like the YAML dependency for file config. You know, I'm not sure if that's a toxic dependency or not. Like, does it have breaking changes such that you produce these version conflicts?
Yeah.
**diego** 25:01 Yeah, the issue is that toxic is quite subjective, right? Because we don't know. I mean, of course, we expect some libraries to be very popular, but I don't know. Anyone can perfectly use PyYAML in their application, right? I mean, there's nothing that's substantive. Yeah. So yeah, this is a structural problem with Python.
And,
**jberg** 25:25 But not just Python, that's what I'm trying to communicate Java has the exact same issues that you're talking about.
**diego** 25:31 Oh, well, so…
**jberg** 25:32 I don't.
**diego** 25:33 I don't feel that bad now.
**jberg** 25:36 Okay.
**Michele Mancioppi** 25:36 I have very, very.
**Bastian Krol** 25:37 I think it's only Node.js who has that, solved differently and makes it a non-problem from the start.
**diego** 25:43 Yeah, only Node has the fancy, and well-designed.
**Michele Mancioppi** 25:49 Java and .NET have it too, come on, it's actually Python the problem here.
No other language.
**diego** 25:55 Excuse.
**Michele Mancioppi** 25:56 Absolutely no concept of class loading domains or anything of the kind. Go on.
**Bastian Krol** 26:01 That only does not have it, because you cannot… can only attach one profile, I think that's a little different, but yeah, again, we digress, I guess.
**diego** 26:10 Hey, curious, Jack, if you had that problem with Python with protobuf in Java and you booted that, how did you solve this problem?
**jberg** 26:20 We booted the dependency, so you get rid of the dependency the same way that you're describing.
**diego** 26:25 So you implemented Protobuf yourselves?
**jberg** 26:28 Yeah, but we do, we do binary encoding of Protobuf ourselves. We hand roll it.
**diego** 26:33 See, they're doing the same thing.
**jberg** 26:35 Exactly! That's what I was trying to tell you when you presented this. I was like.
**diego** 26:39 A lot of sens.
**jberg** 26:40 This is what we did in Java.
**diego** 26:41 See, the guys in Java are… that's the only argument I need now in 5 minutes, you know?
**Bastian Krol** 26:47 There's PRR, there's precedent. Excellent.
**diego** 26:51 I'm not.
**jberg** 26:51 I think there's other languages that have precedent too. So you're not on your own here.
**diego** 26:55 I'm not even… going to bother explaining this to anyone. I'm just gonna say, Hey, Jack says they use this in Java. You know, that's it.
**atoulme** 27:03 Yeah, look at that CR, like, that I put in the chat. This is Jack being incredibly good at his job and removing Jackson.
from the dependencies, and then hand-rolling a JSON serialization right there, and then…
**jberg** 27:19 That's a lot easier than Protobuf. The person who did the hand rolling of the Protobuf was this old guy named Anurag, who's just like, I don't know if you've seen him around. He was prolific when he was involved in this project.
**atoulme** 27:32 He's the best.
I miss him.
**diego** 27:35 All right.
**jberg** 27:36 Exact.
**atoulme** 27:37 He's listening to this recording, and it's like, hey, they still miss me. Yes.
**jberg** 27:41 Come back on a rug. Come back.
**atoulme** 27:45 Oh, well, yeah. Yeah, no, good job, Jack, on that one. Really cool. See? Yeah. Yeah.
**jberg** 27:51 about the toxic dependencies. When it comes to the YAML dependency, that one's a lot trickier because I don't want anybody to be hand rolling a YAML parser, but, I have ideas about that.
**diego** 28:02 We did it for Protobuf, why not for YAML?
**jberg** 28:05 Oh.
**atoulme** 28:05 Oh, you haven't met the Yamo guy.
**jberg** 28:09 Oh.
Yeah, like where JSON seems palatable, YAML is outrageous. The spec for YAML is so complicated.
**diego** 28:17 That's cloud problem.
**jberg** 28:20 Problem, yeah, there you go.
**atoulme** 28:22 No, I met the YAML guy at the KlippCon, and he explained to us that his next version is going to make executable YAML.
And…
**jberg** 28:31 Executable, yeah.
**atoulme** 28:33 Yes. You can run scripts in your YAML. You can actually do HTTP retrievals, so you can include other YAML documents in your YAML. And it's… and you had a C working implementation of it.
**Nikola Grcevski @ Grafana / OpenTelemetry** 28:45 I was like.
**atoulme** 28:45 This solves Kubernetes for real. Then we're done.
Watch this.
Okay, all right.
**jberg** 28:52 All right.
We went on a tangent there about Python, and I think it originated from a good place, which is like, how can we get Python from this opt-in feature in the injector to on by default, like all the other languages?
**atoulme** 29:07 Yep, ye.
**jberg** 29:08 in our tangent, but, you know, that that that's the path we're trying to get to, and I think we're we're all aligned with that in this.
**atoulme** 29:15 Yeah, the SIG is driving and also I see maturation through that. So it's really cool to see the requirements of the SIG now helping the language SIGs find ways to make them better. So awesome.
**Bastian Krol** 29:31 Great.
**diego** 29:32 Alright.
**Bastian Krol** 29:32 Good.
**atoulme** 29:35 Hey, everybody.
Have a good day.
**jberg** 29:37 See ya.
**Nikola Grcevski @ Grafana / OpenTelemetry** 29:37 Yeah, go ahead.
**Bastian Krol** 29:38 Bye.
