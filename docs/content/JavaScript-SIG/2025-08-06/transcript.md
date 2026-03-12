SIG: JavaScript SIG
Date: 2025-08-06
Duration: 60 minutes
Zoom Recording URL: https://zoom.us/rec/share/fMjZxASdKza928TdoDdSx_KJHxrOGfgglKqokZhWDaiYGbBDIPo5QJT5l3Wx2XkL.xjr2FUWP0RykX1H-
============================================================

## Zoom Recording Transcript

Marc Pichler (Dynatrace) 00:01:36 Hello!
Andrei Borza (Sentry) 00:01:43 Hello!
Daniel Dyla (Dynatrace) 00:01:54 Hello!
Not very much on the agenda today, so we can give it another couple of minutes.
The meeting may be short.
Alright, Andre. It looks like the 1st 2 items are yours.
Century v. 10. Now on hotel core 2 dot. O.
Andrei Borza (Sentry) 00:03:48 Yeah. Hi, just wanted to announce this.
just yeah. It's gonna bump some of your download numbers a little bit hopefully. Soon.
Daniel Dyla (Dynatrace) 00:04:00 That's what it's all about is the download numbers.
Andrei Borza (Sentry) 00:04:03 Yeah.
And yeah, I'm just looking for a review on the Aws lambda instrumentation.
Basically, this supports streaming.
Daniel Dyla (Dynatrace) 00:04:16 Yep, okay.
Looks like Jonathan has not responded yet, but it's only been open a couple of days.
Marc Pichler (Dynatrace) 00:04:28 Yeah, he was fairly active. Recently again.
I had on my to do list from last week to reach out to him, but he was active, so I didn't didn't reach out.
Daniel Dyla (Dynatrace) 00:04:47 Is this a bug or a feature like our our streaming handlers meant to be handled and just incorrectly handled? Or was it something that was never implemented. To begin with.
Andrei Borza (Sentry) 00:05:00 It wasn't implemented. To begin with, there's an issue that's linked there. In the description.
Daniel Dyla (Dynatrace) 00:05:06 Yeah. That's that's why I asked, because I saw it's marked as a bug. But.
Andrei Borza (Sentry) 00:05:10 Yeah, I don't think it's a bug. But yeah.
seems more like a feature to me.
Daniel Dyla (Dynatrace) 00:05:18 In any case.
Let's get this reviewed and merged.
yeah. So just call for reviews, I guess. Is there anything in particular you want us to look at, or that's interesting.
interesting, or is it.
Andrei Borza (Sentry) 00:05:32 Not. Really. I think it's fairly straightforward.
Daniel Dyla (Dynatrace) 00:05:36 Okay.
Sounds good.
Andrei Borza (Sentry) 00:05:39 Cool. Thank you.
Daniel Dyla (Dynatrace) 00:05:42 Right. Trent.
Trent Mick 00:05:46 Hey? So I was reviewing Pr. For adding open AI instrumentation, and the Gen. AI. Somecom folks are ahead of the curve on using events and things like that, and we noticed that there are no exports from this amount of conventions package that we have for events. I'm not sure any of the other languages are doing so anyway. So anyway, this adds event underscore so feedback. Welcome on that especially you, Dan, because you were heavily involved in the naming conventions that we're using for that package. So.
Daniel Dyla (Dynatrace) 00:06:21 Okay, I will make sure to take a look at it.
I guess it's just the same as all the others, just with a different prefix. Right cool. That's right.
Alright.
Nothing else on the main agenda today. Anyone have anything they want to bring up? Or should we jump right into triage.
Okay, triage. It is everyone's favorite part on triage bugs, exporter proxy settings are ignored.
Marc Pichler (Dynatrace) 00:07:02 That feature does not exist yet. So that's why they are ignored. It's agent options, anyway. Not the agent that you can pass I was actually reviewing pr before I joined the call. That add adds the feature so I will continue doing that tomorrow morning to make sure that this is addressed. But it's not a bug. It's just lot working this way.
Daniel Dyla (Dynatrace) 00:07:34 Did this ever? They said they upgraded from 50 to 2 0, 3. And problems began. Is this something that ever worked.
Marc Pichler (Dynatrace) 00:07:42 I guess maybe the actual agent was just taking in, but the type shouldn't have allowed for that so it could be that they just passed the agent in there, and we didn't do any like special validations or anything with it, so it never got touched. And then it worked, but it wasn't intended to work at all.
It was always supposed to be actually agent options rather than the agent is. There's there's a lot of these things, because the basically, the the old exporter structure was so open that you could go in and basically said anything that you would like like everything that's supposed to be private was actually public. And then people use that for a lot of workarounds. So that's why we're seeing uptick in feature requests after the 1st version. There, it just took a while for these feature requests to come in.
because, yeah, people aren't updating as often, and they're running on an older version. And then in one like larger sweep, they update packages and then run into these things.
But it's being addressed. Yeah.
Hoping to get this much soon at the Pr. That I looked at. There's very few comments that I would have on it, so I don't think it would take very long to get this out.
Daniel Dyla (Dynatrace) 00:09:21 Okay, closing as duplicate. Then.
Marc Pichler (Dynatrace) 00:09:24 Yeah, I think that's reasonable.
Daniel Dyla (Dynatrace) 00:09:33 Resource attributes before Async attributes settled on SDK. V. 2.
Oh, it's happening in the it does. The diagnostic doesn't read resource or anything. He must be trying to. There must be a log that's trying to to log something.
Resources detected, await.
Marc Pichler (Dynatrace) 00:10:14 This is kind of weird. I thought that that should not happen anymore.
Daniel Dyla (Dynatrace) 00:10:18 They already opened a Pr.
Marc Pichler (Dynatrace) 00:10:34 I'm going to try to reproduce that.
Daniel Dyla (Dynatrace) 00:10:37 This is undoing something. We this was Async, and we went back to having it synchronous.
Marc Pichler (Dynatrace) 00:10:45 Yeah, but that was a very, very long time ago, right?
Daniel Dyla (Dynatrace) 00:10:50 Not that long.
Marc Pichler (Dynatrace) 00:10:52 I think it was, must be at least 2 years now.
Daniel Dyla (Dynatrace) 00:11:14 2.
Marc Pichler (Dynatrace) 00:11:21 The internal structure that we have. It should address this it shouldn't produce these error logs, so something's wrong somewhere.
But I don't think the fix that they propose is the fix that we should go with.
Daniel Dyla (Dynatrace) 00:11:46 It's gotta get back to where we were somehow.
Oh, what's the Pr. That?
And that's fine for now typhoon package, Jason.
Trent Mick 00:14:17 So I think they use this mistake, and they don't realize this is about the engines node in Api logs, and they don't understand, probably that the intent is to merge that into the Api package, which does have admin no requirement.
Daniel Dyla (Dynatrace) 00:14:31 Hmm.
Trent Mick 00:14:33 At least, that's my read.
We did change its engines from Node 18 and 20 back to Node 8, about 6 months ago.
Daniel Dyla (Dynatrace) 00:15:27 And then I guess this it is probably a bug. If they're.
Marc Pichler (Dynatrace) 00:15:40 I mean.
Daniel Dyla (Dynatrace) 00:15:40 This. This should not be causing logs right, because they are awaiting here.
Marc Pichler (Dynatrace) 00:15:48 Yes, so I'm they. They shouldn't even have to await it. The way that the resources are merged together is like it's supposed to be awaited in the export pipeline. Right? So somewhere it must be accessing these attributes before.
like they are settled, as the log says.
Daniel Dyla (Dynatrace) 00:16:16 Yeah, I I wanna try to run this as a reproducer. It looks very simple to reproduce, so I'll assign myself to that real quick, and I'll triage this later. Once I verify it. Because this.
you know, while this isn't necessarily what we want people to do.
At at this point all Async resources should be.
Oh.
it's this.
So the new resource.
It's doing resource from attributes.
I'm sure, if you look at resource from attributes, it's creating it with the flag that says that there's still Async attributes waiting or possibly merge. It's it's 1 of these 2 functions is creating a new resource object that doesn't have the that has the the Async attributes waiting flag set to? True?
Probably it could be smarter about that, and look at all of the attributes being added, and see if any of them are promises before setting that Boolean.
But this resource is a new resource that has not yet been awaited.
Okay, I'll I'll add a a detailed comment here, after after verifying that with a reproducer.
Marc Pichler (Dynatrace) 00:17:59 I actually tried to run this now locally, and I couldn't get any any error docs here.
But it might be that I'm just not getting something. There's also these parsed attributes that they have in there.
We'll.
Daniel Dyla (Dynatrace) 00:18:19 You tried to run the resource one.
Marc Pichler (Dynatrace) 00:18:21 Yeah,
Daniel Dyla (Dynatrace) 00:18:24 Hey! There's a heads up.
Marc Pichler (Dynatrace) 00:18:26 I'm I'm not getting any error like logs right now, but might just be.
Trent Mick 00:18:32 Nor am I. I can't reproduce either.
Daniel Dyla (Dynatrace) 00:18:41 Even if you try to access resource.
Marc Pichler (Dynatrace) 00:18:45 I haven't tried to access it, actually, but.
Daniel Dyla (Dynatrace) 00:18:49 They probably have some
Trent Mick 00:18:55 In a spam processor or something that's trying to access them.
Marc Pichler (Dynatrace) 00:19:07 Yeah, that there's a bunch of stuff missing here as well. They have parsed attributes which aren't there in this code, so we don't know what's in there.
And for this you can actually pass.
you can pass promises as well.
Yeah.
Daniel Dyla (Dynatrace) 00:19:26 Yeah.
Marc Pichler (Dynatrace) 00:19:27 So that might be corporate here, but it should actually set the flag correctly and everything. I also check the code there, and it doesn't seem out of the ordinary. So yeah, it might be that it's just something that's not easy to spot. And it might actually be the thing that might actually be the the thing that you mentioned earlier, that, like the flag, is not set correctly.
but the expression looks fine to me.
Daniel Dyla (Dynatrace) 00:20:07 Okay.
I added a comment, asking where these parsed attributes are coming from. They may be adding one that's a promise there or something, and then not awaiting it, which.
okay.
Trent, this seems pretty straightforward.
I guess this is p. 4.
It's not affecting telemetry or anything like that.
Trent Mick 00:20:43 That was me setting it up, I had a draft started a Pr fix to change to a different thing called yeah. So the okay. Sorry. That's a link to the issue on upstream thing showing it. And then I have a Pr to try to change to a different plugin called license header that I've been using for other repos which works better. But There's a limitation in that thing, in that. It it assumes a single header that's used exactly for every file in the repo. That isn't the case for us, because we have some with some variance in the copyright. So then I have a Pr. On this license header Plugin to add support for allowing some variance in that and then I'll follow up if that thing gets merged and we can update. But bye.
Daniel Dyla (Dynatrace) 00:21:33 Okay, I added the P. 4. For now, just to get it off the triage board.
Trent Mick 00:21:41 Thanks.
Daniel Dyla (Dynatrace) 00:21:44 Old contrib. Pr triage. Let's see, let's just go through the ones that have activity.
Sqs receive, use span links instead of processing spans updated 2 weeks ago.
still waiting on Jonathan, who, as Mark mentioned earlier, has been active on the repo, but probably just hasn't had time to review. This Pr is my assumption.
Marc Pichler (Dynatrace) 00:22:14 Different prs,
Daniel Dyla (Dynatrace) 00:22:17 Yeah.
Marc Pichler (Dynatrace) 00:22:20 Think 2 of them. I merged.
Daniel Dyla (Dynatrace) 00:22:26 Okay.
Marc Pichler (Dynatrace) 00:22:27 Reach out to him regardless.
Maybe it's just too far down the list to register on his notifications.
Daniel Dyla (Dynatrace) 00:22:38 Always give it another ping.
Alright, add page, view, instrumentation, Plugin. This was, we decided to old right.
Marc Pichler (Dynatrace) 00:23:06 That was right.
Daniel Dyla (Dynatrace) 00:23:07 Yes.
Marc Pichler (Dynatrace) 00:23:08 Pr.
Daniel Dyla (Dynatrace) 00:23:10 Yeah.
And it looks like there is a page view event.
Semcon, pr, so, looking at this as a prototype for this pr, then.
Martin, are you on the call.
Marc Pichler (Dynatrace) 00:23:31 No, he doesn't seem to be here today.
Daniel Dyla (Dynatrace) 00:23:57 Think if it's a if it's a prototype for simcom, we can probably merge it and not edit to the auto instrumentation.
which I don't know. If this even does.
Yeah, it's not adding it to any auto instrumentation or anything like that, so we can probably merge it after reviews and such obviously.
Marc Pichler (Dynatrace) 00:24:34 Yeah, adding new packages. It would be easier to have one pr, just adding the scaffolding, and then one pr, adding the code.
because this can get quite large, usually, and it's easier to spot any like inconsistencies with dependencies and stuff that can cause.
Oh, okay, install errors and whatnot and blow up the package log, Jason, and inspected.
Daniel Dyla (Dynatrace) 00:25:07 Okay.
I think that's all for er review. I just wanted to let them know what the status is here. I guess I have a request changes here. What was that?
Okay?
Isn't there a button to dismiss.
Marc Pichler (Dynatrace) 00:25:45 It's all the way down with the reviews section, or it used to be.
Daniel Dyla (Dynatrace) 00:25:55 I don't see the reviews section down here.
Marc Pichler (Dynatrace) 00:25:58 Yeah. Seems to be gone.
Daniel Dyla (Dynatrace) 00:26:02 Maybe I can do it here.
I don't know if that dismisses it or not.
That's requested a review.
Okay? Well, in any case, I can't find the button.
If I refresh, does it still show me as yeah, it's gone.
Add sequelize instrumentation.
Where are we on this updated?
So it just needs reviews, I guess.
Yeah, component owners, he did. There's 3 of them.
So let's looks like none of the component owners have none of the proposed component owners have.
t2t2 00:27:36 Make a thumbs up in the comment to react to it.
Daniel Dyla (Dynatrace) 00:27:42 I'm sorry. What.
t2t2 00:27:43 Scroll down to Fields!
Mark's comment.
3 comments, yes, this one.
Daniel Dyla (Dynatrace) 00:27:52 Yeah, that. So that's yes thumbs up if you're okay with that. But I would. To merge this.
I'd like to see.
I, the 2 of you also approve the Pr. Before it gets merged.
t2t2 00:28:11 Okay, both Martin to win.
Daniel Dyla (Dynatrace) 00:28:17 Okay.
do we have a label for like a waiting owner, review, or something like that?
Marc Pichler (Dynatrace) 00:28:32 No, that's the default status, anyway. So we have.
we have has owner approval which is supposed to be applied once it's approved so that we can filter and merge these quickly.
Only yeah.
Doesn't happen too often that somebody actually applies to labor. But I reviewed heck ther on like adding an automation that would do it so if an owner approves, it would automatically also apply the labor which would be helpful. Because it's 1 more step to forget. Right? So just get rid of that.
Daniel Dyla (Dynatrace) 00:29:23 Yeah, looks like you just added that comment 2 h ago. So that's still just moving along. I guess.
Gcp detector Cloud runs support.
So I don't remember what was the last status here. Decision was to move the code, the Google Repo code into this package. I'll send a Pr, so we're just kind of waiting on on.
Yeah.
Trent Mick 00:29:51 Yeah.
Marc Pichler (Dynatrace) 00:29:53 If the plan is to move that to our repo, we can just close this Pr right?
Because.
Daniel Dyla (Dynatrace) 00:30:03 Let's check with Aaron and the author just wanna make sure everybody's on the same page.
Or already. Another comment on this one.
t2t2 00:30:39 That's me approving.
Daniel Dyla (Dynatrace) 00:30:40 No, it's you approving it. I got you okay and add bedrock. Invoke model with response. Stream instrumentation aws bedrock. SDK.
Trent Mick 00:30:59 We're waiting for.
Daniel Dyla (Dynatrace) 00:30:59 There's only.
Trent Mick 00:31:00 To get back on review comments that I had, I think, scroll down the bottom. I haven't looked in a week.
Yeah. We asked last week if she has bandwidth to work on it.
Daniel Dyla (Dynatrace) 00:31:13 Okay. So I guess this is just still.
2 weeks ago.
it looks like there's been changes since this comment, but still not approved.
Feel bad for Jonathan having to be in charge of all the aws stuff. It seems to be some of the busiest stuff here.
new pr workflow, that's a draft. So I'm gonna go ahead and just skip it.
Dependency, I guess. Actually.
if this is passing, should we just approve and merge it.
Marc Pichler (Dynatrace) 00:32:26 Is that?
Yeah, I guess it's just a dev dependency, anyway. So it should be fine.
Trent Mick 00:32:42 Same major versions, so.
Daniel Dyla (Dynatrace) 00:32:45 Yeah.
mean, if the tests pass and it's a dev dependency, I think it should be okay.
If it breaks something, then I will take responsibility for that.
Marc Pichler (Dynatrace) 00:33:02 You can click the merge button already it will merge when when the tests pass.
Daniel Dyla (Dynatrace) 00:33:11 I think the tests are already passed.
Marc Pichler (Dynatrace) 00:33:13 All right.
Daniel Dyla (Dynatrace) 00:33:40 Looks like the author here just updated it to main. This is just not being reviewed by the components. Owner.
I think it's time to consider marking this as unmaintained.
I guess we don't have to do it on the call, but there's no change in the status here, just still waiting on on our approval. I wonder if we should create sort of Kanban project where we can drag things along to show that, like they are just waiting on owner approval, and, you know, like you said, have it have.
That's kind of the default status. But instead of having labels, maybe a project where we for this triage, where we can drag things along, and we can have everything go into an untriage by default.
Marc Pichler (Dynatrace) 00:35:00 Could also be helpful.
And maybe, if I guess we could also just apply the triage label on new prs that are being opened.
one that we already have.
Trent Mick 00:35:16 And then once there's activity.
Marc Pichler (Dynatrace) 00:35:19 From an owner. Just remove it.
Daniel Dyla (Dynatrace) 00:35:23 Yeah, like, I, I'd like to know, I'd like to see which Pr is are not like are waiting on an owner for a long time, basically is the.
Marc Pichler (Dynatrace) 00:35:33 Yeah.
Daniel Dyla (Dynatrace) 00:35:34 Is the idea updating express types.
Trent Mick 00:35:50 So I I open a Pr. Which generates some discussion which I haven't finished following up on. So David answered my question on there, so maybe let me let me finish following up on that one that'll impact us a little.
Daniel Dyla (Dynatrace) 00:36:04 It obviously doesn't break the tests. But yeah, there's always more nuance than.
Trent Mick 00:36:12 I don't know why I put my face in this one. I hate this stuff so like I removed the types express dependency from instrumentation express, for example, and to compile and test work, even though there's an import type request from expect from express in internal types in there. So I don't know how it worked.
Npmls tells me this. Anyway, I'll follow up.
David's my personal personal expert on typescript stuff. So I guess express now exports types already. So because we're using.
Marc Pichler (Dynatrace) 00:36:51 I'm not sure if they actually do, maybe I'm just completely wrong. I haven't like, whenever I use it I just snap together something really quick to test something. So I tend to use just plain Javascript.
Trent Mick 00:37:09 Don't think it has types.
The express 5 that we have installed does not have a type or types top level in Packagejson. So I'm not sure what's going on there.
Marc Pichler (Dynatrace) 00:37:21 Could be that it's pulled in somewhere from something else.
Yeah, anyway. Needs more investigation. I guess it's when the package gets like when, because the Monorepo has so many dependencies, there's it's very easy that you will end up with one package that's just being pulled pulled in by another one, and then
Trent Mick 00:37:47 Yeah, absolutely. So. I've seen the packages instrumentation Express Directory. Npmls tells me that types express is not installed. But if I go to the top level types express is there on a transitive depth that's 3 levels deep.
So maybe it was grabbing it from there. Anyway. Okay.
we can move on. I'll follow up.
Daniel Dyla (Dynatrace) 00:38:13 Yeah, I was quietly kind of moving on while you were talking. The next one here is the release. It's been open for a month.
I think we can probably go ahead and do a release but the we just merged a Pr. So I'll wait for that to finish and update this, and then I'll do the release when it's done, should be another 5 or so minutes, so we'll come back to it.
Marc Pichler (Dynatrace) 00:38:40 Sorry for not doing that. Last week I was actually planning to do one on Thursday last week.
and then forgot about it.
Daniel Dyla (Dynatrace) 00:38:51 No worries.
And we and then see with broken tests.
That's a draft that's a draft and then see with broken tests enable programmatic config when environment variables are unset.
This has been open for 3 weeks.
Has all the maintainers assigned to it any reviews.
Marc Pichler (Dynatrace) 00:39:26 What's the metal package? I think I passed by this once and able to test because their 1st time contributor?
it is definitely a problem that I've seen reported somewhere before.
Daniel Dyla (Dynatrace) 00:39:47 If you don't set the environment variable, then you can't set a programmatic.
Yeah, that definitely seems like a bug in the config handling code.
Marc Pichler (Dynatrace) 00:39:58 Yeah, it's very convoluted as well. There's 3 different ways that you can enable or disable instrumentations which, like, all have different semantics. So merging all of these together is kind of a pain.
Daniel Dyla (Dynatrace) 00:40:18 This seems like a reasonable priority order to me. But obviously it needs this needs reviews. It's been open for 3 weeks. We should probably take a look at it.
I'm gonna mark this as a bug, actually, because I think you should be able to configure without setting the environment variable enabled. I I think that's a bug, but does not cause any problems in user apps or anything like that.
Low priority.
Marc Pichler (Dynatrace) 00:40:58 Thank you in my actually be a p. 2, bug, because you try to enables or like change something, but doesn't take effect. So you get missing telemetry, and then you have to go hunt for what's wrong.
Daniel Dyla (Dynatrace) 00:41:14 That's fair. I think we can give it. P. 2.
Update, all patch versions.
Looks like it's passing, but probably out of date. Yes.
Redis, v. 5.
Trent Mick 00:41:52 We should definitely do this. I don't know if Amira has bandwidth to review.
Daniel Dyla (Dynatrace) 00:41:56 Yeah, Amir's the component owner here.
Amir, if you have bandwidth for this, it'd be great to get this reviewed. Looks like he's not on the call.
Trent Mick 00:42:22 This one's also doing changes in dB semantic conventions without doing the migration process so it won't go through clearly and cleanly as it is. But so start.
Daniel Dyla (Dynatrace) 00:42:35 It's doing what.
Trent Mick 00:42:37 It is. So. You know, the the dB semantic conventions migration process. Were you doing the update?
Yeah, this is making changes to newer simcom without doing that migration process. So anyway, so there'll need to be some ransoms.
and I'm also not sure if Amir had started to write us 5 support on the side.
Daniel Dyla (Dynatrace) 00:43:01 It's not in spec. It's in some kind, right?
I don't know.
Trent Mick 00:43:13 We have our own issue for coordinating the dB. Migration.
Daniel Dyla (Dynatrace) 00:43:17 Yeah, I just want to link to the.
Trent Mick 00:43:26 To that. Maybe you want.
Daniel Dyla (Dynatrace) 00:43:28 Here we go right here.
Trent Mick 00:44:05 I posted the issue. That's our coordinating issue, for it.
Daniel Dyla (Dynatrace) 00:44:19 Okay.
and kind of annoying.
Oh, I got it!
Oh, looks like my review! I posted as a comment, not an approval on accident.
I?
Oh, different approach with the current tool chain. I think I'd rather keep the Ts up version.
Anton. Were you trying to say something.
Antoine Toulme 00:45:57 Sorry folks, I forgot I was not on good.
Daniel Dyla (Dynatrace) 00:46:01 No worries. It's fine.
Antoine Toulme 00:46:04 Sorry.
Daniel Dyla (Dynatrace) 00:46:11 Okay, I'll leave this for now I'll let David decide which one he likes. Better instrumentation, coa, unmaintained package.
Somebody told them that this is an unmade.
Trent Mick 00:46:29 May I go back to the previous one for a second? I mean, we can follow up in the comments. But while we're here this would involve having an exports, entry, and package dot Json, for every package. Then I don't know if, like, I think we probably eventually want to do this is. But do people recall if we had issues with that in some things, I thought some.
there's some bundlers where the current major version doesn't support exports as a parcel or something like that.
Maybe we don't need to worry about that kind of thing.
Daniel Dyla (Dynatrace) 00:46:57 Yeah, I'm sure that there are a million bundlers that have different behavior. It's part of the reason I hate touching any of this stuff. What the way I normally go is to read the specifications and say, You know, we support specification compliant bundlers, or whatever that's my preferred approach most of the time when possible.
That said, I think Package Jason is not really like a specified. I guess it's specified by Node.
Trent Mick 00:47:33 Parts of it are.
They're like 50 somewhat specified things that are talking package adjacent. But yeah, okay. Anyway. Sorry.
Daniel Dyla (Dynatrace) 00:47:41 Yeah, type and exports are definitely one of the ones are, are definitely the properties that are specified by the node or, yeah. So I think we should, you know, follow the specifications on these. But I see.
Trent Mick 00:47:58 Actually, I take it back.
Daniel Dyla (Dynatrace) 00:47:59 The other one has to do that anyways, right like it's a module.
Have to do that.
Trent Mick 00:48:04 His thing had the module entry. So that's probably good for bundlers to pick up on that.
I think, anyway. But who knows why we need Bundler tests.
If we're gonna.
Daniel Dyla (Dynatrace) 00:48:15 Yeah.
and then, coa, this is adding support for coa 3. But to an unmaintained package like, I like the I like the idea of keeping this up to date.
Kind of raises the question of what? How do we handle these unmaintained packages, though?
Yeah. Will be closed within 14 days.
unless a new owner or sponsor of the feature is around.
Marc Pichler (Dynatrace) 00:48:47 Didn't close it because there was actual activity on it.
usually, if it's unmaintained and there's no activity for 2 weeks, it auto closes.
Yeah.
Checks in this. Reviewing this here.
Oh, this seems to be some activity, so I'd be inclined to keep it open and get that through, if possible.
Daniel Dyla (Dynatrace) 00:49:39 Just add it to supported versions.
changes the test all version to include.
If the test, all versions is passing here, this should probably be okay.
Looks like he is the component owner.
Yeah, get up actions about assign them. So I'll say.
should we say like has owner approval when it's when the owner is opening the Pr.
Have you? How have you handled that in the past? Mark.
Marc Pichler (Dynatrace) 00:50:35 So that's kind of the reason why we require 2 component owners per package.
Suspicious.
But yeah, usually, I just go in and review that in that case
Daniel Dyla (Dynatrace) 00:50:52 Yeah, there's not much to review here. I mean, it's it's it just, adds the version.
It's.
Marc Pichler (Dynatrace) 00:50:58 Yeah, I trust the component owner also to like, make the decisions for this, because I've seen them update and like, take care of the package pretty flawlessly over the past.
I think more than a year that this package has existed so Usually their their code is pretty solid. I will have a look at this.
Oh, separately, though.
Daniel Dyla (Dynatrace) 00:51:30 Settings.
12.
It's adding, version 12. It looks like. Probably these are the changes that were required to make it work. But obviously all the tests are passing, including the test. All versions tests. So I think this is probably good to go.
Marc Pichler (Dynatrace) 00:51:47 I'll have a closer look into like what the changes actually mean that they're doing here.
Daniel Dyla (Dynatrace) 00:51:54 Okay.
Marc Pichler (Dynatrace) 00:51:56 Feels they're getting some step result thing, and that has changed somehow. And I just wanna make sure I understand what's going on before approving it.
Daniel Dyla (Dynatrace) 00:52:17 Looks like I lost my history cucumbers switch from deprecated to stable again. This is the component owner. It's been approved by Mary Leah.
Marc Pichler (Dynatrace) 00:52:40 It's pro for the attributes. Okay, I I didn't see the title there, and thought they would be marking it as stable.
Daniel Dyla (Dynatrace) 00:52:51 No, just, the attributes.
Marc Pichler (Dynatrace) 00:52:53 Yeah. Doesn't look like they touched the package, Jason, at all.
Daniel Dyla (Dynatrace) 00:52:59 And then they update the read me.
given the fact that it's a code owner and it's approved. I'll just go ahead and merge this.
Trent Mick 00:53:16 If Nope, yeah, that'll do. Never mind all good. Yeah, I was just gonna make sure that it's
Daniel Dyla (Dynatrace) 00:53:22 Minor version bump on the 0 dot.
Trent Mick 00:53:24 Because it is changing the the telemetry attributes that are emitted. So it's worth people seeing that.
Marc Pichler (Dynatrace) 00:53:39 I changed it to change the Titan tool.
Daniel Dyla (Dynatrace) 00:53:44 Yeah, as long as you change it before the action actually runs.
Marc Pichler (Dynatrace) 00:53:51 Yes.
Daniel Dyla (Dynatrace) 00:54:29 Pendency.
Wait, who has a Pr open.
Oh, this is adding support for 3, and this is just adding, just bumping the patch version.
So these are not conflicting. Prs, I don't think in any case the tests are still running here.
Interesting. Oh, this is the types to v. 3. But we don't support. Coa. V. 3.
A loader affects a lot of packages still waiting for tests to run.
set to subscript to issue templates providing guidance for end users and others to interact with issues in a measurable way.
Marc Pichler (Dynatrace) 00:56:36 Yeah, they have been using the open telemetry. But to open these sorts of things for our repos, as also the security seek, has used it to update our things. This seems to be a Gc.
Think.
Daniel Dyla (Dynatrace) 00:56:53 Seems fine to me.
yeah, just telling people to use thumbs up whatever seems okay that rerun it. Or do I need to manually rerun this and semantic convention support for Amazon secrets. Manager attribute looks like it just copies it from.
okay. So this just needs review, probably from Jonathan. Again, right?
Yeah.
Marc Pichler (Dynatrace) 00:58:49 One thing.
Daniel Dyla (Dynatrace) 00:58:49 So he was just opened a day ago. I'm not gonna ping him.
Marc Pichler (Dynatrace) 00:58:53 One thing to note is that like the Prs that we're looking at, they are the ones that survived those are the ones that didn't get merged.
So it's not always an indication that somebody is not reviewing anything. It's just built.
You are happy.
Daniel Dyla (Dynatrace) 00:59:15 I did not mean to cast aspersions upon Jonathan. I have seen him being active. That's like I said. I feel bad for him. He's always as the owner of the Aws package. It seems like he's the most requested reviewer most popular.
I see a bunch of stuff in the chat hopefully, people weren't expecting me to.
Trent.
15 min.
Yeah, I was by field. Sorry, Trent.
Trent Mick 00:59:45 Yeah, I feel, yeah, I feel bad.
Make it over.
Daniel Dyla (Dynatrace) 00:59:49 I meant for you to feel bad. I did that on purpose.
Trent Mick 00:59:52 Nice.
Daniel Dyla (Dynatrace) 00:59:54 Okay?
I guess that's it. For today. We're out of time and we're out of Prs and well, not really out of Prs, there's 36 open prs, so if you have time, please review, contribute Prs, beyond that, I guess. We will see you all next week.
Hector Hernandez 01:00:18 Thank you.
Trent Mick 01:00:19 Thanks.
Daniel Dyla (Dynatrace) 01:00:20 Excellent, one.
