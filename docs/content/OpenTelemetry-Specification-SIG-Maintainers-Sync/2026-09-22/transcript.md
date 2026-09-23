SIG: OpenTelemetry Specification SIG + Maintainers Sync
Date: 2026-09-22
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

Reiley Yang (Microsoft Corporation) 00:02:53 Hi, Florian, Michele.
Hey, thanks for joining.
Hey, Tigran. Morning.
Tigran Najaryan (Splunk Inc.) 00:03:49 A little bummer.
Reiley Yang (Microsoft Corporation) 00:04:42 Hey, Ara, thanks for joining.
We'll give, two more minutes for folks to join. Meanwhile, please put your name on the attendees list.
Hey everyone, thanks for joining. We'll start in a minute.
Please put your name on the attendees list.
And Josh, I see that you're here, so we'll start from your topic very soon.
Josh Suereth (Google LLC) 00:06:10 Cool.
Reiley Yang (Microsoft Corporation) 00:06:55 Okay, let's get started, Josh.
Josh Suereth (Google LLC) 00:07:02 Alright, so this one, is, is, approved. I wanted to get at least one other proto person to take a look at this.
There's two things to the discussion here, which is why I said it might take long. The actual change that's being proposed is, for profiling, because we are in the protocol, and we have this experimental spec, and you can make breaking changes in the experimental spec, there will be a flag.
That you send, which is, you know, a version number.
And then, if you are accepting the profile at this, like, V1 experimental package directory, you look at that version number to figure out whether or not you really support The current state of the experimental profiling You know, shape.
So the idea here is, while we're in experimental, we're allowing breaking changes.
But downstream consumers and the whole ecosystem are trying to, like, treat this almost like it's stable, right? But we're not stable yet, because we're leaving open the possibility we might be wrong, or have to make a breaking change, or fix things.
So, to work around that, because we don't really have a version number to put anywhere else, there is a profiling-specific flag, if you will, or integer.
In experimental, and only in experimental, that disappears when experimental's over.
whenever a breaking change occurs, that number bumps, and then you as a consumer basically use that number to figure out what version of the proto you need to read, or you can just say, I only accept one and I reject everything else, so you're not broken.
And so the ecosystem can hang together.
I think this is totally fine, the way it's designed. It's designed to be removed when profiling goes stable. It's hopefully a very temporary thing, because we want to get to stability as quickly as we can, and have the whole ecosystem work. So, I just wanted to call that out, in case people weren't aware of this and see it, because I think this is a good way for profiling to… hang together.
But I… there… there is this overall… there's two questions in my mind I want to make sure that we all agree to. One is about compatibility layers within the pro… within, the protocol, right? And, like, this notion of how we're gonna treat experimental.
Everything they're doing is completely allowed, from the specification we've written.
And I think this is a good way to help the ecosystem deal with some instabilities there that we didn't otherwise have.
So I think this is a pattern that works for experimental. The second would be, we have talked a couple times about content negotiation within the protocol.
That would allow us to make significant changes without breaking the ecosystem.
I think there's some lessons here, but I don't think that discussion's really worth, like, urgent. It's just yet another reminder that we need to get that sorted, or have those discussions, and kind of figure out what we want to do. So, mostly what I wanted to have is this has, like, I've approved this, this is approved by the profiling folks, we have enough to merge.
But I wanted to at least have a discussion here before we click the merge button, so people know what's going on.
I'll leave it for discussion now. I think… I don't know if Robert or Tigran was first, whichever one.
Tigran Najaryan (Splunk Inc.) 00:10:19 Yeah, I can go first. So, yeah, I saw this, I was away last week, Josh, sorry, I couldn't take a look at it. I will take a look. Just a couple comments here, I think it's fine, conceptually, to have this information somewhere on the protocol while it's experimental.
I'm not entirely sure… about the medium that we're using for recording the data in the headers. Did anybody from the collector take a look at this?
were saying the intermediaries should preserve this information. As far as I can remember.
The collector has no way to preserve headers.
in the pipeline.
Unless something custom is implemented there.
Michele Mancioppi (Dash0 Inc.) 00:11:06 Isn't, something that works actually with the context?
I know that you can access,
Tigran Najaryan (Splunk Inc.) 00:11:13 So you have to do… yes, that… you have to put something in the context.
But that would be a custom implementation in the receiver.
I don't think it's going to work by default.
It certainly won't work if you do… If you do botching or anything like that.
forget about that, but I don't think we have budgeting for profiles supported, so there is… There's a bit of a concern for intermediaries there, is all I'm saying, so let's make sure that the collector maintainers take a look at this and confirm that this is implementable.
Otherwise, I think we could just put this in the… the payload itself, right? Not in the headers, the same information could be there.
And the other comment I have is you call this content negotiation, which I'm a bit confused about. As far as I can tell, there's no negotiation at all. It just records the source version. That's it.
There's no back and forth between the sender and receiver. Am I misunderstanding anything there?
Josh Suereth (Google LLC) 00:12:21 No, no, this was, sorry, yeah, I… I should be careful about the terminology I use. When I was talking… we have talked about content negotiating in the past. This is actually about, having, like, fields that represent what the content actually behaves, or what the content actually has, and having this, like.
Nuanced understanding beyond just major version.
Right? And so, I think that there's a piece of content negotiation, which is having that ability, that I think might be something we want to entertain more of. But mostly, I think this only impacts experimental, so, like, the urgent thing is there.
I want to have the content negotiation discussion later, and it's something that this triggered in me, of like, if we had that, maybe that would have been an option here.
Right? But it's not. So, it's a reminder that I think we have some features we might want to add to OTLP.
Tigran Najaryan (Splunk Inc.) 00:13:19 Okay, okay, sounds good. I'll take a closer look, I'll try to do it today.
My only… it seems like I glanced at it, my concern is about the collector.
Conceptually, I think it's… I'll, I'll do an offline media.
Nayef Ghattas 00:13:37 So, I think we've looked at it, and it's… and I think both of your concerns should be covered in the spec about the collector.
So the issue for intermediaries only happens for intermediaries that do not parse the payload, that just take it transparently and reflect it, which is not the case of the collector, because the collector needs to read it, parse it into PData, and then re-export it, after going through processors.
So what happens in the collector case is that we need to implement something in the OTLP receiver.
That tells us whether the protocol version we're getting is, aligned with the PData version that the current version of the collector deals with.
And once that is the case, the collector will treat it and convert it to PData and re-export it. If that's not the case, the OTLP receiver in the collector can just drop the payload because it's not able to… turn it into the PData representation that the current version of the collector knows how to handle. Does that make sense?
Tigran Najaryan (Splunk Inc.) 00:14:44 what you're saying makes sense from the perspective of what the receiver supports, but the PR, as it stands, says the The intermediaries should preserve the version number.
How is it supposed to be preserved?
it has to be stored somewhere as an information while the P data passes through the pipeline so that the exporter can then Look at that version number.
And, when marshalling, use that particular version.
Nayef Ghattas 00:15:15 Oh, by intermediaries, we meant proxies, like, pure HTT.
Tigran Najaryan (Splunk Inc.) 00:15:19 The collector is an intermediary, right?
Nayef Ghattas 00:15:22 Oh yeah, so maybe, yeah, maybe this can be clarified in the, in the PR in that case.
It wasn't meant for you.
Tigran Najaryan (Splunk Inc.) 00:15:30 Intermediary, you didn't mean the collector.
Nayef Ghattas 00:15:32 Yes, we did not meet the collector.
Tigran Najaryan (Splunk Inc.) 00:15:34 So in the collector, then, whatever the version number of the input is, it will be… it will be, unmarshalled into P data.
Assuming that the receiver knows how to do it, it is compatible with that version. Then when exporting, it will use whatever version number the exporter has, not the input version number. So it may change the version number as it passes through the collector, and that's what you expect to happen.
Nayef Ghattas 00:16:02 Exactly.
Tigran Najaryan (Splunk Inc.) 00:16:04 Okay, at the very least, let's make sure we clarify that there.
the collector would then serve as sort of a version transformer, which I think is fine, it serves the purpose in this case.
Josh Suereth (Google LLC) 00:16:17 That is in the Specification Tigran, so I think once you have a chance to read it, that's actually called out in there.
Tigran Najaryan (Splunk Inc.) 00:16:23 Okay, okay, I'll do that. I don't want to use any more time. Okay, thank you.
Reiley Yang (Microsoft Corporation) 00:16:30 No one.
Robert Pająk (Splunk Inc.) 00:16:32 Okay, so I was late, like, 1 or 2 minutes. If there was any further discussion, just help me to read or listen later, have been considered just a simple new, like, namespace, just, you know, Development V2, instead of doing this thing, because I think it's very back-prone, even for the receiver, that they will need to have if statements, etc. I, like, in my mind right now, the biggest drawback of the video will be just, I don't know, bigger binary size, but besides, I think it will be easier to maintain and… I don't know, tell what version you are at right now and what you're supporting. You just, you know, compile the proto that you want to support, you can, you know, not even compile the proto that you do not want to support, and I think it's easier tool-wise.
Yeah, that's my question.
Nayef Ghattas 00:17:23 So, I think the reason we discussed this as part of the profiling SIG, and I'll let other Shaymin if they remember other reasons, but the main one was, if we wanted to update the namespace or the path, we'll need to do it across the entire OpenTelemetry ecosystem, all the SDKs, the collector, all the packages.
Each time we ship a braking change, and we wanted to avoid having the… All that to do each time we want to ship a braking change.
Robert Pająk (Splunk Inc.) 00:17:58 Not sure if it's a real big difference.
Josh Suereth (Google LLC) 00:18:02 Yeah, I do want to clarify that you're not planning to make breaking changes that frequently, right? Like, this is… this is… To me, the one reason I'm happy to prove this is I think this is an emergency escape hatch that we can pull if we absolutely need to, but I'm hoping we don't use it.
Like, that's success to me, is we never have to bump that version number.
Nayef Ghattas 00:18:25 We actually do have a PR in… In the queue that plans to use it.
Josh Suereth (Google LLC) 00:18:31 Okay.
I'll have to take a look at that. Is that the draft one?
Nayef Ghattas 00:18:36 No, it's… it was one of the PRs that is mocked, do not merge, because it breaks the…
Josh Suereth (Google LLC) 00:18:42 Okay.
Nayef Ghattas 00:18:42 the protocol compatibility.
Robert Pająk (Splunk Inc.) 00:18:44 Maybe just to clarify, I do not understand what will be the problems of having multiple namespaces.
like, this should be, like, more than internal, internal, you know, stuff, how you use the protob. It should not escape the API surface, for instance, of the, you know, of the OpenTerm, the API SDKs, etc, and collector as well. I think it should be everything kept internal.
Tigran Najaryan (Splunk Inc.) 00:19:08 Multiple namespaces, I think, Robert, means that you have to generate all those different messages belonging to different namespaces, then you'll have… you have… you just have multiple variants of the profile's data in the P data, just lots of duplication of the… of the generated serializers.
Which is a possibility, but it will bloat up the code.
Nayef Ghattas 00:19:36 And then you'll need to adjust.
Tigran Najaryan (Splunk Inc.) 00:19:38 Or, let's say, a single field change, right? So now you have a copy.
Robert Pająk (Splunk Inc.) 00:19:42 But as Trish mentioned, it's not something that we really want to do frequently.
So, is it a problem if you do it once or twice?
Because if we don't… if we do it, you know, if we use it some, I don't know, string or integer, which makes the version… the more versions we have with the more fields, and the more they'll be breaking changes, I think the code and maintaining this compatibility will be even more harder than just, you know, having duplicated fields, etc.
And the logic between these fields, but preferably the profiling SIG, no.
Knows better if it's really an issue or not.
Nayef Ghattas 00:20:17 So I think as the change is planned right now, the version will only be needed to be supported once there's a proto, release.
And the new proto version, and so when the corresponding project updates the proto release for profiling, they need to decide if they need to do any changes on the receiver or the… or the export outside, be it in the SDK or in the collector, to be able to treat that signal. And we, thought that this was less complication than supporting all the different, versions at the same time.
in all the SDKs and the, And, collector, if that makes sense.
Robert Pająk (Splunk Inc.) 00:21:04 How many SDKs are using this?
Nayef Ghattas 00:21:08 I think there's a couple, there's at least Java, Python, Go.
Robert Pająk (Splunk Inc.) 00:21:14 Go, I don't… I'm sure.
Nayef Ghattas 00:21:17 Maybe not yet.
Florian Lehner 00:21:24 At least for, oh, that is, the SDK.
So we've already generated.
Josh Suereth (Google LLC) 00:21:37 You're still an extension, like a contribib part of Go SDK, right? You're not, like, in the SDK SDK itself, right, Florian?
Florian Lehner 00:21:46 Yes, sir.
Josh Suereth (Google LLC) 00:21:48 Okay. I think that's Robert being a maintainer of the Go SDK, being surprised, is my telling answer there. Yeah, there's a Go SDK, it's just not part of the core Go SDK, it's still part of the experimental prototype.
Experimental profiling stuff, right?
Florian Lehner 00:22:04 Yeah, yeah, I was looking at the protocol and not, not, OpenTelemetry goal, so…
Robert Pająk (Splunk Inc.) 00:22:08 No, I, I, I think Florian only meant, like, generated, generated code for… For, repository, which we still use, like, internal, and yeah.
It's just a generated stuff.
It doesn't matter for them, it's more or less.
packages and modules.
Josh Suereth (Google LLC) 00:22:32 Whereas, I think in Java, wasn't Jonathan working on actually having an SDK that would generate the profile signal as part of the SDK?
Nayef Ghattas 00:22:40 Yeah, exactly.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:22:41 Yeah.
Josh Suereth (Google LLC) 00:22:51 Alright, I think I have… the discussion I wanted to have happen finally happened, so thank you, everybody. I think, looking forward to comments on the PR. Robert, to your question, I think it's a good question for us to answer of, like, you know.
Is it okay if it's high friction? I think the answer we're saying here is, changing the client every time a breaking change happens, versus the current proposal, only the server really has to deal with it, and clients would, like, get a rejection notice if they talk to a server that's not up to date.
So it's a little lighter weight on the ecosystem.
which is the current proposal. I think, Robert, like, if you can get your comments on the PR, that'd be awesome, and then we can hash it out there. I think we had a great discussion, don't want to take any more time, but that's the discussion I wanted to make sure we're having. So thank you, everybody.
Reiley Yang (Microsoft Corporation) 00:23:52 Okay, Robert, let's go with your ask.
Robert Pająk (Splunk Inc.) 00:23:58 Yeah, this one is very easy. I just want to create a patch release for the proto. So far, Florian told that it seems it's not… there's no blocker for the profiling SIG. I have not found any issue myself that will block this, so I'm just creating this PR, and I wait at least until end of this week before merging and creating a release.
any questions or feedback? If… question first, if waiting until the end of the week is okay for a patch release.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:24:32 What's… what's the motivation? Patch releases are typically for bugs. What's the bug?
Robert Pająk (Splunk Inc.) 00:24:38 So, I'm not sure there's a critic or bug, it's mostly documentation. The reason is different, which you might not like. Our GoProto-generated releases are one-to-one aligned with, with the Proto version.
And we just want to fix one bug in our… like, we want to make one improvement in our proto-generated code, and we do not want to just lose this mismatch, and there's… yeah, that's the main motivation. So you can… it's kind of a hack, release hack.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:25:08 Yeah, I see. That… you're right, I don't love it, but it's also, like, sort of, something that I've come across a number of times with these artifacts that we have, which are pinned to, you know, some artifacts In fact, like semantic conventions or the proto-messages, it's like, you know, you want to have the versions as tightly aligned, but sometimes there's, you know, bugs in the tooling of, you know, the dependent generated code.
Josh Suereth (Google LLC) 00:25:43 Cool.
I guess, yeah, you're doing a bug fix release because, there's no major feature changes.
but I guess the question I have is.
Would it be easier just to make a bug fix release where we actually make a 1.11 branch?
And have whatever changes we want for Go in there.
I'm looking at all these changes, and it's all just docs updates and things.
Robert Pająk (Splunk Inc.) 00:26:10 No, no, no.
Josh Suereth (Google LLC) 00:26:11 How to, like, generate the code?
Robert Pająk (Splunk Inc.) 00:26:12 This is not… this is not related anything to the proto itself. We could even use the same one when… it's just about having the versions.
Align.
Tigran Najaryan (Splunk Inc.) 00:26:20 There's no… there's no changes, right? You only need the version number to change, that's all you need.
Robert Pająk (Splunk Inc.) 00:26:25 Yes, if we…
Josh Suereth (Google LLC) 00:26:27 you are releasing changes that are in Maine.
Robert Pająk (Splunk Inc.) 00:26:32 You mean, like, what changes? The only changes were back… fixes here. Like,
Josh Suereth (Google LLC) 00:26:39 Yeah, that's… that's kind of what I'm asking is, like, are we okay with a 1.11.1, or should we just call it 1.12?
like… I'm just looking at it, I don't think… I think it was all the dock fixes that we were doing to update examples and clarifying UTF-8 handling requirements and that sort of thing. Some of that we would normally put in a point fix release, not in a bug fix release, right?
Because they're all… they're all bug fixes, I think it's fine. That's… that's my only question, is like, if you're gonna call it 1.11.1, is it really a bug fix release, or should we just release 1.12?
Robert Pająk (Splunk Inc.) 00:27:17 So I thought… I was thinking that your, I was looking at the changes, I think that your docs are more clarification, but if you don't agree, we can publish this as well.
Josh Suereth (Google LLC) 00:27:28 They are, I'm just, like, if you're gonna make a 1.11.1, we should have a 1.11.x branch and all that kind of rigmarole.
Robert Pająk (Splunk Inc.) 00:27:38 Just in case.
Josh Suereth (Google LLC) 00:27:38 But, yeah, I just don't want to do that.
Robert Pająk (Splunk Inc.) 00:27:41 You can create a branch at any time. You can just go backwards and, you know, make a branch for the commit.
Josh Suereth (Google LLC) 00:27:46 Okay, that's fair. So we could make a branch off of your 1.11.1? That's fine. Okay.
Robert Pająk (Splunk Inc.) 00:27:52 If you do this.
Josh Suereth (Google LLC) 00:27:53 I'll shut up now.
Robert Pająk (Splunk Inc.) 00:27:55 Thanks.
Reiley Yang (Microsoft Corporation) 00:28:00 Okay, no worries, you're good?
Robert Pająk (Splunk Inc.) 00:28:04 Yeah, thanks a lot.
Reiley Yang (Microsoft Corporation) 00:28:06 Okay, Trask.
Trask Stalnaker (Microsoft Corporation) 00:28:12 Yeah, thanks. Just wanted to share something I had learned from… about how the automatic GitHub Copilot reviews work, because I was surprised and not super happy with it. The… so automatic reviews are, like, if you enable in your repo, and many have.
When PRs are opened or marked ready for review.
It automatically does the, the co-pilot review.
and… If a user does not have a co-pilot license, then that's fine. It… gets billed to the CNCF.
what's really… Weird is that if users do have a Copilot license, it still gets billed to them.
Including even if they are out of quota.
It will then fail, because it tries to build to them, and it can't.
So… anyway, just wanna… I have a ticket open with CNCF. They've been discussing with GitHub, I don't know what… Will happen with that, but just wanted to share.
Josh Suereth (Google LLC) 00:29:41 Does this mean everyone's gonna see that I don't pay GitHub enough, and I ran out of quota, like, month… like, weeks ago?
No, like, seriously, this means if I send PRs to OpenTelemetry, like, that I won't get code review because I'm out of quota?
Trask Stalnaker (Microsoft Corporation) 00:30:00 Yep, it'll… you'll get a message, Copilot review will leave a comment on the PR saying that it couldn't review because it ran out of quota.
Josh Suereth (Google LLC) 00:30:15 That's fun, okay.
Tyler Yahn (Splunk) 00:30:17 Trask, I've run into this a few times, actually, which, was kind of shocking, I guess, like, the first time. Like, you're saying that there is a way to have the CNCF build instead of myself for these reviews?
Trask Stalnaker (Microsoft Corporation) 00:30:30 There, if you didn't… if you do not have a co-pilot license at all.
then it will bill the CNCF.
Tyler Yahn (Splunk) 00:30:42 So my mistake was, like, actually having a co-built license.
Alright, so…
Trask Stalnaker (Microsoft Corporation) 00:30:48 Yeah.
Josh Suereth (Google LLC) 00:30:48 We all make new GitHub accounts called, like, your regular GitHub account, dash nocopilot, and then we just approve of them all? Is that what we should do?
Trask Stalnaker (Microsoft Corporation) 00:30:59 I… I'm gonna… one of the reasons I wanted to raise it here was to get people's feedback, so that I can take more feedback to the CNCF and… Yeah.
Cause it…
Tyler Yahn (Splunk) 00:31:15 Well, I mean, my feedback is I would love it if…
Trask Stalnaker (Microsoft Corporation) 00:31:17 Specific…
Tyler Yahn (Splunk) 00:31:18 Yeah, I would love it if the CNCF is able to, like, make this work, and they were able to pay for it, because like, it's really… like, I have no problem paying for it or using that license, it's just that, like, when it stops is the problem, right? Like, that's… and I don't really want to, like, go and put hundreds of dollars into that and just, you know.
For doing hotel PRs. Like, I'm happy to use it where it works, but, like, when it stops, it's like, can it then switch over to the CNCF? That's the only thing.
Joshua MacDonald (Microsoft) 00:31:50 That's… that feels a little shady to me. I would not choose these code reviews if I knew I was paying for them.
And speaking for my employer, I don't think that we should have contributors in OpenTelemetry paying with their own co-pilot for those reviews. They're not very high quality.
and they don't seem to be elective, or… or, like, a user doesn't choose to do that review, I would not… I would not have this policy if I could change it.
Either CNCF should pay, or we shouldn't have these reviews.
Reiley Yang (Microsoft Corporation) 00:32:25 Hey, hey, Trask, I'm curious, for the… for the first-time contributors, do they also have the free CNCF review if they don't have a license?
Trask Stalnaker (Microsoft Corporation) 00:32:35 Yes. If you do not have a… Copilot license, then everything works beautifully.
Reiley Yang (Microsoft Corporation) 00:32:43 I see. That could be risky for CNCF, because hackers might be able to leverage that to review whatever content.
So I, I do feel like I have the personal coverage, you can opt in.
we'll… will protect everyone.
Trask Stalnaker (Microsoft Corporation) 00:33:05 So, I mean, I will say, speaking as a maintainer, I have found the Copilot reviews extremely helpful in the Java instrumentation repo.
But we've also… I've also spent a lot of time improving the, the agent instructions and review knowledge base.
So I find it… I find them extremely helpful. I want them.
But I… I… I… agree, I… I… and I understand from for, commercial org, that this… policy or whatever is typically fine, but I don't think it works for an open source org.
Of charging your users… quota for automatic PRs that we initiate.
Reiley Yang (Microsoft Corporation) 00:34:06 Yeah, no, I mean, I can imagine, like, if people are already OpenTelemetry members, then doing it, like, automatically, or have a way for them to opt-in, so CNCF will cover that. Sounds like a reasonable balance. If CNCF is automatically paying for whatever user-submitted PR, hackers can leverage that, and CNCF might file bankruptcy very soon.
Trask Stalnaker (Microsoft Corporation) 00:34:33 I mean, but honestly, I… I want the Copilot reviews on those, external contribution PRs, because that's what… Prevents me from having to spend my human time I don't know.
Reiley Yang (Microsoft Corporation) 00:34:48 I understand. If you have a button, that's probably fine, but if that's automatic, I think hikers can just, like, leverage that. Sounds like risk.
Trask Stalnaker (Microsoft Corporation) 00:34:57 I mean, they could, but, like, it… I think I would wait to see if that becomes a problem in, practice, because what are they going to do? Like, review against our… in Java instrumentation, knowledge, articles, I find it super helpful to have the co-pilot review already done by the time that I go to review the code.
the PR, I don't want to have to go and then be like, okay, this one looks good, I'm gonna request the co-pilot review and come back 20 minutes later.
Reiley Yang (Microsoft Corporation) 00:35:35 Yeah, same here.
Trask Stalnaker (Microsoft Corporation) 00:35:40 Alright, thank you all. I will pass more… Feedback.
On to CNCF.
Reiley Yang (Microsoft Corporation) 00:35:48 Thanks for sharing. Michele?
Michele Mancioppi (Dash0 Inc.) 00:35:51 Just a second. Apparently, everything is going down in the city, and they're full of sirens. This could take much less than 5 minutes, or way longer, depending on where the discussion goes.
In that PR, there is a proposal for language for describing criteria for an SDK and their instrumentations, and potentially additional logic to be injected.
Through, for example, the injector, but, the same happens today already with, the OpenTelemetry operator.
You just need to add labels, so that the Meeting webhook kind of stuff.
We have had a few, a few back and forths.
There is, a lot of people commented. I believe the comments have been addressed.
Have another look.
Carlos Alberto Cortez 00:36:44 What if there's a comment that you think can be discussed quickly here, it would be nice. Like, some things I think that they are just minor, but probably if we have 5 minutes here, we can iterate over that.
Michele Mancioppi (Dash0 Inc.) 00:36:58 They are, one that is, interesting, that I find especially interesting, because it has implications, for the, the way that we build SDKs is, the, vendorization.
It's, actually from, It's online… well, I'll share the screen if you don't mind. It's probably faster this way.
Reiley Yang (Microsoft Corporation) 00:37:22 Sure.
Michele Mancioppi (Dash0 Inc.) 00:37:24 Except that I'm not allowed to. Alright.
Alright, let's… So, okay.
the, Something that we have seen time and time again with different languages, and for different reasons, is that, having non-openTelemetry libraries in, as dependencies of SDKs and instrumentations can be a liability.
The, in the Python SIG, there has been a significant amount of work.
to come up with OTLP exporters for both Protobuff and JSON that do not rely on external libraries.
for Protobuff, HCP protobuf, and gRPC, that's because, gRPC is apparently one of the most toxic dependencies on the planet in terms of backwards compatibility. Interestingly enough, the Java SIG had gotten to the same conclusion, for, and already vendorized or made a custom implementation of Protobuff.
The, The need that we have for vendorization of libraries is inversely proportional To, the quality of the safeguards of the runtime.
For example, Java. Class loading is amazing. Like, it's really hard to leak classes somewhere else and break somebody else's dependencies. Node is fine. Python, you put all the dependencies in one pot, and chances are you're breaking somebody.
If you inject with dependencies that are not rendered. So there are these kind of two extremes.
This is the reason why… There is language saying, hey, it should avoid, whenever possible, non-vendored dependencies.
This is probably one of the more interesting statements of the suggested language.
And it is also one where I don't know if we've gotten closure yet.
How should I interpret the silence?
That they're on the same page, and it's cool, or…
Carlos Alberto Cortez 00:40:03 Well, Kilak is not here in the call, so we can probably ping him directly.
Forced.
Reiley Yang (Microsoft Corporation) 00:40:10 I have some context here, so I guess the feedback is basically saying, when you say must not, there are language runtimes that they already provide some… mechanism, and they won't meet what you expect. Like, they try not to crash or prevent the application from starting, but there could be cases where must not cannot be true.
Michele Mancioppi (Dash0 Inc.) 00:40:31 That's why the, I had a few rounds of discussions in DMs with, for example, Robert, And, I, I changed the language from must not to should not, like, should avoid.
It's, it's unfortunately one of those requirements where it's a bit nuanced, because as I said, you need this the most.
the weaker are the class-loading equivalent protections in the runtime. So, for example.
If you were and used gRPC in Java, nobody would die, yeah?
In Biden, probably somebody dies, yeah.
Reiley Yang (Microsoft Corporation) 00:41:07 Yeah.
Yeah, I understand. So I… I suggest that you reply back to the comment saying you take the wording, so for… for language runtimes that cannot meet the master node, you try to make it a little bit flexible for them.
Jack?
Jack Berg (Raintank, Inc. – Grafana Labs) 00:41:29 So… I left a comment in the chat, and this is kind of related to the comment that I want to talk about. But… so, in my experience, the toxic dependency, it really is this GRPC, and to a lesser extent, protobuf.
And, you know, if you think about what an SDK really has to do, there's not many other external dependencies you need. You might need an HTTP client, but often runtimes have a good HTTP client bundled into them, so no dependencies required for that.
And then, what else?
Like, right? So, I think, that, like, what I want to convey to maintainers is that, it really is possible to hand-roll your own protobuf serialization.
And it's… it's more doable than ever.
When we did it in Java back in, like, 2021, it was, like, a hard technical challenge. And the person who did it, like, you know, was in the weeds for a couple of months, heads down, trying to make a byte-perfect recreation of what the protobuf library does in serializing messages.
And it's… It's never been more accessible to do that yourself. Like, it feels like a one-week engineering problem to me to, to hand-roll your own protobuf serialization in any language.
So, yeah, we can talk about toxic dependencies a lot, but it's also just, like, very… I think it's very realistic that we just go and recreate protobuf serializers ourselves, and, you know, and then we can move past this conversation forever.
Reiley Yang (Microsoft Corporation) 00:43:09 Yeah, and I shared a link for the OpenTelemetry .NET OTL PX powder. I think the rendering has been done, like.
a year or two years ago, maybe, like, 2 years ago. So, when you look at the dependency, it only depends on the OpenTelemetry API SDK, and the .NET runtime.
I don't have anything about, like, gRPC or Protobuff, or… like, all of them got rendered, so I… I… I don't understand the comment here. Maybe the .NET auto instrumentation should… Use this one.
Robert Pająk (Splunk Inc.) 00:43:43 the question is, I… from… I will say that probably the, Pyot understood it in a way that you should also vendorize OpenTelemetry dependencies as well, because people can use manual instrumentation and could, you know, import this… this OpenTelemetry dependencies.
And that's the main issue that we have, because right now, we are just injecting, we are just, you know, using dependencies of open telemetry, a contrib trip, etc. So, the question is, should we vendor everything? Because there may be some clash with the… with the application, which does some, you know, mix of manual, etc.
Reiley Yang (Microsoft Corporation) 00:44:20 Yeah, the more, the better.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:44:23 From an injection standpoint, you, like, you need to vendor everything, but if you're just talking about manual instrumentation with SDKs, you know, you should also vendor everything, or consider getting rid of the dependency altogether.
Reiley Yang (Microsoft Corporation) 00:44:34 Yep.
I agree.
Aaron?
Aaron Abbott (Google LLC) 00:44:40 Yeah, I was just gonna say, from the Python perspective, we discussed, like, hand-rolling protobuf a couple times. I think the first point is that it, in Python.
There's, like, code reuse, which is great for using Different implementation, but there's also speed benefits, because the language is slow.
So I think it's technically feasible, but… Maybe there's alternate reasons, and then the other thing I wanted to bring up was, OTLP JSON support. Like, does that not, hit the mark in terms of, you know, it's much easier to implement, and doesn't it also, you know, achieve being able to export OTLP from the process without having a vendor dependency?
Michele Mancioppi (Dash0 Inc.) 00:45:19 You should have… you should, Ideally, you would support all the export formats. The reason for that is when you inject a process, you are not going to know which of the, which of the formats is desired by the user. They can set it via environment variables, they can set it via the declarative dependencies, so when you have what the PR calls an auto-instrumentation client, so the combined set of the SDK you're gonna add.
the Alberto instrumentation you're going to add, and potentially stuff around it to make it work, like the site customize.py that we have in system packages.inject Python safely to do all the dependency checks. Ideally, you would be able to support all the exporter formats. You… The Autel JSON, OpTJSON helps, and it's great that Python has been doing that. There are people that really want to run protobuf, and they should be able to inject that and have it work.
Because otherwise, you can get in a situation where you… where you inject an application, and then what the user is asking for, in terms of configuration, cannot be realized with what you want to inject.
Aaron Abbott (Google LLC) 00:46:38 Right, I thought we made… made it so that the default was, like, not specified, and I think many languages don't support JSON at all, right?
Michele Mancioppi (Dash0 Inc.) 00:46:49 I, don't know if many languages don't support JSON, to be honest.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:46:55 Sorry.
Daniel Dyla (Dynatrace) 00:46:55 JavaScript.
Robert Pająk (Splunk Inc.) 00:46:56 They don't.
Daniel Dyla (Dynatrace) 00:46:57 The only language that supported it.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:47:00 Yeah, it's trivial for us to support it in Java, but we say no because it's a footgun. All it does, in our estimation, is reduce performance without any, without any, you know, nameable benefit. So, that's why we haven't done it, not because there's any technical challenge.
Reiley Yang (Microsoft Corporation) 00:47:21 Hey, Aaron, you mentioned Python. I remember there's another thread, people talking about the C++, like, API layer, so maybe that's something you can consider as well for the… for the auto-instrumentation. I mean, injecting an API component from C.
shouldn't have any Python package headache.
Okay, Cijo, I think you're next.
Cijo Thomas (Microsoft Corporation) 00:47:51 I had one question on this PR itself, mainly about who is the intended audience.
As written, the current weighting indicates that the SDK Maintainers are supposed to provide this Documented mechanism on how to inject.
So is the intent that each SDK owner or maintainers provide this, or is it specifically targeting the auto-instrumentation Maintainers? That part is… that determines whether we should spend time reviewing, or whom should review this PR in greater depth.
Michele Mancioppi (Dash0 Inc.) 00:48:22 There is a set of necessary requirements to label an SDK and other instrumentation as auto-injectable.
If a language SIG decides that they want nothing to do with auto-injection, then they don't need to follow this.
Cijo Thomas (Microsoft Corporation) 00:48:36 But that's… that's exactly my question, like, who, like, is… the way it is returned, it says an SDK implementation must do something, which means, the language SIG has to do something to document how to inject an SDK.
Michele Mancioppi (Dash0 Inc.) 00:48:50 Order to be injectable.
So if you want, the language says, in order to be injectable, so if you want to be injectable.
Robert Pająk (Splunk Inc.) 00:48:58 Okay, but it's not that way. I agree with Cijo. It kind of says… it doesn't mean that it's optional. It says, in order to make it working, it must do it. It's not negotiable that you cannot support it. The way it is written right now, it says.
we need it to be injectable, the SDK must do da-da-da, etc.
Michele Mancioppi (Dash0 Inc.) 00:49:18 Interesting.
Cijo Thomas (Microsoft Corporation) 00:49:19 Yeah, it's most languages, the people who maintain the SDK and the people who do auto-instrumentation, there are different groups with some overlaps, and some languages don't have a auto-instrumentation as of today, but may come in the future, which is why I want to decide if Whom should spend more time reviewing this?
Jack Berg (Raintank, Inc. – Grafana Labs) 00:49:38 Yeah, this does seem like some rephrasing is in order, but, you know, the point here is that injecting needs a contract that it can rely on, and it needs that contract to have certain properties, and we want more language to… languages to be injectable. We understand not all languages will be injectable, there's technical challenges that prevent that, but we want to create the incentives and be explicit about the requirements around injectability, so that, you know, we can grow the set of languages that have that capability.
Michele Mancioppi (Dash0 Inc.) 00:50:16 Okay, I'll come up with a way to phrase this. In my opinion, so as much as I would love, every single SDK and instrumentations that are theoretically capable to be injectable to actually be injectable, because I believe it is a superior experience for users.
I'm also… I also think that we should start by making Ghattas obtain per language.
And then, ideally, when we establish That this is actually the great idea I think it is, then the others who follow suit.
Cijo Thomas (Microsoft Corporation) 00:50:52 Yeah, but as of now, like, there is no requirement that each SDK has a auto-instrumentation counterpart.
So it's, like, totally optional right now, so we don't really… as a language maintainer, which do not have auto-instrumentation, I never have to worry about whether someone is going to inject or not. If you're changing that, that's probably fine, but we just need to be, like, very intentional that we are making every SDK…
Michele Mancioppi (Dash0 Inc.) 00:51:15 it was always intended to be an opt-in by Language 6.
Cijo Thomas (Microsoft Corporation) 00:51:19 Yeah, let's just make it, like, clearer, so there won't be any confusion for people who review this one.
Like, I have, like, I play the role of maintainer in multiple languages where there are… auto-instrumentation, like, specifically in .NET, there is an auto-instrumentation, where there are common people between the SDK Maintainers and auto-instrumentation. For other languages, like Rust, we don't even have an auto-instrumentation as of now. There are proposals.
We don't even know whether it'll be injecting or it will be using eBPF, so that's why we'll need to be very clear whom should this requirement apply to? Is it… does it mean, like, language Maintainers, how to… think about how to make it injectable, which is not something which they are used to doing. Anyway, like, that, should be, like, clarified in the introduction, and based on that, I'll spend more time.
Reiley Yang (Microsoft Corporation) 00:52:12 Huh?
Ted Young (Raintank, Inc. – Grafana Labs) 00:52:15 Yeah, so I don't think we have time this week, but would people be interested next week in having a more in-depth discussion about C, C++ findings?
And what that buys us versus what, you know, what limitations come with that.
I don't think we should ever, like, get rid of our native language SDKs and implementations, but it seems like like, a lot of benefits come from C++, and we should maybe, like, really give that a go.
But that's been just kind of a theoretical, experimental thing up till now.
So, how about next week, we have a more in-depth discussion about the pros and cons of that, and people, you know, come, come with their, their arguments prepared?
Carlos Alberto Cortez 00:53:08 Well, Alex Boten had something, I don't know, like, Alex is in the call, probably, he would like to present something. I'm not saying that you should, I'm just saying that you could, if you wanted, if you have free time.
Alex Boten 00:53:21 Yeah, I'm happy to talk about it next week. Won't be able to do it on the spot here, but…
Ted Young (Raintank, Inc. – Grafana Labs) 00:53:27 Yeah.
Reiley Yang (Microsoft Corporation) 00:53:30 Okay, I'll add that to the agenda. Ted, I assume you will be joining the conversation?
Ted Young (Raintank, Inc. – Grafana Labs) 00:53:38 Yeah, I'll be there.
Reiley Yang (Microsoft Corporation) 00:53:39 Okay, I'll take a note. Cijo?
I think it's your topic.
Cijo Thomas (Microsoft Corporation) 00:53:44 Yeah, I just added it, seeing there was some time, So this is something which came up during… Self-observability, defining some metrics for self-absorbability, like number of logs processed, number of metrics processed. So there is a attribute for all those metrics, which says, hotel.component.
auto.component.name, and we auto-generate that one. For example, the first batch processor in the provider will get the name batch processor slash 0, then batch processor slash 1, things like that. But the PR which I have sent is trying to improve that so a user can give a custom name. For example, a batch processor, they can say, this is my batch processor for vendor 1, and there is another batch processor where I send it to a different vendor. So they can name the components themselves.
And it'll be used by the internal metrics as well, so… I don't know if self-observability is just one place where this came up, but also in OPAM-based configuration, if an application has multiple processors and you have a new config from remote OPAM, what component should it get applied to? There is no way to identify an individual component. This is an overall problem in SDK. There is no name even for a provider. Forget just the components, like, the entire provider itself has no name. So I didn't try to fix all of that, but I just try to do a very small, targeted Fix, which is to let, optionally, users give a name.
to the individual components. It could be batch processor.
meter, metric reader, or exporter. They can just give it a name, and if they give a name, then that name has to be used by the internal metrics. If not, it will generate the name, using the existing conventions. So there are 3 PRs.
like, all linked together, one is a spec one, and there is a semantic conventions for internal metrics that is also linked to it, and also a change in the DRIT configuration, because we need to make sure, like, declarity config can be used to name. So all three PRs are linked in the, the spec one.
The question is, like, is there a desire to… like, name auto components. I couldn't find any prior discussion, and like I also mentioned, I didn't try to make it super generic, because this is very specifically targeting individual components, so it doesn't really have anything for… provider, though one could technically name a provider. So any thoughts on this? Otherwise, I'll, continue polishing this. This PR in the spec is marked as ready for review, but anything, the related PRs are still draft, because I'm still polishing it. Any feedback, thoughts on this one?
Reiley Yang (Microsoft Corporation) 00:56:38 I can definitely see the trend here. You've reminded me of the .NET, like, configuration story and the dependency injection. Initially, if your component is being used by the user, and they write the code to initialize the component and also provide configuration.
then you don't have this problem. The problem comes when you have the separation of the component initialization, and the configuration can be provided by another service. Then they don't know each other. Then how would the configuration be able to know if you have multiple instances? Like, if you have a singleton, you're fine. If you have multiple you might want to scope that. Then you kind of, like, already start to think about the dependency injection engine.
So it sounds like you're trying to invent what .NETM has learned many years ago.
Cijo Thomas (Microsoft Corporation) 00:57:25 Yeah.
Yeah, more, like, named HTTP client was one thing, like, you want to have multiple HTTP clients, you want to configure that differently, but you need a name to identify which one you are referring to.
That's a general problem, but here I was trying to avoid being, like, overly trying to, change the entire spec, so I put a very narrow approach just to solve two immediate problems I see. One is the internal metrics, and the second one is when we're trying to configure it from a control plane using our PAMP.
There is no way to identify… if it's singleton, it's fine, which is normally the case, but if an application has multiple SDKs, then there is no easy way to identify which one we are referring to.
Yeah, I'll leave the PR for people to review. Nothing really urgent, so take time and share feedback.
And comments in the PR itself.
Anyone else with comments right now? Otherwise, we can move to the next topic.
Reiley Yang (Microsoft Corporation) 00:58:25 And for the unnamed configuration, do you imagine that would be… Applicable to all the components, whether named or unnamed, or you won't have a separation.
Cijo Thomas (Microsoft Corporation) 00:58:36 No, there… if we don't provide a name, there is a implicit auto-generated name.
Using the pattern, like, batch processor slash 0 for the first instance, batch processor slash 1. So that is currently defined in semantic conventions for self-observability.
But this one puts that into the spec itself. So it says… let user provide a name. If they don't provide the name, then generate this name. That name is not used anywhere in the spec. It's only used in the internal telemetry. So I try to, like, link them together, because there is no.
Reiley Yang (Microsoft Corporation) 00:59:10 Thank you.
Is that durable? Like, if you change the code, what do you.
Cijo Thomas (Microsoft Corporation) 00:59:14 It is durable in the sense, because even if you restart the process, it starts with zero again, so it is durable, because a batch processor will always get the name batch log processor underscore zero. You restart it, you still get the same one. But it's not guaranteed, because guaranteed, as in, if you have two batch processors.
whoever gets initialized gets the name 0, the next one gets one. So the order is… if the order changes due to whatever reason, then the.
Reiley Yang (Microsoft Corporation) 00:59:39 It's not horrible.
Cijo Thomas (Microsoft Corporation) 00:59:41 It's not durable in that sense, but if they only have, like, one component, then yes. But to the technical meaning of durable, no, they're not durable. It could change. If someone injects a poster before or after, then the number would change, so they're not durable in that sense.
Reiley Yang (Microsoft Corporation) 00:59:58 Yeah, it cannot be, like, reliably used as a configuration pointer.
Cijo Thomas (Microsoft Corporation) 01:00:04 Yep, yeah, so the… the user has to consciously provide a name if they want it to be, like, super durable, yeah.
Reiley Yang (Microsoft Corporation) 01:00:12 Thank you.
Cijo Thomas (Microsoft Corporation) 01:00:14 Oleg, thanks.
Reiley Yang (Microsoft Corporation) 01:00:20 Okay, so we'll give, 3 minutes back to everyone. Tyler, I'll move your topic to next week. Thank you.
Jack Berg (Raintank, Inc. – Grafana Labs) 01:00:27 Thanks. See, everyone.
Reiley Yang (Microsoft Corporation) 01:00:29 Next week. Bye.
