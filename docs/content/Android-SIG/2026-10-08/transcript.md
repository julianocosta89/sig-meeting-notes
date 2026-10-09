SIG: Android SIG
Date: 2026-10-08
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Jason Plumb** 04:44 Hey, everyone.
**Vishwan aranha** 04:48 Hey guys, how are you doing?
**Jason Plumb** 04:51 Pretty good, how are you?
**Vishwan aranha** 04:56 Pretty good, just… today's Thursday is meeting day for us, so… so many back-to-back meetings.
**Jason Plumb** 05:01 Yeah, it's a lot here, too.
**Ben Joseph** 05:03 this.
**Jason Plumb** 05:04 I'm running a little bit late. I'm finishing making coffee, but I'm getting set up here.
**Vishwan aranha** 05:10 Sounds good.
**Jason Plumb** 05:18 Hello.
Let's see if I can share.
My water is boiling.
Give it another minute for folks to show up.
**Hanson Ho** 05:42 Welcome back, Jason.
**Jason Plumb** 05:44 Hey, thanks!
**Hanson Ho** 05:47 Where'd you go?
**Jason Plumb** 05:49 Went bikepacking in the Willamette National Forest, which is like in kind of central Oregon in the Cascade Range.
**Hanson Ho** 05:57 Wilamet is such an Oregon name.
**Jason Plumb** 06:02 Yeah, I'm sure it's, indigenous, like, probably Willamette, but I'm not… I'm butchering it, probably.
But yeah, I mean, I think people who haven't ever been up here don't fully appreciate just how… Majestic the Pacific Northwest is, like, genuinely.
And we got to experience some of that, so it was fun.
**Hanson Ho** 06:27 A lot of friends that bike pack, they'll ride all the way up north, from, like, Colorado up to, like, southern British Columbia, and…
**Jason Plumb** 06:37 That's awesome.
**Hanson Ho** 06:38 All the things… not a lot of them, but, like, 4, but… but, you know, enough. I don't do that.
**Jason Plumb** 06:47 That's far, yeah, we… we did… 350 kilometers in 4 days?
This is pretty far.
But a lot of uphill with heavy bags.
Heavy bikes.
Well, light agenda, so if anyone has anything, feel free to put it on there. I put something on last week, I think.
Or earlier this week.
Yeah, I'm still playing catch-up, and I still have internal priorities that I'm juggling, so… Unfortunately, it doesn't have my full attention right now.
But hopefully soon.
**Cesar Munoz** 07:24 just.
**Jason Plumb** 07:26 Yeah.
**Cesar Munoz** 07:28 Yeah, I don't think there's any rush. I know that there's a couple of PRs with some comments.
Tagging you when you get some chance to have a look, no worries.
**Jason Plumb** 07:39 will.
**Cesar Munoz** 07:40 By the way, welcome, welcome back.
**Jason Plumb** 07:44 Thanks, thanks.
Thanks for holding it down while I was gone.
Like always.
**Cesar Munoz** 07:50 Well, actually, it was Jamie this time. I had a sore throat.
That day, so…
**Jason Plumb** 07:56 I know.
**Cesar Munoz** 07:57 Yeah.
**Jason Plumb** 07:58 Hopefully you're on the mend.
**Cesar Munoz** 08:01 Yeah, it's fine now.
Thank you.
**Jason Plumb** 08:05 Well, okay, so I'll jump into my topic. It's, it's nothing too intense. I know that for some of you who've been to KubeCon in the past, you probably have heard of, or maybe you helped out a little bit with this thing called ContribFest.
It's a way for projects to… garner interest from humans who might want to take part in the project, or contribute their first pull request. It's kind of the goal is to, like.
show people the ropes on contributing to open source, maybe for the first time, especially for OpenTelemetry for their first time. And so we've been asked to participate. I will be there, because I have a talk, but I will also contribute to ContribFest.
And they've asked to bring Android and Kotlin repos in, so, what that means is that we should identify some low-hanging fruit, some… Some issues that we think are good for new contributors.
And I think we have a label. If we don't, we can create one, but we should have a label that's called ContribFest, and… it will allow… Us to identify the issues so that we can, kind of walk people through the process of reading, contributing Md. And forking the repo and all of that good stuff.
So, if you have any that are, that come to mind, feel free to tag them with ContribFest, and if that label doesn't exist, we'll get it created.
And we have a month to sort of do that, it's no big rush.
I just wanted to bring that up there for people who think that there could be some good low-hanging fruit for folks. It's a weird time to be doing ContribFest like this, because… People are just throwing their agents at repos anyway, and picking up low-hanging fruit, like, all the time, so… We might have to also create some, so if you have, like.
An idea that's not yet an issue, maybe.
Give that some consideration, too.
Any questions on that?
Okay.
**Hanson Ho** 10:12 I guess.
**Cesar Munoz** 10:13 Basically.
**Hanson Ho** 10:16 But go ahead.
**Cesar Munoz** 10:17 Well, just… I guess it could be… thanks. I guess it could be, any… not necessarily the SDK, but also maybe demo, app changers, like, anything…
**Jason Plumb** 10:27 Totally.
**Cesar Munoz** 10:28 Small, okay. I don't…
**Jason Plumb** 10:29 Yeah.
**Cesar Munoz** 10:29 Anything in mind right now, Bob?
**Jason Plumb** 10:32 And DemoApp is a good candidate, for sure.
**Cesar Munoz** 10:38 Yeah, sorry, Hanson.
**Hanson Ho** 10:39 Is the, hotel zone back this time? I know for EU, there's some… some… issues with the Splunk sponsorship or something like that.
**Jason Plumb** 10:53 I… I don't know the final answer, but I also don't have any good news to give you.
**Hanson Ho** 11:00 So.
**Jason Plumb** 11:01 I… I think it's not gonna be back. That's the last thing I heard.
**Hanson Ho** 11:06 So where is ContribFest happening? Like, is there, is there, is there, like, a booth? Like, a…
**Jason Plumb** 11:12 We'll… no, we'll get, like, a… we'll get, like, a meeting room.
Like, it'll be part of the conference center, we'll have, like, a meeting room where we did it. Like, a couple of times before, it was, like, in a banquet hall kind of thing.
And we seat… it's limited seating, so I think we filled it one time with, like, 50 people.
Because people need their laptops out to actually… you need, like, a work surface, it's not like a presentation-style room.
**Hanson Ho** 11:40 Got it.
**Jason Plumb** 11:50 Okay.
I think Hanson has the next topic.
**Hanson Ho** 11:55 Yeah, this is actually from last week. There's the, the, the PR, was pointed to about, visibility tracker update. So, so I put that up a while ago. I had a look, and.
wanted… big… more… comments from the maintainers in terms of direction, because, what this is, I mean, Ben did all the work to basically wire up the destination.
navigation destination and making that an event. And we kind of deferred the work, at that point to kind of integrate, those types of destination changes to this old visible screen navigation tracker, or screen… visible screen tracker. And this is essentially, you know, that part of it. So I want to get folks' take on.
Whether we want to define a screen in a very concrete way, and basically say a destination is a screen.
And then, make changes to… to override… have something that kind of, like, munches it all together, because, the code changes on the server. There's some, you know, corner cases, but, if… if we want to actually say.
Destination changes… a destination is now a screen, and fragment is also a screen, and activity is also a screen, and there's some sort of rule that we will define to say, if you have all those things, what is the screen?
Which was what this will require.
I think that's generally useful, but whether this current implementation is the way to go, tagging it on is the way to go.
How does everybody else feel about it?
Before I go, like, actually review the code code.
**Jason Plumb** 13:55 I think we probably don't have a good semantic definition of screen.
**Hanson Ho** 13:58 Yeah.
**Ben Joseph** 14:01 I agree, but, like, whatever, I think, whatever we have defined, so far, or, like, in terms of, like, the components that we have identified, say, activity fragment and the navigation destination, they… they… they… they provide meaningful context, so it… we might not be able to define it yet, but I think it's still valuable if we can get, you know, combine these together.
**Hanson Ho** 14:31 Yeah, like, I almost see Visible's… this tracker, tracking, like, activity, and fragment is almost like a structural tracker, it's like, what thing is loaded? The concept of having a screen and munching it together, I think, should exist, but whether it replaces this, because maybe some people do actually do want the activity, or do want the fragment, rather than, like, you know, the navigation destination.
And this will fundamentally change that. So we're… Impose… we're redefining what this is tracking.
It says screen, but, like, it's not tracking screen right now. So… So, replacing this, creating something new.
Those are basically two options.
Where do folks stand?
**Cesar Munoz** 15:21 I haven't taken a look.
At least not that I remember.
I don't think we should never try to be smart about defining By some sort of smart logic of what a screen is.
I think we've discussed this in the past, I… More… I lean more towards the option of providing an extension API.
For each case that we consider.
Might not be part of the… Core APIs, if you will, or agent APIs.
that in this case, I guess it will allow users to say, okay, here's the screen that I'm in right now, that's its name.
And then that would… that will be used as a, As a variable somewhere in a processor somewhere.
To set that screen name.
And then whenever users set another name, then we will use the new name, and It's a very fairly simple manual mechanism.
that I think could also be used by.
on automatic instrumentation.
That wants to be smart.
About deciding when there's a screen on, on… on screen, I guess. So… That would be my… I haven't taken a note, but yeah, that would be my… ideal to provide a manual way to do this. I have a PR.
for these API extensions, if you want to have a look at it.
which will kind of address this issue of the manual extension. Api.
And, for what we already have.
I think it probably should become very explicit, say.
Instead of saying something like, last screen name, instead of providing these kind of attributes.
We should probably be very specific, like, you know, Android activity name.
Or Android fragment name, and then… Not use the word screen unless it's via the… manual API, or… Oh yeah, something like that.
**Jason Plumb** 17:56 Yeah, the contents of this PR are not fresh for me either, but I think in concept, I like this idea, because right now.
screen, vaguely defined, historically defined as, like, activity and fragment. Now that we have composed navigation instrumentation.
And we generate events, the notion of what the current screen is is muddied, and maybe doesn't follow like, there's a gap there for Compose, right? And the data that's being emitted through the global attribute screen appender thing, global screen attribute appender, is probably just either missing or inaccurate. It might just, like, have the activity name, and even though you're navigating to a bunch of different components. So when other things happen, that's behind. So, at least on the surface, this, to me, sounds like a good idea.
To update the visible screen tracker to know what compose screen you're on somehow.
There's probably some implementation details that… And some rough edges, I imagine, but, like, in concept, this seems good to me.
Seems like a good idea.
**Vishwan aranha** 19:04 Would compose instrumentation also use that screen Api, or would like screen names only be like set explicitly by the app.
**Jason Plumb** 19:15 The implementation's not fresh in my mind, so I don't know what this is attempting to do.
**Hanson Ho** 19:20 This adds the activity or fragment, name, in… onto, spans and logs as attributes as they go.
So, something that would, supersede that will take in, data from all sorts of things that potentially could, do a screen, if the automated version will do a screen and use, the manual API Cesar proposed.
And basically write… the correct attribute names, because I don't think last activity is… is an attribute like that's that's not going to last is not a namespace so.
**Jason Plumb** 20:01 No, we gotta fix that, yeah.
**Hanson Ho** 20:04 you.
**Ben Joseph** 20:05 So, sorry, Hanson, but, like, this does not have anything to do with Cesar's API, I believe. This is just… We already have the activity and fragment, being tracked in the visible screen. I think this just interleaves the navigation compose instrumentation into that. It just adds the compose navigation screen also as part of, like, treats it the same way, like an activity or fragment name, I think.
**Hanson Ho** 20:32 Yeah, so this, this, this PR, if merged, like the way it is, effectively redefines what this instrumentation does. It adds the Compose stuff onto it, but then we lose the explicit, I want to know what activity I'm on, or fragment that I'm on before. So the instrumentation will change, because if people were using Compose navigation.
But has other things to track that, like your events.
This will also… if that data is merged in with this data.
they lose the ability to track activities and fragments. So, I think my question is, do we leave some instrumentation that adds activity fragment, and then put on, like, a second similar instrumentation, or even add to this instrumentation, but just add a different attribute that is, like, screen.
So, like, preserving the activity and fragment only bit is… is… is what I'm… I want to kind of understand. Like, do we want to do that?
Because if we don't, then we deprecate this, pick a new name, there is one, then there is no way to track activity and fragment by itself. If we don't want to override it, we have a new attribute. We can even use the same instrumentation if we want, that will track this combined version.
And have a proper, like, you know, I don't know, app.screen.name or something like that.
**Jason Morris** 22:03 just Thinking out loud, but… we've effectively got two different questions that we're trying to answer with one instrumentation, because there's the, where am I structurally in the app? What is the actual structural thing that the user's looking at, but there's also the nominally, where does the user think they are? And they're kind of at odds with each other, and you potentially want to know both for different reasons, and potentially report both for different reasons.
**Hanson Ho** 22:35 Yeah, the instrumentation name is basically saying the abstract where the user is at screen, but the implementation is doing structurally where the user is at in terms of activity and fragment. And that's the contradiction that we're trying to resolve.
**Jason Plumb** 22:51 Yeah, Hanson, I think it's a good question that you're asking, and it's proper to make us think about this. I think we already have this problem between activity and fragment, though, right? Like, those two things overwrite each other. It's whatever last one in there wins, and it's probably fragment.
It's probably activity for a little bit, and if you're using fragments, then the fragment, I think, would overwrite the activity name by being the current screen.
if you're using fragments, and I think that this kind of perpetuates or continues that problem of, like, overwriting what the screen is, and losing some sort of visibility on… there's almost like a stack, right? Or like a… like a hierarchy of…
**Ben Joseph** 23:32 Okay.
**Jason Plumb** 23:33 screen, like, where you are. But without a definition, it's hard to say, like, what's correct, right? Like, what we should do. But if all of those are useful.
In a rum product, then… then yeah, maybe we should surface all of them.
**Ben Joseph** 23:48 Also, given that hierarchy, do you think it's a loss of information, or you are dialing one level deeper into What, what is visible. So, if you, if you know your destination or your fragment, you can infer your activity or, like, the higher level, so maybe it's not so bad.
**Jason Plumb** 24:09 It.
**Hanson Ho** 24:09 It depends on… it depends on the usage, so…
**Ben Joseph** 24:11 Yeah.
**Hanson Ho** 24:12 It's… it's… you are… you are… I mean, this is getting a little pedantic, so maybe, you know, we can, you know, comment in there. If folks feel overriding is totally cool, you know, you can do that, that's fine.
But then… but then we have to… this code will have to basically have an algorithm to say, what does the overriding? And that kind of goes against what Cesar was talking about in terms of the manual API.
**Jason Plumb** 24:42 Yeah, so there is your is your PR open? Like, should we look at that as well?
**Cesar Munoz** 24:46 Sure, let me look for it.
I was thinking that, that there are some cases In which, a single activity might have Multiple fragments in it.
And in that case, I'm guessing there that whatever this callback that we have.
It's it's probably tracking them all.
So so even fragments can Step on each other's toes, in a way.
So I'm starting to even… Think if… if… yes, it's that one, it's the first one.
**Jason Plumb** 25:25 This one.
**Cesar Munoz** 25:26 Yeah.
**Jason Plumb** 25:27 Okay.
**Cesar Munoz** 25:28 Thanks.
I'm starting to even think if… We're talking about… okay, okay, okay, we're talking about several problems, I guess, here. One is that… I guess… On one… okay, okay, the easy one first for me is… We need to get rid of the last, semantic convention.
stuff. And I will… Prefer to do so.
Without any, backwards compatibility anything, because it's never been stable.
So, I will, I will… in terms of semantic conventions, I will prefer. And you know I'm I'm open to suggestions to Have a specific one per… Per… I don't know, solution, I guess, or per… thing. Okay, in in this I mean one for activities. names, one for fragments.
And then, that way, users can see Down to whatever specific architectural type they want to see that's going on in that moment.
Although in that case, I know it should be easy for activities because in theory there should always be one on screen.
For a single app?
**Hanson Ho** 26:51 There's most activity.
**Cesar Munoz** 26:52 But for fragments, I don't know how would that work, to be honest. Probably they will override each other if there's more than one in a single activity.
But the point is that I think we need. We need new names.
That should be specific.
Aside from that, this proposal, She will allow any module.
within the repo to extend the OpenTelemetry ROM API.
with their own stuff. In this case, let's say that we had a screen API that allows users to set a screen name.
And then this same API has a getter that we use in a — In a processor, to set the screen.name value.
We will kind of work like a global, if you will, but… But it wouldn't be a static thing.
And… and… And any instrumentation and any other module can use this extension, so it doesn't have to be manually called only. Maybe if in the future we decide that we want to create an instrumentation that It's smart enough for a lot of people to automatically capture what what a screen is in that in a specific moment. then we could create it, and it will call the manual Api itself.
But of course, it will be opt-in only for users who… Use the navigation mechanism that we think is the most common one, and for them, everything will work.
Fine, magically.
But I do think that this API should be manual.
And.
Yeah, that's all I… I don't know what else to say.
And that…
**Hanson Ho** 28:49 So what I'm hearing is that, I think, most folks want to… define the user-facing abstraction of screen as a thing, and then basically update this instrumentation, from recording activity and fragment to that new concept. Since we're gonna have to change the attribute anyway.
And then we could, after the fact, layer in the API and basically have the API be the source of truth, or where the API writes to as a source of truth.
Where this is pulling from.
So that, it could, so, so all, every, all the, all the events, from destination and activity updates can feed that source, that can be overwritten, and this just basically takes that and slaps it on wherever it needs to be. And then in the future, if we want to do more, like, explicitly show, destination and fragment and activity, this could also be the entry point to add those attributes. But we are effectively saying that we want to.
improve this to, be what the instrumentation name is, which is screen, rather than what the implementation does, which is structure.
**Cesar Munoz** 30:11 Yeah, sounds fair to me.
**Hanson Ho** 30:13 Okay.
**Cesar Munoz** 30:14 And this green manual source of truth, single source of truth API?
should only allow for a single screen at a time. So, whenever you call, or an instrumentation calls set screen name.
Then it will override it.
globally.
Because there should only be, semantically speaking, a single screen.
Only at a time, so…
**Hanson Ho** 30:38 Yeah.
Oh, sorry, go ahead.
**Jason Plumb** 30:41 I agree with that. I think that's a good approach. I think that anything else is probably a little over-engineered and too complicated, and most… Like people looking at a front end where you're showing like a real user monitoring type experience. I think that level of detail isn't that important. It might be important to the app developer, but like to understanding how a user interacts with a thing is less important.
**Hanson Ho** 31:02 Sure, I will… I will com… I will add this as a comment to that, and then review it in that way.
I'll bet you're gonna say something.
**Ben Joseph** 31:11 No, I just… I think, like, the manual API, Do you see this working, like, if somebody… first of all, today with, navigation instrumentation, that has to be explicit and manual, so, there's no.
I think it's fair to assume, at least for today, that, like, if somebody is manually instrumenting navigations, then we can automatically update the global tracker, because they are explicitly interested in that. So I just want to make sure that, like, we don't always some sort of auto instrumentation at least partial like this should be present.
how I've experienced the portal SDKs, like, if you integrate it, like, you get almost everything out of the box. At this point, I think it's mostly the navigation instrumentation that is manually wired. Pretty much everything else, like, you get for free, and I… I really appreciate that experience, and like, I wanna keep some… keep it as close to that as possible. So… Yeah, if we can have this global tracker update.
if the user is using manual navigation instrumentation, I think that… that's… that's all I just want to add, if you don't see any problem with that.
**Jason Plumb** 32:35 I want to make sure I understand what you're saying, but I think what you're saying is that it's nice to have the auto instrumentation, and if there are instrumentations that track navigation, whether it be through activity fragment or compose, having those fill in the current screen even if they do use the same APIs, which I think they should, right? If we have a new API that's, like, set the screen name, it's probably okay for those instrumentations to also set the screen name.
**Ben Joseph** 32:59 Yes.
**Jason Plumb** 33:00 Yeah.
**Cesar Munoz** 33:01 Yeah, no.
**Hanson Ho** 33:02 means.
**Cesar Munoz** 33:03 That's fine.
They probably won't set the right screen name.
**Jason Plumb** 33:08 though…
**Cesar Munoz** 33:09 In some cases, but they're also opting, so users don't like it, they can.
Manually said those.
**Hanson Ho** 33:18 It's… it's… it's buyer beware. I mean, this API could initially start off as internal, and basically the activity fragment and destination updates all call that API. So it… the only one source… there's only one single place that writes to that single source of truth, which is the API. And if that API doesn't… is not exposed manually, and it just becomes an internal thing that everybody internal to the, to the, the screen tracking stuff, we'll use. And then if we expose it, then it becomes, like, an overridable source. So, so this could, this could happen basically in stages, such that, you don't lose the, current functionality, or after this merges.
we don't lose that functionality. And on top of that, you can do the manual stuff. And if we want to get fancy, you can even have disabling of certain frameworks, whatever, but that's step forward 5, not something to consider right now.
**Cesar Munoz** 34:18 Okay, I… Sorry.
I think it makes sense. Essentially, that sounds less aggressive than what I was proposing.
So, essentially, if I understand correctly, it's like, we could have a manual API, which would be the source of truth, the only source of truth.
Implement it, then make the existing instrumentation use it.
To… to set the source of truth.
And… and in the meantime, only internally will be used, and… So, in the meantime, we will still have this… Because let me, let me try to remember… I think it sounds good. So, in the meantime, we will still keep providing this instrumentation that tries to guess what the current screen is, based on activities and fragments that it sees.
And it's just that it will use these… New API, which will be used as a… source for… the new, let's say, what we call screen dot name.
semantic convention, or maybe we can keep on using the same. The old convention. I don't know.
So… The… I think that's… that's fine. Now, what the PR that… We… that we started to talk about this.
Wants to do is to, on top of that, include also compose navigation.
To put it into the mix, So now the instrumentation has to… Now it has, like, 3 things to take into account.
when deciding what's the current screen name, I guess. It has an activities… fragments. And now the Navigation from Compose.
Is that correct? I guess.
So, okay, so… We can say that our, current Legacy… let's call it… Magic screen, recognizer.
instrumentation.
We'll… do we want it to… Handle these 3 things.
or would do we want to keep it only with activities and fragments? I guess that was my question.
**Hanson Ho** 37:00 I think my original… that was my original question, too, and I think Jason and Ven are saying that they want the magical screen thing to take into this, so it's a replacement and not a new thing. Because last.screen.name is wrong anyway, so we have to migrate off of that.
it's either going to app.screen.name, which is effectively, conceptually the same as what the name is, but not necessarily what the implementation is, versus going to app.activity.name, which is what describes the implementation, and not, like, the intent, which Jason was saying is a bit, perhaps, over-engineering and less useful than having, you know, the screen thing.
So, I think the proposal is, having the logic to basically understand all three and set precedents, whether it's in the current implementation form.
Well, probably not in the current implementation form, eventually, but this could probably work initially. And then the refactoring will happen, where.
the API, first internal, perhaps, will allow processors something to set a single source of truth, and the instrumentation, or at least the processor, will just be pretty dumb. All it does is look at the source of truth.
And then write the attribute.
And it's up to the logic that basically, takes in all three potential events, that maybe listens to, the lifecycle callbacks and, the destination events, and basically, you know, decides.
on… based on some rule, you know, what… what is happening, and setting the right value. And then that API can then be exposed. I mean, the simplest way to do it is expose it to the users, so they can set an override.
So that, that could be done.
**Cesar Munoz** 39:00 Right.
**Hanson Ho** 39:00 But that's afterwards.
**Cesar Munoz** 39:02 Right, so we're talking about… and we're talking about… I guess I'm… we're talking about two different systems, like the existing one.
Which will probably stay the same as it is, and on top of that, we'll… get… become aware of Compose navigation stuff, and it will keep on doing what it's doing right now.
And then in the future, once we have this manual API source of truth.
We will, use the new semantic convention for whatever it provides.
And… We probably On top of that, we'll create a new automatic instrumentation That tries to automatically find what the new value for screen name is, in order to make things easier for users.
Or maybe we will refactor this existing system.
to use that new manual API and set what it believes to be the right screen name. Okay, okay, so it's like… merging them in the… okay, okay, I see now, thanks.
**Hanson Ho** 40:14 Right now, the source of truth is whatever this does. But I think eventually the source of truth is gonna be… somewhere else, and then multiple consumers could set, and get from that, and not have to worry about having a duplicate logic to figure out which is the correct one.
**Cesar Munoz** 40:30 Got it. And so just for for for from what we have to do right now, I guess.
If everybody agrees with.
Us being okay to add.
Compose navigation on top of activities and fragments.
Then I guess we can just proceed with what is here, which will add that functionality.
And for the time being.
There will be no semantic convention changes.
So that'll… We'll keep the last.screen.name, things like that, right? Just that.
**Hanson Ho** 41:07 the semantic convention could be done in parallel. I don't know about… it's probably okay to change, like, start adding, destinations.
with a minor version. I don't think we need to, like, you know, bump major version. But, you know, next week we're probably going to be ready to talk about, you know, semantic convention changes and major version bumps. But I created the issue, but there's… there's a lot of detail. I don't want to create 25 separate issues, so I decided to… Not create 25 issues.
And then just wait until next week before we talk about that, which is why I didn't put it in the, in the thing.
**Cesar Munoz** 41:47 Thank you. Okay, then I think it's fine, we can… Probably move on with the, with the new addition of… Compose navigation… Source of logic, I guess, or…
**Hanson Ho** 41:59 Awesome.
**Cesar Munoz** 42:00 Defining the screen.
**Hanson Ho** 42:02 Look at this week.
**Jason Plumb** 42:03 Yeah, I think I'm aligned with that. I think I agree with the description of the current behavior and where we're trending and what this PR does. Does anybody take issue with this? Is anybody really concerned about this overriding?
replacing activity.
**Hanson Ho** 42:17 A little bit, but then I'm just.
**Jason Plumb** 42:18 little.
**Hanson Ho** 42:19 I'm just… I'm just guessing what folks are using this for, but, you know, it's a guess. And we can add fragment. If we want to add that detail, I think we can do that later.
**Jason Plumb** 42:30 Yeah.
Okay, I… just to that… to that point, I tend to err on the side of… trying to user create abstractions that apply across other platforms. So like iOS ideally would also have a notion of a screen, like a browser would also have a notion of a screen, although they probably spell it page, you know, but it's the same concept, right?
**Hanson Ho** 42:54 you.
**Jason Plumb** 42:55 I try and like, you know, keep that rather than exposing or leaking out the platform specific implementation details through the telemetry names.
**Hanson Ho** 43:05 Yeah. App.screen.name seems like an app domain attribute versus activity. We might be talking about Android.activity.
**Jason Plumb** 43:15 Yeah.
**Hanson Ho** 43:15 know, in the meeting on Tuesday, we're talking about whether we need Android namespace, and I was like, I hope not. And then, well, right here, first meeting, it's like.
Maybe we do, if we do, so…
**Jason Plumb** 43:30 Do we know who this is? Do we know who this is?
**Ben Joseph** 43:36 I don't think you've seen it before.
**Jason Plumb** 43:37 Okay.
It seems like they've worked on the other stuff, too.
**Hanson Ho** 43:42 He's got LinkedIn, so click on his LinkedIn.
**Jason Plumb** 43:46 Okay.
**Cesar Munoz** 43:46 Just wanted to add, we don't have to discuss the details right now.
Okay. But maybe for the future.
I think I… if I understand correctly what Jensen… Jason is mentioning.
Is that probably, you know, having this abstraction that works across platforms?
It's also… it's nice… Also, for end users who just want to see, okay, I just want to know what the screen is.
I don't care if it's an activity or whatever.
And and And I agree with that. I do know that there might be some people who want to know every little single technical detail.
And for those, maybe we can also send fragment and activity and something aside from that.
What I'm not sure is if… Those little technical details.
She'll be present as a global attribute.
Because… I don't know, they feel, like, too specific for it to be on… for them to be on every single signal.
So maybe in the future, We could create a specific, I don't know, activity… started.
dot name.
Event, and then we just send it when an activity starts, and then there will be some way for you to… for users to search.
what activities have been started, I guess. But it's not like you have to stamp that on every signal that will be like that will add up, I guess.
**Jason Plumb** 45:34 There's a trade-off there, for sure.
**Hanson Ho** 45:36 Mrs.
**Jason Plumb** 45:37 The trade-off being, like, you have to keep state, you have to remember what screen you're on somewhere, because when… when the crash happens, you're gonna want to answer the question of what screen was I on.
**Hanson Ho** 45:46 I mean, there are patterns to do this. I mean, we… especially if we're talking specifically about fragment and activity, you know, there are lifecycle things that we can listen for, slash SAS somewhere, have a process that looks at that conditionally, or simply offer it as an API that instrumentation can call and get. Like, what's the last fragment, what's the last activity? And then we don't have to manage the actual population of the attributes.
Folks can do it ad hoc if they want, and that's the kind of stuff that that we can start offering is effectively a platform abstraction layer to provide metadata for ad hoc consumption. Things like, what's my last network state? What's my power level, without having to bind to, you know, the version-specific API. That's the kind of value we can add, if we choose to, going forward.
**Jason Plumb** 46:40 Cool, I want to make sure we give enough time for the next topics. Are we ready to kind of button this one up?
**Hanson Ho** 46:45 Yeah.
**Ben Joseph** 46:46 Yeah, just wanna add that we already got rid of the last screen names with app screen previous dot name.
**Hanson Ho** 46:55 We've.
**Jason Plumb** 46:55 replaced it. Did I do that work? Who did that work?
**Ben Joseph** 46:58 You did, you did.
**Jason Plumb** 46:59 Okay. Sweet.
**Hanson Ho** 47:01 Is it in the local semantic convention?
**Ben Joseph** 47:04 Yes.
**Jason Plumb** 47:05 Yeah, the importance of anti-conventions. In here somewhere.
**Ben Joseph** 47:09 Okay.
**Hanson Ho** 47:10 Is it previous, or is it the last one that we detected, i.e. is it actually the current?
**Ben Joseph** 47:18 So this is for the, Lifecycle events where we used the previous name.
**Cesar Munoz** 47:25 Buzz for events. Okay.
**Hanson Ho** 47:27 Okay.
**Jason Plumb** 47:29 And then the old one is still here, but deprecated.
Because I think, I think we allow the flag to… the compat layer still emits the old one.
**Ben Joseph** 47:39 Yep.
**Hanson Ho** 47:39 Cool. If we choose to use this, then the port will be more straightforward. Actually, it'll be the same, we'll just do another deprecation if we choose to, like, get rid of the word previous. Because the implication is that that's the last one that we detected was loaded, so the implication is we should be on the screen, right?
**Ben Joseph** 47:57 I think there's a current one as well. There's a current one.
**Hanson Ho** 48:00 one.
**Ben Joseph** 48:02 So, the visible screen tracker uses something else. This previous is basically for one activity to another, like, when you, like, that lifecycle event, the transition, so… Okay. Which activity to which activity did you move to? So… Main activity to settings activity. Main activity is the previous name.
**Hanson Ho** 48:22 So, so, so, so we, so we are still using… so this is still using an attribute.
That we don't… with the name that we don't want.
I have it.
**Ben Joseph** 48:33 off.
**Hanson Ho** 48:34 That actually lists this. I can check it.
**Ben Joseph** 48:37 Yeah.
The span attribute, like, Visible screen tracker has a, span pros… I think it, it.
A span processor reads from it, and then stamps it on every attribute. Sorry, on every span or log.
And I don't recall which exactly it is it uses.
**Jason Plumb** 48:59 I think it's this thing, right?
**Ben Joseph** 49:01 Yeah.
**Jason Plumb** 49:03 Oh, but no, something updates this.
Is there a screen appender?
**Ben Joseph** 49:09 Yes, it's… it has a neat screen in it.
**Hanson Ho** 49:16 Wait, isn't visible… isn't that…
**Jason Plumb** 49:19 Here, screen attributes, span processor.
**Hanson Ho** 49:23 Yeah, that's the one that I was looking at, right?
App screen name.
What is app screen name?
**Cesar Munoz** 49:31 which uses the visible screen tracker.
which the Pr wants to add.
**Jason Plumb** 49:36 Exactly.
**Cesar Munoz** 49:37 Compose navigation on top.
**Jason Plumb** 49:40 Yeah, which is why, which is why I would override.
**Hanson Ho** 49:42 But what's the app screen name define? What's the.
**Jason Plumb** 49:45 That's right.
**Hanson Ho** 49:46 Yeah.
**Jason Plumb** 49:46 Have attributes.
So these are generated, right? This coming from the Kotlin still.
**Hanson Ho** 49:51 Okay, so this is not last, then. This is… this is… app.screen.
**Ben Joseph** 49:57 Name, yes. Okay.
**Jason Plumb** 49:58 the.
**Hanson Ho** 49:58 Okay.
**Jason Plumb** 50:00 So.
**Hanson Ho** 50:02 Cool.
**Jason Plumb** 50:03 We have a different topic here, and I don't want to run long, but we should.
We should not have 3 sources for semantic conventions. That's… that's my topic. Let's talk about it next time.
laughs.
**Hanson Ho** 50:14 I create an issue for it, and yeah.
**Jason Plumb** 50:16 Thank you. Vishwan.
**Vishwan aranha** 50:20 Hi, so I just wanted to check on these two session PRs, and, like, briefly outline what's next. Like, both of these have been reviewed, I believe, so I just needed a merge, so, both of these, like, keep the changes internal without introducing, like, any new public API, so if you guys can give it a look and see if it's good, and I would just need a maintainer to merge these.
If there's no other blockers you could think of. And, I will have… refresh input wiring PRs coming up next, and I will, like, update those and send you guys for review, but at the same time, I will have some couple of questions that I'll probably bring it up in next SIG, where we can discuss it in detail.
As we go.
**Jason Plumb** 51:05 Okay, cool. I definitely have not reviewed these yet, so thanks for bringing them up.
**Vishwan aranha** 51:11 Thanks. Very good, Richard. Thank you.
**Jason Plumb** 51:12 Yeah.
**Cesar Munoz** 51:13 Thank you.
**Jason Plumb** 51:27 Okay, it looks like we've fallen off the end of the agenda.
Which is good. We did it. We finished.
**Cesar Munoz** 51:37 Sounds like it.
**Jason Plumb** 51:38 Does anyone have anything else that they want to bring up today?
**Hanson Ho** 51:44 there should be issues, or topics about, semantic event stuff next week. Couldn't… couldn't wrap it up, so… No use creating issues and talking about the same thing as last week.
**Jason Plumb** 51:56 Cool.
Alright, well, hopefully I can, give some more attention here soon, we'll see.
But… Thanks, everyone. Appreciate it. We'll see you next time.
**Ben Joseph** 52:10 Thank you guys. Bye. Bye.
**Cesar Munoz** 52:11 Right.
