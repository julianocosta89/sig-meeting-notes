SIG: Specification SIG
Date: 2025-07-01
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Carlos Alberto Cortez** 02:06 Hey? Hey? We have only 5 people now. I don't know whether there's any holiday somewhere.
but otherwise let's start in one minutes, maybe 2 in case, you know.
yeah, if people show up very soon, we can start.
**tristan** 02:26 I don't think a lot of people are in Canada.
It is Canada day.
**Carlos Alberto Cortez** 02:30 Oh, right, somebody could mention that. Yes, you're right.
We have a pair of items in the agenda in the meantime. So yeah, we can
gonna start in a second.
Okay, let's start 1 min. We also have Robert, who wanted some feedback on
a Pr, so I would like to have him around.
Or maybe it's it is that people are taking summer holidays. Maybe that's the case. I don't know
in the previous years we had that situation, you know.
to.
So let's start. You don't make sense, you see, only 7 people. What? Yeah. U.S.A. independence day week.
Correct.
Okay, let's go over the items maybe we can discuss. We have Robert at least to discuss one item. So the 1st one is about the proto repo a small spec change around unavailable on retry. Info.
This is a minor change, and it has a few reviews, basically is relaxing this one regarding status calls
It's good to go, I think, and tigger and review that.
And after some discussion he's fine with it.
But yeah, for your information, I think we're ready to go to go ahead and merge this one.
If not, please raise your voice today hopefully, you know.
We will not release right away, but still would be great if somebody has anything to say, otherwise we will merge this one.
**Robert Pająk** 04:49 I just have one thing to say. Actually, it's not relaxing. It's basically fixing the specification, basically the mask requirement that didn't have in sense, because even then, later said that other, there were other like possible other possibilities.
**Carlos Alberto Cortez** 05:04 Yeah, correct. He's yeah mentioning that. So technically, it's a yeah, it's it's a big box.
I think that the only reason ticket didn't merge was because there were some conflicts or some checks failing. But if things go ahead, it's it's it's it's good.
So in that case, yeah, we can merge that.
yeah, I don't think we need anybody
else's point of view in this one. So I guess we can merge it. Live.
Oh, okay.
okay, the next one Robert, you want to share I can share for you. Otherwise.
**Robert Pająk** 05:51 You can share. It's just asking for reviews and nothing more. It's just clarification of part of the spec, and nothing more than that. I saw that your your question, Carlos and I asked you. And yeah, that's basically it.
**Carlos Alberto Cortez** 06:06 Yeah, I guess that the question here is whether we need diagrams
review as well or not. What do you think.
**Robert Pająk** 06:18 We can wait. This is, there is no rush.
**Carlos Alberto Cortez** 06:23 Yeah, because, Jack, you know. So approve that which is a good sign. But yeah, yeah.
**Robert Pająk** 06:29 Can you call out here, Tigran, if you can take a look so cute.
**Carlos Alberto Cortez** 06:38 We look up in the call. So yeah, we can probably ping him
and wait up, I would suggest, wait a pair of days.
on the season holidays, and then just merge it. You know.
**Robert Pająk** 06:52 Fine.
**Carlos Alberto Cortez** 06:57 Okay, thank you for that. Next one. Adriel.
**Adriel Perkins** 07:02 Hey? Yeah, just wondering if it's you know, ready to be approved and and merged made a lot of the adjustments people people were asking for there was a couple of comments I chose to just resolve and not make changes for that was the application developer. One versus application owner. Application owner is what is in the glossary of the current open telemetry
space, and so I chose to stay with application owner instead of moving to application developer. And then the other one was.
I'm not sure if it's caused unnecessary confusion, but the whole phrase about the onus is on the application developer for receiving the set context from the SDK and passing it to its own process, spawning mechanisms.
I know that the like.
The libraries today do not spawn processes. But I just the reason I put this there is, so that in the future, when this is a you know.
And now that this is in the spec.
no one's going to be like, well, hey, we can just go ahead and set the processes like, set the context in the process for them and spawn the process. I think the the agreement was, we don't want any of these libraries to do that. It's it's the onus is on the application owner. And so that's why that for that wording is there? But I'm not sure if it caused any confusion, because today no one actually spawns processes in the libraries as far as as far as we can tell.
So anyway. I made all the adjustments that. People have comment on. Thank you for the feedback.
Like to move forward on this, either either getting it approved or making approved emerged, or making another iteration. If if that's what's necessary.
**Carlos Alberto Cortez** 08:45 Yeah. The last questions came from Robert. So, Robert, if you could take a last look, would be great.
**Robert Pająk** 08:52 I will do.
**Carlos Alberto Cortez** 08:55 Thanks.
Thank you so much. Yeah. Otherwise. Yeah. Once Robert has reviewed that. I think we are good to go.
**Adriel Perkins** 09:03 Yeah, there, there were a couple from Ludmilla. Yeah, the other day as well. And so I I did.
**Carlos Alberto Cortez** 09:07 Okay, let me like.
**Adriel Perkins** 09:09 I resolved them, as well.
**Carlos Alberto Cortez** 09:12 For your consideration
**Liudmila Molkova** 09:16 I'll take another look. Thank you.
**Adriel Perkins** 09:19 Cool thanks.
**Carlos Alberto Cortez** 09:20 Yeah, thank you so much for that. And the last one is Mila.
**Liudmila Molkova** 09:25 Yeah, that's a quick announcement. We have some problem with the latest semantic conventions we released yesterday. We are fixing it. It breaks code generation. So you should not be able to release them anyway.
if you were able to. Let's figure out why you have no checks for for this kind of issues, but you shouldn't be able to. Sorry about this for fixing it. We will have fixed hopefully sometime this week.
That's it.
**Carlos Alberto Cortez** 10:00 Perfect.
Thank you for the announcement I hear selling. So I guess we are fine for now.
Okay, that's all. In agenda. Do we have anything else.
If not, I would like to ask the middle and trust. What's the wait. That's not what I wanted. Okay.
what happened to the attempt with the complex types.
**Liudmila Molkova** 10:33 Yeah. Great question. I think trust is not here today.
This laptop
still has some. As far as I can tell, minor comments to address. I will go through them
as soon as they can. We would like to get
a few more approvals. I'll
ping some people who commented, but didn't approve or reject in person, I think
specifically, I think Dan Dialer and Josh Soros had some thoughts, and I know
Jack is is not going to approve.
**Carlos Alberto Cortez** 11:21 Okay, I think I, we have done in the call. So for your consideration. And yeah, we let's ping Josh in case he wants to take a last look.
**Daniel Dyla (Dynatrace)** 11:29 Yeah, I'll look through the
Pr again. There, I think there's been changes since the last time I reviewed it.
But I think my my core problem with it is still
not addressed, which is that it affects
like it. It still allows complex attributes in things that affect
identity and metric identity and things like that. Not I'll look through it again.
**Liudmila Molkova** 12:01 Yeah, it. It allows them. It also asks for the
I believe the hash or deeper quality. But there are some minor changes. Why do you think
it's a problem.
**Daniel Dyla (Dynatrace)** 12:21 I think it's
it just complicates things and makes things more difficult. I mean it to me. The fact that we're adding it and then adding language that discourages it
is a smell that maybe it's
it it to me. It feels like we're adding this feature in order to satisfy a language specific concern around some language ergonomics in Java.
and just wanting to use the same type everywhere, not because anybody actually is asking for that specific feature
and to me it seems like a breaking change in the protocol
to start sending complex attributes, particularly when they affect identity.
said, I will look through the Otip again.
**Jack Berg** 13:24 I think we can leave leave Java out of this if if
you know the. If. We decided that
we wanted to limit the complex attributes to a more narrow scope, and not everything where attributes appear. Java would be fine
if attributes want to, if complex attribute types want to come everywhere.
Java will be fine. We we can. We can evolve our way in either case. So I don't think it's a Java language thing.
**Daniel Dyla (Dynatrace)** 13:58 It was my understanding that that was why
it was being allowed in places like metric attributes and entity. Identifying attributes was because something to do with wanting to reuse the same
hyper interface everywhere, and that it would be a breaking change if you didn't, that that was my understanding. From weeks ago.
I don't know if that's evolved to be different, or if it's just an incorrect understanding.
**Liudmila Molkova** 14:27 And that's 1 of the reasons. But it's not any. Any specific to Java.
Having multiple attribute types has been a problem you need to convert between them. They need to interrupt somehow it creates another sort of smell.
I saw some people, Josh Mcdee unmuted. Did you want to say something.
**jmacdonald** 14:54 Sorry that was a mistake. I have nothing to add.
**Liudmila Molkova** 14:57 Okay.
**Jack Berg** 14:57 Yeah, just to maybe reinforce, maybe, where this sentiment was coming from. So it in Java. And I suspect this will be the case in all languages. If there's sort of a bifurcation between where complex types are used
which kind of domains allow attributes with complex types, and which domains just have a more limited definition. It creates some awkwardness and user confusion. And that is definitely the case. We can find a way to evolve our way around it, but it will, I think, always be a somewhat a source of confusion for users indefinitely. If we were to go down that route
and you know in in some very real ways. It's cleaner if you know.
all usages of attributes share a standard definition.
But that was just one part part about what you were talking about, Daniel. So.
**Daniel Dyla (Dynatrace)** 15:59 Yeah, that. So that was part of it. It was not like I. I don't obviously work on Java. I don't have like Java specific opinions. It just felt like this
was being added in order to satisfy that constraint which felt like a backwards constraint to me.
It just to me. The bigger issue is that it seems like a
breaking change on the protocol. I mean it once you allow it, people are going to use it, and you can say
like we discourage it. But that's not going to happen.
And adding, adding a feature that you discourage on day one just seems, and it.
**Robert Pająk** 16:43 So I just I just want to call out.
**Daniel Dyla (Dynatrace)** 16:46 Yeah, adding a deprecated Api.
**Robert Pająk** 16:49 Daniel. It's not prohibited on the protocol level.
**Daniel Dyla (Dynatrace)** 16:53 I know it's not prohibited on a protocol level.
**Robert Pająk** 16:57 So what do you refer to them?
**Daniel Dyla (Dynatrace)** 16:59 So I mean, it's on the protocol level. It's possible to send
but it's much easier from like
a support like you know, in full transparency. At Dynatrace we drop these, and if if somebody complains.
we say this is specified is not allowed, and we drop it
if it becomes allowed, but discouraged. We're gonna have to start accepting them. And it, you know, it complicates things. And I, you know, I think it's a breaking change. I don't think it's something that we can't work around like. It's not like. It's a problem long term.
and I wouldn't use that, you know, any one vendor or back end as a motivation to to
you know, to to discourage a feature or anything like that. I just don't.
I don't see the motivation for adding them everywhere
and discouraging it on day one. To me that seems like it's something that we're saying. We don't want users to do this.
but we are going to make it possible. Anyways.
**Liudmila Molkova** 18:13 And then, if I remember oh, go ahead.
**Tedsuo** 18:16 I was just gonna ask just for clarity. You're, you know, there's some places where we're in
intentionally extending this right? Like you're aware of that right like we wanna add the.
**Daniel Dyla (Dynatrace)** 18:27 Totally aware of that. Yeah.
**Tedsuo** 18:28 Okay, cool. Just making.
**Daniel Dyla (Dynatrace)** 18:29 Yeah, I know. I know that we want that, that. Yeah, in having it be intentional on on logs and and like, trace attributes and and stuff like that where it's intentional, because there are motivating features. I totally understand that.
Adding it to the other places, because.
**Tedsuo** 18:48 In the name of ergonomics, is.
**Daniel Dyla (Dynatrace)** 18:50 Yeah, it just feels weird to me.
**Tedsuo** 18:53 Yeah, cool.
**Daniel Dyla (Dynatrace)** 18:54 To to say we're gonna add it everywhere because we need it in one place. But please don't
like at the the argument feels weird to me.
**Liudmila Molkova** 19:06 Yeah, I think we have 2 different camps, and one like
we had a version where we.
I think, recommended not to have them on certain signals, and we got a feedback that it's very complicated
if we allow them somewhere, let's allow them everywhere.
My my view on this, that
people who want to put complex attribute on metric.
I don't know what their motivation is, but if they really want it, they will put it
as Jason, anyway.
**Daniel Dyla (Dynatrace)** 19:48 Yeah, but that's fine.
I think
string and the SDK doesn't have to worry about trying to figure out how to like handle equality. And
it complicates the SDK, the identity within the SDK
for a feature that we're telling people not to use.
**Robert Pająk** 20:05 I just want to call out one thing. I think there are more cases when you're putting attributes to the metrics. You need to put more care, like cardinalities, etc. So I think that this is basically an inherent problem of metric, of the identity of the metrics at not itself by the type. So, for instance, if there will be a good cardinality like for for a complex type.
it won't cause such an issue. If, for instance, someone to put a a natural metric attribute like a client IP address, for instance.
it will be more problematic than that. So I think it's just. So it's just discouraging just to make it easier and more efficient. But yeah, I think that this I think that's basically just about, you know, identifying and in metrics to use the most possible efficient attributes.
**Liudmila Molkova** 21:00 Then we'll.
**Robert Pająk** 21:00 So I see.
**Liudmila Molkova** 21:01 The types on this and implementing the the deep equality is not a problem. Really, it's not efficient. Yes, but it's not a problem either.
**Robert Pająk** 21:12 Yes, yes.
**Daniel Dyla (Dynatrace)** 21:15 Yeah, I mean, it's not.
It's not a big problem, but it just seems I I don't know. It's something that I I don't think we
need.
Nobody asked for it.
**Liudmila Molkova** 21:28 Oh, nobody asked for it, but people complained that we had 2 different attribute types and go. It caused problems for people.
And let's say I want to report both span and metric.
so I would populate some attributes that are common across them.
And it will be very difficult if they have different types.
**Tedsuo** 21:59 Yeah. And I think likewise, there's some issues with
extending. If we're saying like, we're going to extend attributes right? And these attributes share a type. It's like a non breaking Api change to extend that type.
But if you now want to go back and say some of these places that we're sharing the same attribute type.
Some of them are going to have one attribute type in other places. They're going to have a different attribute type. That is a breaking change.
So
it's not just a convenience thing, right? Like it's a it's an Api compatibility issue that we have to thread. At least, that's that's my understanding about
in some languages.
**tristan** 22:43 Yeah, if it wasn't supported in metrics, I think a lot would have that problem. But yeah.
are you saying only metrics identity? It's not being asked for, or.
**Daniel Dyla (Dynatrace)** 22:56 And that's that's the the primary concern for me. The issue
is, at least in js, like, we already get a lot of pushback on deployment size and code size, and every line of code that we have to add that we're like.
we know are is almost never going to run
like we're gonna have to add this deep equality check now to our metrics. SDK, that will never be used.
Which, you know, exacerbates that problem for us.
**Liudmila Molkova** 23:30 Yeah, they're right.
It's minor. But otherwise otherwise, what
more types? Right? And they are all set.
**Daniel Dyla (Dynatrace)** 23:39 Yeah, but types compile away completely. They don't exist in the final bundle.
**Tedsuo** 23:47 Are you talking about size, even in Nodejs applications? Or you're talking about people trying to use it in the browser.
**Daniel Dyla (Dynatrace)** 23:55 It's both we get complaints about both.
**Tedsuo** 23:57 Okay? Yeah. Cause I would say, the browser stuff. You know, we're we wanna fork that off
but if it's nodejs as well, I get you.
**Daniel Dyla (Dynatrace)** 24:06 Yeah, we we can talk about this in the browser.
**Tedsuo** 24:11 Yeah.
**Daniel Dyla (Dynatrace)** 24:11 Project Sig as well, but I think Api is unlikely to work.
**Liudmila Molkova** 24:20 It, then it are you currently wearing your Spec sponsor hat or the Javascript Maintainer hat?
And would you be looking into the Javascript specific solution which is totally allowed. You don't have to accept.
Yeah, extended.
**Daniel Dyla (Dynatrace)** 24:41 It's.
**Liudmila Molkova** 24:42 It's everywhere.
**Daniel Dyla (Dynatrace)** 24:43 I guess both. I'm I'm not like I
to A as the Js. Maintainer. I would say it's something that
I don't feel is needed. But it doesn't cause a huge problem.
and as a spec sponsor, I would say the same thing, it just doesn't feel like it's needed, and also doesn't cause a huge problem. I'm not. I'm not intentionally I I didn't mean to be the one blocking this
I just also I feel like approving it is is me saying, I think this is a good idea.
I guess I'm I'm somewhere in between. I'm not blocking.
**Tedsuo** 25:22 Right.
**Daniel Dyla (Dynatrace)** 25:22 And.
**Tedsuo** 25:24 I mean, can we make this optional.
**Daniel Dyla (Dynatrace)** 25:28 I think it already is. There's already wording in there that says
something along those lines like I said, I need to. I think there have been changes since the last time I reviewed it, and I need to look through it. But
I think there's already wording around there around that.
**Tedsuo** 25:45 Because that's that's kind of what I would hope it'd be given that the main. The reason why we're putting this in there is, we're we want to acknowledge that in some languages like we're trying to thread compatibility with adding features. Right? And so for languages. Where? That's a problem, we wanna say, go ahead and do this back ends. Everyone else like, let's sort out.
You know how we deal with this data, but
I think it's totally reasonable at the same time to say, if if it's better for some implementations to to split the types, and that isn't a compatibility issue.
you know.
Then, likewise that should be an acceptable way to implement it.
It's okay for the spec to be a little messy in that regard, I guess, is what I'm saying, right? Like, we're trying to thread.
you know, implementations being clean
if the spec is a little messy. But that makes the implementations cleaner. That's fine.
Anyways, go, have a look and come back.
**Carlos Alberto Cortez** 27:01 Okay, yes,
I'm getting some silence now. I guess that we will continue this offline.
Okay? Perfect.
**Liudmila Molkova** 27:11 Thank you.
**Carlos Alberto Cortez** 27:12 Yeah, hopefully, yeah, hopefully, we make progress. I think this object has received a lot of reviews, but it would be great to merge it whenever it's ready, you know.
Okay, perfect. Yeah. Somebody was taking notes. Sorry about thank you so much for that.
Do we have anything else. We have kind of an hour. We don't have many people. But if you want to discuss something.
feel free to raise your voice now.
Okay, so back to work, I guess. So stay safe and see you very soon.
**Jack Berg** 27:43 Take care, everyone.
**Liudmila Molkova** 27:46 Thank you.
