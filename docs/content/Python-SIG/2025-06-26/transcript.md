SIG: Python SIG
Date: 2025-06-26
Duration: 38 minutes
Zoom Recording URL: https://zoom.us/rec/share/kLMoHigwW4JbwdT1wYQX5fQUXqTcUSRTYcCknO7S8RPTHRTk6OboPlOkCIMtKXqJ.GbhdOEj7F9pSCGJL
============================================================

## Zoom Recording Transcript

**Riccardo Magliocchetti** 01:57 Hello! Welcome, everyone!
We're waiting a few more minutes, and then we'll start.
The meantime, if you have any topics to add to them.
Agenda. Please do.
And while you're at it also, please add yourself as an attendee, also in the notes.
Thank you.
Okay, let me ping to the Maintainers, and then we can start in a moment.
**lechen** 05:36 Hey, guys.
**Riccardo Magliocchetti** 05:39 Hey?
We're waiting for you and Aaron before starting, let me ping Aaron.
Wow.
okay.
okay. So maybe we should start so welcome again. Anyone to this week weekly call.
1st topic is from my room, but I don't see it is so we'll probably just skip it for now and go to the next one.
And this is like from me. Yeah, just wondering what we want to do with the events, duplication and and more work towards stabilization of the log signal.
So I guess the plan is to like once. Review is fine, just merge the the names, and I did the application for events correct.
**lechen** 07:44 Yeah, it's fun.
**Dylan Russell** 07:48 I'll try to resolve the comments on the event. Deprecation. Pr,
**Riccardo Magliocchetti** 07:55 Thank you.
**Dylan Russell** 07:56 Yeah.
**lechen** 07:58 Yeah, I think I was talking with Dylan, too. I think we can address the instrumentations changing over to the new Apis separately in a different release.
**Riccardo Magliocchetti** 08:09 Oh, nice!
**Dylan Russell** 08:10 Yeah.
**lechen** 08:14 I'll be reviewing Hector's Pr today. So.
**Riccardo Magliocchetti** 08:33 Okay? And then next topic, it's from you, Dylan.
**Dylan Russell** 08:38 Yeah, yeah. So it's related to the events deprecation.
so let's say, we get that merged.
And then I'm able to like update all the instrumentations to use, like the logs Api and SDK, instead of the events.
How long do you think we need to wait before we like.
remove the events Api and SDK.
**lechen** 09:13 I don't think we've ever removed components that were deprecated.
However, this was only because we've already released the stable versions of those signals.
As like instrumentation info to instrumentation scope. So we've always just kept them there with a deprecation warning we could do something different for events, seeing as it is. Experimental.
I don't have a strong opinion. It's just that like, if you know.
users are depending on it. It's it's kind of jarring just to have their stuff break, even though it is experimental.
And secondly, it is part of a stable package. So it's just kind of awkward.
Is there a reason why you just you want to just get it removed?
**Dylan Russell** 10:06 Yeah, just just to get rid of it.
**lechen** 10:11 Yeah.
**Dylan Russell** 10:13 No.
**lechen** 10:15 Yeah, I can go either way, I think, removing it, it will will take a little bit of like communication. And Pr, that's pretty much it. So.
**Dylan Russell** 10:27 Okay.
**lechen** 10:29 Yeah, we don't have a a precedence, for like the amount of time to wait for this. So we like, as soon as we get those changes that we can start the conversation for this for what we want to do.
**Dylan Russell** 10:42 Alright. That sounds good.
**Riccardo Magliocchetti** 10:48 Yeah, thank you. Do you know, what's the status of like our events documented or already deprecated on the specifications documentation.
or may never been added. Now, yeah.
**Dylan Russell** 11:10 I didn't see anything about events in in our docs. Is that what you're asking in the.
**Riccardo Magliocchetti** 11:15 I was wondering about the Dev stream.
But yeah, as far as it will already be updated.
Your Devon name, I guess so like there's no way like a person that is not using already events, but like would want to start using them. Yeah, I saw this.
**Dylan Russell** 11:45 Right. Yes, I think like it's been deprecated in the spec.
**Riccardo Magliocchetti** 11:54 Yeah, okay, that's yeah.
Okay, so probably, what should I add to the notes? Like, okay.
**Dylan Russell** 12:13 Maybe like revisit after.
**Riccardo Magliocchetti** 12:16 Okay.
**Dylan Russell** 12:17 Yeah, you could say that, too.
**Riccardo Magliocchetti** 12:21 Cold.
**Dylan Russell** 12:22 But yeah, probably revisit it after I update all the instrumentations. And yeah, that's probably a good time to revisit it.
**Riccardo Magliocchetti** 12:37 Okay, let me add that I have a an out of 3 instrumentation. But you have to update. So like, it should be easy to update. But yeah.
**Dylan Russell** 12:50 Yeah, yeah, I already started updating them.
the only question about that is.
will we do we switch the instrumentations to just set the event, name field in the log.
Instead of this event, name attribute, which is what they said. Now.
or do we like keep the event, name, attribute.
and also set the event name field in the log.
which is like the new field that people are supposed to use.
I think it'll be up to like the instrumentation owners, if such a thing exists.
There's only 4 that are broken.
Oh, and 2 of them are Google. So.
**lechen** 13:53 4 of them that have that are using events right now.
**Dylan Russell** 13:58 Yes, 4 that are using events. Yeah.
**lechen** 14:04 Yeah, I think the what we've done in the past was to, yeah, I think it's the Gen AI stuff. Specifically, yeah, we can have a chat with the Gen. AI. Folks about this, but I think in the past like the best thing to do, and the we've seen the reaction from like users. Is to like. Let them know ahead of time.
I think the deprecation message will help from the events. And then. But we don't want to like release a version that like just immediately breaks them. So perhaps we might have a version that supports both.
That's an idea, but I I feel like the gen AI folks have.
we'll we'll might have some opinions about it, so.
**Dylan Russell** 14:57 Okay.
**lechen** 14:58 Yeah.
**Dylan Russell** 15:01 Yeah, the spec committee was like, or at least in the in the bug where they were like.
we're moving to event name said.
it's okay to just switch over, because events are still kind of like experimental.
But then they also said, like, it's up to each instrumentation to decide what they want to do. So.
Yeah, happy to check with the Gen. AI people.
**lechen** 15:32 Expect people.
**Dylan Russell** 15:34 Bye, yeah.
**Aaron Abbott** 15:37 Hey, Dylan? So the deprecated events. Api. If they keep using that, they'll just continue to get the event name as the attribute. Right event.name, attribute.
**Dylan Russell** 15:47 If they yeah, if we just keep the events. Yeah, if they keep using the events Api and SDK, but I feel like at least the ones in upstream. We should switch over to using the logs. Api and SDK.
**Aaron Abbott** 16:02 Yeah, yeah, I I would be inclined to say the new event name field on the log entry.
We should only use that to set the perdobu field, and if people want the previous behavior they'll they'll stay on the deprecated events. Api, which tells them that what they're doing is deprecated, or they can.
If they want backward compatibility and move to the new Api. They can just set event.name explicitly.
But since this is like a new feature in the logs. Api. Technically, I think we should just implement the new behavior directly.
**Dylan Russell** 16:39 Okay, yeah. I'm good with that.
**lechen** 16:43 Yeah, Aaron, I think before you joined, Dylan was asking whether we would remove the events. Api completely.
So I I guess.
that is an argument for not doing that. So.
**Dylan Russell** 16:57 Finding a place.
**Aaron Abbott** 17:00 Yeah, I mean, we'll remove it at some point right like
**lechen** 17:04 Yeah.
**Dylan Russell** 17:05 Okay. Thank you.
**Aaron Abbott** 17:07 But yeah, I think to start, we can.
we can do this. And then.
yeah, I mean, we, we could just choose a date that we're gonna remove it like, technically, this is all unstable.
So we could choose a date and then put it in the warning messages. But maybe we could. We could discuss that offline. I mean, I think it's all. It's all unstable. We don't, wanna, you know, break people necessarily. And say, Gotcha, it's unstable. But yeah.
**Riccardo Magliocchetti** 17:41 Yeah, question about your whisper, but is it like the removal of events? Is a prerequisite for making the log signal stable.
**Dylan Russell** 17:55 I think they're separate.
**Riccardo Magliocchetti** 17:57 Okay.
**lechen** 18:05 I think I think even having events as part of the Login signal isn't isn't part of the making the logging signal stable right?
**Dylan Russell** 18:22 And there's not much that like. It's literally just one field on the log.
**lechen** 18:27 Yeah, yeah, I'm just saying, yeah, but we'll probably have it in before then. Anyways. So.
**Dylan Russell** 18:33 Yeah.
**Riccardo Magliocchetti** 18:38 Great thanks and any other comments.
Okay, so we can go back to the 1st topic from Aaron.
**Aaron Abbott** 18:57 Sure. Yeah. Sorry I joined a little bit late, and so so I'll just present this. This was a questions from the Gc. That we got, and we kind of went over this and had an open discussion in the Gen. AI Sig, which I found kind of helpful. But you know, most of this is just kind of bookkeeping and forward looking stuff, but I think it would be nice to have the discussion with the community, too. So yeah, there is the specific question from the Jenny saying, but we could just if people are up for it, we could just go through some of this and try to jot down some of our.
Some of the collective thoughts. Would people be up for that.
**lechen** 19:47 Oh, what what is the ask? Exactly. Sorry.
**Aaron Abbott** 19:52 I just want to get people's thoughts on these questions. So what were the Sig's biggest achievements? What are we planning in the upcoming 12 months.
Are there any areas subprojects, that the Gc. Or Tc. Could help.
**lechen** 20:05 Oh, nice. Okay.
**Aaron Abbott** 20:07 Yeah, and that, and then we'll just, you know, drop some notes here, if that's reasonable.
**lechen** 20:18 Cool. Do, do we wanna leave this to to the end after we've gone through other Prs and stuff?
Or are people okay with speaking about now.
Me to think about it for a few minutes.
**Aaron Abbott** 20:36 Okay, that's fine. Maybe I think there's only one other Pr here or a couple of topics from Ricardo. So why don't we start with that and come back.
**Riccardo Magliocchetti** 20:47 Okay.
So yeah, this other one is for me. It is like it was like.
like, I have to. I'm trying to fix the the issue where the grp. 6 porter is not setting a proper user agent.
at least not the one we want, but that is something that start with Hotel, Otlp exporter, python.
And so I create a Vspr that is reusing the Grpc primary agent.
Primary user agent option set on the channel.
And so yeah, so please take a look. I would like to have this.
The next release is possible. But again, no hurry, and also I would like to being able to override this in my distro in the distro maintain.
and so I also worked on with other Pr.
But makes possible to bus exporter parameters from the SDK configuration.
So these are all internal functions, so shouldn't be like, should be fine to change them. But if you have any opinion very more than welcome, and also while I did, I fix it a bit of typing. So at least now the not strict type checking is fine.
And yeah, it's a bit lame. But I have the time checking changes and the other changes in this. Npr, but yeah, I can create another one if it's not fine. But yeah, so please just take a look at this.
**lechen** 22:57 Hey, Ricardo? For the second pr.
Jeremy, didn't you work on something similar for this? Needing to kind of configure something in the telemetry pipeline from the top level.
coming up.
**Jeremy** 23:16 Oh, oh, different, Jim. Okay. I was like, what are you referring to?
**Riccardo Magliocchetti** 23:25 Like me.
I don't.
**Jeremy** 23:26 Were you asking? Were you asking me, or or.
**lechen** 23:29 It was another, a master's.
**Jeremy** 23:31 Oh, okay, I think maybe you're referring to the are you just referring to the I think you're referring to like a Microsoft internal spec. About the protocol of the Otlp exporter.
**lechen** 23:44 No, no, not this, not the the configuring exporter.
Parameters.
From the from the top level.
**Jeremy** 23:53 Oh,
**lechen** 23:54 The the up here.
**Jeremy** 23:58 Let's see.
**lechen** 24:00 Wait. Who's sharing right now?
**Riccardo Magliocchetti** 24:03 I'm shedding.
**lechen** 24:07 Could you switch to the others?
You switch to the other Pr.
**Riccardo Magliocchetti** 24:16 Which one?
**lechen** 24:17 Yeah, yeah.
**Jeremy** 24:22 Yes, okay. There was. Oh, right? Right? I think you can give my sampler sample argument, configuration. Pr. There was a there was a scenario in the past where we couldn't fully configure samplers, because samplers require an argument.
how did we end up doing it? I mean, there's the sampler environment variable.
But I would have to look to see, like what the, what the style of the actual solution was to see if it was similar to this it was. It was a while ago.
**lechen** 24:55 Okay, yeah, this might be related to like like distros, kind of abstracting away the internal components of the pipeline. But we still want to be able to kind of configure them.
Somehow this might apply to our distros as well. So.
**Jeremy** 25:12 Hmm.
**lechen** 25:15 Maybe exporters is the only thing that we need right now. But I can see like in the future, like you want to configure sampler processor stuff like that to given that, it is a smaller change right now, I'm okay with.
I'll I can review this but perhaps we want to think about like, maybe abstracting this, too.
Cool. Yeah.
**Riccardo Magliocchetti** 25:45 Okay. Thank you.
**lechen** 25:49 Yeah, I'll take a look.
**Riccardo Magliocchetti** 25:50 Yeah, I guess that probably like, if we probably retake, look at config when we are going to. If we are going to implement the the Yaml config files, so that will probably require like to take a deeper look at this for me.
**lechen** 26:10 Right.
Oh, Ricardo, I'm curious. For your distro scenario.
Is it the case that you don't want to expose custom like your own custom. Apis.
no, I really just. My issue is that we want to discriminate traffic from upstream and from our own distro.
**Riccardo Magliocchetti** 26:43 And so I would just like to override it. The the Grpc user agent.
also the Htp username. But that's already doable. Yeah.
Oh, got it.
Well, well, no, the H. 2 B. Is not already doable, but I have to think you know I do the same.
Something similar for Http. No other thing of it. Okay.
But yeah. So you know, my scope is really small. Just the user agent.
**lechen** 27:23 I see.
**Aaron Abbott** 27:24 Yeah.
I think I left a comment on there, Ricardo. I don't know on not the past, the config one, but the one on just adding the options it was like right now, the the config kind of mirrors, the Grpc config. So we have whatever like. If somebody says insecure, or if they have the Otlp endpoint passed via environment variable, they can just override the specific subparts of the config that they want via the so like. For example, you added a Jrpc options parameter.
But like we could have an kind of escape hatch which is just to provide a channel directly.
Yeah, I agree. I don't think I don't think the end user would like that. But at the same time you can imagine like, should we go the other way and and just take a user agent option instead of taking a Channel options. I don't know. What do you think.
**Riccardo Magliocchetti** 28:20 Like I don't know. Like everyone.
probably like, avoid to create like an option for every like a parameter for every option. So.
**Aaron Abbott** 28:36 Yep.
**Riccardo Magliocchetti** 28:37 Really.
**Aaron Abbott** 28:39 I guess it's.
**Riccardo Magliocchetti** 28:41 But the way, like, as far as I understood, understand. For the Glpc bindings for the languages have a way to set the user agent properly without using this thing.
And so another option would be to take a look at Grpc, like, I've tried to take a look.
but I haven't seen the the actual code.
but I think that at least for Java, they have a way to to just set the the user agent instead of providing the primary user agent or the secondary user agent.
**Aaron Abbott** 29:22 Right.
**Riccardo Magliocchetti** 29:23 But yeah, I mean, the problem is that the like line 77. There.
**Aaron Abbott** 29:29 That just doesn't do anything, because the way Grvc works is that it? It has to provide this in into the C Api, and then the Grpc dot primary user user agent passes it through to the C Api.
So it's like, I guess an implementation detail a little bit.
I don't know.
**Riccardo Magliocchetti** 29:58 Yeah, like, it would be like, it is me a surprise like figuring out what this thing is not doing anything. But yeah.
at least, not what expected, but.
**Aaron Abbott** 30:11 Yeah, I mean, I don't want to bike shed this like, I think we can add this channel options, and it solves this use case. I think there's a couple of other things you can probably do with it if you want to pass things through. So I think it has some general utility.
**Riccardo Magliocchetti** 30:27 But yeah, like, if.
**Aaron Abbott** 30:29 I guess I'm just trying to say, if distros want to do something crazy.
we could just let them pass the channel directly. So but yeah, let's let's not bike shed this. I think it's fine.
Should we? Should we remove line 77, though? Should we remove that default header? Now that it doesn't do anything.
**Riccardo Magliocchetti** 30:50 Like, I don't know, like I have no idea if someone on the server side is receiving this metadata stuff, because, like this Glpc metadata stuff is documented in Jrpc. Documentation. So we're also like an example of a server. And the client sending this stuff so.
**Aaron Abbott** 31:12 Metadata. Right? Yeah.
But I think this this user agent one in particular, I think it will just always get overwritten by the C. Api. So I think this is pretty much a No. OP. If I remember correctly.
**Riccardo Magliocchetti** 31:27 Okay, like, I don't know.
**Aaron Abbott** 31:32 Yeah, I'll leave a comment on the Pr, that's fine.
**Riccardo Magliocchetti** 31:34 Thanks.
Okay.
So yeah, I sent a media already added some topics.
Maybe I don't know.
**Emídio** 31:55 No, I.
**Riccardo Magliocchetti** 31:55 Technical. Yeah.
**Emídio** 31:56 Just. I'm just adding some notes to help answer the questions.
**Riccardo Magliocchetti** 32:06 Thank you.
Yeah. I think, like, maybe, like everyone else, if you have something to to add, just add to the doc and maybe don't know. We can revise it next week if you collect more stuff.
I don't know.
**Aaron Abbott** 32:37 Okay.
So you're saying you wanna you'd rather do this offline.
**Riccardo Magliocchetti** 32:41 Yeah, like, yes, but like, we have plenty of time, so we can do it right now.
**Aaron Abbott** 32:50 That's okay. Let's come back to it next week. I think there's no rush even if people don't write anything in line, I think people can think about it for a week, and we'll come back to it.
**Riccardo Magliocchetti** 33:00 Yeah.
does that sound good?
Yes, anyone else has any last minute topic to discuss?
Okay? And then thank you, everyone and see you next week.
**Dylan Russell** 33:28 Alright. See? You guys.
