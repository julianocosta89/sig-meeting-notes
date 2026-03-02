SIG: Specification SIG
Date: 2025-09-09
Duration: 33 minutes
Zoom Recording URL: https://zoom.us/rec/share/Fg43LxDlTgYLuFJ1euX5zqLlBe9Ybml1G0WScxukgHUkJPthsZZQcTxqPCAC4d5c.wzvcHPhkn8fTs89b
============================================================

## Zoom Recording Transcript

**Liudmila Molkova** 01:06 Hi, everyone.
**Bogdan Drutu** 01:10 Dream.
**Carlos Alberto Cortez** 01:11 Eve.
**tsloughter** 01:15 Hello.
**Bogdan Drutu** 02:21 Okay, let me start.
Do we go to the agenda first, or do you want to go for the… Issues.
**Carlos Alberto Cortez** 02:37 I think we go to the agenda these days.
-Oh.
**Bogdan Drutu** 02:41 Perfect.
Trask, you're first.
**Trask Stalnaker** 02:49 Yeah, thanks. I just threw this on, Robert, to… because I think there's some disagreement
Bugged in, oh, am I frozen?
**Ted Young** 03:06 I can share.
**Bogdan Drutu** 03:07 Okay. Oh, you want me to share… er, let me… yeah.
Let me do that.
Soon.
**Trask Stalnaker** 03:19 Robert, I don't know if you want to…
Since it's your PR, kind of describe the, what, why you're proposing this.
Put you on the spot here, is that alright?
**Robert Pająk** 03:36 Yes, it's fine. You can also show the file changes, maybe, and I will say what I do not,
This is the thing which is important, that basically, if someone calls enabled on something, for instance, here, or the logger.
He should get the most up-to-date response.
Because otherwise, people… because currently, the specification says, which is in development, this one is not, this one is stable, so the one in development, which describes the behavior of
For instance, logger config disabled.
Says that, basically, the changes, for the disabled.
do not need to be immediately visible. This means that if someone configures something that should be disabled, then the enabled call may still return enabled, which, in my opinion, is an incorrect behavior.
**Trask Stalnaker** 04:48 Yeah, so, yeah.
**Robert Pająk** 04:49 In my opinion, this is… this is just invalid, with the correct… with the correct stable semantics of the enabled API calls.
**Trask Stalnaker** 05:00 So, the background of, this was added, I believe, at the request of the, of Java folks,
to, Basically allow it, so that we don't need to make that check volatile.
And… It's a… at least in Java, it's…
not uncommon. One of the two major logging frameworks also doesn't do a volatile check on the enabled flag.
And kind of to, the general… it's, when you're updating the… I think the use case… the use case, at least, that we're targeting from the Java side is remote configuration.
And so, when… if you update that enabled flag remotely.
There's not really, like, you're not really…
guaranteeing any synchronicity anyways, it's kind of… Just whenever that… comes in.
**Robert Pająk** 06:12 So, from the… as far as I know, from the Java memory model, it's not volatile, it's just a field.
It can… in theory, it can be never visible.
**Trask Stalnaker** 06:23 In theory.
**Robert Pająk** 06:25 And I saw this even in practice, to be honest.
such things, not for OTL, but basically in different software. When some processors… because it's also depending how, basically, caches work on some CPUs, so I was dealing with things that were never propagated. I think it's…
So, in my opinion, this just promotes incorrect behavior.
And I would say that it's not properly implemented in Java, if there's no volatile and non-synchronization at all.
And that's why I also want the statement to be removed, because in my opinion, it just… Bless us…
Incorrect, like, behavior, which is totally, you know, unpredictable.
**Bogdan Drutu** 07:13 Yeah, I…
I have probably less experience than you, Robert, but I've never seen this in practice. Like, I know the statement in JVM, but…
I've always seen that value.
sometimes for forgetting, but that's less important than the correctness. Josh, you wanna go, Nate?
**Josh Suereth** 07:32 Yeah, I think…
**Robert Pająk** 07:33 I can say a little words, probably you haven't seen it, because it was Intel, and Intel processors normal, or AMD, basically, has additional, refresh. I saw it on Intel Atom, personally.
and AMD process… not AMD, RM processors as well.
**Josh Suereth** 07:52 Yeah, that's what I was gonna say, is it depends… the memory model is very different on certain architectures, and so I'm with Robert that I think it's a problem that we need to believe it when it says it might never be accessed. But also, the other thing is true, Robert, if we were to make this volatile.
it will destroy the performance of anyone using OTEL logging in Java, because you're corrupting your cache.
your CPU cache, every time you log something.
Or you check everything.
**Trask Stalnaker** 08:23 The time you check a debug… is debug enabled?
**Josh Suereth** 08:26 Exactly. So, like, there's, there's a,
There are things we could do so that we only check volatile every n times or something, or things that we could do to make sure eventually you do a volatile read, but if we always do a volatile read.
It is disastrously bad on performance, to the point where it could actually make it so people don't even log.
That's… that would be my fear. Like, so we need to strike a balance between Correct behavior eventually.
If we have, like, dynamic things going on, and, the performance implications of the overhead of OpenTelemetry, right? And I think here, we're solidly in, do A, bad thing happens. Do B, bad thing happens.
there's got to be some middle ground, so I think the way this is worded gives us enough flexibility to make the system better, but I agree with you, if we just never volatile read, then there are certain architectures where that is actually problematic, and we should fix it.
That's where nerdy me would use, like, crazy, you know, language that does native things, but in Java, there are things we could do to make sure we eventually have a volatile read. Like, that's a thing we should encourage and open as a bug. So I'm with you that this is a problem and should be outlined, and maybe needs some more language to discuss.
But I, I, I don't think.
**Robert Pająk** 09:48 It's always in a few.
**Josh Suereth** 09:49 Board to require its development.
**Robert Pająk** 09:51 So let's keep it, maybe, the current statement.
I'll make a note later, why I have removed it, what I'm really, like, closing this PR.
**Bogdan Drutu** 10:04 I would… though, I would clarify a bit, because it says here, should not…
not necessary for implementation to ensure that. I would clarify here that
it eventually should be visible. Like, let's say that
Whatever clarification we put here is that this doesn't…
the statement that is right now, it doesn't guarantee that eventually it will be visible. Let's make sure that it can be implemented to be lazily available, or whatever you call it, lazily visible, or something like that, so that the Java for…
**Trask Stalnaker** 10:44 Eventually confirmed.
**Robert Pająk** 10:45 Eventually visible.
**Bogdan Drutu** 10:47 eventually consistent, or something like that, is very good terminology, but let's make sure we don't guarantee 100% correctness, but we also guarantee that after a period of time, X milliseconds, seconds, whatever it is, we guarantee that will happen, so…
We have to periodically read that thing.
**Robert Pająk** 11:12 Good feedback.
**Bogdan Drutu** 11:14 Does it make sense to everyone to ask Josh? Yeah. Clarify that, at least? Perfect.
**Trask Stalnaker** 11:23 Thank you.
Thanks, Robert.
**Bogdan Drutu** 11:30 Okay.
Hmm, let me… Okay.
Oh, thank you for whoever took the note.
Robert, again?
**Robert Pająk** 11:52 Oh, Jesus, sorry, let me… That's confusing.
**Bogdan Drutu** 11:57 When is the PR you are looking for, let me…
**Robert Pająk** 11:59 I will fix it. Edit.
Okay, I edited, the hyperlink. Yeah, this is this one.
I just wanted to have especially more eyes on it.
And I don't… it doesn't need to be merged. I don't say we need to merge it, we can even wait for more weeks.
I just want to have… As much pos… as much reviews and opinions, if possible.
I created issues for all the languages. I think it would be good to double-check this kind of stuff.
**Bogdan Drutu** 12:39 Okay.
**Robert Pająk** 12:40 One thing which was brought in another PR, which we may just go
Even now, I'm just adding to the agenda. I just really thoroughly refer to one minute before the sick meeting.
So… Is it good?
**Bogdan Drutu** 12:57 I, I think… Based on my previous usage of
the SDKs and APIs and current usage, because I'm using it a lot, Java will be the most problematic one. So I would… I would really want
Though that issue to be closed before anything else. Anyone else? I don't feel they have some strong statement as Java did in their implementation, so…
**Robert Pająk** 13:22 I think JavaScript also has, if I remember correctly.
**Bogdan Drutu** 13:25 I'm not using JavaScript, sorry, for that, but Java, Go, some of these C++, but Java is the most tricky one to get it right here.
**Daniel Dyla (Dynatrace)** 13:39 Robert, can you expand on what you think the JavaScript issue is?
**Robert Pająk** 13:44 if I remember correctly, Danielle, you didn't want to enhance, you didn't want, you were against…
Adding the possibility to use extended attributes for metrics.
for instrumentations Co.
And I do not stream…
**Daniel Dyla (Dynatrace)** 14:03 I was against it not because it couldn't be implemented in JavaScript. That was not a… it was not an implementation concern, it was that I… I thought it was.
**Bogdan Drutu** 14:16 Against the…
**Daniel Dyla (Dynatrace)** 14:16 It doesn't matter why. We've been through this. It's not an implementation problem.
I think the main implementation problems would be that, in JS, we know we have at least two third-party SDKs, and I have no idea how they handle that data, so if the API just starts sending
things that we previously said we would never send, we may break them, and they'll be mad, and I think it will do reputational damage to the project.
I mean, we can handle it in our SDK just fine, but.
**Bogdan Drutu** 14:51 Yeah, can you do… can you, Daniel, I don't know JavaScript, but can you have… some sort of…
wherever you open this API, you open it in a new API, so that, that,
The implementation will be forced Do something, and it's not gonna just break overnight.
**Daniel Dyla (Dynatrace)** 15:17 Yeah, just a new API method, where instead of, like, add attribute, it would be addExtended attribute or something like that, is that what you're asking?
**Bogdan Drutu** 15:24 It's possible. It's obviously not, like, ideal, but it's possible. It's not ideal, but if that is breaking… that is breaking backwards compatibility to extend that, in your opinion, which probably is, then I'm fine with having a different method that does it.
For not breaking compatibility for SDKs.
**Josh Suereth** 15:45 So, I, I wanna, I wanna clarify…
the rules here, by the way. So, it doesn't break backwards compatibility, it breaks forwards compatibility. So, for rules lawyers out there, you could argue this doesn't break backwards compatibility, and you'd be right.
But I agree with everything Daniel's saying. Forwards compatibility is just as important and causes risk to us. So let's… anyway, to be clear, forwards compatible would be, if somebody's using a new thing with an old implementation, does it continue to work?
Whereas backwards.
**Daniel Dyla (Dynatrace)** 16:14 Yes.
**Josh Suereth** 16:15 Yeah, anyway.
**Daniel Dyla (Dynatrace)** 16:16 And we have already had,
run-ins in the past around this. We document, like, we…
you know, we document that explicitly as not a guarantee, so we can do it, it's just that people will be unhappy with us, because… and I can say that with confidence, because we've done it in the past, and they were unhappy, so I already know that that will happen.
**Bogdan Drutu** 16:44 Another option is to reach out to the implementations, Daniel.
Give them… give them a month or two until you open the API.
they can do one or two releases to prepare that, and then… I mean, it's not a perfect solution, but it limits the blast radius of who can get affected by that.
**Daniel Dyla (Dynatrace)** 17:04 Yep, I guess I… all I'm saying is, like, I'm not trying to rehash… these are all the arguments I made on the OTEC, and I… I think it's a reputational damage problem, not a technical problem.
**Bogdan Drutu** 17:16 Okay.
**Daniel Dyla (Dynatrace)** 17:17 And the OTEP was, you know, the community voted, so…
**Bogdan Drutu** 17:21 No, no, no, but again, you can implement with a different method. If you believe that this is very important for the language and the behavior, I'm happy to see a different method for this that is extended attributes, or all attributes, whatever we name it. If you think it's a reasonable solution
Or something, if you want to have insured forward compatibility.
**Daniel Dyla (Dynatrace)** 17:44 Right, okay. Yeah, and fortunately, I think most languages don't have third-party SDK implementations, or at least not many of them are in massive use. I might be wrong about that, but I think we might be unique there.
**Trask Stalnaker** 17:58 I mean, it's a good point to reaching out to them early, or making sure they're aware, because there is… we did build that 6-month clause into the implementing of this, because of similar concerns around backends receiving that kind of data.
**Ted Young** 18:18 You're sharing your Slack, FYI.
**Daniel Dyla (Dynatrace)** 18:25 Oh, Jen, we see your Slack.
**Ted Young** 18:26 Yep, okay.
I… I feel like, just when it comes to alternate implementations, we are clear that
We do expect the implementations to keep up to date with the API. In other words, we don't…
We do not expect new APIs to work with old versions of SDKs.
And that includes alternate implementation, like, just for what it's worth, if those are the people you're concerned about. Yep.
**Daniel Dyla (Dynatrace)** 19:01 true, and we did document it, and all of that is true, and that does not stop people from going on Twitter and saying, OpenTelemetry sucks because they broke our implementation overnight, even if we didn't do it overnight.
**Ted Young** 19:15 Right.
**Daniel Dyla (Dynatrace)** 19:16 I'm just telling you, this is… we had directly had this problem already in the past, and we will… there is no possible way to avoid that conversation. It's going to happen.
**Ted Young** 19:27 But maybe… I guess I'm just kind of agreeing with Bogdan that if we do outreach first, maybe… maybe it's okay.
Because we aren't talking about infinite implementations, right? Like, we're talking about a couple of known implementations.
**Daniel Dyla (Dynatrace)** 19:42 Yeah.
**Liudmila Molkova** 19:44 We should have this conversation every time we add new API then, because every new API is non-forward compatible.
**Bogdan Drutu** 19:52 Right?
**Daniel Dyla (Dynatrace)** 19:53 Well, it's…
**Bogdan Drutu** 19:54 Unless you add a default implementation.
**Liudmila Molkova** 19:57 Y-yeah.
And this is then in hands of those who write the APIs, maybe.
But essentially, this is the problem with any API we have.
**Daniel Dyla (Dynatrace)** 20:08 It would be different if it was adding… if the specification was adding a new method that accepts different parameters, because that's been…
well-established. This is changing the definition of something that was already Spect'd.
**Liudmila Molkova** 20:24 Well, to some extent, it's adding a new way to add something to the attribute collection.
**Daniel Dyla (Dynatrace)** 20:31 I… I don't want to re-litigate the OTEP. I mean, it's… I'm just…
**Ted Young** 20:45 Compatibility's just different in different languages, right? Additive strings aren't a big deal in JavaScript because it's dynamic, but if you mutate the signature of something everyone's using, right, that's… that's a thing that potentially can break.
**Daniel Dyla (Dynatrace)** 21:00 Yep. Yep. And it's, you know, it's part of…
potentially, you know, not just potentially, it's partially my fault, it's the way that the API and SDK communication is done, made this difficult. If I had foreseen this type of change when we designed the API, we may have designed it differently. Unfortunately, that's not what we did. So, we have to deal with what we have, not with what we could have had.
As I said, I don't want to re-litigate the OTEP. It is not a technical problem, but I already know that there are people who have been unhappy in the past who will be unhappy again.
It is what it is.
**Bogdan Drutu** 21:38 Okay, so, Daniel, let's summarize this. I think maybe we should clarify somewhere in the spec that it's okay for some of these changes.
Or clarification in the future to have overload or new methods, depending on whatever is the appropriate terminology and pattern in that language.
And that would give you an escape patch.
**Daniel Dyla (Dynatrace)** 22:04 Yeah, I mean, there is no concept of, like, overloads and stuff like that in JavaScript. That's just…
Yeah, it would be nice to have an escape hatch, but I… yeah, I… I think it's a…
I think it's a social problem, not a technical problem.
Go ahead.
**Ted Young** 22:29 And I think the solution in this case is to maybe try to…
to use this as an opportunity to reach out to them and say, like, how should we communicate? Like, what's the way to communicate to the SDK implementation community for, like, JS OpenCloud?
How should we be telling you guys when things change in the API? Like, how do you want to hear about this? Because it…
you know.
the contract that we have is that things will change in the API, and if you implement the API, you're expected to keep up with it. So how do we…
We're gonna do our best to not do that all the time, but how do we tell you when we… when we change this stuff?
**Daniel Dyla (Dynatrace)** 23:15 Yeah. Okay, and in any case, I think we've talked about this long enough.
It's awesome.
**Robert Pająk** 23:24 Okay.
okay. So, I also opened the second PR, which is kind of an equivalent, where I try…
To add to the, specification.
This new set of… this new, this new, attribute types.
So, basically, I need reviews here, because adding… having this thing specified is harder, especially that I think this kind of new types should be in development status initially.
And one of the things which I wanted at least to briefly say, that the OTEP initially has had this language that Autel API may support, setting
complex attributes on metrics, resources, instrumentation, scope, span, events, etc, that it's not a requirement.
But if I remember correctly, this was basically based on the feedback from you, Daniel. I think Trust added it because we were not convinced that this is necessary, but I'm not sure
if we want to go this way, and add to all the API in metrics, in, I don't know, somewhere when there's instrumentation scope, and this language that, you know, this… these three or two,
types from, from, from the attribute type or any value do not need to be supported, or we want just to go, complex attributes every… everywhere. So, there was a similar conversation here.
We do not… I don't know, Daniel, do you have some opinion right now, or not really, on this one?
**Daniel Dyla (Dynatrace)** 25:14 I… would just say that my opinion is unchanged.
I… Okay.
Yeah.
I…
**Robert Pająk** 25:25 So… I understand.
**Daniel Dyla (Dynatrace)** 25:27 I don't, I don't know. Yeah, my opinion is unchanged. I don't think I want to expand right now.
**Robert Pająk** 25:34 just to double-check that I understand it correctly, so…
So, your opinion is that you would only add support for complex attributes for the places where we see it as kind of necessary, and you see it as valuable, right?
**Daniel Dyla (Dynatrace)** 25:53 Yes, I would only add it where, where the use cases make sense. I would…
Try to avoid adding it.
anywhere where it causes, unnecessary overhead, in this case. Identifying re… identifying entity attributes affect metric identity, which is on the hot path for, you know, to check the, the
The identity of the metric, when you… when you, you know, call add on a counter or whatever, it adds additional
In my view, unnecessary complexity of the hot path.
**Ted Young** 26:35 Is… is this just…
a design exercise that we can leave to the different implementations, because I feel like I've heard from SDK maintainers that they have different priorities. Like, in some languages, people want
to have it consistent and regular everywhere, and that helps with ergonomics and stuff like that. I'm hearing from other maintainers is, like, they would rather be, like, particular about this to help use language.
**Robert Pająk** 27:01 I think that's…
**Trask Stalnaker** 27:03 That's exactly why we included the language here, to be flexible.
**Robert Pająk** 27:08 Yeah, so I need to basically change this PR so it has lost flexibility. So I need to rework this PR to make sure that people can go opt-in or to this functionality in, for example, from matrix if they want to, but they are not required to do so.
Okay.
**Daniel Dyla (Dynatrace)** 27:28 Yeah, I mean, we'll see… we'll see what people in the community say about it, too, because once you can add complex attributes on metrics in…
I don't know, Java or Go or something like that, people are gonna come to JS and say, why can't I do that here?
I think eventually, the experience will have to be consistent everywhere.
Yeah, I don't know. That's… that's why I was arguing… On the OTEM.
**Robert Pająk** 27:59 Goodness.
**Daniel Dyla (Dynatrace)** 27:59 I think now that we're past that, I think…
**Robert Pająk** 28:02 That's why I said it here, that,
if they're acceptable, you know, for example, on OTLP, then maybe you should add it to the APIs anyway, even that… even if there would be consequences, you know, performance consequences.
Yeah.
**Daniel Dyla (Dynatrace)** 28:18 Yeah, that's our current plan right now, is to add the implementation, and then put in the documentation, like, we don't recommend this, it may cause,
Yeah.
**Robert Pająk** 28:29 all the routes.
Okay, so… I see.
**Daniel Dyla (Dynatrace)** 28:35 So, we'll probably implement it just to avoid having the argument with our users when they come to us, if they come to us. But we'll document it as, like, you know, we don't recommend this.
**Liudmila Molkova** 28:48 Actually, The document, it does not recommend it.
**Ted Young** 28:52 According to ATAP.
It's helpful that these are actions users can technically take, but don't make any sense. So it's not like they would reason themselves into these being, like.
**Robert Pająk** 29:04 Yes. Great.
**Ted Young** 29:05 with expected outcomes that they're not getting, right? It's just like, you could technically do this weird thing, and then we drop the data on the floor, because that was weird.
**Daniel Dyla (Dynatrace)** 29:17 Yeah, I mean… We've had in, like.
In JavaScript, because you can do anything Like, we've had…
Issues where people put, like,
You know, classes with circular references, places where they shouldn't, like…
It would amaze you what people do, and it's not tech… it's not possible for us to guard against it at, like, a compiler level the way you would in a reasonable language.
**Ted Young** 29:50 Right.
I guess that's my point, right? Is, like, it's not… it's not actually, like, a new problem, especially for dynamically typed languages, where people will…
We'll stuff objects into anything and expect it to get converted into something useful, and sometimes that happens, but sometimes that's not a good idea.
So it's not… it's not like we've introduced a new class of problems to the world by having…
**Daniel Dyla (Dynatrace)** 30:19 Yeah, I think I made my arguments on the OTEP. I can accept that the community went the other way, and now we're in the implementation phase, and I'll implement what the community decided.
**Robert Pająk** 30:39 Daniel, I will try to… I will make a note here. Feel free to edit it later, if you… if I have any… if I just, you know, say something wrong, improper, or anything.
Is this right for you, Daniel?
**Daniel Dyla (Dynatrace)** 30:54 Yep, that's fine.
**Robert Pająk** 30:56 Okay.
Thank you, I'll stop sharing.
**Bogdan Drutu** 31:03 Okay, I do believe that that was our last.
Topic, or no?
We just…
**Trask Stalnaker** 31:12 Sometimes topics magically appear mid-meeting.
**Bogdan Drutu** 31:16 I'm lost a bit where we are right now.
No.
**Robert Pająk** 31:21 Yep.
**Bogdan Drutu** 31:23 I think we're… oh, okay.
**Carlos Alberto Cortez** 31:24 Here we are.
**Bogdan Drutu** 31:27 confusing.
Okay, any other things?
To discuss the Dean?
Then, let's call it. Thanks, everyone.
**Trask Stalnaker** 31:46 Bye.
**Carlos Alberto Cortez** 31:46 field.
**Josh Suereth** 31:48 Thanks, Bogdan.
