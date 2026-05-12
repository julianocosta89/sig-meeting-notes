SIG: Kotlin SIG
Date: 2026-05-11
Duration: 31 minutes
============================================================

## Zoom Recording Transcript

**Hanson** 00:27 Unmute. Hello?
**Jason Plumb** 00:30 Aye.
**Hanson** 00:34 How's it going?
**Jason Plumb** 00:37 Oh, it's going.
Did we get Jamie today?
**Hanson** 00:45 I think so.
**Jason Plumb** 00:46 Okay.
**Hanson** 00:47 So, bank holiday. We also have a new person that might be… that will… will be joining.
**Jason Plumb** 00:52 Cool.
A new embrace, or from somewhere else?
**Hanson** 00:56 New embrace, per se.
**Jason Plumb** 00:58 Cool. Whoa!
**Hanson** 00:59 Hey, Jamie, did you just record, finish recording, or no?
**Jamie Lynch** 01:04 Not just, but… a webinar the other day, so… taking shots.
**Jason Plumb** 01:10 Coincidentally, I wore my Embrace socks yesterday.
**Hanson** 01:13 Oh, nice!
We have two sets of socks, I think. The ones that are… I don't know if the ones you got are the good ones. There's, like, one that's, like, more like a knitted texture, and I like that. Those ones better.
**Jason Plumb** 01:27 I don't know which ones.
They felt like cheap swag.
**Hanson** 01:32 Yeah, there's, there's the cheap swag-feeling type, then there's, like, the better type.
**Jason Plumb** 01:36 Okay.
Okay.
**Hanson** 01:47 Oh, actually, the other person joining is also Jason.
Whoa.
**Jason Plumb** 01:52 A little bit confusing. Fine.
There we go.
**Jamie Lynch** 01:55 know if Jason was tagging along to this one, or…
**Hanson** 01:58 Yeah, I think he might, pop in, just to… just to hang out.
But I don't know if we have to wait, Let's see if Carlos is coming.
**Jason Plumb** 02:37 Jamie, I have a request for you.
**Jamie Lynch** 02:39 Yup.
**Jason Plumb** 02:40 If you respond to a… code review comment, like, if there's comments, and then you respond to them with a code change, can you please resolve the threads?
**Jamie Lynch** 02:54 Yes, I can do that.
**Jason Plumb** 02:55 Yeah, just because having them open just makes it, like, at a glance, you think it's, like, there's still work going on. At least I do. Maybe that's flawed, but, like, if it's just been taken care of, just resolve it.
Is that cool?
**Jamie Lynch** 03:07 I'm happy to do that. Yeah. I don't think we have that conventional embrace, or maybe I'm skipping that conventional embrace as well, but yeah, I'll try and bear that in mind.
**Jason Plumb** 03:18 Cool. I mean, it's not a requirement. Some repos have that as a requirement, that there can be no open threads before merge, and I'm like, that seems dogmatic, but, yeah, just having them… it just… it feels cleaner to me to have it, like, go away after the push.
**Jamie Lynch** 03:33 Yeah, understood.
**Hanson** 03:34 sometimes I don't close, because I worry that what I did, didn't satisfy the comment. So I'm like, you know, I wait for the commenter to close, but…
**Jason Plumb** 03:43 Oh, okay.
**Hanson** 03:44 So, and also, sometimes I leave comments, like, as, like, an addendum to say, hey, I'm explaining some stuff that I want to put in the code. So, I have two anti-patterns that, you know, affect that, but, you know, I try to do what the repo, conventions are, so…
**Jason Plumb** 04:02 That's cool. I mean, yeah, there's probably not one clear approach. I just… I saw the one about the fuzzing, and I was like, oh, he did these.
**Jamie Lynch** 04:17 Let me share screen while we're waiting.
Bye.
Feel free to add items to your agenda, otherwise… Whoa.
I was gonna say it might be a quick one, but depending on how far we discuss this one, it might not be that quick.
**Hanson** 04:36 Jason isn't coming, he's got, like, another meeting, apparently, that overlaps, so… yeah.
**Jamie Lynch** 04:44 We can just… kind of start chatting about the attributes slash package API, I guess.
So, as a recap, I think those were the two main… Oh, attributes, and kind of, like, baggage slash propagation were the main things.
that need to be done before the logging API could be described as stable.
So… I think Let's see what we pick up.
left off.
So, there was an implementation of any value Which was written in the specification.
And that ended up getting merged.
But as part of looking at the specification, Ed.
Didn't actually specify, but it makes sense to add a… any value.
Well, let me go to the spec, it'll probably be.
Let me turn one.
Let me see if I can find the attributes API for the spec.
Yeah, so this is defining via any value type, so you can have primitives, arrays, etc.
So we've implemented that value type now.
But in the, Tribute Collections.
Where did it say? Yeah, so they're top-level collections of key-value pairs, they're distinct from a… So it's not necessarily that it has to be represented as an any value in the implementation, it's just it has to be one of the types of any value.
If that makes sense.
I guess.
Yeah, so I guess there's a question.
**Jason Plumb** 07:14 I mean, I'm following…
**Jamie Lynch** 07:18 So I guess the question.
**Jason Plumb** 07:19 I'm following what you're saying.
**Jamie Lynch** 07:20 Yeah.
So, I guess the question is, like, what, if anything, needs to change about the current Attributes API?
I'll see if there was anything else on there.
Yeah, so I think that was kind of one of the things we discussed a few weeks ago.
**Jason Plumb** 07:41 Yeah.
**Jamie Lynch** 07:41 Fuck.
And… What other types were there?
Whatever. It's some sort of… Yeah, man, there's a couple of there that we could discuss, potentially.
**Hanson** 07:55 So, for, 4, Carlos has confirmed that what we have is fine, because, the, the behavior, there's, like, a separate,
**Jamie Lynch** 08:08 Yo.
**Hanson** 08:08 clear, so, you know, what we have is… is… I think it was documented or noted in the thing, so I think, that part of it is… confirms, or conforms.
**Jamie Lynch** 08:20 Okay.
That's… good to know.
**Hanson** 08:26 Sorry, that's 5, I mean.
**Jamie Lynch** 08:27 Oh, 5.
**Hanson** 08:28 4 and 5.
**Jamie Lynch** 08:29 4 and 5. Okay.
**Hanson** 08:31 Yep.
**Jason Plumb** 08:35 So one thing that may not still be clear to me is how we might leverage the API we have today to build a complex structure. And by that, I mean… You know, if you had… a list of objects, and those objects contain a list of other objects. Can you do that today in our API? And I don't know that we can.
I think our API…
**Jamie Lynch** 08:58 Yeah.
**Jason Plumb** 08:59 Limited.
**Jamie Lynch** 09:00 I don't think you can do that with attributes.
**Jason Plumb** 09:06 I think you're supposed to be able to these days.
I think they want that to be the case.
**Hanson** 09:14 But is…
**Jamie Lynch** 09:15 Okay.
**Hanson** 09:18 But is any value supported, like, for attributes, in all of the implementations?
**Jason Plumb** 09:28 That I'm not sure of.
**Hanson** 09:32 I feel like as long as we get it to a point where, it's as… I mean, not… maybe not even where Java is, I think we're okay to go forward. I mean, if there's, like.
Specific combinations of complex attributes that are not supported.
I think we can… and API modification is additional, or additive, then I think we can still move forward.
**Jason Plumb** 10:01 I agree, but do we need that to declare stability, I guess?
I don't know the answer.
I'm looking right now to see what Java has. I swear I've looked this up, like, 10 times.
But let me look it up again.
**Hanson** 10:24 So right now, the body could be any value, but an attribute can't be a complex any value?
**Jason Plumb** 10:36 That's what it feels like, at least through the attributes mutator. Go ahead.
**Jamie Lynch** 10:41 Yeah, in the Kotlin API, it's not possible to set an anyvalue type as an attribute value.
So… you could set, like, a Boolean, or a string, or a list of primitives, but… You wouldn't be able to, like, pass through a representation of, like, a complex object.
**Hanson** 11:02 I want to say we looked at this, and then we said that Java didn't support it.
**Jason Plumb** 11:09 I wanna say we looked at it too, but let me see…
**Hanson** 11:14 We can certainly have a task that says to support that, the API and the implementation, but whether it's part of stability is probably…
**Jamie Lynch** 11:24 Yeah, I don't see a… I'm, like, unambiguously worded in this way.
**Jason Plumb** 11:30 I'll show you where it is.
**Hanson** 11:33 The last time I took a look.
**Jason Plumb** 11:34 So the long history was that, like.
The long history was that, like, for a very long time, it was only logs.
that allowed for a complex attribute, and there was a PR, there was a whole movement to try and, like, unify that so that logs weren't special.
And they kind of ended up applying that to sort of all attributes. So any attributes anywhere can contain other attributes. That was kind of the idea. In Java, let me give a link to where I think this is accounted for now.
So…
**Hanson** 12:10 Must be relatively recent within the last.
**Jason Plumb** 12:11 The reason we might… Well, the reason we might not have seen this too… is because you'll notice it says Extended Attribute Key.
**Hanson** 12:22 Which I think…
**Jason Plumb** 12:23 I think they just… that actually might not be… that might not be accurate anymore, but there was this, like, incubating phase where it wasn't on attributes, it was on extended attributes.
So this, this key… that's returned is an attribute key of type value, and value is the any value in Java now.
And so that's probably why we didn't catch this, but you can…
**Jamie Lynch** 12:46 Yeah.
**Jason Plumb** 12:46 You can create a key of that value type, and then you can do a… you can put it… So…
**Jamie Lynch** 12:52 Yeah, that's pretty recent.
**Jason Plumb** 12:54 Attribute type there online, yeah.
**Hanson** 12:56 159, or sorry, 1.59, so which is, like… The latest?
**Jason Plumb** 13:02 Five months ago or something?
**Hanson** 13:04 Oh, fine.
**Jason Plumb** 13:04 No.
**Hanson** 13:05 No.
**Jason Plumb** 13:05 I think it was, like, 5 months ago. Were it 6-something? I don't know.
**Hanson** 13:08 Okay, oh, okay.
**Jason Plumb** 13:09 they can… Making shit up here now. It's 162 is the latest, so there's only 3 versions ago. So recent, yeah.
**Jamie Lynch** 13:18 Cool. So, it feels like this is something we'd want to support then.
So… How would folks feel about…
**Jason Plumb** 13:27 The weird thing is, aside from a… Yeah, aside from a couple of, like, AI use cases, I don't know that anyone… has… Strong use cases for this.
**Hanson** 13:42 I think we could support it, or we certainly.
**Jason Plumb** 13:44 So I think we should… I think we should build it. Sorry.
**Hanson** 13:48 We should… I think…
**Jason Plumb** 13:49 I feel like my VPN is laggy or something. Let me get off this VPN, it's, like, killing me here.
**Hanson** 13:56 I mean, we could enter a task to, you know, do it. Whether or not we want to, like, hold up stability for this, I don't know.
If it's quick, and you can turn it around quickly, then, yeah, sure, why not? But, like… It feels like if something Java's just added, it… it's like a changing requirement. We weren't… this wasn't… like, when we started looking at this, this wasn't there, so… And Jason is still there twice now, so…
**Jason Plumb** 14:26 Oh, shit.
Yeah, that, I swear, I swear sometimes the lag is, like, just enough to be painful, and, you know, I'm exaggerating it now, but it was bad. Hopefully, hopefully not being on VPN makes it better.
**Hanson** 14:45 Cool. So, yeah.
**Jamie Lynch** 14:46 Yeah, sorry, go ahead.
**Hanson** 14:48 Oh, yeah, we can add the task, and let's figure out whether or not this is something that we need to do before stabilization, like, let's see if there's anything else.
**Jason Plumb** 15:04 I think we should add a tracking issue to the milestone, I can do that.
**Hanson** 15:08 Okay, cool.
**Jamie Lynch** 15:11 Thank you.
Okay.
So… Were there any additional points we wanted to discuss on this? Maybe, like, 6, 7, and 8?
Does anyone have thoughts on any of this?
**Hanson** 15:46 I feel like… I feel like these are all fine.
**Jason Plumb** 15:52 Yeah, I don't… I don't have it fresh in my brain what number 6 looks like, but I think 7 is fine.
And… I mean, 8, I think, has the same problem in Java.
Like, the unwieldy-type problems, yeah.
**Jamie Lynch** 16:12 I think we might have… No, we don't have examples of what it actually looks like.
**Hanson** 16:20 Does supporting any value make this more complex?
Like, is there, like, a null , any value that… that… that is, you know… null double versus null string, or… like, does that make that more complicated, or…
**Jamie Lynch** 16:38 I think we do have a null or empty case in any value.
**Hanson** 16:44 Right, that's separate, so, okay. So if you have an…
**Jamie Lynch** 16:50 But yeah, I suppose you would just… Check whether it was any value.
And then you can kind of deal with it.
**Hanson** 17:00 And if we have a… if we have a… if we have a, an attribute, that has a null value, and the key is, a particular type, does that get erased as we push it down, or is that persisted?
**Jamie Lynch** 17:23 I'm not sure.
I thought that any value only had a string key.
And… But I've not looked at it for a while.
**Jason Plumb** 17:37 That sounds right to me.
**Hanson** 17:41 What sounds right? That… the type…
**Jason Plumb** 17:43 Okay. Frankie.
**Hanson** 17:45 Okay.
**Jason Plumb** 17:54 Oof.
**Jamie Lynch** 18:01 Okay, I can just add a note that bows seem to be okay, unless folks have… Concerns about 6, 7, and 8.
**Hanson** 18:12 No, I'll take a look at 8 if I… if I find a minute.
But, so far, yeah, no objections.
**Jamie Lynch** 18:31 Cool.
Yeah, and I guess the other thing to share is that I've managed to do a bit of work on the baggage and propagation implementation over the last couple of weeks, so… I guess that's more for Carlos when he is around, but there's something to review now.
**Jason Plumb** 19:00 I just created a pretty short stub issue there.
**Jamie Lynch** 19:04 Thank you.
**Hanson** 19:16 And has Carlos taken a look at the Propagator's API as well, or the implementation?
**Jamie Lynch** 19:22 Yeah, I think what I'll do is I'll probably ping Holosk after this, just to let him know that it's there, and, then it's on his radar.
**Hanson** 19:32 Cool.
And what other tracking issues do we have, that's still open? Or is this it, basically?
**Jamie Lynch** 19:42 It's basically this, and… I think… Yeah, and this one that Jason has just opened.
**Hanson** 19:56 Cool.
**Jamie Lynch** 19:59 Yeah, so those were the ones for the tributes, and then… be… context.
**Hanson** 20:07 Mmm.
**Jamie Lynch** 20:07 propagation package API. I think one was implementing a beefy propagator.
So… That felt like it was probably… Low priority to me, but it is… Written down in the spec… Specification.
Oops.
The other one was, What we do with the current context, and what the default should look like, which… is… I guess, a little more controversial.
**Hanson** 20:47 default is… yeah.
**Jamie Lynch** 20:49 So we can chat about that. If there's any other topics folks want to talk about, we can also do that.
**Hanson** 20:56 No, let's talk about context.
So, I think right now, there is… the default is global, there is no default context, but you also added… Jimmy added the implementation, I think last week, where we have thread-based contexts so similar to Java, so any SDK user can basically go back to what it was before for Java and say, hey, this is the… the default context is thread-based. We don't want that, or, you know.
That might not be a good idea for default, because, threads and coroutines in Kotlin is just kind of a mess to say that you could depend on The thread local, by default, is a bit, apps could defend… certainly, opt into that, but, like, I think as a general principle, it's… it's, I think, a bridge too far for me, as a default, and something that I'm not a particular fan of, for… for Java, anyway, for the Android use case. So I think having the default to not do that, but having the ability to… for people to do that.
Feels like it's a good compromise.
**Jamie Lynch** 22:07 Yeah, I think… We probably want to… Implement some sort of… Contact storage mechanism for… That's, like, based around coroutines.
And Yeah, I'm not sure how that's gonna work, actually, without… Some sorts of bytecode instrumentation, or… Yeah, or a user interfering their own app, basically.
**Hanson** 22:39 That's the thing, they basically have to thread this through and use it when it's appropriate, so it's… I think as an option, definitely, I think that should be offered. Whether it is a blocking thing for stability, I think is, I don't think it should be. I think what we have is good for stability.
**Jamie Lynch** 23:01 Yeah.
**Jason Plumb** 23:03 I think Java has the same problem in newer versions of Java.
**Hanson** 23:06 Hmm.
**Jason Plumb** 23:07 Because it's not… it's not quite coroutines, but they have, like, these lightweight virtual threads that are not… I think they're not fully accounted for.
in… with the SDK, but probably with instrumentation it is.
I think.
Let's see if I can find an issue.
**Hanson** 23:29 I think my personal philosophy is when in doubt, don't over-assume, especially as a default, V1.
Which is, you know… Which is, I think, what the current proposal is.
When people want something more akin to what they're used to in Java, then they can have it.
It's just that they have to be very full-eyed, you know, this is what I'm opting into.
What is your preference, Jason? Do you have a… do you have, thoughts about this?
**Jason Plumb** 24:09 No, and I mean, I'm not… I'm not… I don't necessarily favor one way or the other. I think right now.
Getting stable on minimal, that… is good enough, I think should be the approach. I think that's what we've been trying to do.
I don't think it has to be… comprehensive, but I think… And it is probably case by case.
Like, I mean, spec is there for a reason, we want to be spec compliant.
But there's always, like, some edge cases that aren't maybe fully accounted for everywhere, and it's… maybe we can round, like, round that corner a little bit later.
But I think it's case by case.
So in the case of context and coroutines, I don't know that… I don't know that I… I don't know what's right in that one.
**Hanson** 24:59 but not defaulting to any specific implementation other than global, as, like, the first V1. What do you think about that?
**Jason Plumb** 25:10 What does the global look like again?
I'm a little out of.
**Jamie Lynch** 25:16 Mr.
**Jason Plumb** 25:17 Honestly. What does, yeah, what does a global context look like?
**Jamie Lynch** 25:21 So it was literally just one… One class, but… or one instantiation that is shared between all threads and all co-routines.
**Jason Plumb** 25:35 So, like, two simultaneous spans that are happening, how do they… How does that get tracked between… threads.
Or I guess in that case, it doesn't?
**Jamie Lynch** 25:48 Oh, it doesn't.
**Hanson** 25:51 I think the idea is that using set current is extremely dangerous in the Android context, that unless you have full control about what's being instrumented, you shouldn't use it. And if you have full control of the instrumentation, you should be able to figure out what can depend on the current and what can't.
**Jason Plumb** 26:09 Yeah.
It sounds like a hard problem, and I think I haven't thought about it enough to be… to speak intelligently about it.
But it sounds like a heart problem.
**Hanson** 26:26 Yeah, I think it's just… there's no good way to figure it out. Like… instrumentation and the app is a lot more coupled in the client… end-user client context than it is for backend, where you have your own, basically, thread to execute on, and you deal with it on your own. You're not sharing resources. And the fact that we are sharing resources, implies that.
you can't know anything. The central arbiter is kind of the app. The app knows potentially everything. And that's only in the code that it, you know, creates. It can also have, like, a third-party library that does its own thing with threading, which can fuck things up real bad.
**Jason Plumb** 27:11 Yep, we see that, I think, or we… I think, historically, we have seen that in some, like, Scala libraries or something that do some weird… Lightweight, you know, resource pooling thing.
**Hanson** 27:26 I think the operative question, like, to my mind is, what is the least harmful default? To basically say, don't use current context, it's not really supported by default, unless you opt into one, and then you could kind of use it. Or opt into the… thread-based default, and say everybody has to opt out. And… and who would actually benefit? Would people… would more people want the, thread-based context, or would people want the no context?
**Jamie Lynch** 28:04 I think maybe it would be good, if one of us kind of summed up Like… All the potential mechanisms on that issue, and the kind of, like, trade-offs involved with like, writing instrumentation with them, and what the defaults of the SDK should be.
I think I'd probably aid discussion for, like, next time, and I'd definitely be interested to get, Carlos' thoughts on this one as well.
**Hanson** 28:35 You could give me an action item to do that. I'll do that, and I'll do the, the required stuff that I said I was gonna do last week, and I haven't… well, I have the PR, but I haven't updated and submitted it.
**Jason Plumb** 28:50 Yeah, it might help me when thinking about this to have a couple of code examples, too, of, like.
Creating a context and needing to share it between units, units being threads and coroutines and… What that might look like.
**Hanson** 29:05 Yep.
**Jamie Lynch** 29:08 Cool.
So, next item, Jason.
**Jason Plumb** 29:14 Yeah, just, have you heard any updates on that, Jamie?
**Jamie Lynch** 29:17 I have not. Okay. Oh, it's… kind of waiting for one of them to get back to us. Do you want to ping, or should I?
**Jason Plumb** 29:28 I can… I can reach back out, because I'm on an email thread that one of my colleagues started, because I think he knows them.
**Jamie Lynch** 29:35 Hmm.
**Jason Plumb** 29:36 I don't know if they're in Poland, or if… I don't know how he knows them, but I guess he knows one of them, and so the contact was made originally with Marcine, but then also this… Vesevo… Vesev… Vesevo Lad?
is roped in, and I guess he's, like, one of the… he's, like, the lead for the Kotlin project.
So I'm like, that's a great person if they want to spend 20% of the time helping us, that would be amazing.
So… Yeah.
**Jamie Lynch** 30:06 Yeah, it would be really cool if we could get contributions for that.
**Jason Plumb** 30:11 Yeah, let me… let me reply to this thread and just see what the next steps are and what we can do to facilitate, like, to help them, you know, take part, because that would be awesome.
**Jamie Lynch** 30:20 Thanks.
**Jason Plumb** 30:21 Yep.
And I will, I think I, I think I have… Oh yeah, you are on the… you're on the email thread, too, so I will just reply to all, and I will keep that thread active. Okay.
**Jamie Lynch** 30:32 We'll spread.
**Jason Plumb** 30:33 I thought you were on that.
Cool.
**Jamie Lynch** 30:39 Cool. Anything else to chat about?
**Jason Plumb** 30:49 Not for me.
**Jamie Lynch** 30:51 Cool. We got, 15 minutes back then.
**Jason Plumb** 30:54 Hooray!
**Jamie Lynch** 30:57 Cool. Thanks, everyone.
**Jason Plumb** 30:58 Thank you all. Yeah, take care.
**Hanson** 30:59 Bye.
