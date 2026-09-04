SIG: Android SIG
Date: 2026-09-03
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Vishwan aranha** 00:20 Jason.
**Jason Plumb** 00:24 Hey, good morning, Vishwan. How are you?
**Vishwan aranha** 00:26 Morning, pretty good, how about you?
**Jason Plumb** 00:29 Oh, it's 8 AM, so, you know, it's early.
**Vishwan aranha** 00:33 Do you have your coffee yet?
**Jason Plumb** 00:35 I'm working on it.
**Vishwan aranha** 00:36 Okay.
**Jason Plumb** 00:37 I started my first cup.
**Vishwan aranha** 00:42 Ben won't be joining us today, he's, out in Vienna, Austria. Okay. So…
**Jason Plumb** 00:48 Nice.
**Vishwan aranha** 00:51 I'm holding the fort down for Grafana. Most people are at the conference, so…
**Jason Plumb** 00:55 Cool, and it's in Vienna, that's… that's great.
**Vishwan aranha** 00:57 Yes, yes.
**Jason Plumb** 00:58 I wish I could go to Vienna. Sounds awesome.
**Vishwan aranha** 01:00 I had to go to DC last week, or I didn't want to travel again, so I just did not go. But yeah, it's a good time to catch up on things.
**Jason Plumb** 01:09 That's cool.
Alright, let's, that's not it. That's it. Okay.
Let's… yeah, let's give it, like, a minute or two. I mean, I guess, yeah, a couple of people won't be here, but hopefully… A bunch of the rest of the crew is… Hi, Hanson. Hi, Jason.
**Hanson Ho** 01:35 Yellow!
Jason Zuck.
**Jason Plumb** 01:38 I know multiple JSONs…
**Hanson Ho** 01:46 You know who you're working with, or the ages of people you're working with, with their names?
Generationally.
**Jason Plumb** 01:53 Oh, yeah.
**Hanson Ho** 01:54 At least in, you know, America and English-speaking countries.
**Jason Plumb** 02:03 I only know one Hanson, though.
**Hanson Ho** 02:05 Yeah, that's… outliers are outliers. We're ageless, by definition.
**Jason Plumb** 02:12 I do know at least two Cesars.
**Cesar Munoz** 02:15 Hey, hello.
**Hanson Ho** 02:19 Yeah, I've worked with several Cesars.
**Cesar Munoz** 02:22 I don't know any other Cesar English-speaking word.
**Hanson Ho** 02:26 Oh, they're all…
**Cesar Munoz** 02:27 This would be a common name there.
**Hanson Ho** 02:28 They're all Spanish.
**Jason Plumb** 02:29 Yeah.
**Hanson Ho** 02:30 Like, Spain Spanish, too.
**Jason Plumb** 02:37 While I'm sharing the doc, feel free to add yourself to the attendees list and any agenda items. We've got a few things front-loaded.
I'll just jump in, it seems like we have a quorum. Yeah, so I noticed that I was just looking through the list of PRs, and I was like, these were kind of stagnating down at the bottom, and now they're passing, and like, I think we commented on these… Are we on API 37 now? Is that why these are passing?
**Cesar Munoz** 03:06 I think we are.
Yeah.
**Hanson Ho** 03:10 I thought… I thought we were on for a while.
Or at least, compiling against, using 37.
We never target anything, because we're not an app, but…
**Jason Plumb** 03:23 So if we go to the README, is it gonna tell me API 37?
**Jamie Lynch** 03:31 This sounds familiar. I think I bumped the example app to use 37.
So, maybe as a consequence, photos, PRs are passing?
**Hanson Ho** 03:42 Oh, are those example apps updates?
An SDK update?
**Jason Plumb** 03:46 Good question. Well, good question.
Demo app…
**Hanson Ho** 03:52 Yeah.
**Jason Plumb** 03:53 This is in the root.
But it's probably not used by anything other than the demo app, right?
So if the demo app is now on 37, that would explain it. Yeah, okay. Let's see if the other one is as well.
Demo app. Okay, then that explains it.
Just for completeness… Let's verify that.
Yeah. Okay.
Cool. Well, then we can get those merged. It's just that they've been out there for a long time, and that's, that's all I was really getting at with this.
In fact, let's just do it right now.
Why is this not clicking?
There it is.
Alright, one more.
Not that one.
This one.
I'm awake.
**Cesar Munoz** 05:15 No rush.
**Jason Plumb** 05:28 Oh, yeah, we're not gonna do that now. Okay.
Do that afterward. Let's move on to Vishwan, who has joined us today?
**Vishwan aranha** 05:39 So I just have two related session topics. They overlap with, like, Cesar's manual API proposals, so I'm, like, happy to discuss them together.
I'm trying to finish the remaining, like, Android session work, and there's a PR that I opened, which started as the activity and, like, the expiry change, but it's, like… it's really, like, raised, like, a wider API question, so I just moved it back to draft so we can, like, agree on, like, the behavior before I reshape any of the code. I'm not, like, tied to the current implementation at all. I mainly want to leave with, like, a clear direction and, like, a sensible order for, like, the remaining work that we can, follow through, like, an agreement for this.
And, I can walk you guys through the main concept of this. Like, first, like, what should, like, main, activity mean? Like, I see two options. One is, like, a state, in which, like, the app would say… app says, like, the user is active or inactive, and that remains, like, true until it changes.
and the other, like, is an event. Like, the app reports that meaningful activity just happened, and then… and that, restarts the inactivity timer. So, which model do we want Android sessions to use? And, I would also let, like, Cesar chime in, so, with whatever you have in mind, or anything you want to add.
**Cesar Munoz** 07:00 Yeah. Thank you, Vishwan.
And… and by the way, thanks for… for… for tackling that issue.
the… the… So, I will say, just… Just for the… just… just for context, I think in the time that I've been working in this SIG, I think sessions has always been a complicated topic.
And so… and so, I… I… I think I can promise that nothing else should be as complicated as this.
Topic that we're gonna discuss right now.
So it's not like everything is, like, like this.
The problem with sessions is that They are not thoroughly defined.
In OpenTelemetry. I think Hanson was… Gonna take a look at it.
a while ago, but I know, I know it's complex, and… The other thing is that we don't even know what's the way that we should… Send sessions.
apparently… Ideally, it should be through something called entities.
But entities have been… getting in shape for the past, I think, 2 years, and… and I… I don't think it's… It's done yet.
So… so we're kind of blocked on that. So in the end, we just decided to… To do our own thing in this project.
Which was what we thought was the best for most apps.
And that was just to stamp a session.id attribute Into all of the spans and logs.
And so… Essentially, we can define what we… think it's best.
Within this project, so long as we don't… put it as a… so… So we created the session provider, API interface, which should be pretty simple, it just really just provides a session ID.
Because the behavior underneath it, it's something that, since Open Telemistry didn't define it clearly, because it's really difficult.
We… we did our own, let's call it, opinionated implementation for it, which is in the agent. So what you're describing about what's an activity, or user activity, or something like that, is actually something that we can define.
Here, and it would only work for Otelandra, and ideally, it should work for most apps.
But it won't work for all apps, so that's why session providers, it's still there as a fallback.
for users who have different, you know, use cases. So… To your question, what should we do about activities in general?
So it's something that we discussed a while ago, and I recorded our decisions in that issue.
Where, essentially, we currently are… Saying that when the application is in the foreground, the user is active, and when it's in the background, the user is inactive.
But that's… that's not always the case, and… And so, essentially, we just wanted to avoid, you know.
I guess, assigning behavior to this kind of labels that are OS-specific, and just say, okay, let's just have these two states active or inactive.
And then, probably by default, we keep doing the same thing.
Of when the user is in the background or in the foreground, the app But then we will provide a manual way for users to override that.
So, does that… does that help a little bit?
Or if somebody else can chime in and has something else to add?
**Vishwan aranha** 11:10 That helps me. If anyone else has anything to add, feel free.
**Hanson Ho** 11:15 Yeah, so… I think we went on the right path here with sessions, in terms of defining what it means in the data model, and what it means in the agent. But I think we need to take it a step further. So… Tying explicitly, Session change to… active, inactive.
Forces us to basically make these two things the same.
I think a session?
Can and should be able to be changed.
independently of anything in the user or, layer. And if we have that.
then the manual API can simply… Start a new session.
or end the session, and not start a new session, whatever it is. And our session code should be able to do the correct OTEL thing by firing the right events, and basically depict, or represent, model what a change would be.
Then we can have the things that drive session change, like, foreground, background, essentially call into that.
So unlike, unlike, I think, the visible screen, which is, I think, a lot more complex to define.
all we're doing here is saying, sessions change. So, I think it's much easier to kind of have a manual API and a, kind of lifecycle-based, automated, triggering.
live happily together. Because if you want to completely manually control it.
Just don't add the lifecycle handler.
If you want the lifecycle handler to handle it, add the appropriate one, whether it's changing fragments, whether it's changing, activities, changing destinations.
background, foreground, however you want to do it. The agent will have, like, a default behavior, but you're able to, through the use of manual APIs, build your own session change.
So, if we don't have this.
we should build it, which is the separating, the actual change, session change API, from the foreground, background, listeners, in order to do that.
And then we expose that as a session change API, however it looks. Like, you know, whether it's just start session, return, whatever it is, we'll talk about that. But then effectively have the, the, lifecycle-based stuff use the manual API and drive the change.
And everything should live happily ever after.
So hopefully, at this, like, at least at the, at the… forget about the modeling, the modeling's a different issue, but, like, at this layer.
like, something like that, decoupling the lifecycle stuff with the actual session change API, would allow us to… to… to… Basically, have a good default and let customers do whatever they want.
**Jason Plumb** 14:19 I will add to that, you know, thanks, Cesar for some of the history, like, that's really important to provide a context, like.
a lot of what's in Android predates the client SIG in some ways, and there were decisions made about session that were agreed upon, but not written down, and sort of… I… I stated my intention… Either last week or this week, in the, in the, spec call.
to start up a session, we no longer call them working groups, I got clarity on that, we call them… SIGS, it's a special interest group, that is only, dedicated and time-limited, so maybe we'll call it 6 months or 9 months.
to defining session.
and what its semantics are, and the various concerns, and how it ties into other concepts, other entities, like the resource, the user, and really get that written down, and do the hard work. Unfortunately, I had some stuff come up internally that's gonna take my attention away from that for at least a week, but I really do think that it's long overdue. There's definitely consensus that we need that definition in OpenTelemetry, and then we can implement it in Android.
**Cesar Munoz** 15:39 Yeah, I… Thanks, and I agree, I just wanted to, I guess, Somehow just land.
On what we can do now.
And, and.
**Jason Plumb** 15:52 Totally.
Fully agree, fully agree.
**Cesar Munoz** 15:54 Yeah, which is probably what… which one it's… it's… it's probably most concerned about, and essentially, so… So what we can do now is… Essentially, we… we… So, users… If they want to, they can define their own session process.
by creating the implementation of Session Provider. So, that's why Session Provider must stay as simple as possible, and I think your PR touched it.
And that's why I was like, probably we shouldn't add these, you know, API changes.
And the reason is because of that. Since there is no official Management of a session.
Ideally, we should keep that as simple as possible so that users can come up with their own management ideas of when to start or end the session. Now.
If we keep… if we keep that aside, and then now we focus on our implementation.
Which is, that we essentially track when the app is in the background, and if it stays like that for 15 minutes, we end the session. That's essentially what we do.
Right now.
Maybe we can add some manual APIs.
For users who want Our implementation, but still want to Manually set that active-inactive state.
we're talking about a, like, a special use case here. It's not like they want to control the whole session management.
But they also don't like the way R behaves by default.
And that's where I think there could be some manual APIs that we can Somehow provide them If it's needed, but essentially, it shouldn't be needed if they just create their whole Implementation from scratch, which… it's probably a lot of work for some of them, so… you know, that's why I'm partnering about this manual API stuff that I'll discuss later, but… but yeah.
So, in, in… In your case, Vishwan, We might want to add this Because it's something that I… we need to discuss later.
But essentially, if we decide that we want these manual APIs, extensions, if you will.
Maybe that's something that… your PR could be… could become.
But… but let's see. But aside from that.
just handling sessions in general, I don't think that should change Because there is no general way to handle sessions, so… so at least the interface should stay the same.
onto further notice.
**Jason Plumb** 18:48 I feel like we did a pretty decent job with this design, and have we… we stabilized this module, right? I think session is stable in Android?
**Cesar Munoz** 18:57 I think so, yeah.
**Jason Plumb** 18:58 Yeah, so I feel like we went over this, like, a lot, and I feel like we landed on a pretty decent API for this. I think where one of the gaps is right now is that if you wanted to use or supply a custom session provider, which is not our default implementation.
There's not a great way to do that now. I think you might be able to do it with Core, but I don't think there's any way in the DSL, that's why I was clicking around in there, to see if, to see if there was any way to do that, and I don't think there is. You know, we allow you to customize the amount of idle time before… background time before we roll over, the maximum lifetime of a session, you can register listeners or observers, but other than that, there's not a lot of customization in the DSL.
You could imagine another method on here, and I'm not suggesting we do this yet, but you could imagine another method on here, which was, like.
Session provider override.
Right? And then you give it one of these implementations.
And it just does the needful. And then you can… then you can sort of… Poke at and change the session whenever you'd like to, right?
**Cesar Munoz** 20:10 Which… which I think we need, and I think it's something that Jamie added today, so maybe we'll…
**Jason Plumb** 20:15 Yeah, okay.
**Jamie Lynch** 20:17 one of the VRs to discuss later. So I'm just, like.
**Jason Plumb** 20:20 driving the thing you just did? That's okay. Fun. Cool.
Haven't seen it yet.
May not look at it this week.
Okay, Vishwan, have we just overloaded you with information?
**Vishwan aranha** 20:35 Totally…
**Jason Plumb** 20:36 Derailed your ideas?
**Vishwan aranha** 20:37 I'm okay, like, I just wanted to get an idea about how we can proceed, and I'm okay with Cesar's PRs and everything going in, and then I can probably, like, add comments and ask if I should divide this into, like, including things that I need as we go through this.
But I think I have a pretty strong idea about, like, how we can proceed with this, so, and I'll definitely ask questions on PRs and otherwise.
As we proceed… as I go through this more.
**Jason Plumb** 21:07 Cool.
**Cesar Munoz** 21:07 Thank you.
**Jason Plumb** 21:08 Yeah, thank you.
**Vishwan aranha** 21:09 And second is just, my second question was, like, the sequence for remaining session work, like, should we open, like, focused upstream, issues for, like, any, version, persistence? Or, like, do you guys want to go with, like, one task for that? I can create, like, separate tasks alongside, if you guys agree with that.
So we can tackle them In a focused way.
**Jason Plumb** 21:35 I'm still not awake yet, so I'm not sure if I'm following the… There's issues about session persistence, is that what these are?
**Vishwan aranha** 21:42 Yes, so this is session persistence and a couple of other things that I added. Okay.
**Cesar Munoz** 21:51 Oh, I'm not aware of.
**Jason Plumb** 21:53 I mean, has it been around?
**Cesar Munoz** 21:54 I can't remember.
**Jason Plumb** 21:55 I think that's why they're a year old.
Yeah, this is true.
So, the question is mostly how to sequence these, like, if you were to… if one were to tackle these, like, what sequence should they go in?
**Vishwan aranha** 22:09 Yeah.
**Jason Plumb** 22:11 I don't even know.
**Hanson Ho** 22:14 Isn't these… isn't it just… these, like… orthogonal to, like, whatever changes you have. It's just, like, session-based sampling is broken because a bunch of things don't respect it, and we need to fix them all for it to work, so feel free to take it in any order kind of deal.
**Vishwan aranha** 22:32 They can technically…
**Cesar Munoz** 22:33 like, at least this one, I think it's… Just that we wear sampling spans, but not logs.
Based on sessions, so… it's kind of like a… kind of like a book.
But it should be independently… Workable doesn't have to… anything to do with the session management process.
**Jason Plumb** 22:53 Can I close this one, Cesar is a dupe.
**Cesar Munoz** 22:56 Oh, yeah, yeah, that's fine.
**Jason Plumb** 22:58 Okay.
**Cesar Munoz** 22:59 To be honest, I forgot about these.
**Jason Plumb** 23:02 Let's just close it as a dupe, and then… this is… when it says events, it's really in log, so I'm gonna do that.
**Hanson Ho** 23:08 No, we'll call it a fence? Okay, cool.
**Jason Plumb** 23:10 I mean, we also have a lot.
**Hanson Ho** 23:11 That's true. Yeah, yeah.
if we don't have a label or something like that, I mean, it feels like session-based, sampling is broken until, like, a handful of issues are fixed. So, like, giving it, like, a session label feels like it makes sense, and these seem unrelated, work.
I mean, it's related in that everything needs to be done in order for this to work, but it's… it's not directly tied.
To your previous work.
**Jason Plumb** 23:39 Right, these are both related to sampling, and I think the sampling just leverages the session. I don't think it… Are you concerned that there might be an ordering problem with those?
**Vishwan aranha** 23:53 Yeah, it's… yeah, I think there might be some overlap or something, so we have to, like, cross-check if some of them are valid anymore. I don't even know, like, if they would be valid or not. I have to cross-check and test them. But I just wanted to raise this before we take any action on this.
**Cesar Munoz** 24:10 I think the log sampling should be workable.
Right away. I think that one should be fine. The other about using samplers… In the session, in the log.
processor or something? I forgot which one it is.
I don't quite remember or understand that one, so… or if we want that one, yeah.
**Jason Plumb** 24:35 This one, you mean?
**Vishwan aranha** 24:37 Yeah, I think a span, like, or log may need the current session ID, but reading that ID, like, should not, like, tell the SDK that the user was active or something.
**Jason Plumb** 24:48 Oh… So, yeah, well, yeah, because there's, like, I think the… it used to be, and it might still be this way, that the act of reading the session reset a timer, right?
I think it used to work that way. It might still.
**Cesar Munoz** 25:03 I think so, yeah, in our implementation.
**Jason Plumb** 25:06 Yeah, yeah.
**Hanson Ho** 25:08 Which is another reason maybe decalping those would be… be good.
like, I think fundamentally, What changes a session, and the session itself is… Different concepts. Related, but different.
**Cesar Munoz** 25:29 I think we need to think through this one a little bit further.
**Vishwan aranha** 25:33 Yeah.
I can… we can discuss next, SIG as well, or we can… passively discuss through this to PRs, if that works. Or, like, a task, I can create a task for that and respond to that, if that works faster.
**Jason Plumb** 25:53 I don't know about faster. For me, for me, that's fine. I'm just… I'm in, notification overwhelm and focused on a few other things right now. Okay. Sadly, So I think… I think talking about it in SIG is good, but if you… if there's specifics, I think being specific would be helpful. So what… what about the session sampling is… is concerning in the current implementation? Like, what prevents… or what… what do you think… to… to Cesar's point, if you were to implement or fix the sampling for logs, how would that impact the larger session effort?
**Vishwan aranha** 26:28 So, for this topic itself, like, Android still need, like, versioned session storage, and, like, clear rule that process owns that session, so… that's why I wanted to open, like, a focused issue for that, like, separate from 910 and other tickets, so…
**Jason Plumb** 26:43 Oh, that's super welcome, yeah, yeah, you can totally do that, that'll be helpful.
**Vishwan aranha** 26:47 So, yeah, it would cover, like, basically what we save in migrations and any bad data process ownership, so that's why I wanted to… my basic idea of the second topic was, like, creating, tasks that we can work independently on now without affecting anything.
So…
**Hanson Ho** 27:03 Are you looking for an OTEL API, and not just an Android Agent API, that returns the session ID?
**Vishwan aranha** 27:11 Yeah, basically, yeah.
**Hanson Ho** 27:13 Okay.
And reading attributes isn't good enough.
**Vishwan aranha** 27:19 I think there was some issue that I ran into, but, I don't recall off the top of my head, I've just forgot to… I forgot to click on that, yeah.
**Hanson Ho** 27:30 I mean, it's good to open an issue so we can discuss more focus in a more focused way, but if you're looking for an OTEL API that returns a session, that will be… that might be a little harder to get. If it's an agent API, or reading from the attributes, then I think we're in business.
**Vishwan aranha** 27:50 Sounds good. Let me open a task for that and, like, describe, and then maybe we can have an async discussion as well before next SIG, and maybe on the next SIG, if you guys have a… don't have a chance to look through that, then we can, Go through that, if that works for you guys.
**Jason Plumb** 28:05 Yeah, that works for me.
**Cesar Munoz** 28:06 Yep.
**Hanson Ho** 28:07 Yeah, I'm curious how Session does it, if, or sorry, Spans does it, if, if, if we can't do it with logs.
**Vishwan aranha** 28:18 That's good.
**Jason Plumb** 28:20 Okay, are we ready to move on?
Sounds like we're ready to move on.
Okay, there's a proposal for some manual APIs here.
Let me do a little…
**Cesar Munoz** 28:31 bye.
Right, so I'll try to keep it as quick as possible, because I think all the details are in there, but essentially.
So, I, I, I… I saw a message from Jamie in Slack.
And I think it's about… I'm not sure if I properly understood it, but it's… was it, like, something like this idea… was about… Not having to ever… increase the API surface?
of… Rum.
Or something like that.
That…
**Jamie Lynch** 29:17 Yeah, basically, I think… I was just trying to understand, the intention behind the PR, and whether it was to avoid having to create, like, specific APIs for new features, or… For something else, yeah, I think… what I've usually leant towards EarnBase, at least, is just creating specific interfaces and APIs that have Strong typing for new features, but I… Might have got the wrong end of the stick about what this is doing.
**Cesar Munoz** 29:56 No, that's fair enough. I wanted to try and clarify that, so… the, I guess the… So… Similarly to, in, in, manual, sorry, automatic instrumentations.
There are a bunch of stuff that we don't want to be part of.
The, core default functionality.
And I think that's where these APIs fall into. It's like… It… it… my… like, it's not important or… you know, core enough for these APIs to live, in… in ROM APIs.
like, first-class APIs?
But it… Provides a way, like, an optional way for users to get some Some handles, if you will, or some knobs.
to… to… to use for some very specific use cases. So it's kind of like… it kind of, like, falls in between.
And I think today we don't have something like that, and I fear that if we don't add something like that.
Two things could happen.
One is that… Whenever we need to provide users with some sort of manual APIs, we might either Start adding a bunch of statics.
All over the place.
or… We might, or we might start adding stuff to the core APIs that it's not… Generic enough, or it's not, like, broad enough for it to be there.
So… So that's why I… I thought about this. I mean.
It doesn't have to be like this. I guess what I like about this approach is that it's structured.
And it kind of gives the same rules for the same kinds of APIs.
Which is very similar to what we do with AMR instrumentations. Like, they have to have, you know, this AMR instrumentation implementation, and they have to register it, and so, so forth. So, that's kind of, like, what this is. It's like, I know that there might be some cases, and I guess probably a better example for this is the, I mentioned sessions, because that was one of the main reasons.
I thought about this, but… but the other one is the screen, but we discussed the last SIG meeting, the screen, the current screen.
definition.
Where… I think it's fair to say that there's no way for us to know which is the current screen for a user.
And at the same time, we don't provide them with a way for them to… to… to define it So maybe this could help, at least with that use case.
in which we provide this, intermediate API, so that users can, only when they add, you know, the, the… visible screen tracker.
For example, they will get access to these screen, manual API that lets them select what's the current screen.
But it's like, this will be optional APIs, and it would be depending on what you add.
Into your project, similarly to instrumentations.
So, that's kind of, like, the idea behind it.
**Hanson Ho** 33:46 So, Cesar, the main reason behind this, is it more to.
isolate, like, dependencies, so the API might expo- like, might pull in, like, a different module that you don't want to have, so that it doesn't get pulled in by default. Or is it more, like, it may not be stable, we may not want to actually continue to support this, we'll see. Or is it another reason? Because the alternative would just be, as Jamie said, put it into, interfaces.
and have Local Solitude Realm implement those interfaces, and basically just have it, you know, available for everybody using the SDK. The reason to have people do a couple more things to get access to it, what's the main reason for you to want that?
**Cesar Munoz** 34:35 Right.
So, I don't think what… you know, what Jamie mentioned about just adding stuff into the existing interfaces.
I don't think that will go away with this.
It's just that I believe that whenever we decide to add new interfaces, like, general interfaces for ROM API.
I think that should be done for stuff that… Is needed for everybody.
So it's not, like, a specific use case that needs that API.
And… and so… And I guess I'll kind of, like.
Probably repeat a bit, because I think Jason wasn't here.
**Jason Plumb** 35:19 Yeah, sorry.
**Cesar Munoz** 35:21 No worries. So… I guess the idea is to have, like, this middle ground where There is something that is not… cross, I don't know.
It's not used across the whole… it's not used for everybody.
Only… it's optional for users who want that functionality, and they need some sort of knob to tune that functionality in some way.
So that's where this would be used. So… I guess, in a way, well… Yeah, I don't have a good analogy for it, but…
**Hanson Ho** 36:06 Another reason would be accidental usage, like, prevent people from accidentally using it. So, like, you know, make it a little harder, because it's kind of risky. One reason one. Reason two is, we may not want to feature support it in the future. So, you know, we may not want to put it in the main one.
**Jason Plumb** 36:25 Yeah, Hanson, just to jump in, it sounds like when this was being described earlier, it sounds like the incubating features that Java has, right, where it's, like, some stuff that is new, and we think people will want it, we probably want to adapt it, or adopt it, but for now, it's just incubating, and we can see how it plays out.
**Cesar Munoz** 36:45 Maybe that could be a use case for it, but that… the thing is that the way that you… you mentioned… the way that you explain it sounds like everything that it's incubating will eventually land, you know?
And I don't think that has to be the case for these.
**Jason Plumb** 36:59 Okay.
**Cesar Munoz** 37:00 It's like, sometimes… They're just needed for a specific use case.
**Jamie Lynch** 37:04 So, is the intention for… So let's say, using, like, some third-party networking library that's not super popular, let's say we have some instrumentation for that.
That networking library would define an API extension Within its own module, and that would allow for… user of that instrumentation to configure that API, and they would do it via the module, rather than like, the Android Agent API?
**Cesar Munoz** 37:42 Yeah, that could be a use case. I guess… I guess a nice… I don't know if configuring it, but… Really, the best example that I can come up with is the second current name.
Use case.
Because right now, as far as I'm aware, we don't… Include the auto screen, current screen instrumentation.
by default, I don't… maybe we do… I don't know.
But the point is that, let's say that that is an optional instrumentation, and we want to provide users with a way for them to set the current screen name.
So, I wouldn't add… into OpenTelemetry ROM, I wouldn't add that function. I wouldn't add that setter, you know, set current screen name. That's… that's a very specific use case that I… that shouldn't be in such a global place.
And, as I was mentioning, then there's a flight over here.
as I was mentioning, the… The other option could be, which I wouldn't like to fall into.
Then, to provide a bunch of static functions, For users to handle.
these behavior.
So, this kind of gives that middle place where also users… I don't know if you've noticed, but users can actually access these extension APIs through the ROM objects.
**Jason Plumb** 39:08 Yeah, like this.
**Cesar Munoz** 39:08 So…
**Jason Plumb** 39:09 Right.
**Cesar Munoz** 39:10 So it feels, like, kind of like part of ROM, but it doesn't have to be in ROM.
So it can be optional, the added, kind of.
**Jamie Lynch** 39:19 Okay, so the actual Android agent or implementation wouldn't actually have any knowledge of those APIs, but it feels like it from a user's perspective.
**Cesar Munoz** 39:31 Yeah.
**Jamie Lynch** 39:31 Cool.
**Hanson Ho** 39:32 So, so it's.
**Cesar Munoz** 39:33 I mean, you've… Yeah, go ahead.
**Hanson Ho** 39:36 So it's like an… so it's… so the reason would be the compile time isolation, then. If you… you have an optional instrumentation that you don't depend on, you don't have to pull in that instrumentation, or you don't have to pull in that dependency.
But if you have it, then you have access to that module, and therefore that API. So, with the screen tracker, for instance, you'll have, like, a screen tracker module.
That is optional, that you don't have to depend on, but if you do depend on it, you can basically pull something from there and get access to some API via the RUM object as the entry point.
**Cesar Munoz** 40:12 Yeah.
**Hanson Ho** 40:12 Okay.
**Jason Plumb** 40:15 Yeah, I am a little bit leery of extensions, because they scare me, and I think they provide sometimes an inconsistent user experience.
And it makes the reader of code have to understand a broader context sometimes, which I think is… maybe more of a burden than I sometimes want, but… I understand why they're there, and they have their… like, they're super powerful, and there's prior art, like, we have extensions in… Various places already, so…
**Hanson Ho** 40:50 Another way to achieve this is basically have, some API that we support in these optional modules, and basically just have it there. Because you're gonna have to reference, you know, you know, screen tracker, whatever, anyway. And that could effectively have an API. So, Like, it's not a static per se, but it's, you know, module-based, something that you can access.
Whether it's this lookup-based thing where you pass in a class and it returns, or something where, hey, I know I'm accessing. I have a hard, dependency on some module, and on some module, you can access, you know, an API,
**Cesar Munoz** 41:35 Yeah, yeah, that's true, it's just that that will just cause that any… every module will do its thing, you know, which, in terms of being confusing, I think that that would be even more confusing.
**Hanson Ho** 41:46 I mean, yeah, I mean, having a single entry point and passing in something that… that is from that module and having that return interface is, I think, reasonable.
**Jason Plumb** 41:56 So, Cesar question, but I haven't looked at this really at all yet, but question about it. So, this is all… this PR, this extension, does not help with initialization or configuration, it's… it's access to… stuff after the fact? Like, it's access to internals after the fact? Is that primarily… Yes. Okay. Okay.
Yeah, I want to keep us on track for time, because we're getting a little bit close, and there's still a few more items, but go ahead.
**Cesar Munoz** 42:26 Got it. No, I just wanted to say, like, we don't have to make a decision right now.
But if, you know, if we ever get another use case in which We want to provide some sort of manual API, but we don't want to extend ROM because it's not a broad enough use case.
You know, we can take a look at this. If there's another… if there's another approach, I'm open to take a look at it as well. I really just wouldn't like every model… module to do its thing.
Or to start creating statics all over the place, things like that, so…
**Jamie Lynch** 43:01 Yeah, definitely.
**Jason Plumb** 43:02 I think we're all in agreement on the static thing, hopefully.
what… what I would think when I go to look at this and try and get my head around it is, if it's purely extension, then it feels kind of safe to have to try out. If the impact to the… to the… actual API and the actual, agent is pretty minimal to support this, then I'm all about it. Like, I'm all about, like, creating little add-ons that can be evaluated, incubated, whatever, like, especially if it doesn't have, like, a major change, but that's what I'll look at when I review that.
Cool, thanks for bringing that up, Cesar. I think that's great.
I'm thinking about some hard problems.
Okay, telemetry docs, PR's too big.
**Cesar Munoz** 43:56 It's not meant to be merged. I mean, it will… I will split it, but I wanted to give the whole idea.
**Jason Plumb** 44:03 Oh, yeah, essentially.
**Cesar Munoz** 44:04 elite, I guess, just to summarize it.
This will make unit tests and Android tests to generate a YAML file with whatever they capture.
And the YAML file will kind of look like this example here.
And then… and then that was it, and then another… another tool will take this and put it into a README. So that's essentially it. There will be some… nuances, probably, is the word, to take a look at. For example, I noticed that the first time I ran it locally, I got session ID as one of the attributes, which It shouldn't be, listed in a specific instrumentation, because it's a global attribute, so… so things like that probably would need some configuration stuff.
But essentially, well, also some stuff that Jay mentioned.
**Jason Plumb** 45:02 Yeah.
**Cesar Munoz** 45:03 But essentially, it's just generating a YAML file based on tests, which will require us, I think.
This will be the main, thing to be aware of is that we will require us to use specific unit JUnit rules.
To be able to capture this test's data.
And that's it.
**Jason Plumb** 45:28 Cool. Yeah, I think this idea is great, because it's kind of like an integration… Like, it uses the real code with the real tests to get the real, actually generated telemetry.
metadata, and… Yeah, I think that's great.
**Jamie Lynch** 45:46 Yeah, this is awesome. Yeah, I think my one comment was just we'll have to be careful about making sure the tests are actually covering What telemetry can be captured in different scenarios?
Because you can get different paths for instrumentation, but I think we can solve that.
**Cesar Munoz** 46:08 Yeah, true.
Yeah, this info is as good as our tests.
**Jason Plumb** 46:13 Yeah.
Okay.
So, I added this one. Yeah, Cesar, thanks again for doing that. I think that's fantastic stuff. I'm looking forward to having that in place.
Yeah, so… I don't know if anyone else looks at this stuff, but… I did notice… Two months ago is what GitHub says, so we need to do a release.
I could probably start that today, and maybe have it done tomorrow?
If that's cool?
**Cesar Munoz** 46:52 Sounds good to me.
**Jason Plumb** 46:53 Are there any PRs that you would like to see in this release?
**Jamie Lynch** 47:01 Nothing from me.
**Jason Plumb** 47:03 Okay.
I was looking through here yesterday, and I didn't see anything that was like, oh yeah, we should get that in.
**Cesar Munoz** 47:15 And not that I'm aware of.
**Jason Plumb** 47:16 Okay.
Okay, cool, I will start that off, today.
**Cesar Munoz** 47:25 Thank you.
**Jason Plumb** 47:37 Okay, Jamie…
**Jamie Lynch** 47:40 Yeah, I don't think we need to go through these in any depth, it's more just kind of a heads up, but, I know we were discussing Mike.
stabilization and kind of poverty between the core module and the DSL last week, so… I created a few issues of stuff I did see.
So I'll try and work through that gradually, I guess.
**Jason Plumb** 48:09 Cool, I love the label. That's… awesome.
there was something in core, you kind of tickled my… my brain, there was something in the network… this thing that I think I intended for us to talk about, and I didn't add it to the agenda.
**Jamie Lynch** 48:28 Got it, yeah.
**Jason Plumb** 48:29 But this is… this is great. I love, like, trying to… to keep chipping away at core, which is really what this is intended to do.
But I'm concerned about that one dependency.
**Jamie Lynch** 48:42 Yeah, I wonder if it's worth… Like, kind of having, like, an intermediate module, rather than making call depend on For network instrumentation.
**Jason Plumb** 48:53 Are they in services now? Is that where that stuff is? Or is it in core?
**Jamie Lynch** 48:57 I think it was partially in core and partially in services.
Yeah. But I think Ultimate is only used by network instrumentation.
**Jason Plumb** 49:10 But it has to be exposed through core in some way, right? Like, there's some… I forget what the API looks like.
**Jamie Lynch** 49:17 Yeah, I think we got a bill… We have a dependency on… I think, like, a carrier, or carrier finder.
**Jason Plumb** 49:26 That's right.
Well, at least in terms of concept, to me, it seemed flawed.
for a chord to ever depend on instrumentation.
That relationship seems broken. I mean, like, the agent also… like, it only should depend on instrumentations that it wants to install, and it shouldn't, like, depend on it for, like, core functionality, basic utility.
**Jamie Lynch** 49:54 Yep, fair.
**Hanson Ho** 49:56 I feel like there's certain things that, like network, parts of this should be part of core.
And not instrumentation, like… like, there are some… this is basically a shim over the Android API, so anybody could conceivably depend on it. Instrumentation could be built on that, like, that should live in instrumentation if you want the attributes, you know, appended or whatever, but I think… some aspect of it probably should live in a, as Jamie said, like an intermediate module, or inside a core, but definitely the relationship shouldn't go the other way. There's… there's nothing… In instrumentation that should ever be dependent on it by agents, or a core, or something like that.
**Jason Plumb** 50:47 I mean, I think we talked last week about services being a bit of a bucket, just like a… like a hodgepodge, but I think in concept, that was the intent, was to provide this layer on top of the Android platform, which… you know, Hanson's saying that network is kind of… The network stuff that we're providing is kind of… sits on top of the platform.
Which is why I thought Services maybe was an okay place for it, even though… Services is a mess.
**Hanson Ho** 51:17 I mean, in concept, services should be that middle layer between Core and… and… and instrumentation, right?
**Jason Plumb** 51:26 I think that was the idea, but it's, like, I think we failed, right? Like…
**Hanson Ho** 51:30 Okay.
**Jamie Lynch** 51:32 That brings in lots of dependencies that aren't needed by certain modules, so…
**Jason Plumb** 51:38 I'm in the wrong.
**Jamie Lynch** 51:39 Yes, in principle, what we want is to split it out into, like, services, network, and… above.
like, modules.
**Jason Plumb** 51:48 Yeah, like a module inside of services that's just for the network stuff. I think that… I mean, that does taste pretty okay to me so far. Like, I think I like that idea.
**Hanson Ho** 52:01 Yeah. Service is just ill-defined. Is services doing instrumentation as well, basically?
**Jason Plumb** 52:06 No.
Like, it doesn't generate… none of these generate telemetry, if that's the definition of instrumentation.
**Hanson Ho** 52:15 Yeah, yeah.
**Jason Plumb** 52:18 Yeah, this thing is…
**Hanson Ho** 52:20 I'll take a look at…
**Jason Plumb** 52:21 Kind of just, like, the container for all of the services, and then an individual service is just a tag interface.
**Hanson Ho** 52:31 Take a look at it.
**Jason Plumb** 52:32 And the factory is what produces these two things.
Yeah, it's… it's a mess, but… There's some room to improve that.
**Hanson Ho** 52:42 I feel like when we ripped stuff out in the services, we kind of knew that, like, because everything was just one big glob before, and we kind of put some stuff in core that we think belongs, and then everything else kind of just… Pulled into services,
**Jason Plumb** 52:56 Yeah, it's funny that, like, nothing else up here, right, the factory and services, none of these mention network at all.
I bet you we just moved… I bet you we moved this in here from somewhere else.
Does anybody remember the history on this?
like, here's this PR, maybe.
Let's see…
**Cesar Munoz** 53:17 And we've done a lot of cleanup, so…
**Jason Plumb** 53:20 Yeah.
**Cesar Munoz** 53:21 He's been moved to…
**Hanson Ho** 53:22 Dependency from core to network instrumentation.
Like, that… that's… That's good.
**Jason Plumb** 53:28 Oh, this is, like, the exact thing. That's funny. Okay, but then what's this one?
Same thing.
**Hanson Ho** 53:38 Cherry pick.
**Jason Plumb** 53:39 Yeah, so…
**Cesar Munoz** 53:40 I think what Jamie mentioned of just having that standalone module, cool work.
Yeah.
Yeah.
Which, I think it was what, as you said, Jason, the idea… initial idea for services to be this common Kinda split by service.
Kind of common tools.
**Jason Plumb** 54:06 you.
**Cesar Munoz** 54:07 the Android SDK.
But… but yeah.
**Jason Plumb** 54:14 Yeah, so maybe Services Network.
**Jamie Lynch** 54:16 Yeah.
**Jason Plumb** 54:17 Yeah.
Okay, cool. I will leave a note right now.
**Hanson Ho** 54:25 So what the current PR is just… Pulling stuff apart.
More so than… than changing dependencies.
**Jason Plumb** 54:35 Totally.
**Hanson Ho** 54:36 It's just okay.
**Jamie Lynch** 54:37 moving stuff around.
**Hanson Ho** 54:38 Oh yeah, that's fine.
I thought we had, like, some weird dependency that we're trying to, like, get ourselves… Rid of, but we probably did that with the… 2 months ago.
**Jason Plumb** 54:50 Yeah, I think that thing we were looking at here, I think this was a mistake, I think we broke, or I think we… The fact that this is cherry-picked makes me think we did a patch.
This is kind of sounding familiar to me, and it wasn't that long ago, I should be able to remember this, but I have too many concurrent work streams for that to be practical for any single human being.
Yeah, I think this was an accident, and we had to patch it, if I remember.
**Hanson Ho** 55:27 So there was unreal dependency, we just accidentally introduced it.
**Jason Plumb** 55:30 I think so.
**Hanson Ho** 55:31 Okay.
**Jason Plumb** 55:33 I think as part of that move, it created a dependency that shouldn't have been there.
Okay, we've hit time.
Any last things that people want to bring up before… We call it?
Okay?
Good, lively discussion today, thank you.
**Vishwan aranha** 55:57 Thanks, guys.
**Jason Plumb** 55:58 dear.
**Cesar Munoz** 55:58 Hey.
**Hanson Ho** 55:59 Right.
