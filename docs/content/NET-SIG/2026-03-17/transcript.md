SIG: .NET SIG
Date: 2026-03-17
Duration: 30 minutes
Zoom Recording URL: https://zoom.us/rec/share/FmOToSOY1IKgA3E4Y-hRtjDvxn02icPN14j9b8866R3KyNxZkSNncv2AoEnVg0IL.4WaswZJ4Sh2xX02i
============================================================

## Zoom Recording Transcript

**Martin Costello** 00:41 Hey.
I think Raj is gonna make it, but I know Helen isn't.
Is there anything you need to review you want to put on the, agenda? Here's Raj.
**Rajkumar Rangaraj** 03:11 Martin, do you want to drive? I have a hard stop today at 11.25.
**Martin Costello** 03:16 Okay. Give me a second.
And… Come on, Chrome. Right, there we go.
So, first item on the agenda, Raj, did you have a chance to catch up on the issue?
**Rajkumar Rangaraj** 04:10 I did spend a lot of time on that.
**Martin Costello** 04:15 Okay, cool. So I put a comment on here, I had a quick look into the YAML library.
And put a few more comments. Anyone have any feedback?
**Rajkumar Rangaraj** 04:26 So I…
**Martin Costello** 04:27 so far?
**Rajkumar Rangaraj** 04:28 Yeah, This is what I believe with all of my research on this one.
or configure it, like, for example, this is what I think we should do, or if we take a configuration from Java and place it here, the same YAML, it should work for .NET 2. That's what our goal should be.
And based on the design, I feel we have been… we have burnt our fingers so many times by using a vendor library.
I would vote to say that We do a handwritten configuration. It's not going to be very, very trickier here.
That's what I would recommend us to do here, because you might… just before you had come, Martin, we did a big work on removing Google Protobuf library dependencies, and we did a handwritten serialization and everything.
The reason is, this repo was… get hit several other times by a CV from those libraries, and if those don't get serviced on time, the SDK will be unsecure.
So… It's better to have the similar principle followed On this one.
**Martin Costello** 05:50 Right, so you're proposing we just implement the minimum possible subset of YAML assets?
**Rajkumar Rangaraj** 05:56 That's correct. Yes.
**Martin Costello** 06:04 Do you have an idea on roughly how much work that is?
**Rajkumar Rangaraj** 06:09 No, I did not estimate on that work at, so… need to try… check the… on the estimation, need to look at the other vendor-este library and how much of that is what we needed for our implementation. So anyways, it's… it's going to follow the similar guidelines and everything.
with the agents doing the coding and all, I don't think it should take a longer time, more than a month on this one.
**Martin Costello** 06:41 I guess, I guess, CVEs aside, I guess one advantage of that idea is we don't have to, Tackled the problem of how do we take vendor code, vendor code, but keep it internal?
Or the dependencies problem.
**Rajkumar Rangaraj** 07:02 We could try that as a first step, if you want, because that's our internal implementation, and later we can have an option to change, completely, remove, and wire up our implementation is needed.
**Martin Costello** 07:17 Yeah, I… I guess… maybe… because I've not fully read the declarative config spec myself. I guess it depends how much of it we need to use, because I remember I asked Jack, who wrote the spec. About… YAML features at OTEL Unplugged, and he said that they'd picked a version of YAML that didn't require anchors, which would massively simplify the implementation, so maybe if it's… if the structure's relatively simple, then… maybe writing our own's the easiest way to go if we don't need to support lots of exotic YAML features.
**Rajkumar Rangaraj** 08:06 I, I agree with you.
**Martin Costello** 08:12 Ehh… Did you have any feedback on point number 3, which is… for being able to use this from Contrib.
**Rajkumar Rangaraj** 08:35 Sorry, Martin, like, your voice is breaking, I missed what you asked.
**Martin Costello** 08:40 Oh, sorry, did you have any thoughts on item 3, about how we could design it so that libraries in Contrip could support declarative config?
**Rajkumar Rangaraj** 08:53 Not it. Still, it… what I would like, what I thought is it should be extendable.
Dope.
But no, like, to be answered, if I need to precise answer, no, I don't have… did not think about that yet.
**Martin Costello** 09:18 Okay That's fine.
And I think point 4 is just me making an observation that it might flush out stuff we need to change with regards to reloading.
**Rajkumar Rangaraj** 09:29 Yeah.
**Martin Costello** 09:30 I think the rest… the rest of the conversations that I've put there so far has all been related to the vendoring, so I think… We've not answered the question, but we've added another possible approach that avoids a number of the possible problems raised. Was there any other thoughts or feedback you had about stuff we might need to do?
**Rajkumar Rangaraj** 09:57 That's all, Martin. I don't have anything else, because I thought, let's make it… when I was going through it and looking at all of the previous challenges, what we had, we thought we'll follow the same ideology instead of inventing a new one.
Definitely taking a package dependency is not an option… should not be an option for us at all.
Rendering is still acceptable, but maintaining the rendering coding, or if there is a bug, we need to We should be in a position to fix ourselves or have an expertise in the code that we copied over.
That's another challenge.
we need to be prepared for, if we plan to take it. But yeah, with all… taking all that into consideration, custom-written one would be the best fit for us.
And, the… on the other one, just, I'm throwing the idea of the contrary part, like… I, I mean, I did not look into it in Java or Go, how… extensible this is. Probably, I think we need to go and learn from that how extensible is it? They give you a package, or how it works. Based on that, we need to have the extensibility point.
to take it to the… not only to the contrary web, for example, there is a exporter outside of these repos, how we will… they can also utilize this one.
**Martin Costello** 11:31 Yep, that's fair. I think I was just using Contrib as an example rather than only for Contrip, but yeah.
**Rajkumar Rangaraj** 11:37 Yeah, yeah.
I think we can… I'll write down my thoughts here on Martin. I think we can continue the conversation here instead of waiting on the next SIG and everything. I think that would… In that way, we can keep on brainstorming instead of waiting on 6 on 6.
**Martin Costello** 12:01 Okay, cool.
Anyone else got anything they'd like to chip in about declarative config?
**Matthew Hensley / Grafana Labs** 12:12 There's One thing to consider, and can also put it in the issue, is, like, hot reloading and such, it's gonna be… Quite interesting to get implemented across instrumentations.
Assuming that's… Yeah. No, it's there, but, like, the fact that .NET has native Instrumentations?
So, like, HTTP client, ASP.NET Core.
**Martin Costello** 12:42 Oh, right, I see.
You know, like, it's… they might have, like, statics in memory of stuff that we can't reload.
**Matthew Hensley / Grafana Labs** 12:49 Yeah, so just stuff that relies on eye options to be injected directly versus an eye options monitor. It's a… Just wanted… Mention it before, we make any… Big decisions.
**Martin Costello** 13:13 Yeah, cool, thanks.
Anything else?
**Rajkumar Rangaraj** 13:21 Sorry, I had an issue, and I had to restart the Zoom session.
I did not hear last one minute. Hopefully, nothing, no, there was no question for me.
**Martin Costello** 13:31 Nothing for you, Raj, no.
I've made a note of the stuff Matt said, I'll pop it in a comment on the issue when we're done.
Okay, so that's all for the YAML item.
Judith, you've got some stuff about the log bridge?
**Julius Koval** 13:53 Yeah, hi, so based on what we talked about two weeks ago, I tried to open up PR, where I tried to We've basically removed the… You know, flags from the LogsBridge API, where it's internal and… single releases.
And then Pyotr denied it because he had made, this issue, and… a comment some time ago where he basically made some complaints about the current state of the API.
some things that, I guess, You know, aren't in compliance with the spec, or whatever.
And so, I guess I want to go through them.
dumb.
I guess the easiest complaint to fix… It's a… if you scroll up a bit, it'll be there.
You know.
**Martin Costello** 14:48 this list.
**Julius Koval** 14:49 Yeah, yeah.
So, it says that there's the missing field observed timestamp. I could try to add it and open a PR for that, if that's okay. That should be pretty easy to fix.
**Martin Costello** 15:08 Yep.
**Rajkumar Rangaraj** 15:09 Where you plan to add that missing field, like the absorbed timestamp, is it going to log record as a public field, or where is it going?
**Julius Koval** 15:20 Well, I don't know about the object log record, but when we're using the Logs Bridge API, we create, A struct called log record data, which has all the fields, like timestamp, and severity number, body.
Event name, and so on.
And I guess it should also have observed timestamp, which it currently doesn't.
**Rajkumar Rangaraj** 15:44 How does… all I wanted to, understand is how does it change, or, the current, or whatever the, public API surface that we have it now?
**Julius Koval** 15:58 Well, it would add, Rajkumar Rangaraj 15:59 Where does it go, this observed timestamp, and is it going to have an impact in the output that we see? For example, in the console output, we see a few fields being emitted out. Would this be another one come and sit there?
**Julius Koval** 16:13 This would be another field.
If that's… if that answers the question.
So it shouldn't be breaking chains or anything.
Obviously, I'd love to look into it a bit more, but…
**Rajkumar Rangaraj** 16:35 I'm not able to hear, I believe.
I have a weird issue, like, I changed my network, and… Headset, nothing works.
**Julius Koval** 16:46 Sorry, is it better now?
**Martin Costello** 16:51 I can hate it.
**Julius Koval** 16:53 Oh, okay.
Rosh, can you hear me?
Oh, okay.
**Martin Costello** 17:01 She's dropped off again.
I'm not entirely sure if it's entirely Raja's fault, because I'm… getting that as well, so it might be Zoom.
**Julius Koval** 17:13 Well, I tried to readjust my mic a bit, so I don't know if it's better now.
**Martin Costello** 17:19 I can hear you at the moment.
**Julius Koval** 17:22 Okay.
**Rajkumar Rangaraj** 17:23 I just joined. I don't know whether it was my audio issue or something, like, it's the third time I have this issue on. Sorry, Julius, I did not hear anything. I thought you were speaking for a very long time.
**Julius Koval** 17:36 Oh, well, can you hear me now?
**Rajkumar Rangaraj** 17:39 Yeah, it's better now.
**Julius Koval** 17:41 Yeah. Also, I guess to answer your question, observed timestamp would be another field.
Yeah, so… You know, it shouldn't be breaking change, I'll have to look into it more, but…
**Rajkumar Rangaraj** 17:55 Okay.
So, I would say we go incrementally on this. I know this PR was blocked with the log record to be, like, the object kind of data type and all that. So, if we have to wait on those kind of blocking changes, we need an OpenTelemetry 2.0.
So, already Blanche joined, and he said that we already deviated from the spec when, even before the logs was, stable, log spec was stable.
The .NET logs was made stable, so we all… we have that gap.
So we want, just for saying that for LogsBridge, you need to cover that gap, does not, make sense, because if we have to do that.
We have to wait for… fix all the things and release the hotel2.otel.net 2.0, and then we have to walk towards that. But I would… I strongly, like, support in the current state, however, we need to add the LogsBridge API with whatever the APIs we have.
We should aim to get it then, and if there is anything that needs to be introduced like this, this can be incrementally introduced instead of blocking your PRs.
Martin, I don't know whether you agree with it. I want to take your, Cheers.
**Martin Costello** 19:19 It makes sense to go forward incrementally, But… At the same time, if we want to actually ship the logs bridge, then… It would make sense to not merge the stabilization if there's stuff there that shouldn't be there, because otherwise we won't be able to release anything from main.
**Rajkumar Rangaraj** 19:43 Got it.
**Julius Koval** 19:50 Okay, so I'm not exactly sure what the conclusion is. Should I… I mean, should we try to make it more spec compliant?
Incrementally, is that it?
**Martin Costello** 20:02 So, I think maybe in the short term, it makes sense to try and do PRs to add Anything that's, like, a must, that's somehow gone missing, but do that when it's still behind the experimental flag.
Because then the act of doing the PRs might flush out if there's braking changes required or not.
And then, when we've got it to either… all the changes are done, or we've done all the changes that don't need a braking change.
then at that point, we could stabilize the API and say that's the 1.0 version, and then anything that's needed that's breaking could then come in separately as 2.
**Julius Koval** 20:43 Sure.
Okay, so we'll try to look at all the… you know, stuff is missing from the spec, and I'll try to… Added in.
**Martin Costello** 20:59 Okay, thanks, Judith. Sorry, sorry for messing you about with the approval, and then the not approval, because, yeah, I wasn't aware that there was any missing features. I thought it was just done, and it just hadn't been exposed yet.
**Julius Koval** 21:16 Yeah, no worries.
Also, one more thing, actually.
I was, playing around with the protocol serializer that we have.
And I tried to add support for nested key-value lists.
And I have a working proof of concept.
And, you know, if I fleshed it out a bit, like, could I try to make a PR? Is there any interest in that?
**Martin Costello** 21:48 That sounds reasonable to me, if we're gonna need it at some point.
**Julius Koval** 21:52 Okay.
**Martin Costello** 21:54 Also, that would help keep the size of any PR down, if that's, like, a self-contained… Change.
**Julius Koval** 22:02 Yeah, yeah, that'll be salt content.
**Martin Costello** 22:11 Cool. Any more on the logs bridge stuff from anyone?
**Julius Koval** 22:17 I don't think so.
Actually, there's one, I guess, tangentially related thing.
And the OpenTelemetry spec, there's the concept of the context.
And so I guess we don't have that… directly in .NET, right, is my understanding.
I guess we're using activity.current.
Kind of.
**Martin Costello** 22:44 For tracing, yeah.
**Julius Koval** 22:45 Yeah, okay.
Okay, sure.
**Martin Costello** 22:55 Cool, okay, that's everything on the agenda.
**Rajkumar Rangaraj** 23:01 Martin, one more thing I just want to check. If you recall, we were thinking about one patched version of a release. Should we even think about it, or just, Move it to the next minor version release itself.
**Martin Costello** 23:17 Well, I was… I was keeping it… I was suggested keeping it pending that issue I pinged you about last week.
**Rajkumar Rangaraj** 23:26 Yeah.
**Martin Costello** 23:26 But if that's not moving anywhere, then I guess we could do the patch release.
**Rajkumar Rangaraj** 23:33 Okay.
**Martin Costello** 23:35 Because, yeah, I was just trying to avoid, I guess doing, like, a patch release within, like, a day of each other, or something like that.
**Rajkumar Rangaraj** 23:43 Good.
**Julius Koval** 23:46 And, while I…
**Rajkumar Rangaraj** 23:48 I'm sorry for both that. Thank you, guys.
**Julius Koval** 23:53 Sure.
Thank you. Bye.
And, so I had one last thing.
Yep. Regarding the Protov serializer… So I got the nested key-value list working for the serializer, like I mentioned.
But, I haven't looked at the console and Zipkin exporters yet. So, I guess, I guess we'll want to get that working for them as well.
**Martin Costello** 24:22 So, the console exporter… Yes, if it makes sense. We don't… worry about the specific format of that being locked into anything. So, if we want to add it Stuff to that, that's fine.
if I remember correctly, Zipkin, unless I've confused it with a different one, Zipkin's going to be deprecated towards the end of the year, so if I'm… correctly remembering that, then I wouldn't worry about the Zipkin one.
**Julius Koval** 24:53 Okay, cool.
**Matthew Hensley / Grafana Labs** 24:55 I incurred that, and also, In case you haven't checked, compatibility with the collector.
there was… there's a, handwritten Prometheus… not Prometheus, Protobuff.
Serializer in the collector now, and… What was that, Martin? Back in October?
when they rolled it out, and it wasn't compatible with the R.
Handwritten protobuf stuff.
**Martin Costello** 25:23 Yeah, that was… something to do with histograms, that issue was. But, We do have some collector integration tests that should help validate that.
But yeah, a good, thing to point out, yeah, that's something we'd need to check as well.
Let's have a quick look at the issues.
But, let's see… So… so the only new issue for Core Repo… is… Someone asked, can we downgrade?
the .NET framework versions of the dependencies?
They haven't replied yet, but I've pointed them to the… Very long issue from last year, when we changed all the versions.
And I also… They pointed out that going backwards would be a breaking change.
So, we'd probably leave it until dawn at 11, and then at that point.
there'd be nothing to go back to, because 8 and 9 would be out of support.
So, we could potentially revisit NET Framework and Standard, using latest… Sometime between now and November.
Well, you've got the new ones, and you just… Use the latest in your old framework version.
Chaos… Nothing new, for Contra… what have we got since last week? So… Raj opened an issue the Gen AI stuff?
Someone else at Microsoft added a comment on that, and I've added a comment, so if anyone else has got anything they'd like to add to that, that's encouraged.
And then two issues I've created today, if anyone has any opinions on them.
while working on the .NET 11 stuff, there's… ASP.NET Core has added support for adding tags to activities.
put on 11, so we can remove some of the ones we do.
And the tests have fleshed out that we and them are behaving differently.
But, based on what the semantic convention says.
I could argue either way is correct, so I don't know which one should be the, like, the blessed version.
But I think it makes sense that they… that the implementations match, so if anyone's got any thoughts on this, on which one.
Is the most correct?
then, either we need to make a change, to match what… NET 11's gonna do, or we should do a PR to .NET, to ASP.NET Core 11 to tweak the behavior so it matches how OTEL currently works.
And then the other one is… I noticed we depend on ASP.NET 2.1 for .NET standard support for ASP.NET Core.
I'm just musing over whether we should bump that forward to 2.3.
or not.
Sorry if anyone's got any feedback on that.
Feel free to stick a comment in the issue.
and… Repairs… I did a PR just now to add support for HTTP query, which got added to the spec last summer, I think, if I remember correctly, but we didn't react… we haven't reacted to it in other support for that. And then I've just got a few minor refactor… refactors.
Otherwise, nothing new since last week.
Is there anything anyone else wants to discuss?
**Matthew Hensley / Grafana Labs** 30:02 Nope, I'm good.
**Martin Costello** 30:07 Cool. Well, let's end it there, then.
Thanks for coming, Vice.
See you next time.
**Julius Koval** 30:14 Thank you. Bye.
