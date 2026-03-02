SIG: GC Project Management (EU)
Date: 2025-07-14
Duration: 31 minutes
Zoom Recording URL: https://zoom.us/rec/share/0y8PNuLfkQW1kxPbmIFLWK_QJ5HqANhHI8alP0TYXQhpfTj5HWfuU817jd8uysmc.KTaPPm7KIg-qwily
============================================================

## Zoom Recording Transcript

**SN Severin Neumann** 01:20 And Robert will come back.
**Robert Pająk** 01:22 Yeah, we'll come back.
Curious about what about the rest.
**SN Severin Neumann** 01:27 Yeah, I don't know. Everybody said they can't. They turn us at half? So yeah, let's give them a minute.
**Robert Pająk** 01:32 You. Probably they're just finishing their own meetings, I guess.
**SN Severin Neumann** 01:35 Probably something like that. Yeah.
**Robert Pająk** 01:39 Will you be driving today.
**SN Severin Neumann** 01:41 All right.
**Robert Pająk** 01:42 We will be driving, sharing your screen today, or you're not able to.
**SN Severin Neumann** 01:47 To what sorry I did.
**Robert Pająk** 01:48 Will you be sharing your screen and driving the meeting.
**SN Severin Neumann** 01:52 Yeah, I mean, I can do that. Yeah, let me actually
depending. Who else joins? But I have.
I can. I think I can do this
I'm using.
That's that link yeah, I can set up by
if anybody else is joining otherwise free. And
oh, there's a little bit to do?
No, no, no, no, that was completely the wrong one.
It's weird, hey, Rossi? Good morning.
Now, I'm sharing the right screen.
Yeah, you can see that.
**Robert Pająk** 03:11 Yes, we can.
**SN Severin Neumann** 03:14 Looks like there's a little bit to do. But yeah, let's see how long it takes us.
Let me do something else.
Okay.
let's talk about, did we? I mean, it does not matter right? We can also go up to bottom.
Missing environment variable for cardinality limit.
yeah, it looks like Robert you you looked into that one already.
How is it with like the the declarative configuration? Is there like a
like? The moment we have something in declarative configuration. Do we get environment variables automatically out of that? Or do we need to say, like, yeah. But this has to
FA variable. Okay, okay.
**Robert Pająk** 04:16 I think the preference is to not add environment variables. So that usual just people rely on configuration. That's what I heard. But I'm not really sure, or maybe
I'm not sure
we can ask the declare we can ask the we can put it to the configuration, seek as well.
**SN Severin Neumann** 04:33 Yeah, it's actually a sick issue, right? So isn't there a board or something like that?
**Robert Pająk** 04:42 They have a project for sure, and I think they have a label as well.
**SN Severin Neumann** 04:46 Yeah, I I think there's declarative configuration stability. I'm not sure if I should put it to that, I mean, it can still throw it out again. It's like, Hey, this is
the weekend.
**Robert Pająk** 04:57 I think we have a label as well. Yeah.
**SN Severin Neumann** 04:59 Yeah, probably bomb
conflicted area configuration. It is already area configuration. I think you did that. But it's in sick issue. Then, right.
**Robert Pająk** 05:09 Yep.
**SN Severin Neumann** 05:14 Should we tag them and say like, Hey, can you take a look something like that?
**Robert Pająk** 05:18 Make me smile.
**SN Severin Neumann** 05:20 Common fake maintainers
or approvers. I always like taking the approvers, probably in that case the same set of people. But
yes, ta-da, like that.
Good done.
I mean.
Okay, open telemetry, protocol exporter, something something.
what's the Pr about?
Clarified?
**Robert Pająk** 06:42 Which could be accepted. It's a good Pr.
There are 2 places where we specify default protocol for Otlp.
**SN Severin Neumann** 06:50 Okay, and.
**Robert Pająk** 06:51 It says in, and the 1 1 lacks information that the default could be different.
**SN Severin Neumann** 06:56 Oh!
**Robert Pająk** 06:57 Then the one very.
**SN Severin Neumann** 07:00 Okay. So I I label it as accepted and like.
and you're kind of the sponsor. But but I think it's trivial, right? I mean, it's like it. It's
yeah, smaller enough or uncontroversial enough to be implemented without a sponsor. Right?
**Robert Pająk** 07:19 That's correct. It's like a bug fix. Almost.
**SN Severin Neumann** 07:23 Something like that, you happy, and I'm head B.
Anything.
Oh, Whoa! Whoa! Mtls something.
Remember those
Robert, you you come prepared right? So you you know all of that already. So so tell us more.
**Robert Pająk** 07:50 Yeah, to be honest.
So each time I see the stuff regarding to Tlp authentication and stuff like that.
I feel that there are already some
SDK environment variables, and I think it supports a lot of the cases. But anything which is more than that should be probably covered by the languages. And this is what the auto is basically about. But in my opinion, the Otap isn't even needed. Basically, the Otlp implementation exported implementation should create their own hooks to make it configurable.
and for other cases I think the Otlp exporter in the collector already probably supports most of the cases
probably to, but that's just my guts feeling, and I have not looked into deeply. But a lot of people which are, you know, they just see they're missing. For example, in Python one kind of configuration they do not. They would like to have, and they just create kind of these proposals.
**SN Severin Neumann** 08:57 I know.
**Robert Pająk** 09:00 You see, they want to have passwords as environmental variables. I do not want to have things like that.
**SN Severin Neumann** 09:05 No, I I never understood why people want to have passwords, and and what but anyways
**Robert Pająk** 09:28 For me. These are
I would just just probably refer it to the auto that this is an advanced scenario that they're not aiming to, you know, basically cover each possible authentication
scheme or type using environment availables especially that these are not.
I would say, default things that people are doing.
This is not a typical use case.
**Juraci Paixão Kröhling** 10:00 So I have an opinion here.
**Robert Pająk** 10:03 Go on!
**Juraci Paixão Kröhling** 10:04 And my opinion is, first, st no new environment variables. We have an embargo on those right. So that's at the very beginning it goes. It is wrong already, because we have an embargo, so we cannot move forward with environment variables. And the second is, I kind of agree with you, Robert, but at the same time, I think Mtls is such a popular
way of doing doing authentication among services, especially for service mesh kind of scenarios.
So I would, I would see I would love to see this feature being added, not as environment variables, though. What I do.
what I would prefer, though, is at least for the collector. We delegate pretty much everything to underlying libraries.
So let's see what the underlying libraries offer in that. In that case, like, if the underlying library for for Tls. For go offers a client key password.
then I think we we should.
We should. I know it is generic. I know it is not for go only.
but I guess my point is, if it is, if the libraries that we use underlying libraries, they use it, we should not prevent our users from.
**Robert Pająk** 11:24 Yes, that's that's exactly what basically, I think a lot of guys in the auto are proposing
just to not just to make it more, you know. Just kind of add this possibility, this feature for the users.
**Juraci Paixão Kröhling** 11:35 Yes.
**Robert Pająk** 11:36 They can accomplish it. But without, you know, introducing new environment, variables and stuff like that.
**Juraci Paixão Kröhling** 11:41 Yeah, yeah, I'll.
**SN Severin Neumann** 11:43 I think also like I mean, sure our our main thing is Otlp. But like.
if I use any other protocol
like it's it's in how you say this in English, like like it's it's or to go to Otlp right? It's weird to say, like, Hey, I configure I mean, I even don't understand why it would do this for every signal independently. I mean, there's probably like
the one situation where someone sends it to like different different backends or something like that. But yeah, I. But but overall, I I think, yeah, I mean, that's something like where we say, like, Hey, we cannot introduce new environment variables. But
is this, then, again, a config thing like, should this be handled by the configuration sake, or
**Juraci Paixão Kröhling** 12:30 I think so.
**SN Severin Neumann** 12:32 I'm like.
**Juraci Paixão Kröhling** 12:33 I would say, I mean, I see both ways I see, for so why is it? Spec? It is back because we have this configured in the spec for all of the other parts of the communication.
Why is it a specific signal? Because, again, we by spec, by the spec, we can have different endpoints for it.
**Robert Pająk** 12:52 Yes.
**Juraci Paixão Kröhling** 12:53 But I think it does belong to the configuration sake.
Let's see configuration.
So I I would prefer action to be taken there.
But it. They say
pack has to evolve as well, so I think a word or 2 extra to this pack would be warranted.
but implementation would be on the on the Sig config.
**Robert Pająk** 13:17 Touch.
**SN Severin Neumann** 13:20 And then I write something like
during triage. We agreed, and this is a topic more than like, alright.
**Robert Pająk** 13:33 At least they should drive it.
**Juraci Paixão Kröhling** 13:35 Yeah.
Yeah. And and they should adapt the current spec that we have to address this like, it doesn't have to be fully implemented here, but this pack has to be adapted with this, and implemented by the C config.
**SN Severin Neumann** 13:48 Okay. Do you want me like to extend my words there a little bit
with what you just said? Or do you want to.
**Juraci Paixão Kröhling** 13:53 Perhaps just a change to the spec might be needed, but the seek config would be the ones to do this change.
**Dan Gomez Blanco** 14:06 That makes sense to me. Yeah.
**SN Severin Neumann** 14:07 But say, config, what was the real person?
**Juraci Paixão Kröhling** 14:12 But the C config would be responsible for for changing this back.
**Dan Gomez Blanco** 14:24 I guess, to your point as well. I think at the moment it's not like you can't. I mean you can do it. But like, if you're on a in a service mesh, you're probably using a proxy for Mtls
stuff right?
I mean, that's that's how people normally do it at the moment.
**Juraci Paixão Kröhling** 14:41 Yeah.
**SN Severin Neumann** 14:45 Okay.
Next one Metheus. Something so I would assume that goes to the Prometheus.
It's a Sig issue and goes to.
They have a board these days? Right?
Yeah, yeah.
**Dan Gomez Blanco** 15:11 Yeah.
**SN Severin Neumann** 15:14 I don't think they have a label.
Good.
No, they don't.
Okay.
cool.
And then there's another one, I think was Memetheus.
Same thing. I guess I just
turn it into a sick issue and put it into.
**Dan Gomez Blanco** 15:46 These 2 are related right.
**SN Severin Neumann** 15:49 Yeah, I I mean, they're both by the same also. So yeah.
**Dan Gomez Blanco** 16:05 Quite timely, I think there was a somewhat from Victoria on the
the spot of was it a spot of El Ricci that was like
trying to get some feedback on what people would expect from
Prometheus or resource attributes in Prometheus.
**SN Severin Neumann** 16:23 Hmm.
okay, there's 1 that came back with, follow up, okay, yeah.
That's like, we, we talked about this a few weeks back. I remember that now.
it's what did we say last time? I think like.
Oh, yeah.
**Juraci Paixão Kröhling** 17:25 I think we talked about that a few weeks ago. Can you.
**SN Severin Neumann** 17:28 Yeah, yeah.
**Juraci Paixão Kröhling** 17:30 Oh, yeah, there you go. You have a comment there on July.
**SN Severin Neumann** 17:33 Yeah, we we tag javascript and pipe maintenance and like, Hey.
take a look into that. And then I remember that you said, like, you have something in the collector, but
**Juraci Paixão Kröhling** 17:45 Yeah, I mean
just to recap what I what I remember, and and Pablo is here. So Pablo can can correct me if I'm wrong, but I think so. We we do have a field in pet data, or even perhaps in the proto.
For goal returning. What is the size of the message, and I think
so. That's 1 way of doing that. But this one here is different. It wants the size of the log record, which is kind of impossible to well, not impossible, but very hard to determine.
Because what
so many levels to unpack here, so at the storage level, we may end up storing resource plus record attributes. So the size that we see on storage is different than the size we see
on in the wire, on the wire? We do we account each log record to include the each resource attributes? Or do we care only about the record like the record itself?
And if it's only the record, then we could in theory have that kind of information with proto objects.
And I see that Pablo left a comment here. So, yeah, yeah.
And I think
at least, during my my Jaeger days. We never. I mean, we hide. We've hidden this one here the size behind a feature flag, because it was
the performance, for that was really bad. But I think I remember somebody from the collector saying that it's not bad nowadays.
But I don't know, Pablo, have you heard about anything on specific on performance for that one.
**Pablo Baeyens** 19:27 Hmm!
I vaguely remember this being expensive to calculate, but.
**Juraci Paixão Kröhling** 19:35 Yeah.
**Pablo Baeyens** 19:38 I don't know more than that.
But yeah, we use something like like this, the protosizer. So we rely on the prototype library for.
**Juraci Paixão Kröhling** 19:48 So I think. I don't think it is language specific. I think it is like, if people want to know what is the records the log record size on the wire.
Then it's a proto matter.
and the size of a proto message is the same, no matter the language that generated that
so in theory it could be calculated.
But why do they want that? I mean, is it worth the the performance impact? And
I think what I mentioned. So some things are coming back to my mind. So one of the things that that we we discussed was, I think it might make sense to give users this possibility, but not been there by default, like people would have to
explicitly flag that. Oh, I want this as a as a metric, but not measuring that by default.
because it might be very expensive.
I just realized that the 2 concerns that I have are actually the 2 questions that they have here like how to accurately calculate the size, and how to efficiently calculate the size.
**SN Severin Neumann** 21:10 You don't apparently.
**Juraci Paixão Kröhling** 21:14 I mean efficiently, perhaps accurately. Certainly you can do that. The proto message is the same.
**SN Severin Neumann** 21:33 So to make it short, what's like? Do we want to like?
Keep it on community feedback and check?
I think my question is more like, how do we drive that conversation like
it looks like there is value in this conversation. But
how do we like move this forward?
Does anyone of you want to answer to that issue? Or if some
guidance here, or do we just want to
ask the author if any of the things
ret so far is helpful, or probably not.
**Juraci Paixão Kröhling** 22:30 I think this belongs to the Tc.
They're clearly different angles.
To take into consideration like people people need. I mean, I could use that myself.
And having a way to do that, independent of the language, or, you know, having that
being part of the Sdks, or whatever would certainly be helpful, but at the same time, what are the trade-offs? I don't know what are the trade-offs for all of the languages out there, so I think it does belong to the Tc.
To seeing.
**SN Severin Neumann** 23:08 To do what so so to.
**Juraci Paixão Kröhling** 23:10 Both to see whether this is something that can be done and should be done.
which are 2 jam questions, right?
I mean, could it be.
**SN Severin Neumann** 23:19 And so we put it into.
So I put it into deciding Tc. Inbox.
**Juraci Paixão Kröhling** 23:28 I think so. Yeah, and leave a comment to the Tc. Saying, we see arguments on both sides like during the triage. We were not. I mean
we don't. We don't know. We don't know. During the 3.
**SN Severin Neumann** 23:41 I mean.
**Juraci Paixão Kröhling** 23:42 Whether we have enough information to make a call on this one, and I think the Tc. Is the one to make the call.
**SN Severin Neumann** 23:50 So during triage we were not able.
Make a decision on that. If this is feasible at all, and if this is desired.
**Juraci Paixão Kröhling** 24:03 So you all agree with that feedback.
Do you all agree with that statement?
Okay.
**SN Severin Neumann** 24:14 Yeah, I, mean, yeah.
**Pablo Baeyens** 24:18 Yep.
**SN Severin Neumann** 24:19 So we need your guidance to.
**Dan Gomez Blanco** 24:23 Yep.
**SN Severin Neumann** 24:24 To move forward or close this issue.
So here you go.
Any concerns, Mr. Burding.
**Robert Pająk** 24:52 Have you added scene box, label.
**SN Severin Neumann** 24:55 Sorry.
**Robert Pająk** 24:56 Have you added the Tc. Inbox label.
**SN Severin Neumann** 24:58 Yeah, I think, so, yeah.
**Robert Pająk** 25:01 I see. Yeah, there it is.
**SN Severin Neumann** 25:02 Yeah, it's 2.
Okay. Oh, I think we are out of issues
and we have 5 min left. Is there anything anybody wants to discuss in those 5 min. I'm not sad if we
can call it a day, but
happy to discuss anything that's taking 5 min.
You're muted.
**Dan Gomez Blanco** 25:29 I'll mention it more than anything. But yeah, you can see now, the new
issues here have that sort of like guidance to for people to thumbs up stuff I think I've seen. I started a sort of like a batch thing to to get some metrics and actually people engaging more with issues or not.
So yeah, I'll leave it there running. But you can basically maybe
maybe something like that we want to do in triage in the future would be like.
Look at the well, I guess in this case it doesn't. In the spec repo. We've already got the.
you know, the workflow. You can. You can. The the most. Yeah, exactly. The most thumbs up
can see like that.
She doesn'.
Yeah.
So maybe that will be another.
Yeah, okay.
some of them would be like, yeah, this has been, this has been going for a long time. 2019. That is.
yeah. That issue is going to go to school soon.
**SN Severin Neumann** 26:32 Yeah, let's keep an eye on that as well.
**Dan Gomez Blanco** 26:34 Yeah.
**SN Severin Neumann** 26:35 Okay. Cool.
**Dan Gomez Blanco** 26:38 Okey dokes.
**SN Severin Neumann** 26:40 I'm here to drop back to you.
**Dan Gomez Blanco** 26:41 Thank you. Bye-bye.
**SN Severin Neumann** 26:42 Bye-bye.
**Pablo Baeyens** 26:43 You.
**Robert Pająk** 26:44 Thank you. Bye.
