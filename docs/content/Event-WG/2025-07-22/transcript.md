SIG: Event WG
Date: 2025-07-22
Duration: 32 minutes
============================================================

## Zoom Recording Transcript

**Robert Pająk** 00:23 Hello!
**Trask Stalnaker** 00:28 A just stepping out for a sec. Be right back.
**Liudmila Molkova** 00:58 Hello! Hi! Folks!
**Robert Pająk** 01:03 Hello! Trust will be in a moment.
**Liudmila Molkova** 01:05 I'll need to drop off in 30 min.
I have a flight later today. And I realized that we need to go to the notary.
and because I'm flying with my daughter, and my husband needs to sign the consent.
And it was fun discovering it last night.
**Robert Pająk** 01:30 I see just a last moment last minute.
**Liudmila Molkova** 01:33 Yeah.
**Robert Pająk** 01:46 Anything that you want me to add to the agenda to ask them. You are
oh, I see trust, is already sharing.
**Trask Stalnaker** 01:55 7, 22, I will. I will look at the
Your Otep updates today. Vanilla.
Yeah. Thanks.
Reception.
**Liudmila Molkova** 02:13 I think I might have forgotten to push something I will check in a second. I'll push because I I've seen something I didn't expect to see during this back call.
But yeah, thank you. Appreciate it.
**Robert Pająk** 02:32 Yeah, from my side. I just rejected my
request changes so that people will not be field reviewing the auto because.
**Trask Stalnaker** 02:43 You rejected your all, your your Pr. The one pr that you rejected, or you blocked
for about the complex attributes.
**Robert Pająk** 02:57 Could you.
**Trask Stalnaker** 02:59 Value, the empty value, pr.
**Robert Pająk** 03:01 Made it. I made it as blocked and created a separate issue, for it.
**Trask Stalnaker** 03:05 Yeah, I I wish that you could block your own Prs.
**Robert Pająk** 03:09 Yourself, yeah.
**Trask Stalnaker** 03:10 Yeah.
**Robert Pająk** 03:10 It will be. You can do it if you if you can, if it will make it easier to make sure that nobody you know merges.
**Trask Stalnaker** 03:17 Merges. Yeah, without putting it to draft, which I mean, it's another.
**Robert Pająk** 03:24 But then people not review it, and I.
**Trask Stalnaker** 03:26 Exactly.
**Robert Pająk** 03:27 This is just about the order how things are being processed. Yeah.
**Trask Stalnaker** 03:31 Yeah.
**Robert Pająk** 03:34 Also, I'm going. I'm going Pto, starting from tomorrow until Tuesday.
so I won't be doing. I won't be able to review your your auto because.
**Liudmila Molkova** 03:49 You will have plenty of time to review it. Don't worry.
**Robert Pająk** 03:52 Maybe I will be able to join the next meeting on Tuesday. It depends, how the drive of the whole family will go returning home.
**Liudmila Molkova** 04:04 You should take a break.
You work too hard.
**Robert Pająk** 04:09 Thank you.
**Trask Stalnaker** 04:10 We're just gonna slow roll. We're on the slow rollout of this Otep. I don't think anything.
It's gonna take some while to build momentum.
**Liudmila Molkova** 04:23 And it's summer.
**Trask Stalnaker** 04:25 Yeah, yeah, I'm gonna be out Thursday, Friday, and then
not next week, but the week after. Oh, yeah.
**Robert Pająk** 04:37 Okay, but let's move slowly, then.
**Trask Stalnaker** 04:48 Let's see, I was going to work on the
log filtering Sam Trace based sampling, but did not. So I will.
Still. Let's see trade log.
**Robert Pająk** 05:15 You can copy from the 1st item below from yeah.
**Trask Stalnaker** 05:22 Yeah.
cool. But I liked. I liked the
discussion last week, and where we landed on that.
Yeah. And then the complex attributes making
progress on that. Thank you, Robert, for kicking that work off.
Are these the 3? Is there? Are these the kind of our 3 work buckets right now, or do we? Is there anything else that
missing.
**Robert Pająk** 06:19 I think it's more than enough.
**Trask Stalnaker** 06:21 Hi, yeah.
But yeah, it helps me to categorize things into those buckets. Cool?
Oh, it don't need to.
**Robert Pająk** 06:38 I think one.
**Trask Stalnaker** 06:39 Week. Let's.
**Robert Pająk** 06:40 I have one question just to, you know, this is something which reminded me to during today's sick meeting.
Do we need anything for the span event deprecation? Or is it mainly this log exception out?
Or is it something more that we need to do and follow up also there.
**Liudmila Molkova** 07:02 Think the migration plan there is to not do anything until events are stabilized.
**Robert Pająk** 07:09 Okay.
**Liudmila Molkova** 07:10 Let's let's check.
So 1st we need to stabilize log based events. And I think it's stable in the Parotta.
**Robert Pająk** 07:31 I think it's tabled already everywhere.
If you check the Api, etcetera.
**Liudmila Molkova** 07:37 Yeah. Then I'm just looking into the for for 3. 0, the Otep, where we have a plan.
**Robert Pająk** 07:43 Yes, yes, yes.
**Liudmila Molkova** 07:44 Deprecation.
**Robert Pająk** 07:44 Brooks.
**Liudmila Molkova** 07:47 And then we're saying, stabilizing, meeting exceptions and events where the logs Api. And this is where we need this setup.
**Robert Pająk** 07:54 Yes, that's what I thought.
Okay, then we're following the plan.
**Liudmila Molkova** 08:00 Mark span record exception as deprecated. And then we mark span and add event as deprecated.
It was a nice setup trosk. It looks so clean.
**Robert Pająk** 08:17 It's not scope gripped.
Yeah, it's nice.
**Liudmila Molkova** 08:20 Yeah.
okay.
**Trask Stalnaker** 08:26 So that's future after
**Robert Pająk** 08:33 Log exception auto mainly, I would say.
**Trask Stalnaker** 08:41 And I mean it is.
I think it's questionable whether events are stable or not. Like, I know. Event, name.
We stabilized.
Does that mean that events are stable.
**Robert Pająk** 08:58 From my perspective, from the data model. And Api Cs, not sure if you need anything from the semantic conventions.
**Liudmila Molkova** 09:09 You can use events without semantic conventions.
**Trask Stalnaker** 09:19 What do we say.
okay.
**Liudmila Molkova** 10:05 So have a link to the semantic conventions that talks about events.
and there is essentially a guidance to put things into attributes.
I would not consider.
I wouldn't consider it a hard blocker for stability that that document is stable.
They can also stabilize the do. Okay, if we're comfortable with it.
**Robert Pająk** 10:36 You mean the semantic conventions guidance regarding the events.
Support.
**Liudmila Molkova** 10:40 Yeah, the generic one, not specific events, but just in general.
Oh, it's stable.
**Trask Stalnaker** 10:55 It is. Look at that! Jack is on it.
**Liudmila Molkova** 10:59 Is it stable as an attribute? There's the not.
**Robert Pająk** 11:06 It doesn't look like it looks like a field.
**Liudmila Molkova** 11:09 I mean it could be then populated as attribute.
**Trask Stalnaker** 11:15 Oh, no no appreciate.
**Robert Pająk** 11:16 3 months ago. So I dubbed, Yeah.
**Liudmila Molkova** 11:18 Yeah.
**Trask Stalnaker** 11:19 We can check
spec and product. Yeah.
yeah, pretty sure.
So why haven't we announced that events are stable?
Should we announce events are stable. Do we feel there's anything?
For some reason I felt like
I had this impression that there were.
There was more guidance that we wanted around using events that that was related to the complex attribute story
and like Java, for example, we're not.
We don't have complex attributes on events yet which
makes it sort of hard to really.
I mean, there's a lot of events that are flattened that you can do flattened.
**Robert Pająk** 12:38 Just one second.
I think it was kind of announced. I think Austin created a blog post around stabilization of events. I'm not sure if it was talking explicitly about stabilization.
and I think it was after it was stabilized
in this pack or or somewhere in Europe, right around the time.
Yep.
**Trask Stalnaker** 13:21 Okay.
**Robert Pająk** 13:24 We can.
Reminds me of one thing.
Should the event name on the data model, I think it was stabilized around April. Basically.
you can get blamed. Probably.
**Trask Stalnaker** 13:41 I was, gonna look at our matrix, do we have event
name? Yes, we do. Look at this. And some people.
Java has it.
**Robert Pająk** 13:55 I think I done it in the stabilization pr.
And I think there was some reason
why Jack didn't want it for Java, and I do not remember why. Maybe it was priorit.
I do not remember right now.
**Trask Stalnaker** 14:15 Okay.
I'll send a Pr and tag him on. It is looking at some stuff.
**Liudmila Molkova** 14:30 So there is no no reason not to stabilize events. It seems so.
**Trask Stalnaker** 14:36 Or it seems that they are stable already.
**Liudmila Molkova** 14:40 So yeah, like, if I'm a user and I use public Api in Java or go
everything I am in stable.
Oh, always true.
**Trask Stalnaker** 14:52 Yeah.
**Liudmila Molkova** 14:58 And now of the improvements we're talking about, it's it's incremental. From from there.
**Trask Stalnaker** 15:04 Right.
**Robert Pająk** 15:09 Yay want a blog post around complex attributes.
together with this Pr that they'll they'll they will be adding more attribute types.
**Liudmila Molkova** 15:21 I think a blog post and complex attributes would be interesting. Yeah, I wonder? Like.
do we have them in go and on Spence.
in in development, or they, is it possible to add a complex attribute and span and go.
**Robert Pająk** 15:43 No, it's not.
**Liudmila Molkova** 15:44 So.
**Robert Pająk** 15:45 We do not want to add anything which is development status to stable packages.
**Liudmila Molkova** 15:50 Right.
So I wonder if we had any language that allowed it in development?
Then it would be cool to announce it then. Otherwise it's just okay. We're announcing the future.
I can maybe work.
**Trask Stalnaker** 16:10 6 months is 6 months.
It's a while.
**Liudmila Molkova** 16:18 Yeah.
**Trask Stalnaker** 16:18 And not, and not they'll fly by.
**Robert Pająk** 16:22 It will.
**Trask Stalnaker** 16:24 There's not much. Yeah. At 1st I was like, really, 6 months from now, instead of 6 months from back, when like. But then I realized, well, like
November and December don't really count. Anyways. So
basically, we'll be releasing. You know, there's not really that much difference between October and January.
**Robert Pająk** 16:44 Like, I think you know, for some companies, you know, which kind of sometimes have plans like on almost half year basis or yearly basis. I think such blog post may have an impact in their planning.
so I don't think it will hurt.
**Liudmila Molkova** 17:04 So I'm thinking
I actually am working on the Pr that adds a complex attribute to span in semantic conventions in genai.
It would be in my best interest to maybe blog about them and maybe work out some way for python to get it in experimental mode
and
showcase it all together like showing a specific example would be very helpful for people to understand that we're not doing something absolutely crazy which they they've thought initially when we just introduced the the plan.
**Robert Pająk** 17:43 Yes, like.
**Trask Stalnaker** 17:45 Yeah.
**Robert Pająk** 17:45 I'll just continue my my thing which I started. It won't be any harm if people who have are having endpoints accepting Otlp will already support complex attributes.
That's why I think it might be good, you know, to put even the blog post. Even we don't do it in specification.
It's already being supported by the collector.
and people can, you know, do can accept it before the 6 months. Also, as Ludom, you are told, people may have experimental apis sdks, etc, which will already send it.
**Liudmila Molkova** 18:19 Yeah, I, I can.
**Robert Pająk** 18:20 We'll have more feedback, and we'll have more feedback before the 6 months. Hopefully.
**Liudmila Molkova** 18:25 Yeah, I can. Do the blog post. I would actually love to 1st merge the the
semantic conventions. Pr, that introduces the precedents.
**Robert Pająk** 18:41 Yes.
**Liudmila Molkova** 18:41 And then show it all together. It might take a few more weeks before it gets in. It's we are making great progress. But it did. We're not at the end of the journey yet.
or I can completely imagine this scenario, and it would have us
less power. I feel less effect posit, more negative effect. The imaginary scenarios like, we've got a lot of feedback that we're doing it for bad
wrong reasons.
**Trask Stalnaker** 19:18 Yeah. Yeah.
I think in python, like in dynamic languages.
It could be released in a stable package potentially under a flag.
I'm gonna look at Java.
**Robert Pająk** 19:42 I think it will be only for Php. Because I think only Phd. Has stable Api.
You mean for other signals. You're right.
**Trask Stalnaker** 19:51 Yeah, yeah.
**Robert Pająk** 19:52 Yeah, you're right?
**Trask Stalnaker** 19:58 And I'm gonna take a look. I wonder if we
I might look at what that would require in Java.
Okay, cool. Cool. Yeah, yeah. I'm glad we're thinking about that.
**Liudmila Molkova** 20:18 Cool. So then, let's set an action item on me to figure out the log.
**Trask Stalnaker** 20:31 Go ahead, anonymous coyote.
**Liudmila Molkova** 20:34 Hi! Am I anonymous coyote.
**Trask Stalnaker** 20:36 It appears.
**Liudmila Molkova** 20:38 Okay.
**Trask Stalnaker** 20:40 And Robert that leaves Robert as the anonymous chinchilla.
**Robert Pająk** 20:46 Yeah.
**Trask Stalnaker** 20:52 It's kind of too bad you can't see what you are, you you your own always.
**Liudmila Molkova** 21:00 Oh, you're a Lemmer.
**Trask Stalnaker** 21:02 Oh, oh, those are cool! Yes.
**Liudmila Molkova** 21:10 Wait. So this are not about events being stable, but about complex attributes. Right.
**Trask Stalnaker** 21:15 Right, right, right.
**Liudmila Molkova** 21:16 Let's put it here.
Do we need to do anything in this pack, or do we? Do we want to write a blog saying events are stable.
**Trask Stalnaker** 21:30 Kind of like. I don't know if like what
I feel like. If I didn't know that like either, there's something fell out of my brain that or like, there must be more widespread confusion
about this topic.
So
yeah, I might be interested in working on that. But let's but maybe, but not immediately.
I'll also be happy for somebody else to do it.
**Robert Pająk** 22:18 So event, event, name was stabilized 11th of April, so exactly one week before Austin's blog post, and it's a pity that we have not called out it explicitly that it also went stable in this blog post.
**Liudmila Molkova** 22:35 There is just one thing that is in the development status
So if I'm posting the link in the chat, if trust you can present.
Oh, sorry. If you search for development in this, Doc, you will find it.
**Robert Pająk** 22:55 The Api.
**Liudmila Molkova** 22:57 Yeah.
**Robert Pająk** 22:59 Yeah, but this, this will go away
in favor of extended attributes. In my opinion, right?
The only reason it is here. It is because this standard attributes. Yeah.
so we will get rid of it.
**Liudmila Molkova** 23:21 Now that we know how we will get rid of it, I think we are more comfortable, saying it's.
**Robert Pająk** 23:29 Yes.
**Liudmila Molkova** 23:29 Rainbow.
**Trask Stalnaker** 23:31 Right. I see what you're saying is that, yeah, we didn't quite have.
We didn't have that piece of the story figured out.
**Robert Pająk** 23:46 Basically the types. If the types that are in the auto will be there, the standard attributes, then you simply refer in the data model of locks directly to the standard attributes, because.
The only types which are missing.
And also this part of the specification is just talking about additional you know, kind of functionality of the SDK. It's not
coupled to, you know. I don't know log records by yourself.
It's kind of also opt in.
**Liudmila Molkova** 24:23 Right.
I mean, when we are ready.
**Robert Pająk** 24:47 The only thing flattened attributes. It's not really true, because for the event in the specification there are already complex attributes for the event record.
The flattened is only in, you know, in Java, for instance, and some languages.
**Trask Stalnaker** 25:05 It depends on the implementation.
**Robert Pająk** 25:29 Yep.
**Trask Stalnaker** 25:41 Yeah, I think that could make kind of a good outline.
**Liudmila Molkova** 25:51 Given the state of our event, things
would we be even comfortable stabilizing the semantic convention document? I think it has very little
on top of the spec. Now.
It's 1 sentence, not that adds information.
Top of the spec that we recommend to use the collection of attributes
the rest has just pierced back.
**Robert Pająk** 26:47 Is it saying somewhere that they should have the same structure also here.
**Liudmila Molkova** 26:54 Bullet point 4.
**Robert Pająk** 26:57 Unique leading with, yes, even structure. Yeah.
**Liudmila Molkova** 26:59 But it's also in the spec language I I.
**Robert Pająk** 27:02 Yes, yes.
**Liudmila Molkova** 27:10 I kind of feel that we do. We need this, Doc.
I mean, we can have once.
**Trask Stalnaker** 27:20 Yeah, should we move this?
I mean, should we move this to the spec.
**Liudmila Molkova** 27:28 Yeah.
**Robert Pająk** 27:33 I think it's the thing is that in the spec, the semantic conventions, if I remember correctly.
our kind of user facing how the people should use it while way the Apis, etc, is more like for the contributor, so we will not put like recommended. You know, the capital case. At least this is how I see it currently.
**Trask Stalnaker** 27:59 Yeah.
**Robert Pająk** 28:01 So there's bigger, I see. Come.
this becomes guidelines. Yeah, guidelines. And you know best practices. In my opinion.
**Liudmila Molkova** 28:08 It's the same kind of policy.
and some other Sam conf non open telemetry can have a different policy, and both will be compliant with spec.
**Robert Pająk** 28:21 The thing which we may consider changing. I'm not sure if severity numbers should be you wanted to. May
may, or should the severity number.
**Liudmila Molkova** 28:35 I mean, we can talk about should, but it's May everywhere, in this background here.
**Robert Pająk** 28:42 In the spec. It's just said that it's optional, like everything is basically optional.
**Liudmila Molkova** 28:50 In the same.
So if we think about this document as a set of semantic conventions, policies for semantic conventions themselves, and
we don't really care about stabilizing this document right?
**Trask Stalnaker** 29:32 Just put it, I think.
It's still something.
I think that's nice to communicate our intent.
**Robert Pająk** 29:45 That's also why I think non-normatively.
But, given this kind of recommendation, should we even call out that
in semantic conventions, that the body may be used.
Is it like a con? Is it contradicting? Because, if I remember correctly, there was some kind of I don't know, maybe not written decision. That body should be left empty and.
**Trask Stalnaker** 30:17 We could say should not contain body here.
**Robert Pająk** 30:19 Yes, yeah, that was what I was thinking to put stress more on using attributes
which will have this, for instance, the same name as the event name. I remember that we are talking about this.
**Liudmila Molkova** 30:34 So then, this document should be reworked into
semantic convention policies. Now it feels like it's the recommendation for everyone.
**Robert Pająk** 30:50 Yes.
**Liudmila Molkova** 30:53 But there are valid cases where we are going to use body like log mapping.
and even in semantic conventions we could define that the specific log record that in our security event from Ocsf.
It might have something that goes into the body, and it would be used in semantic conventions.
**Trask Stalnaker** 31:17 Yeah. I wonder if we, instead of norm it trying to do normatively
cause it is a little weird for all 3 of these things to have the same like.
**Robert Pająk** 31:30 Yes.
**Trask Stalnaker** 31:30 Like events, should generally have attributes. Events should not generally contain body.
and then, like I don't know.
**Liudmila Molkova** 31:40 All right.
**Trask Stalnaker** 31:42 I know, Ledmilla, you need
you needed to leave. We could.
**Liudmila Molkova** 31:46 Yeah.
**Trask Stalnaker** 31:46 Pick this topic up
**Robert Pająk** 31:49 Yes.
**Trask Stalnaker** 31:49 In the future.
**Robert Pająk** 31:50 No rush.
**Liudmila Molkova** 31:52 Yeah, cool. I I have to leave trust I will let you know. On the exception set up.
There are things that I forgot to update, or my AI
over messed up whatever I don't know.
**Trask Stalnaker** 32:07 No rush. I'll yeah. Whenever, whatever day you
tell me, too, I will review it.
**Liudmila Molkova** 32:15 Wonderful. Thank you.
**Trask Stalnaker** 32:16 Yeah.
Alright.
See? Y'all.
**Robert Pająk** 32:19 Conversive travel, bye.
**Liudmila Molkova** 32:21 Thanks. You, too. Enjoy your time off.
**Robert Pająk** 32:24 Bye.
**Liudmila Molkova** 32:25 B.
