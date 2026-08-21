SIG: OpenTelemetry Profiling
Date: 2026-08-20
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

Nicolas Savoire 00:01:17 Hello.
Florian Lehner 00:01:19 Hello, hello.
or probably Bonsai?
Nicolas Savoire 00:01:27 So, we are going to work together, soon? Sorry.
Nayef Ghattas 00:01:42 Hello.
Florian Lehner 00:01:53 Hello, welcome back, Felix.
Felix Geisendörfer 00:01:57 Thank you. Good to be back.
Scott Gerring 00:03:52 I just spent 4 minutes in the old Profiling SIG Zoom room.
was lonely.
Felix Geisendörfer 00:04:00 Yeah, it seems like we have a new fancy Linux foundation set up now. It took me a while to click the right buttons as well.
Looks like we're 5 minutes in.
Who's been moderating while I was… Absent.
Nobody?
Christos Kalkanis 00:04:50 Florian… Florian did it.
Felix Geisendörfer 00:04:52 Okay.
Christos Kalkanis 00:04:54 I'm not as good as you, though, Felix, so…
Felix Geisendörfer 00:04:58 Oh, should I continue? Florian, do you want to continue? I'm just asking.
Florian Lehner 00:05:02 I think… I think there was a downfall in quality of documentation, so if you can continue, I would appreciate it.
Felix Geisendörfer 00:05:11 I would be happy to give it my best shot. Okay, then let's do this.
Let me share my screen.
Okay, so welcome everybody to the August 20th edition of the Profiling SIC. As usual, we'll go through previous action items, and then through the items that are on the agenda.
If you have something you would like to discuss, but didn't have a chance yet to put it on the agenda, please do it now.
And… we can start with the action items. Since I was out a little bit, somebody has already prepared these. Is this up to date, or do I need to look somewhere higher up in the document for action items? Does anybody know?
Florian Lehner 00:06:05 I put them there, they are up to date.
Felix Geisendörfer 00:06:08 Okay, thank you so much, that's great. Then I guess my first question is, is Alexey here? If not, we'll push his stuff down a little bit.
Alexey Alexandrov 00:06:17 Yeah, here.
Felix Geisendörfer 00:06:21 And then.
Alexey Alexandrov 00:06:21 You sit and put all your stuff.
Felix Geisendörfer 00:06:23 up.
Alexey Alexandrov 00:06:24 Okay, yes, I added a note to the first one, the… the orphan check… checks was actually fixed, by Florian, some time ago, and then there was… there was a couple of follow-up fixes. The… it's the same as the reference check, and we… we, we've fixed this. Florian, do you think there's anything left? But I think it… I think it was done. I think we can call it done.
Florian Lehner 00:06:50 Should be fine. I can have a second look, but should be fine.
Alexey Alexandrov 00:06:55 Yeah, yeah, yeah.
Felix Geisendörfer 00:07:06 Okay, cool. If… No more thoughts on this, and thank you so much for all the work done on this so far.
Alexey Alexandrov 00:07:15 I think… so, now I'm… I'm remembering, for Orphan Check, there was one… there was one note, but I think it's… it's probably minor, but we can discuss it, is… I think we currently, we will not… we will not, detect orphans.
if, Well, no, we will… we will detect it, but not kind of, like, in a single… so imagine… Imagine allocation… is orphaned.
Because it's not referenced by any sample or stack.
But this location also references some functions that are not referenced anywhere else. So currently, we will detect that locations are orphaned, but we will not kind of, like, detect that everything that is referenced only by orphans is also orphaned. But I think this should be fine, because the main purpose of the… of ProfCheck is if someone writes a producer of profiles, And… their code basically has a bug where it produces some orphans. I think the most important thing is that they will see, like, oh, locations are… locations are orphaned, and they will fix that.
And that should fix… and then maybe, maybe then they will detect that also all functions are also orphaned. So I don't think there is a strict requirement to, like, detect everything. I think the most important thing is to have diagnostics for people to start fixing things, and fix all of them eventually.
I hope it makes sense.
Felix Geisendörfer 00:08:48 I think it makes sense. I was trying to capture an actual example, but I realized I need to look at the prototype for that to make sense. But I think I get the general idea, like, if something…
Alexey Alexandrov 00:08:56 It's not a direct…
Felix Geisendörfer 00:08:58 Orphan, it still has a reference to something else, but that thing is an orphan, then you…
Alexey Alexandrov 00:09:02 You can think of it as a tree, basically. Like, imagine the whole subtree of something is orphaned. Currently, we will complain only about the root of that thing, but technically, you could detect that, and you could say, like, oh, like, this whole subtree is orphaned, and here are all the entities.
Christos Kalkanis 00:09:18 So the current check is not exhausted, basically, but it acts enough to attract attention if there's a problem, so maybe we can add a to-do, so that we don't… like, if someone takes another look at Product Check, maybe in the future, we'll know that, okay, maybe if we want to have better checks, we can implement this functionality as well.
Alexey Alexandrov 00:09:36 Yeah, yeah, adding a to-do, I think it makes sense. I can, I can add a to-do.
Felix Geisendörfer 00:09:40 Yeah, but it's not so bad in the sense that, like, if somebody gets this error message and then they fix it, they'll get the next error message about a potential child in that tree being orphaned, so eventually they'll get a valid profile by running this. It's just a recursive process, not a one-time check.
Alexey Alexandrov 00:09:55 So it's eventually correct.
Felix Geisendörfer 00:09:58 Yeah.
Oh, I like Eventually Correct. It's better than that one.
Okay, that makes sense. Yeah, maybe adding a to-do for now doesn't seem like… urgent, but yeah, nice, nice to do at some point.
Alexey Alexandrov 00:10:15 It's a Toronto.
Nicolas Savoire 00:10:16 The current and mature will produce orphans, right, with the resolving of reference.
In the string table.
Alexey Alexandrov 00:10:32 What do you mean? Sorry, I didn't get the question.
Nicolas Savoire 00:10:35 I mean, because I was just recently looking at the code for resolving and converting and resolving reference.
So that, resource attributes, use references in the dictionary, but… In the un-marshalling process, we leave, I think we'll leave strings in switch tables that are not referenced anymore.
Alexey Alexandrov 00:11:01 then, then… then I would say this is… this is… this is a bug. I… I think currently the orphan check and duplicate check in improv check is… is a flag that is off by default.
So, you may want to run it with that flag to check whether there are orphans or not.
Nicolas Savoire 00:11:20 But it's just, I want to say that we intentionally, in our implementation, create our fans. That was… that was my point, that's what…
Alexey Alexandrov 00:11:28 W-wh-why?
Like, in general, profile… like, in general, the recommendation is not to have orphans, because there can be any intermediate stages in the profile… in, like, in the implementation of how profile travels, like, in the collector or somewhere, that will… that will drop the orphans, because they are… Like, the… everything is considered to be rooted from… from samples.
Nicolas Savoire 00:11:59 Yeah, but the way the un-marshalling, works, basically we… when we unmarshall… un-marshall profiles that has attribute which has references into the profile dictionary. We replace these references by inline strings, by inlining the strings to be transparent, but we leave the string into the string table.
And we set back the reference… the… the references… Indices to zero, so they are not referenced anymore.
Florian Lehner 00:12:32 And are you talking about, implementation in the OTEC Collector for profiles, P data marshalling, you know, marshalling? Yes, I think there was an issue with this, but this should be fixed now upstream. The solution… is, if I remember correctly, to always start from an empty profile.
And then populate the empty profile instead of, taking… when merging two profiles, not extending one, but always start with a plain one and bring in everything into the new one.
And I think there's still, open PR on the… or, like, the collector contrib side to improve this process.
But in general, I think, and I agree with Alexey, there should be no, there should be no… Orphans, at all.
Alexey Alexandrov 00:13:36 I think… I think maybe one thing that maybe we don't have is that our orphan check should recognize Attributes that point to strings.
Felix Geisendörfer 00:13:58 And when you say that, you mean, like, attributes that make references into the strings table?
Alexey Alexandrov 00:14:03 Yes, correct.
Florian Lehner 00:14:08 Yeah, I think we don't have such a… Check at the moment.
And also the duplicate check on attributes, is missing at the moment, so I have to… Follow up on the functions, lines, functions, lines, location, and links, but, the, the attributes check is, still missing, yeah.
Alexey Alexandrov 00:14:33 I'll add myself an action item to take a look at, orphanCheck for the, for attributes with string reference.
the easiest is probably I'll add a test… I'll take a look whether we have a test case for that, and if not, I will add it and see.
If it passes or not.
But I… we probably don't have it.
Felix Geisendörfer 00:15:00 Okay, I don't have anything to add other than a question, Alexey. The orphan checker you implemented, was that a separate thing in the Profiling SICK repo, or did you eventually integrate that into Collector.
Alexey Alexandrov 00:15:14 It's… it's… it's in SIG Profiling, it's part of ProfCheck, actually.
Felix Geisendörfer 00:15:19 Okay.
Alexey Alexandrov 00:15:20 It's just under a flag that is off by default, but it's part of the same checker.
Felix Geisendörfer 00:15:43 Okay, cool, thank you so much.
And… Nicolas, can you maybe quickly confirm if the orphan situation seems to be what Florian was mentioning, and that you can maybe check later on that pull request that Florian mentioned, if it fixes your issue? I just want to make sure we don't have two separate issues, and we're missing Some detail here.
Nicolas Savoire 00:16:07 Yeah, sure.
Felix Geisendörfer 00:16:09 Okay, then yeah, you can just Slack or something afterwards. Thanks.
Then, anybody has anything else for this? If not, I would like to move us along to the next item.
Next item is Alexey. Figure out what to do with the old profiles, OTAP.
There was already discussion on this.
I thought we had a decision for this a while ago, but maybe, Alexey, you can update.
Alexey Alexandrov 00:16:55 I think we waited for… yeah, this one has been open for a long time. I think we waited for Christos to merge the documentation updates, was that?
Felix Geisendörfer 00:17:08 It's landed.
Alexey Alexandrov 00:17:10 So, okay, it was merged. I… I should take a look.
The discussion was, like, once we update… once we update the current, like, official documentation.
what to do with the old OTAP? Is there… I don't remember, like, is there an official process for, like, closing them? Or maybe we can just, like, add a… add a… note at the top of the OTAP text that some parts of this OTAP can be out of date, see the up-to-date documentation here and there? Would that work? This seems like the easiest thing to do.
Christos Kalkanis 00:17:50 Yeah, I think if I remember correctly, the consensus was that we shouldn't really delete it, or maybe we can't delete it, but we could add a commenter to reference the up-to-date.
Alexey Alexandrov 00:18:00 Okay.
Christos Kalkanis 00:18:00 to communicate.
Alexey Alexandrov 00:18:02 Yeah.
I think it's useful in… for history, in some sense, so…
Felix Geisendörfer 00:18:10 Yeah, so too, yeah.
Alexey Alexandrov 00:18:12 Making… making it clear that… It's an earlier version, makes sense.
Felix Geisendörfer 00:18:20 Yeah, then I guess…
Christos Kalkanis 00:18:21 Sure, I can take that on, I can, I can actually…
Alexey Alexandrov 00:18:25 Okay.
Thank you.
Felix Geisendörfer 00:18:30 Okay, thank you so much, Christos great.
Okay, I think… There's probably not much more to discuss here.
Florian has more thoughts on the profCheck thing we discussed already.
Florian Lehner 00:18:44 Yes, we merged the first duplicate check, and these are the follow-ups for message functions, message lines, message locations, and… Message link.
So it follows the very same concept, it was just merged, in 108.
It does basically the very same.
Felix Geisendörfer 00:19:07 Okay, so this needs review?
Florian Lehner 00:19:09 Yep, please, if you have time, every, every feedback is welcome.
Alexey Alexandrov 00:19:23 And we also… we will also need this for attributes, correct?
Florian Lehner 00:19:28 Yes, I did not do the attributes yet, because I think it needs a little bit more attention, and I have it not, I have not clear viewer yet what is the best way to do so, because we have attributes on various messages.
And, for the, duplicate check, this needs to get merged in some way. The lines, functions, location, and links are very simpler to handle. That's, why the attributes I did not do that, that… I did not implement yet, but, it's still on my, to-do list.
Alexey Alexandrov 00:20:07 Yeah, attributes are a bit, trickier to handle, because they're kind of, like, variant type with so, like, many possibilities.
Felix Geisendörfer 00:20:28 Okay, so it sounds like next step is review the pull request Florian raised, and then after that, let's figure out dealing with the attributes.
Florian Lehner 00:20:37 Yep.
Felix Geisendörfer 00:20:38 Okay, unless there's more thoughts on this, I think Nayef has updates on OTLP versioning.
Nayef Ghattas 00:20:53 So, no, I don't have a lot of updates. The main update was that there was… Felix left a comment on the doc suggesting we use the, an integer for the version instead of The revision dash the integer.
I don't know if anyone has thoughts on this, I think that makes sense, so I was going to update the proposal to just have a revision and open the PR.
Felix Geisendörfer 00:21:21 And… Maybe the… to clarify what problem this solves is if we put these, sort of.
name of the current phase we're in into this version number. Then, if we switch from the last alpha version into beta.
a client would automatically have to interpret that as a breaking change, but it might not be. In fact, our last alpha release might be identical to the first beta release, and so using an integer that doesn't have any notion of which phase it is allows us to actually Separately decide to go from alpha to beta without that implying to be a breaking change.
Okay, you're gonna still update this, and I think you also discussed, looking into one other proposal we… we were discussing internally. Is that your next step, Nayef?
Nayef Ghattas 00:22:57 Yes.
Felix Geisendörfer 00:23:06 So, maybe I can summarize quickly what we were discussing there. So what we're doing right now is basically, making life easier for consumers, because with this version number, they will know which version of hotel profiling they understand, and if they see a change in the version number that they are not aware of, they can assume it's a breaking change, and they shouldn't consume that payload.
If they see an older version, they can maybe convert it if they want to do that. But basically the, publishers, need to now be aware of this, so we need to somewhere publish this mapping of, like, hey, we make a breaking change, so the number is now… goes from 4 to 5. We can maybe put that in the release notes of the, OTELProto, but unfortunately.
protobuf has no idea of declaring an integer constant in the format, so they might struggle with programmatically updating this more automatically. And so it's a little bit of a hassle for the producer, but makes life for the consumer very easy. The other option would be for the version number to actually be the hotel version number, which is for the producer very easy, because they typically have a pipeline where they upgrade the hotel protobuf stuff, and they, in that pipeline, know what the hotel version number is, so they could bake that into the protobuf code they generate, and so they could send the version number, but now the server actually needs to understand which bumps in OTEL version numbers are breaking changes, and in fact, most of them won't be, because there will be hotel protobuf releases that are not even touching, but they will produce new version numbers, so the receiver can no longer assume that just because the version number changed, there's a breaking change. So, I think we're probably going to go with this option here. I think this is the least evil of all, but there were some trade-offs discussed between Nayef and myself.
Nayef Ghattas 00:25:24 Yeah, and part of the trade-off, to be clear, is that the… different, components that are producing profiles, like SDKs, do have… the projects do have access to the proto… protoversion, but sometimes it's in a bash script, somewhere that is used to pull the proto repository and to vendor the portal or generate them, so it doesn't necessarily… live in a place where it's easily accessible to code, so we need to modify the tooling in each repository to be able to pull that and put it in a constant, and somewhere we can update it in the code.
And it's not clear whether that is, necessarily worth the hassle.
Felix Geisendörfer 00:26:06 And I think this, considering also that this is not going to be a forever thing that we expect to maintain once we go stable, I think this is the lesser Ivo, it's easier to describe.
Every bump in the number is going to be a breaking change, and people upgrading their producer code will just have to… they have to do work anyway to produce profiles in the new way if we make a breaking change, and they just need to also look at the change log, saying, hey, the version number you're supposed to send is now this one.
Seems reasonable.
Alexey Alexandrov 00:26:34 And when… and when, Profile Center GA… 3 trays…
Felix Geisendörfer 00:26:40 Completely.
But basically, the historical components that customers might still have installed are early adopters, they will continue sending this version header, so production systems receiving profiling data can still try to convert these older, not stable versions of the Profiling signal into whatever they need on the backend.
Or at least produce an error message for the… to the client, saying, hey, upgrade your client.
Alexey Alexandrov 00:27:07 Dropping it later means that there is no… there will be no way to distinguish current state, like, early alpha state and GA state, is that a problem? Or… Or enough time will pass.
Nayef Ghattas 00:27:20 So, they have a different path in… they will have a different path in gRPC, because the current alpha state is V1 development slash profiles, and the stable state will be V1 slash profiles.
Alexey Alexandrov 00:27:33 Or is it, like, the package will be different.
Nayef Ghattas 00:27:35 Yes.
Alexey Alexandrov 00:27:39 Is that… is that captured in… in the profile in some way?
there's schema field or something like that, that points… because I understand the package is different, but if someone is comp… like, if you're just deserializing the bytes, you don't know what the package is, you just, like, you just deserialize the bytes.
Nayef Ghattas 00:27:58 Yeah, there's also, I mean.
It's not captured in there, but also we cannot capture it in there, because you need access to that data before boxing the bytes.
Because if you… Don't have it before, you don't know how to pass the bytes exactly.
So what most OpenTelemetry components have access to is the path To which that data was sent.
And can use that to discriminate between both.
Felix Geisendörfer 00:28:30 I guess the other option would be that we just say that whatever the last version number is that we publish should be continued to be used by the stable signal.
That would also be an option.
Alexey Alexandrov 00:28:47 Yeah, but then… but then maybe you wouldn't… wouldn't want to have development in the… in the field name.
Nayef Ghattas 00:28:55 Excellent.
Felix Geisendörfer 00:28:57 I'm…
Nayef Ghattas 00:28:57 I mean, the… those fields will be either HTTP headers, or… Jrpca request metadata.
So, something that is… has access to those fields also presumably has access to the endpoint, or the gRPC service.
Alexey Alexandrov 00:29:16 Oh, so this field is not going to be a part of the proto itself.
Nayef Ghattas 00:29:20 No, yeah.
Alexey Alexandrov 00:29:20 I misunderstood.
Okay.
Felix Geisendörfer 00:29:28 Yeah, I think if the gRPC endpoint changes, it's probably good enough, right?
Alexey Alexandrov 00:29:32 Yeah, I think, yeah, it's… at least it's not, at least it's… At least, like, it seems it's the same… Surface where both the endpoint name and this attribute is available, so it's enough information to make… to make the choice.
I think the only question is, do you ever want any downstream clients that are kind of, like.
further downstream to be able to know the difference, but I assume the answer is no.
Felix Geisendörfer 00:30:00 No. In fact, even the collector, like, once we go stable, the collector might decide to not support the V1 development at all anymore, for example, and… Yeah, it would be just an optional, or maybe an optional thing you can enable with a flag or something.
Alexey Alexandrov 00:30:18 Yeah, in a way, this is probably better so that… This, this, this surface where This kind of dispatching can… can… Can be done is limited, rather than… People start checking diversion.
In a lot of different places.
Yeah. So I think… I think this makes sense.
Felix Geisendörfer 00:30:48 Okay, then, unless anybody has more thoughts on this, I think next step is for Nayef to update the proposal slightly, to also declare where we're going to put the version numbers, maybe, I think the release notes are the best place.
Maybe also add a section on answering that question that Alexey just raised, because I think it's a good question, so we have that written down if it wasn't already.
Nayef Ghattas 00:31:12 I think it's in the doc.
Felix Geisendörfer 00:31:14 Yeah. Oh, okay, then… highlighted in red and make it big. No, just kidding.
Nayef Ghattas 00:31:21 I know Tikan also asked the same question, so I'll maybe highlight it.
Felix Geisendörfer 00:31:24 Yeah, no, I forget that it was in the doc as well, and I read it not too long ago, so no worries. But yeah, just update the numbers, and then hopefully we can get it. What's a… do we need TCRAN to approve it, or somebody, or is it already pre-approved?
Nayef Ghattas 00:31:40 Tegan has already pre-approved it, we just need to open it as a PR in the OpenTelemetry Proto repository.
Felix Geisendörfer 00:31:49 Sweet, thanks. Then, I will move us along, protest if you don't want that. Florian has, a Florian Information Process SD… context SDK proposal.
Florian Lehner 00:32:03 Yes, as we are moving on with the process context, we have readers, now we need someone to actually make use, or someone that produces the data, and I opened a proposal in Go.
Go repository of OpenTelemetry, so people can actually, actually make use of the process context and populate it, so that, EVPF Profiler, but also OBI can make use of it.
It's very simple, it just… follows… most of the publisher's, standpoints. So, a new publisher that, can accept, resource attributes, resources.
And, then publish them over the, over the socket, as we have defined them by the protocol. Yeah, if you have any feedback on it, happy to receive it. If you like the approach or the idea, give a thumbs up. My next step is to, after this meeting, join the OpenTelemetry Go Meeting, and talk with the GoSig, and, ask them to get this implemented, basically. Not basically, but, get this moving forward so, more people can make use of the process context, and, we have more data.
Add more context. Yeah, that's all.
Oh, did I just talk and, was on mute?
Felix Geisendörfer 00:33:38 No, no, no. Okay.
Florian Lehner 00:33:39 Sorry. Sorry. Okay, let me repeat myself. Sorry, sorry, sorry.
Scott Gerring 00:33:47 You weren't on mute, it's so good we had you.
Ivo Anjo 00:33:49 No, we heard you, yeah, yeah.
Felix Geisendörfer 00:33:50 Yeah, yeah, I said you… we heard you.
Florian Lehner 00:33:52 Okay, sorry, I just noticed my… okay, sorry, damn. So, yeah, if you have feedback, feedback is welcome. That's the short summary.
Felix Geisendörfer 00:34:04 On first glance, with what I remember from the context I work, this looks good to me, but I guess we have some people who worked on this very closely here. I don't know if you see anything wrong with it, or… looks good.
Scott, give thumbs up.
Florian Lehner 00:34:19 The only thing that is not covered is the extra attributes. Extra attributes, I think, that's still in the working, but for the resource attributes, it covers the fundamentals.
But extending this approach with further extra attributes, should not be a breaking change, but more an extension.
Scott Gerring 00:34:41 For what it's worth, we've got a PR open over on OTel Rust as well that we've been slowly pushing along, so hopefully we'll have more than one SDK with it soon.
Felix Geisendörfer 00:34:52 Is the interface similar to what you're doing on the Rust side?
Scott Gerring 00:34:56 I will go and check it out tomorrow.
Felix Geisendörfer 00:35:03 Okay, thanks. And then, Florian, is for you the next… no, I guess the next step is you ping people who would be interested in implementing it, you're not planning to do it yourself, is that what I heard?
Florian Lehner 00:35:13 I have an implementation for it already, I just need to talk to the GoSik people just after this meeting.
Frederic Branczyk 00:35:24 Without having, read any of the… PR… oh, sorry, it's just an issue. But, like, how… how do we intend this to, Like, we don't actually intend anyone to use this interface directly, right? Like, people set these attributes already in the SDK somehow, and this just kind of gets set automatically, no?
Florian Lehner 00:35:50 No, not really. So, this is more like the… I instrument my application.
So it's not part of the auto-instrumentation approach.
And people can just, share resource attributes as they like. So, at the moment, they don't need to. They can also be selective on saying, hey, I'm sharing this kind of resource attribute, but not the rest.
That's up to use how the people are using, the approach.
Felix Geisendörfer 00:36:18 Can I ask if you're saying that nothing will be done automatically if you have SQL SDK, or some will be done automatically, but if you want extra attributes, you have to take care of it?
Florian Lehner 00:36:29 It's not done automatically. So, if you instrument your application with this, with this API, then it will show up in the process context protocol or the sockets, but it's not part of the auto-instrumentation, so if someone just does the auto instrumentation with Go, I think this would be another part of the… of having a discussion with the GoSik, how they enable such features that, then expose this information.
Frederic Branczyk 00:37:03 I'm not really worried about auto-instrumentation, but, like, people already explicitly say, you know, I am this part, or whatever, right? I feel like those things should automatically be added to the… to this context.
I can't remember what the exact interface is in the Go SDK for this, and whether that allows for that, but, like, naively, as a consumer of the library, I would expect that if I set these attributes once.
They end up in places like this automatically.
Florian Lehner 00:37:38 Yeah, that perfectly makes sense, but it should be also only the next natural step on this. Okay, okay.
Frederic Branczyk 00:37:45 There's not, like… It's just, like, that's… that's what we want to do next. It's not like there's a reason why we're not doing this at all.
Florian Lehner 00:37:54 Yeah, yeah, no, no, it's probably more the next natural step.
Frederic Branczyk 00:37:57 Alright.
Then, in a sense, I don't care as much about this API.
Felix Geisendörfer 00:38:03 I do care a little bit, because it matters on whether this is an internal package or a public package that consumers are supposed to use, because if we have applications starting to use that, and then the SDK is doing it automatically, you might have conflicts, so I think we should be clear.
And my preference would be to just make it internal for now, and really strongly push for the SDK to automatically call this. Exception might be if there's additional attributes, but even those, maybe those can already be supplied to the resource through existing mechanisms in the SDK, so maybe we don't need to publish any public interface for this.
I think.
Frederic Branczyk 00:38:43 My hope would also be that this comes up in a review.
Florian Lehner 00:38:49 I can take this point, to the GOESIC meeting just after this call.
And, how they preferred, things to happen.
Nayef Ghattas 00:39:02 Let Scott correct me, but I think the way this is implemented on Rust is that when the… when we're initializing the SDK and setting resource attributes, those would be automatically propagated to the process context.
Scott Gerring 00:39:18 believe that is the case, but it's been a while since I cut the PR, so I will report back synchronously, unless Naya, if you've just done this in the background and you can give definitive advice.
Frederic Branczyk 00:39:30 That's the behavior I would expect.
Nayef Ghattas 00:39:33 Yeah, that's also my recollection, but I haven't looked at the PR recently.
Scott Gerring 00:39:39 I mean, insofar as you have the resource for the SDK, it seems intuitive that you can push it through automatically, but…
Felix Geisendörfer 00:39:53 Okay, but I think we all agreed that this is how it should ideally work. Like, ideally, you use an OTEL SDK, and context… Process Context is published for you automatically, so you don't need to do anything to be a good, process as far as CBPM profile is concerned.
Frederic Branczyk 00:40:11 People shouldn't need to know that this exists in the first place.
Felix Geisendörfer 00:40:14 Exactly, yeah.
Scott Gerring 00:40:15 It's also not like there's a recurring runtime cost to having set it up, so I don't really see a substantial downside there.
Felix Geisendörfer 00:40:48 I guess the one caveat is if they, like, are realizing, oh, I can get attributes about my process from the profiler, and I want to see something new there, they need to figure that out, but that could still be an SDK-level API, not ours.
Okay, cool. I think that covers it well, but if anybody has something to add, please do it now. We have about 20 minutes left, so we should… Continue?
Okay, then… next topic would be… Scott Memory Profiling? Pull request, 1 out of 4, go for it.
Scott Gerring 00:41:21 I'll try and be real quick with this. Thank you all with the support with the PRs so far.
Especially Florian and Christos. I think the first one should be pretty good at this point. The one question I have to you both while we're on the call is whether or not we want to cherry-pick in the trace improvements from the other branch, or if we want to merge them separately on top after this, I don't mind either way.
Christos Kalkanis 00:41:45 Yeah, well, it's up to you, Scott, whatever you think is best.
Scott Gerring 00:41:49 I'm trying to optimize for giving people the least amount of nightmares with all these PRs as possible, but I don't mind. I can cherry-pick it in tomorrow morning, and we can ship it all that way.
Christos Kalkanis 00:41:58 Okay, let me know if there's something else I need to do, because you mentioned that there was some subsequent changes to your pull request. Maybe I need to pull those in, or if you're happy to fix it up.
Scott Gerring 00:42:09 Oh, P.
Christos Kalkanis 00:42:10 I can, I can do the… I can do the work.
Scott Gerring 00:42:12 No, that's okay, I can pick it, I can adapt it, I'll ping it back to both of you for feedback, and then I think we should be good with the first one. And I'm hopeful that this is one of the weirder ones, because it's pushing the interfaces out to support the patent in general, and then the profiler on top for the allocation profiling.
With the probes work, with these little adapters, should be relatively straightforward.
Christos Kalkanis 00:42:35 Great. Thanks for doing this.
Scott Gerring 00:42:37 No, no worries.
Florian Lehner 00:42:39 Maybe just one question. The only concern I had left, that's why I did not approve it yet, was around the pre- and post-processing of the traces, and if we want to limit it on the… on something like the origin ID. Yep.
Scott Gerring 00:42:59 criteria.
Florian Lehner 00:43:00 Okay, perfect, okay, my thinking is, like, hey, limiting now the scope of this and having it limited is easier to have it now than expanding it later, because we are doing this always in the hot path of, handle trace and handle trace is something that is… Not parallelized well, and we have a lot of locks, so, this can be a bottleneck in the future, and that's… that's… that's what was the original of my concern, but,
Scott Gerring 00:43:33 Yeah, no, I agree. I pushed back initially, because I thought maybe this is a premature optimization, but I went through it again in more detail. You convinced me, I adapted it. And again, I agree with you, I think it makes sense to Take the hard lessons and the hard path that we've won, and continue to apply them, rather than regressing and then moving back again, especially insofar as it's in the interface.
Florian Lehner 00:43:54 Cool, cool, yeah. Thanks for calling. Thank you. I will have a look again.
Scott Gerring 00:44:01 Alexey.
Alexey Alexandrov 00:44:03 I'm sitting… next to… well, some folks are remote, so not sitting, but, like, I know well TC Malloc, Google TC Malloc allocator people pretty well, and, like, they're very close to me organizationally, so I can also offer if… If there is desire in the future to… to… like, if there's anything that TC Malloc allocator could do to support this, then I'm happy to help.
Scott Gerring 00:44:28 We… we would be very excited about that, I think. I mean, ultimately, we've tried to keep the user space side so simple as possible that you can foreseeably upstream it into the allocators.
And the kind of hope that I've got in the back of my brain is that once we support it here, once we can point it and say, this is valuable and it works, we can take that back to the TC Malloc folks and whatnot, and use that to push that That wheelbarrow up the hill, so absolutely, let's loop back on that in a bit.
Frederic Branczyk 00:44:54 Two… two small things. One, I'll make sure that Tommy reviews this, because I think this would make GPU profiling, significantly simpler on our end.
And then two, have we ever gotten any responses from the Mimalog people?
Scott Gerring 00:45:14 we have a PR from one of the other Datadog folks adding the kind of regular sampling path pattern to MemAloc, I don't know what's happened with it. I have the PR link handy, I'll go… I'll check it out, and I'll chuck it in the notes.
But that would be very helpful, yeah.
Frederic Branczyk 00:45:30 You're mentioning this.
Scott Gerring 00:45:31 Really heavily heavily used, right?
Frederic Branczyk 00:45:33 Yeah, I asked because we… have been pretty desperately trying to reach anyone to answer even the simplest things on me malloc, and we can't get anywhere, so I wonder if anyone has any connection to Microsoft.
to find… A way to get through to them.
Scott Gerring 00:45:55 We have actually one other person internally who might be good. I will speak to him. I'm thinking of Christoph here, da-da-dog gang. Maybe that will help.
Frederic Branczyk 00:46:06 I think this, like.
train of thought has easily existed for 2 years now, and we have never had any input from the Memeloc folks.
Felix Geisendörfer 00:46:18 I want to point out that we had Alban here reporting security issues in the past, and he's at Microsoft, so that could be a good threat to pull on as well.
Frederic Branczyk 00:46:26 Actually, no other one.
I can try that one.
Felix Geisendörfer 00:46:39 Cool then. Yeah, maybe try Alban first, and if you can't get anywhere, we can work with Christoph. He knows some people at Microsoft, and maybe between those two leads, we can figure out a pass.
Frederic Branczyk 00:46:49 Yeah, cool.
Scott Gerring 00:46:49 Yeah, he's been looking at the moment anyway at whether or not we might be able to get USTTs into the .NET runtime, but that might be a different part of the battleship that I assume Microsoft is.
Felix Geisendörfer 00:47:00 We could get what? USDTs?
Scott Gerring 00:47:02 If we could have the sampling hooks that we need within the .NET runtime, so we could sample managed allocations as well, with a similar pattern.
Frederic Branczyk 00:47:09 Fair enough.
Felix Geisendörfer 00:47:10 Great.
Scott Gerring 00:47:11 It would be pretty fancy, huh?
Felix Geisendörfer 00:47:28 Sweet.
I'm very excited about living in this future where all these Allocators and kernel things.
know each other and like to talk to each other. That would be a really nice world to live in.
Scott Gerring 00:47:40 It's a beautiful dream.
Frederic Branczyk 00:47:41 Yeah, I was just gonna say, it's just a dream at the moment.
Felix Geisendörfer 00:47:45 It might just happen. I mean, we've got some momentum here. We've got some people pushing on it, and we're not being told it's a complete no, so let's see.
Cool. I'm sure there's more in memory profiling, but is there more on this particular thread that we should… Get two, or should we move on to the other three items?
Scott Gerring 00:48:09 I think we're good.
Felix Geisendörfer 00:48:10 stand up?
I don't know if that's stale or not.
Frederic Branczyk 00:48:14 I believe it's stale.
Felix Geisendörfer 00:48:15 Okay, stealing.
Alexey Alexandrov 00:48:16 sort of stale.
Felix Geisendörfer 00:48:18 That's fine.
Okay, I'll move as long. If somebody wants to go backwards later, let me know. Frederic, you've got a topic on metric-style temporality.
Frederic Branczyk 00:48:27 So both of my topics are, you know, I have the chance to redesign my system right now, so I want.
Felix Geisendörfer 00:48:34 Congratulations on that channel.
Frederic Branczyk 00:48:35 Thank you, thank you. So I want to see if some of the judgment calls we made should be rethought.
So, like, basically, we, a while ago, like, I don't know, years ago, we, we, like.
naively adopted the, like, temporality from metrics, and then removed that again. But, I think… I'm not suggesting necessarily to add it back, but I do wonder what should consumers Use as an indication to know whether a profile represents, you know, the change… a change rather than a snapshot.
Right? Yeah, go ahead.
Felix Geisendörfer 00:49:21 I… I believe we were discussing using semantic conventions for that by declaring the, sample types as well-defined sample types, which would then indicate some temporality, but maybe I'm misremembering. Somebody would remembers more. Please speak up.
Frederic Branczyk 00:49:47 I suppose I don't… I no longer have a horse in the race, but, whatever it is, I think we should at least… we should document it in the proto.
Florian Lehner 00:50:05 maybe I'm remembering wrong, but I think we have a comment in the Proto around time duration.
And that is said if you… if we set it to zero, that it's implicit, that it's a snapshot, and if it's, to set to something else than, zero, then it's more, duration with the time Unix timestamp.
So… I think we had some discussion around this, but, maybe not the best documented.
If this makes sense.
Frederic Branczyk 00:50:40 That… that would be a reasonable thing. I mean, that's exactly what I… what I wrote here. Maybe we can quickly double-check this…
Felix Geisendörfer 00:50:51 Double checks that. So, where would that be on the duration?
Frederic Branczyk 00:50:54 Oh yeah, you are correct. That is how we documented it.
Felix Geisendörfer 00:51:01 Is it on here?
Frederic Branczyk 00:51:04 Well, I suppose we documented the inverse.
Florian Lehner 00:51:09 Yeah, yeah, I think we can improve on the documentation, at least, yeah.
Felix Geisendörfer 00:51:15 Okay, but I think we're aligned on the intent, like, if this field is set to zero, it's a snapshot. If it's not zero, it's not a snapshot. Yeah. And somebody could do… pass over the comments to make this more clear.
Frederic Branczyk 00:51:27 I can… I can take that.
Felix Geisendörfer 00:51:30 Oh, sweet.
Okay, cool. Then… Problem was already solved, we just forgot.
And next one is Frederic again. Let's see if this one's easy as well.
Frederic Branczyk 00:51:53 Basically, basically the question is.
How do we communicate to a consumer that two data points Are the same, or at least… represent the same kind of data, so that, you know, representing them in the same flame graph is a valid thing to do. Even in the event, at least that's how Florian answered initially here, even if we have sample type, sample unit, period type, period unit being the same thing.
Or are we saying those four things being the same should always be safe to merge?
Florian Lehner 00:52:33 So… just to give a recap on what I've written in the document, I think if, sample type, unit, period type, and, period unit are the same.
Then the way this data was collected should be the same. And it's up to the, the other describing attributes, like resource attribute, scope attribute, and profile attribute, to find, define a more granular view, I would say.
But if I say, hey, give me everything for… This resource, they should be mergable in that sense.
Yes, the risk is probably, attributes are not limited, so, cardinality is on the back-end side, the high risk, if you… how you want to deal with it, but, I think At least… They should represent, or having the same sample type, sample unit, and period type, the period unit should at least have the guarantee for the backend that, they are… were collected, in the same way, so… If that… it makes sense.
Frederic Branczyk 00:53:53 Yeah, maybe let me provide an example of what I'm thinking of. Let's say I want to merge some kind of profiling data across the entire infrastructure, right?
what are the keys that I need to provide in order to get that guarantee, right?
So, like, let's say… like, an example that we've had come up was, you know, CPU time that is both collected from the agent, as well as from a Go runtime, because it was, you know, collected in a serverless environment or something.
I think this is reasonable to show in the same flame graph.
But why, right? Like, which pieces of data in our proto tell me that this is a safe thing to do?
Felix Geisendörfer 00:54:46 Wait a second, just on your use case?
you're collecting the CPU profile for the same process with two different profilers, and now you want to merge it?
Frederic Branczyk 00:54:56 No. Different, different processes, but I want to show them all in one plain graph.
Felix Geisendörfer 00:55:01 Okay, because if you have an overlap, then you might produce.
Frederic Branczyk 00:55:04 That's a different… that's a different question. That's trash.
Felix Geisendörfer 00:55:07 Good, good. Okay, so you basically just have one process that was processed, profiled with eBPF Profiler, one with Go, they both have CPU, now that you want to see that together because it was, I guess, on the same host, or you don't care, you want to do it in for a wide, like, something like that.
Frederic Branczyk 00:55:22 Exactly.
Felix Geisendörfer 00:55:28 Is there any reason that this, what you wrote here, would not be the right key for that? Is anything missing?
Frederic Branczyk 00:55:33 Not at all. That's… that's what… that's the implicit… choice we've made on this data, but I wanted to kind of gather if anybody felt like this was an incorrect thing to do, and if we do think that this is true, then we should probably also document this within the proto.
Florian Lehner 00:55:54 The only thing I would add, maybe, is the period. So, besides the period type and unit, also the period, because the Go runtime uses a sampling frequency of, I think, 100Hz.
And eBPF Profiler, 19Hz, so, merging then will come… will invalidate the data, so I would take at least also the period into account.
Frederic Branczyk 00:56:21 This goes back to… I actually thought about exactly this, and it goes back to a conversation we had, like, 2 months ago. I pinged Felix on this on the channel today, because we never actually resolved this conversation of Whether we should encourage profilers to ever send counts?
Or whether they should just always already do this multiplication with the period.
Alexey Alexandrov 00:56:49 I think… I think I'll take an action item to write a short talk about that. I… I really want to kind of, like, finalize the discussion, and I think we… I think when we had it, there's, like, enough context that, like, maybe… maybe I can write something down, and we can discuss, in the… in the next meeting. I think, like.
We need, like, a coherent set of options, and Yeah, there was this discussion about, like, whether… whether you can use the… the, the period to kind of, like, represent the default count for things that don't carry the count as part of the sample information, and we… yeah, we… and I think, like, this also fits, like, if you're using sample type information as a key.
is the period a part of that, or it's not a part of that? It's… because I was also thinking of a case, let's say I have, like, heap profiles for the same process. Like, maybe, imagine, like, the Java side of the heap and C++ side of the heap.
And that, I would probably want to merge. And, like, the sample… the sample type is the same, but the period might be the same, might be different, because these are, like, kind of, like, separate heap profilers.
Yeah, so I'll… I'll write something up, and we can… We can… let me add an action item.
Felix Geisendörfer 00:58:10 Okay, cool. Thank you so much. Yeah, I think it will take somebody to take, like, A hard look at this and think about it for a little bit, and propose something, and then we can either update documentation or make some semantic changes to the protocol as needed.
So yeah, you can either just document how… what we have should work, or a proposal on how we should change it for this, and it all makes sense. Thanks.
Alexey Alexandrov 00:58:33 I'll document it first and see if, like, if there's a proposal that, like, organically falls out of that, or, like, list a few options, and maybe with a preference, and then we can walk through that.
Felix Geisendörfer 00:58:45 Sweet.
Thank you so much.
Okay, then maybe we'll wait for that before we spend more.
Effort, okay, and maybe gets us to 1 minute for metadata enrichment in the eBPF profiler from Nayef.
Nayef Ghattas 00:59:00 Yeah, so for the context, I think, Florian counted it, but we have, like, 9 different PRs with slightly different implementations in the profiler.
in the VPF Profiler to add metadata, and each have their trade-off. This is, for example, blocking the part that is reading the hotel process context on the Profiler side, like, the PR is blocked, because there has been many multiple rounds of reviews, and there is not necessarily alignment and agreement on how we should do this. So, what I did here is list all the use cases that we have for metadata enrichment in the profiler, and have an open question with the trade-offs from the different PRs, and I think Florian also has a gist where he compared all the different implementations.
and the different trade-offs we could take, and I'm essentially… I essentially think we should find a way to move forward on this question, because it's been sort of floating since April, and we're not able to… to move forward on this, so I wonder what we should do here. Should we, schedule another sync meeting with, especially the folks on the EVPF Profiler to discuss this? Any other suggestions?
That is the… the TLDR.
Christos Kalkanis 01:00:20 So, which document would be the better for review? I think, does the Google Doc, make more sense? As people can leave comments there, because the GIFTs… I mean, I guess you can leave comments in GIFs as well.
Nayef Ghattas 01:00:33 I think that the Gist was focusing on the implementation details. I tried to extract the trade-offs from the implementation details in the Google Doc, so…
Christos Kalkanis 01:00:43 Okay, so what I would suggest is, let's get Timo pulled in, so that he can review the document that Nayef has created. Roger, as well, if you can do a review pass, that would be great, because Roger I worked on the existing process meta enrichment API.
And let's look… so that would give us some sort of broad alignment, so that, you know, we don't just spring this later, in front of Timo, then we ran into more blockers and so on.
So let's just get, the shape moving in the right direction.
Felix Geisendörfer 01:01:20 Okay, cool. You'll take an action item for this, Christos?
Christos Kalkanis 01:01:24 Yeah, yeah, sure.
Felix Geisendörfer 01:01:25 Okay, sweet.
Okay, we're at time, but if anybody has either a thought on this or some other last thought, let me know.
Alexey Alexandrov 01:01:39 The only question I had, like, I thought… I think, like, during the period discussion, Florian, who is not here anymore, mentioned some document, and… but there was… there was no link… maybe I misheard, but… I'm curious, like, is there a document that I missed?
Nayef Ghattas 01:01:55 No, I don't think there's… I think he was mentioning what he wrote on the SID Meeting notes prior to the meeting.
Alexey Alexandrov 01:02:01 Oh, okay. Okay.
Frederic Branczyk 01:02:06 There are some prior notes from June 9th or something like that.
But, I think that's it.
Alexey Alexandrov 01:02:13 Yeah, I linked those, but I thought, like, maybe there's a separate one or something.
Christos Kalkanis 01:02:18 Quick question, Frederic, because you brought this up today. Now that reminds me, we also have, like, a very similar issue here, that the sample type is completely unspecified, so in theory, anybody could just come up with anything. There is not a single registry of sample types, which is a problem if you're trying to do correlation across either multiple producers.
So I think the consensus there was that we would formalize it, somehow, like, come up with a list, and put it maybe in some other conventions, maybe in a specification, so somewhere that people can refer to.
I'll go back and read the…
Frederic Branczyk 01:02:54 Yeah, maybe read the notes. I don't know, I remember it as just we put the well-known list of things into the proto, but maybe I'm misremembering.
Christos Kalkanis 01:03:06 Yeah, the product right now doesn't have it, like, it's just… it gives some examples, for example, like, and I think some of those are pulled from paper, maybe one or two are not even there, like, let's just average, right?
Frederic Branczyk 01:03:17 Yeah.
Felix Geisendörfer 01:03:22 Okay, I'll leave it to you to follow up after the meeting.
I think, since we're at time, thank you so much, everybody, for joining, thank you so much for all the work, and as usual, have a nice local time.
Ivo Anjo 01:03:40 Thanks, everyone.
Christos Kalkanis 01:03:41 Alright.
Frederic Branczyk 01:03:42 Thanks, everyone. Bye.
