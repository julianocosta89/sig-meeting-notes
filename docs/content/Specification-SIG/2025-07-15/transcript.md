SIG: Specification SIG
Date: 2025-07-15
Duration: 38 minutes
============================================================

## Zoom Recording Transcript

**Liudmila Molkova** 01:53 Hello!
**Bob Strecansky** 01:56 Hello!
**Carlos Alberto Cortez** 02:21 Hey? Hey? Let's wait minutes.
We have 11 people, which is not a bad number. But let's wait for more. People. Show up.
**Liudmila Molkova** 02:41 Carlos, do you know whose turn it is to run the meeting.
**Carlos Alberto Cortez** 02:48 Yeah, it's mine.
**Liudmila Molkova** 02:49 Oh, well.
**Carlos Alberto Cortez** 02:51 Jack was supposed to. Yeah, but he's busy this week.
**Liudmila Molkova** 02:55 All right.
**Carlos Alberto Cortez** 03:08 Okay, 1 min.
Okay, let me share my screen.
Here we are. There perfect.
Okay, let's start it don't make sense. So let's go over the items as always, you add any item later on. Please don't forget to put estimated time. That help us track, you know.
and get all the items included, although we have only a few items today. But let's go over them. So 1st one Uk, 5 min.
**Lukasz Gut** 04:13 Alright, hey, everyone! It's me again. So last week we talked a little bit about the measurement processor.
pull request. So there is some new approvals since the last week. But Dprs is still open, and essentially there is like, I think, 2 last bits that perhaps restrain us from from merging it. So unfortunately, I see we don't have Jack today. But there is one comment. I basically put a link directly to to the comment in the in the document.
I think it's it's the other comment, where he has some. If you open the this thing? Yeah, and click on the 1st one here. Yes, this one.
So we had some discussions about additionally specifying that the on measure function also has access not only to the measurement which is vaguely specified today, but also additional resource, scope, and instrument metadata as well.
I essentially think that we probably should leave it. For now, out of the scope for this pull request not to let feature creep in and we are also merging this in development status. Anyway. So it is expected that we may do some breaking changes, but also not to leave this conversation and void. I basically put some some 2 proposals for how it could be addressed later in the future.
so yeah, we don't have Jack today. If any of you have any any comments around this topic. Please tune in in this in this conversation.
And another topic that they wanted to raise today is some concerns from Pallorette. So he actually brought this topic.
**Robert Pająk** 06:11 Okay. Sorry to interrupt you. I think that Jack already approved the Pr. Which I think means that he's fine. Without addressing this.
**Lukasz Gut** 06:20 Okay.
okay, then, perhaps I can resolve the comment. I I thought he would resolve the comment, I, if that's how we, how we do it. Here. I'm fine with that alright and moving on then to pallorette so you, I think, brought this topic up in the go SDK group, specifically right. And there is some concerns about ability to drop or modify measurements. You listed a couple of these concerns here that the use case is narrow. There's some risk to statistical correctness, right? And that this also could technically be solved by attaching additional attributes.
So I wanted so I know. Jack, and I think Joshua had some stronger opinions on this subject. I think the argument was that it would be a miss if we merged this feature without ability to drop or modify measurements.
so my question is whether we should basically cut this scope a little bit at this point, in this Pr or simply merge this regardless.
And this may be the primary point of discussion today.
**Reiley Yang** 07:43 I would block the Pr. If we revert the ability to modify and remove things, it'll be a big mess, and it's inconsistent with other signals.
**Lukasz Gut** 08:06 My my opinion, I didn't put it here, but my opinion is also greatly.
**Robert Pająk** 08:09 Yeah.
**Lukasz Gut** 08:13 Sorry. Go ahead. Robert.
**Robert Pająk** 08:15 You say, Ms, but what are the use cases that we are trying to solve? Is it just a feature that we want to add because we can add it?
Or is there some motivation? If there are some real use cases that we want to do it because we listed some the reasons why we think it's a bad idea.
So basically, we think that metrics are important to have as much basic as but as good statistically correctness as possible, and giving the ability to drop measurements or to add additional calculations. Make may then just be a food gun for the users, and we even haven't heard of a single use case where it will be need actually needed.
**Lukasz Gut** 09:05 I think one of the use case that was discussed in the context of this Pr was unit conversion specifically for for modifying measurements. For example.
**Robert Pająk** 09:19 Yes. So in my comment, I said that basically, if some, why would someone to change a unit? The semantic convention says, What are what are the units? So the user expect to, we expect that user measuring this unit.
And yeah, and basically, that's it.
And we do not make any additional, you know, transformations which can bring additional rounding errors.
**Lukasz Gut** 09:47 Yeah. And the the other use case is, well, actually, duplicating measurements. So processors basically doing some sort of, you know.
I don't know how to how to call it properly.
Oh.
yeah, basically, taking measurements right? And and calculating some tangent value from it. Right? So in order to support that we also probably would need to support, actually modifying the measurement. There is no one without the other, I suppose.
**Robert Pająk** 10:22 And yes, so it's a functionality. But we do not understand the use case. Why would someone want to do it?
**Lukasz Gut** 10:36 I don't have that good arguments for this. This is why I.
**Robert Pająk** 10:40 Yeah, I think.
**Lukasz Gut** 10:41 Jackie.
**Robert Pająk** 10:43 I think there are questions really which right now spoke out that it will be a mess if you have any use cases for it.
I think Ted wants to add something.
**Ted Young** 10:59 Yeah. I just wanted that when it comes to the used cases to also, maybe just throw in to consider SDK versus collector, pipelining kind of thing?
Can we be more supportive of like, more flexibility in the pipeline portion rather than the SDK portion? And would that end up solving the use cases for things like you know.
measurement conversions and stuff like that.
**Reiley Yang** 11:45 Only if you have the collector involved.
there are cases where you just send data directly from the SDK. You don't have another place.
**Ted Young** 11:53 Right? Right? I would say generally. As a design rule, we don't try to require that people run the collector, but we're also not looking at used cases necessarily that are required for running open telemetry.
I'm so that's it's more of a question like, if we're talking one. Do we have enough information to do these handle these use cases in the collector, because if we don't, that's a good reason to put some kind of facility in the SDK, even if it's an S edge case, because we want to support edge cases with our broad user base.
But if we can do it in the collector or in fluent bit, or in, you know, some other kind of piece of middleware.
and it's rare that we think people should be having to do this kind of thing. Maybe it's not worth the cost.
**Tyler Yahn** 12:56 Well, I think I think also to Ted's point, like the idea of all of the measurement manipulation that's been proposed like is better served to be doing that on a completed aggregation of data as well.
Like, there's there's never a use case where you're like.
want to take every 5th measurement and say that instead of it being milliseconds, it's microseconds right like.
if you want to do a conversion of units, it's a conversion of the aggregate, not not a measurement itself.
And so I think that, like there's, I don't know, like I agree, like, I don't see a use case for manipulation of individual measurement values. I definitely think aggregate, or I'm sorry. Attributes are a thing that Roberts pointed out may need to be addressed. But like that's a I think I think a separate question.
**Carlos Alberto Cortez** 13:55 Tristan.
**tristan** 13:58 Yeah with with unit conversion. I'm curious how that would even work, since you create the instrument with a unit. Right? And so then there's a processor on it that changes the unit. Are you creating a new instrument that has a new unit.
**Tyler Yahn** 14:16 Yeah, I agree. I think that's that's a that's only going to cause more confusion than than help at that point. And I think if you did wanted to change the unit you need to, you need to change the instrument itself as you're coming out.
Which is something that is again, like goes to that post-processing idea.
**Reiley Yang** 14:36 So I put the comment, I have a concrete scenario where one attribute might have a lot of values, and we want to group them.
Instead of reporting all the numbers.
**Tyler Yahn** 14:52 I'm sorry. What do you mean by group them.
**Reiley Yang** 14:54 I'll give you example, like, if you have Http status code and people might give you a lot concrete values from a lower level implementation like a device driver might give you something very low level, and you don't want all the possible values. You want to group them so you can control the cardinality.
You can say like, if I see any value that I I don't even know I'll put them as unknown, and for values that I know. I'll only take the 1st digit.
**Tyler Benson** 15:27 Is that grouping the metric metric value, or an attribute value, though.
**Reiley Yang** 15:33 So you re-aggregate the metric by collapsing certain dimension like you have a dimension which has 10 different values, and you worry about if some underlying implementation. Later they change, they give you additional value. You won't put additional value as one single thing, like an active number or something.
So in this way you can control that particular dimension.
**Tyler Yahn** 16:03 Yeah, I I think if there's a lot of different ways you can go about that, though.
I mean, can't you do view selectors to drop attributes. Can't you do post-processing of attributes.
**Reiley Yang** 16:12 Cast.
**Tyler Yahn** 16:13 A total stream like having having a processor here. To look at individual measurements is way more than you need to to address that situation.
**Reiley Yang** 16:23 Yeah, so you can re-aggregate. However, like I, the way I look at environment processor is, it has the capability which allows you to do all these things without having to like invent all the other mechanisms. So like the general design principle. Here I'm following is, I want to have less pieces, and one piece is capable of doing a set of things that are very similar. Instead of you have a piece that can do maybe 50% of the thing. Then for the rest of 50%, you need to use a different tool, and we keep inventing the tool.
**Tyler Yahn** 16:59 Yeah. But I mean, if if you're talking about attribute re aggregation, I think if there's a a unified way that you can address that I think like post processing or somewhere in the views or in advice, like. We already have all these places that.
**Reiley Yang** 17:13 You can.
**Tyler Yahn** 17:14 Right. And so what I think Robert's pointing out here, though, is that like attribute, processor is way. More than that, like it is, it is kind of like coming to a project with a massive sledgehammer where you need something that is just, you know.
a screwdriver like you're you're really building a lot more than just that.
**Ted Young** 17:39 Yeah, I just kind of wanted to say, in the interest of time, we probably won't be able to work through everything here, because it seems like at the heart of this is a kinda needs info. It would be great to do a round of collecting up use cases that we want to solve right, and then evaluating where in our pipeline.
you know, the cost benefit of solving these would be best, and then revisit. Whether this is the right solution. That would be my suggestion at this point.
**Robert Pająk** 18:15 I have one question.
Maybe it's already, I think if we just drop from this Pr the ability to drop and to have this measurements. Would you then not accept such pr. etc, addition to the specification.
because it would still allow to add it in the future? If there is a consensus, because what I seen I think it will be hard, in a in a timely manner, to get a consensus on the measurement on, you know. Basically on the measurement side, I do not see any anything controversial on the attribute, on modifying the attributes during the measurements.
**Lukasz Gut** 19:03 I would also like to point one last bit which is basically what now Robert was saying, but actually flipped.
We are specifically merging this and stop those development so maybe we can allow people to try this out.
And because we maybe don't come up even with use cases. Sometimes this is the case with open source software. Right? You give people the software and they use it for things. You wouldn't imagine that they would use it, and we can always backtrack, because this is why we reserve the right to make breaking changes when we merge in the development status.
I think this is why, primarily it was designed.
So this is my my 2 cents.
We've been on this Pr. For a long time.
**Reiley Yang** 19:52 I agree. So my suggestion is, unless we see by having the ability to modify or remove attribute, it's going to give a huge comp like a huge pain in the implementation, and they give concrete reason why it's going to hurt performance or something. Then I I would be leaning towards having this capability.
**Tyler Yahn** 20:16 Well, I mean, I think it's already been expressed that it's complex to add this into pipelines that already exist, that this is this is replumbing a lot of things just to address this, I think.
yeah, you can make the argument that we should just go ahead with it, because it's easy, because there's already this Pr, but like this isn't actually the end, like, it's actually needs to get implemented. It needs to get evaluated and all that kind of thing like.
I think I think the onus of burden is on the person who wants to add something.
If you want to add something to the specification. You justify it, and I don't think it's been justified as the problem.
**Carlos Alberto Cortez** 20:54 For the sake of time.
I suggest, we focus on the use case scenarios as Ted mentioned. And yeah, we don't have to be super stable here. But yeah, let's work on that. Maybe you guys, you can focus on that Tyler and the rest of the maintenance can provide feedback or anybody, for that matter. Of course.
**Reiley Yang** 21:14 So I have a question, Robert. Do you think this is a blocking issue for the Pr. If it's a blocking issue, then you should block it.
If it's not, then let's merge it, and people can still do the prototype and give feedback, and we can make changes.
**Carlos Alberto Cortez** 21:27 Yeah, that's a good question whether we want those use cases to come before we merge this one, or do we? Do we hold on.
**Ted Young** 21:38 Before. Please let's let's figure out our use cases before we merge things into the space.
**Carlos Alberto Cortez** 21:50 Okay.
I think that would work fine.
**Reiley Yang** 21:56 Yeah, then, then Ted and Robert, maybe one of you should block the Pr and be very explicit what we need to do here.
because we already have approvals. And by the process, if you have multiple approvals from different companies, we can, we can merge it right. Cause I want to be very clear, so nobody will merge it by accident.
**Ted Young** 22:16 That's fair.
**Carlos Alberto Cortez** 22:17 But actually, usually you can leave a comment. You're saying that, you know, yeah. Anyway, usually just remember that we have to resolve all the comments.
**Ted Young** 22:25 I'm I'm happy to honor that request, though, and if you just want someone to make a blocking review to say.
**Reiley Yang** 22:32 We have people from the Tc. Who approved the Pr. Which join the meeting.
Yes, I can do it.
**Carlos Alberto Cortez** 22:40 Okay, thank you so much. Ukash. Yeah, let's keep discussing that. Yeah.
Thank you so much.
Now, for the sake of time, let's move on to other stuff. We don't have any items. But yeah, I think that a lot of the previous item needs specific, very specific. Input so let's move on. Yeah, Robert, you have a few items.
**Robert Pająk** 23:00 Yeah. So basically, just asking for review of this one, we do not need to merge it. But if it's controversial, or if it's, for example, anything I'm not sure. Maybe. If I ask the configuration, seek to look at it. But I think the right area configuration. So someone from the configuration should look at it.
I think we can go forward unless someone has questions or comments.
Nobody press the thumbs up.
**Carlos Alberto Cortez** 23:30 Well, you can go further if I remember correctly, I think that some 6 already have this behavior. Right?
So if that's the case, I think we are good to go.
**Robert Pająk** 23:43 Yes, I gave at least one example. I was not looking to more of them.
**Carlos Alberto Cortez** 23:48 Can we do that? As a last thing? I can do that myself, if that's yeah, I think I will do that myself just in case, but otherwise I think it's fine. Configuration is different. And probably, yeah.
honestly, okay, I will do. Then a follow up later today.
**Robert Pająk** 24:03 Thank you.
**Carlos Alberto Cortez** 24:06 Okay? Next one, yeah, or telescope schema.
**Robert Pająk** 24:11 So this is a follow up from the premier tools compatibility. Basically, those are asked to also kind of include it into semantic conventions. And this Pr has changed very, very much from the previous week, because it only adds the scheme, URL, because there was not a common agreement. If we should. Basically add an autoscope prefix for all of the attributes for non auto ep exporters. It kind of was saying like, it depends of the Otlp exporter. So we kind of I just prefer to reduce the scope of this of this pr, to only add something which is not controversial at all. So only at the auto autoscopes. URL. One thing which I wanted to give a remark that in the proto model the schema URL is higher than the instrumentation scope.
I'm not sure what is the reason? Probably historical reasons. This is my guess, but at least in the specification which Carlos, you recently merged this camera. URL is seen as part of the instrumentation scope.
So yeah, just a remark that there is some kind of there are a little bit, you know, subtle differences in the way the Schema URL is presented in different layers.
Interchange is very small.
**Carlos Alberto Cortez** 25:35 Yeah, maybe David Ashfold can. You know, since he's relatively Prometheus one, he can probably give his heads up.
**David Ashpole** 25:47 Yeah, I'll take a look. This this should be pretty non-controversial, right? This because you've cut out all the attributes related stuff.
**Robert Pająk** 25:57 Yes.
**David Ashpole** 25:59 Okay, but we, we still have to discuss what to do with the attributes.
**Robert Pająk** 26:05 In the Prometheus, especially.
**David Ashpole** 26:08 Yes.
**Carlos Alberto Cortez** 26:14 Well, good.
Yeah. I will have a comment here that, yeah.
we will be waiting for David's feedback.
Okay?
Next one. Then.
**Robert Pająk** 26:26 So this is kind of just a clarification, it goes some approvals. Jack had some good comments. I did my best to address them, but I'm not sure if Jack is online. So I think we can wait on it.
And yeah, that's it. Basically.
**Carlos Alberto Cortez** 26:42 Yeah. Jack is not here this week, I think.
or he will be busy part of the week at least.
So it's up to you if you want to wait.
**Robert Pająk** 26:49 We can wait.
Okay, I cannot merch, anyway. So yeah.
**Carlos Alberto Cortez** 26:54 Okay.
**Trask Stalnaker** 26:55 Jack is on paternity leave. So he's gonna be pretty sporadic for yeah.
**Robert Pająk** 27:05 So I think, Carlos, that if you have some time you can just take a look and use your judgment. If it's better or not. I can always make a follow up here if needed.
**Carlos Alberto Cortez** 27:16 Yeah.
Okay.
Likewise, if anybody here, even if you are not into into logging, please take a look. It'd be great to have this one merged, otherwise it would be standing forever. You know.
**Josh Suereth** 27:31 Yeah, Robert, can you? Can you summarize the the complaint right now, or the concern.
**Robert Pająk** 27:38 The concern right now is that the current the current description regarding the current currency safety.
1st of all, it's misleading isn't telling the truth.
And it's not even giving any suggestions how to solve it. So basically, what I'm changing is to mention that the log record in this decay.
it's not.
is. It is optional to be concurrent, safe, and I'm not sure if it's concurrency in any language that I checked.
and that to be and in order to make sure that users do not have race conditions.
they should make a clone of the record when they are used in any concurrent processing, because this is the only way how to basically avoid race conditions.
because even if someone only reads the record.
if there is a concurrent modification in another thread, it will be still a race condition which was kind of which is something which kind of was not obvious in the previous recommendation.
Also, I wanted to add some normative language here.
**Josh Suereth** 28:48 No, I I meant like from from Jack. What was his concerns with the update.
**Robert Pająk** 28:52 The concern was one simplification.
So you can. We can maybe open the comments, please, if you're able, Carlos.
I'm not sure if it'll be here anymore, because I resolved them.
But they'll be in the conversations. I think there were only 2 comments.
**Carlos Alberto Cortez** 29:16 Hmm.
**Josh Suereth** 29:19 Alright, so I guess the the thing that you're saying is, you think you've resolved Jack's comments? He hasn't had a chance.
**Robert Pająk** 29:24 Exactly.
**Josh Suereth** 29:24 Update those comments because he's out. But you think they're resolved. And you want someone to check over. That's that's all I was trying to confirm is like. If one of us.
**Robert Pająk** 29:31 Yes.
**Josh Suereth** 29:32 Over and help on behalf of Jack.
What should we be looking for? And what was the concern? Okay.
**Robert Pająk** 29:37 I try to. I. As you see, I try to explain as much as possible, even in my eyes here.
so it will be validated by anyone.
**Carlos Alberto Cortez** 29:48 Yeah. Yeah.
I guess that one question that I have is whether it could be useful to get maintainers to look at this, since this clarify something in the actual implementations.
**Robert Pająk** 30:11 It will be worth. If people writing implementing the locks, SDK. Will take a look at it.
It may help, if it may help solving some bugs. If people are using it improperly.
**Carlos Alberto Cortez** 30:28 Okay. By the way, we can actually, after we do the release for this month, we can merge these, and we still will have one month, you know.
**Robert Pająk** 30:36 That's a good idea. Yeah.
**Carlos Alberto Cortez** 30:38 I will leave a comment on that one following Riley's advice, that we will hold on this after we do this month's release.
**Robert Pająk** 30:44 Thank you. Guys.
**Carlos Alberto Cortez** 30:48 Perfect! One more.
**Robert Pająk** 30:55 At.
I was hoping that there will be someone here from the configuration seek. I don't know who is there in the configuration seat, but this is mostly so, basically, I'm trying to help with the stabilization of the stabilization of the declarative conflict, even though I'm not of part of the configuration seek. So I started reviewing the specification. And I tried. Basically, I'm trying to make things more understandable and more consistent. So basically, in one part there is a term which says config operations, and there's also something called config provider, and the config provider and config operations are they kind of do not have nothing in common which makes very confusing when you read it and try to understand it. So basically, I try to propose to just call it SDK operations or operations, because it seems that the intent was that these are the kind of SDK functionality or operations functions, basically that the configurations is supposed to be provided. So yeah, that's so, Jessica, asking for reviews and checking. If if my Pr is really keeping the original intent.
**Carlos Alberto Cortez** 32:08 Yeah, since Jack is not around, we should. Poke, I think. Tyler, yeah, you are also part of the configuration group, and Alex Button.
**Tyler Yahn** 32:19 Yeah, I can. I can take a look.
**Carlos Alberto Cortez** 32:22 Sweet before I forget. Let's just have a small comment. Here.
here we are perfect, just in case to be double sure.
Okay, thank you by the way, I totally forgot to ask whether there's any question. But I guess you're fine on these items from Robert.
Okay, we're fine. Next one trust can lead Mila you want to share, or I can share for you, or you just allow us minute comment on merging this one.
**Trask Stalnaker** 33:02 Yeah, no need to share. Yeah, just thank you. Everyone for your months of listening to us and providing feedback on this Otep. We are going to merge it today.
That's that's all.
**Carlos Alberto Cortez** 33:25 Sweet.
Yeah, I hear no comments. I think you are. We're we're ready to go. So feel free. Actually, we have. Yeah, anyway. Yeah, today.
Okay, that's all. We have anything more in the agenda.
Going twice.
Nothing. Okay, please. Then, yeah. Just take a coffee or consider reviewing some of these items, you know.
Thank you so much. And yeah, stay safe.
See? You soon.
**Trask Stalnaker** 34:06 I.
