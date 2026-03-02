SIG: Python SIG
Date: 2025-06-19
Duration: 33 minutes
Zoom Recording URL: https://zoom.us/rec/share/gY4h3bdd7B3W08A9A030GyoUxT-E8zKwYcEMESvcmC6MmZTzWpL6isKhUXmKMsub.9ikMrU9OTxLLjg2X
============================================================

## Zoom Recording Transcript

**Riccardo Magliocchetti** 02:21 Hello!
**tammy.baylis** 02:26 Hey! Ricardo.
**ezziomoreira** 02:29 Hello!
**Riccardo Magliocchetti** 02:30 Hey, Tammy, how are you doing.
**tammy.baylis** 02:36 Good thanks. In Canada we don't have today. Off we. We have our day in September instead. So I'm here.
Yeah, how are you.
**Riccardo Magliocchetti** 02:47 I'm good. I'm good starting to getting hot here in Italy, but I'm good.
**tammy.baylis** 02:54 Oh, oh, my goodness, yeah, stay cool.
**Riccardo Magliocchetti** 03:08 Well welcome everyone to this week. Python sig weekly call if you're new to them.
To this call I shared in the chat a link to the notes where we list ourselves as attendees.
and also, if you have any last minute topic, please add it to to the notes.
and we are waiting a few more minutes for more people to join.
**ezziomoreira** 03:39 Okay, I have a question. This is my 1st meeting here I'm
I'm as you. I'm I'm member chain of the localization, the openness documentation for Portuguese.
And I can start to contribute with Python. Okay.
**Riccardo Magliocchetti** 04:10 Like come, and when you should talk with the media.
which is an approver, and also speaking Portuguese.
**ezziomoreira** 04:19 Yeah, yeah, I'm working with you.
**Riccardo Magliocchetti** 04:22 Oh, okay.
**Emídio** 04:24 As you is from my team here.
**ezziomoreira** 04:26 Hey? Hello! Amish!
Yes.
**Riccardo Magliocchetti** 04:29 Oh, so you already know everything, so.
**Emídio** 04:33 I just asked him to present himself.
**Riccardo Magliocchetti** 04:36 Yeah.
**ezziomoreira** 04:36 Yeah.
**Riccardo Magliocchetti** 04:37 Welcome again.
I forgot to share the screen again.
Okay, can you see my screen.
**tammy.baylis** 06:10 Yes.
**ezziomoreira** 06:10 Yep.
**Riccardo Magliocchetti** 06:11 Thank you.
Just kidding.
So yeah, I think we can start.
Okay, I've added the for 2 topics.
The 1st one is about dropping the bottle instrumentation in concrete
bottle is an old client to consume my Ws. Apis. It has been substituted by bottle free since at least 7 years. And
so, yeah, I was wondering if what do you think?
Because I don't think we have users.
And yeah, we can probably just drop some cici time by removing the package.
**Dan Gomez Blanco** 07:05 The thing is, Peter.
A long time as well, since Aws has been telling everyone to move to Moto 3 as well, you know, just like the package itself, but
I don't know how many people are still using portal.
Probably not many.
**lechen** 07:22 Yeah, I'm okay with droppings.
Maybe like, create it. We can create an issue. Give it some baking time. And then
or just remove it from our ci and supported list of instrumentations.
**Riccardo Magliocchetti** 07:42 Okay. Thank you.
**Emídio** 07:43 I also agree.
**Riccardo Magliocchetti** 07:46 Thanks. Let me update the notes.
**lechen** 07:49 Is that for boto and boto Core, I'm assuming.
**Riccardo Magliocchetti** 07:54 Nope, bottle core is the the one, the back end of bottle free. So it's the one we want to keep.
Okay, next one is also from me.
Yeah, I would like to contribute a basic opmp client.
and the Pmp is a protocol created for ending like configuration, remote configuration for open telemetry instrumented application.
And yeah, probably like, the client will be like a new package.
But it will require some integration. I've created a draft Pr
with some notes, and also like an example on how to use the the client.
And so, yeah, like, I'm working on it. Still working on it. I'm writing tests right now.
and so sorry if it's so much and so like the next, I guess next week or the week after I probably have, I can create like a draft. Pr, so you can look, you can take a look at the code.
And yeah, like, I don't expect like any comment right now, but
just like to to introduce the topic. And if you're interested, I left like also link to the specs.
So you can, you know, read about the protocol and stuff like that.
**Dan Gomez Blanco** 09:55 It's good.
**lechen** 09:55 Yeah, Ricardo, we're actually interested in this, so I'll I'll take a look at it and let me know if you want to review
Jefferson.
**Riccardo Magliocchetti** 10:04 Sure. Thank you. Yeah. I know that new relic has a rust client, but is still not still a work in progress.
Yeah, like, let me add, like one thing that makes this different than other things configured by entry points.
is that, like every vendor, we implement its own back end. And it's a configuration. So
like the protocol is standardized.
But the thing you can do
it's not. And so yeah, like, probably like, we won't ever have, like
a generic handler for a client, because, like different vendors, will support the different options.
But maybe once we start like different events of standard implementing things. We can probably share some code.
But yeah, I don't know if done. You ever like different experience.
Yeah.
**Dan Gomez Blanco** 11:12 I have a question like, what would be? I mean, maybe that's too early. But what would be the behavior if you modify certain parts of the SDK, that you know, can affect the telemetry that's being produced. Would it be like like a hot reload of some of that config.
and I'm not sure I'm just thinking about like resource properties, for example, resource attributes.
If you know very changed and you're restart the SDK, and then you're pulling
like metrics, for example, via Prometheus, and then there will be a
counter as a counter reset. I don't know things like that. That. Could that could basically have side effects. If you restart the
the SDK, I guess.
**Riccardo Magliocchetti** 12:00 Yeah. And this like, like one thing I haven't mentioned. But
this is like, really like basic client and agent implement, the Opmp protocol. And in order to implement like
this kind of things like updating SDK configuration, we probably need some rework around the SDK because the moment everything is static, so we can configure it only once.
Yeah. But yeah. So I still haven't looked at introducing like the concept of config, but can change.
But yeah, so this is just like the the 1st
stepping stone in order to have like, at least the protocol.
Yeah, so yeah, I haven't. Still, I haven't yet looked at
make it fixed, dynamic, or stuff like that.
**Dan Gomez Blanco** 12:53 Yeah, I think there was a discussion in the hotel configuration. Well, someone started a discussion on them
even for the I guess the config file is like, what happens? I mean, will it be?
Will it support? What? How do we handle like, you know, hot reloading of SDK config?
So I don't know if there's any sort of
yeah, any guidance at the moment on that or any spec related to
what happens. If you restart the SDK that I know of.
**Riccardo Magliocchetti** 13:30 At the moment. I don't know.
Okay, then let's move to the next topic. That is, from a medium protograph 6.
**Emídio** 13:57 Hey?
We are receiving some
Some ask from users to support Protobuf 6.
And this is quite similar to the situation. We faced with protobuf 5,
we need to generate the profiles, update some dependencies.
and we get in the state that
user is token portable lower than version 6
won't get innovations, updates of the SDK and things like that.
But
The thing is, we have 2 options right now to support that which is one.
relax the dependency on open telemetry portal
to support our support of 6. But we
we are still in a scenario that we can't guarantee that it really works.
And the the second option is to is my Pr, which is
support, only one version of Protobus 6.
And he generated profiles, using that version.
So I would like to have some
opinions about that. If that's the the moment we should switch, because for now and beyond
portable, we guarantee that generated code of your works for ration 6 and 7.
So when they launch, for example, version 7,
we won't need to generate proto files
because they now are guaranteeing rolling window compatibility which doesn't exist right now.
**lechen** 16:18 Yeah, I don't think we have a hard kind of
policy, for, like supported protobuf versions.
But I think we can do something similar to what we have, as like the rolling window for a supported python version as well, I think if we just drop support for Portable 5. There might be
people who complain about this.
And then let's take a look at the initial issue.
portable 5 is expected to end of life next year. Right?
Something like that.
**Emídio** 17:00 Yeah.
**lechen** 17:02 March, 2026 right.
**Emídio** 17:04 Right.
**lechen** 17:06 So. Isn't that a little preemptive to kind of drop support for this.
**Emídio** 17:12 Yeah, that's why I shared the option one which which is just a relaxed opinion.
But
**lechen** 17:21 Yeah. Well, we'll what was the issue with that? Like you're saying like it. It might not be.
It might not work, or something.
**Emídio** 17:30 Yeah. So we don't have a guarantee that
if you relax that dependency, the package will work for version 6.
I'll do the test pass and everything based on our Ci, that's all.
That's was also concerned on when you switch to portable 5.
**lechen** 18:01 Right? So the issue is like since we only have a single, I guess. Source that we can use for profiles. We have to choose between 6 and 5,
and we don't know if 6 can is backwards compatible with everything right.
**Emídio** 18:18 Yes, because the code is well generated with with another version.
**lechen** 18:27 Yeah, perhaps we can. Tried per group of 6.
We don't. We don't have any. We don't have any tests for this right is what I'm hearing.
I'm just.
We won't know like, until we actually release.
**Emídio** 18:48 We can create it can create a new test requirements, file
with those with other versions, new versions, and make a magnetized run in the sky.
**lechen** 19:04 Yeah, it's possibly something we could do. I think this issue is gonna keep coming up. Since we're kind of bound with like one set of files like this is gonna happen for future versions of protocol as well.
**Emídio** 19:15 Yeah.
**Riccardo Magliocchetti** 19:23 Yeah, I just did a quick query on
the downloads of protocol versions. And it it looks like the
6 is already the most used
most use version at the moment. So.
**Emídio** 19:42 Yeah.
**Riccardo Magliocchetti** 19:46 Like, it looks like, yeah.
**Emídio** 19:57 So I think we can do in the short term.
relax it, try, relax the dependency, and later we can
drop the the support of version 5, and support only. Version 6.
**lechen** 20:20 Is there?
Think? I'm okay with that thinking about the long term? Would it be unreasonable to like?
Have, like different versions of the Ltlp exporter.
Oh, sorry like any any an exporter that uses protobuf.
**Emídio** 20:50 Like every time we change. And
a new version of proto, we released a new version of of the Twilipix partner
like a, v, 2 v, 3.
**lechen** 21:06 Yeah, something like that.
**Emídio** 21:09 Yeah, I, think we.
**lechen** 21:10 Like do that?
Oh, sorry. Go ahead. Yeah.
**Emídio** 21:13 Would be possible. But starting from Protobus 6,
we have some guarantee that it works
the generated code. We work in the next versions.
So this put us in a comfortable situation.
**lechen** 21:32 Yeah, so perhaps this is just a 1 time thing.
**Emídio** 21:35 Yeah.
**lechen** 21:38 yeah, I'm I'm I'm open to longer term solutions. And we can see how it works out in the future.
Okay, with the short term solution. For now see, see if it is.
If there's many changes that need to be made, or if it's if protobuf 6 is still backwards, compatible.
at least for our use case so.
**Emídio** 21:58 Okay, okay, thank you for.
**lechen** 22:02 We might need to make our decision. To like just be like, oh, we are upgrading a port above 6, based off of like.
you know, like numerical data.
And then we just need people to upgrade.
**Emídio** 22:18 Yeah, we might need to do that.
Yep.
I think there is already a Pr implementing the short term solution. Take a look and help it. Get me.
**lechen** 22:31 Cool Vincent.
Feel free to update the issue with what we talked about.
**Emídio** 22:37 Yup, sure.
**Riccardo Magliocchetti** 22:48 Okay, I think this was the last topic.
Anyone has a last minute one.
Okay, so thank you. Everyone. And you have 40 min back.
**Dan Gomez Blanco** 23:07 Thank you.
**Riccardo Magliocchetti** 23:09 Thank you.
**ezziomoreira** 23:10 You, too. Bye-bye, guys.
**Riccardo Magliocchetti** 23:12 Bye, bye.
