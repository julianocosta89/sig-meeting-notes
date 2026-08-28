SIG: Go Compile Time Instrumentation SIG
Date: 2026-08-27
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Dario Castañé** 03:23 Hello, everybody. How are you?
**Azhar Momin** 03:27 I don't renew.
Doing great, I love you.
**Dario Castañé** 03:33 Good to hear that. I'm doing well, too. Yesterday, I was quite busy.
So, I wasn't able to reach everything you linked, but I kind of skimmed that now.
Anyhow.
A pretty… pretty soul-so idea, but it looks good.
**Azhar Momin** 03:52 Okay.
Yeah, I wanted to go over that, there were some open questions in one of the issues, so… Huh.
I want to take a look at that and get your feedback on those as well.
**Dario Castañé** 04:07 Okay, cool.
Okay, so then let's start. Let me share my screen and… Let's go together through this.
I'm just going to move… I'm going to prepare.
One window for this.
Now I lost that first one. Okay, here you are.
Am I missing something? Yeah, I'm missing something.
That further move on.
What is it?
Okay.
Karen is Korean, let's talk.
Nope.
That happened here.
Okay.
It was showing me that.
Okay, no.
**Azhar Momin** 05:43 Yeah.
**Dario Castañé** 05:50 Oh, today… Meeting notes… It's for all the participants to add themselves.
Let me know.
One… Okay, Azhar, everyone, we can go.
Through 100… well, yeah, that one.
**Azhar Momin** 06:53 Yeah, it will open, the list issue on… Compile control.
Nope.
**Dario Castañé** 07:03 If you want.
**Azhar Momin** 07:05 Compile, the fifth issue.
migrate Instrumentation and PKZ.
**Dario Castañé** 07:11 Okay.
**Azhar Momin** 07:12 Yeah.
So… I had asked you about this in our… My, last meeting as well, there are, first open question is, regarding the module path naming.
We do not fully, align with the naming, from GoContrep. We do not have this, OTLC suffix.
So should we have this or not? This is one of the open questions.
And the second question is, we have some dependencies in the Top-level Instrumentation module.
So maybe we should have separate modules for NetHTTP, Kafka, and gRPC, so we will not have this dependency leak problem.
those two, and, I left one more in the comments.
I've shown me also how, minimum OTLC version defined in the rule files at the top level, maybe, so that OTLC can decide whether it can use this instrumentation or not.
I have these three, questions. We can go over these, maybe.
**Dario Castañé** 08:24 Okay.
The auto suffix… I think I didn't catch it properly. You said we didn't, have agreement on that, or did I misunderstood?
**Azhar Momin** 08:39 I mean, GoContrib has this, for example, if you look at the Mongo, MongoDriver path, they have this OTelMongo suffix.
But in our instrumentations, we do not have any suffix, so maybe we can have ORCLC Mongo, or we can leave it as is.
Both are fine dummy.
But, if we do this right now, this won't be a breaking change. If we decide to do this in future sometimes, it will be a breaking change, so that's why I brought it up right now, so it won't be a breaking change right now.
**Dario Castañé** 09:11 Okay, yeah, I see.
**Azhar Momin** 09:22 Beautiful.
**Dario Castañé** 09:23 I'm considering… Because… So… What would, the migrated URL look like? Like, go.opinternly.io, I understand.
**Azhar Momin** 09:48 Yeah, and then…
**Dario Castañé** 09:49 This country part, too.
**Azhar Momin** 09:51 Yeah, we'll have AutoCon trip, maybe.
**Dario Castañé** 09:55 Okay, then we have the auto leak here. So, like, it would be, like, go OpenTelemetry.io, slash country, but slash Instrumentation slash And here is the question, right? If having that auto-leg here, or, at the end.
**Azhar Momin** 10:11 I actually just saw I made a typo in the issue.
But, let me add that here.
Let me send it in the chat, maybe.
**Dario Castañé** 10:24 My main concern is that If we go this way.
URLs are going to be differentiated by just one character.
You know?
Yes, it would be Hotel Mungo and… Autelic Mongol.
**Azhar Momin** 10:42 Yeah.
**Dario Castañé** 10:43 And we… we pronounce it, like, Otelic, like, there is an I or some bubble there, but… It isn't. So, mmm… I don't know, maybe it's fine. I think this is… Something of personal taste in…
**Azhar Momin** 11:01 Yeah.
**Dario Castañé** 11:01 Kinda?
**Azhar Momin** 11:03 Not an important one.
**Dario Castañé** 11:05 No, no, no, but… I think it's good that we tried to align.
But what I want to avoid is causing confusion. So, I would bring this to the… to the Slack channel, like, kind of a poll, and be like, hey, we are considering the two final forms of the URLs, the import URLs, for our contracts.
This is one option, this is the other option. Maybe if you… Consider there is a third option.
Please, state it in the… in the poll.
Like, like this one that you shared in the chat, that would be a third one.
**Azhar Momin** 11:47 Okay, I…
**Dario Castañé** 11:49 I like this one.
Yeah.
It's kind of redundant, but redundancy is good in this case, because it doesn't… lead to confusion. You cannot confuse.
Because you wrote, accidentally, authentic.
You need to write otelic-country.
To actually get something.
**Azhar Momin** 12:14 Yeah.
**Dario Castañé** 12:17 Let's… let's ask in the Slack channel before taking this decision.
But yeah, I agree, we should align. Some way, in some way, we should align.
Okay, perfect.
**Azhar Momin** 12:32 The second is this dependency leak problem.
**Dario Castañé** 12:36 Give me a second, I'm going to…
**Azhar Momin** 12:38 Okay, okay.
**Dario Castañé** 12:39 all over the three different info URLs for contacts.
Okay, no, I cannot assign it to you. Well, I would just write your name behind.
Okay.
Import URLs.
Yeah, sure.
I'm going to just write for Joop.
put here, I read it.
Romo.
Eric option?
The one in the chat.
Where is the tab? Here.
Perfect. Copy link… And the second question.
the dependency leaks. Should we still have a top-level goal mode in Instrumentation currently in potential packages?
Okay, yeah, here I can give on… an answer from experience. DTRES Go works in this way. We have a root Go mode, but it's for, like, the shared… actually shared functionality, resale profiler, etc.
But the contributes, each… each of them, they… they have, its own, GoMode file, so I… I agree. This is the way. Also, Pantherometry ecosystem has crosslink.
to resolve… Internal dependencies, so when you are developing into this repo, you are not, like, having… having a package that depends on another one, and suddenly you are not really testing what you have implemented in the other one.
So, crosslink should be the way to… yeah. We should introduce Crosslink if we want to do this.
**Azhar Momin** 15:16 Okay.
**Dario Castañé** 15:23 Let me copy… Dude… Thank you.
Oh, excuse me.
Secure… I need an order.
And all those things.
Okay, perfect.
I mean, again?
I would… just… make clear in the Slack channel that we are… We have discussed this.
I'm going to do that myself, just to make sure that everybody else is aware of this. So I don't want complaints later, like, hey, why did we… why did we do that?
so, I will do it after the meeting.
**Azhar Momin** 16:26 Okay.
**Dario Castañé** 16:28 Perfect. What else?
**Azhar Momin** 16:30 There's this third issue, comment I left in the same issue.
Regarding the, version, or… hotel seeing the rules file.
**Dario Castañé** 16:42 Here?
**Azhar Momin** 16:43 In the issue number 5, in Compile Engineer.
**Dario Castañé** 16:50 I'll…
**Azhar Momin** 16:51 The same one that you had opened for this.
**Dario Castañé** 16:53 Oh, good. There's one.
**Azhar Momin** 16:56 No, no, it's just…
**Dario Castañé** 16:57 the other one.
Okay.
Yeah, sorry.
**Azhar Momin** 17:01 Yeah.
**Dario Castañé** 17:02 Weapons?
**Azhar Momin** 17:03 Yeah, the last comment there, regarding the minimum OTLC version.
Sorry, my internet reconnected.
**Dario Castañé** 17:25 No, don't worry, it's me that didn't follow what you said.
your internet is fine to me. So yeah, Okay, yeah.
I agree.
**Azhar Momin** 17:43 I mean… Yeah, because right now, we do not have this. And we can also use this, this for… this in the Ecosystem Explorer later, so the registry can automatically insert the, minimum OTLC version needed by, repo.
**Dario Castañé** 18:05 Yeah, like this one. No, this is the field that you're suggesting.
**Azhar Momin** 18:09 Yeah, this is for the whole repository, and then this will be automatically inferred from all the instrumentation in the repository.
**Dario Castañé** 18:21 Yep, it looks good to me.
This is for the whole repository.
**Azhar Momin** 18:26 Yes.
And I was thinking we should also have… yeah, I was thinking we should also have all the single instrumentation package as well.
**Dario Castañé** 18:39 Okay, we can do both.
Yep.
But for starters, I think it's okay to have it.
At repository level.
we are always on time. I mean, if… If it's possible to implement at first, it's okay too.
**Azhar Momin** 18:59 I mean, yeah, if we have for an Instrumentation package, then for the whole repository, it can automatically insert that.
**Dario Castañé** 19:07 Okay, then yeah.
Yep.
**Azhar Momin** 19:16 Yeah, I'm…
**Dario Castañé** 19:16 I think.
**Azhar Momin** 19:17 real time.
**Dario Castañé** 19:17 right direction.
**Azhar Momin** 19:18 I'll create an issue for this in AutoCD for them.
**Dario Castañé** 19:22 Perfect.
Wonderful. I also saw…
**Azhar Momin** 19:28 I wanted you to look at this, these issues that I created are… because I created this with the help of an agent, maybe I missed some things.
Cool.
If you can take a look at the sub-issues.
**Dario Castañé** 19:45 To these sub-issues, okay.
**Azhar Momin** 19:48 Yes.
**Dario Castañé** 19:48 Okay.
And this one we already reviewed, so I'm going to skip it.
We look fine.
the basic structure… Great.
Initial set was a pentarametric your Compile.
Ratme… contributors, Asian… Security, right, policy testing, semantic conventions… Yeah. Okay.
Actually… Now that I see this… Yeah, we cannot create the other kind of URLs, right?
Because the other ones would be… will be a… There will be a conflict.
If we tried to do… This, this would be our conf…
**Azhar Momin** 20:49 Yeah, we cannot do this. Yeah, I'm in OTLC.
Oh, this.
**Dario Castañé** 20:53 Yeah, we are like this, yeah. Yeah, then, not even a poll, let's go ahead, yeah. Let's do a hotel concert. We don't have so many options, and let's do, like, here, like… With the Autelic Mobile, yeah.
Yeah, now I saw it more clearly than initially.
Yep, let's go ahead with this. Let me update.
Comfort.
There you go on… Perfect.
In this way, we don't block anything.
Of the initial setup.
Yep.
Let's do this… And let's align on the suffix, and that's all.
No need for the poll.
We are following the ecosystem as it is.
Okay This one looks good to me.
Anything that you want to discuss here?
**Azhar Momin** 22:11 No, no, no, I only hope the feedback on the initial issues.
**Dario Castañé** 22:16 It's… really fine. I think it's a well-defined.
**Azhar Momin** 22:21 Okay.
**Dario Castañé** 22:21 issue, step by step, that's something that I appreciate.
So, let's go for the next one. Yeah, I am skipping the migrating Instrumentation one, but let me double check.
What? Yeah.
Maybe it needs some updating?
Just to make sure that we include what we have discussed.
In these three open questions.
But that's all.
Okay.
Perfect.
Migrate Instrumentation? Okay, this is the same one.
Good day, John.
No.
This and this, okay.
Set up the continuous integration workflows and test infrastructure, followed by country repositories, set up GitHub Actions, migrate each end-to-end.
Migrate integration to set up release scripts.
My only concern is this… this is a very large, item.
**Azhar Momin** 23:40 Fair enough.
So I need to drill them down into some of the shoes, maybe.
**Dario Castañé** 23:45 Yeah.
Okay, bye.
Apart from that, okay.
First country release, another intervention. Once the country reports test and ready, cut the release and open another week to consume the current instrumentation. Contact release, update utility to consume Instrumentation… I'm dreaming. I'm dreaming for the day.
We'll get rid of the bundle.
Yep.
Everything looks good.
**Azhar Momin** 24:19 Okay.
**Dario Castañé** 24:19 Is there anything you want more feedback about?
**Azhar Momin** 24:23 No, this is all, end of 1023 on Ecosystem Explorer.
I'd appreciate if you could look, Look at that as well.
**Dario Castañé** 24:35 Yep.
Right away.
This is the one. I'm going to change the view.
Okay.
Yeah, I read this… A little bit quickly.
But I put the focus on what you said on the message. It was, consumption.
Your portfolio looks fine to me, but let's go from the top.
Do we document all the lines of registry layout… that it consumes a single signed Asian article per repository release.
Okay, delete a specific registry is generated at… Okay, probably this has been answered before, but… How does… Autelic know what registry hash it needs to pull.
**Azhar Momin** 25:52 Yeah, the catalog contains the registry hashes, so it will first read the catalog, and based on that, it will load the registry.
**Dario Castañé** 26:01 Okay.
Yeah, I was going to answer myself, right, if I read the next section.
Okay, thanks.
Oh, okay, I see.
**Azhar Momin** 26:22 And in future, we can have other repositories in here. For example, GoContrac. If we add, rules there, then it will also be automatically taken by OTC.
**Dario Castañé** 26:33 Nice.
Okay.
Yeah, because I was going to ask, I see this supports multiple repositories by this schema, so…
**Azhar Momin** 26:43 Excuse me.
**Dario Castañé** 26:46 That's cool.
Considerated metadata for the specific repository for its contents, and reference implementation.
Okay.
Catching include fields.
your dream.
when we… Split.
contracts from Autelic.
Instrumentation are going to land here anyway, right? But the URL path is going to be just the one for the contraries.
**Azhar Momin** 27:35 Yes.
**Dario Castañé** 27:37 Okay.
It doesn't matter that they are to… well, actually, yeah.
I'm going to answer myself again, yeah, because they're here in the example.
you are pointing to the open telemetry, Autel HCDB, so yeah, this is a different report.
Okay.
Cash computational immutability… I guess this is, like, shared with… also with, with the rest of the OpenTermit ecosystem, I assume…
**Azhar Momin** 28:07 vicious.
**Dario Castañé** 28:09 It's a little copy of what they do in the other repos. Okay.
Okay… to be fine… Consumption workflow.
Okay, perfect.
Okay, authentic V1 and V2.
So… If we ever have a B2, What will happen is that Athletic itself will be the one deciding, I want to go against V1 or V2, right?
**Azhar Momin** 29:20 Yes.
**Dario Castañé** 29:21 Okay, yup.
Sounds perfect.
Okay, Let me just double-check something. The application period. When a new schema version is released, the whole directory is frozen. It will remain on the CDM for a grace period. Okay, so all the latest, continue fetch.
Yeah.
And this is just code.
**Azhar Momin** 29:59 Is it difficult.
**Dario Castañé** 30:02 Okay, yeah.
I'm not going through it now. Probably, as I see, it's just adding a few things.
Here and there, so… looks…
**Azhar Momin** 30:14 Yes.
**Dario Castañé** 30:16 Looks good.
Also known recruitment.
Thank you for taking care of this.
That one, yeah.
Perfect. So… I guess the ecosystem… slash country people isn't block.
We can go forward.
**Azhar Momin** 30:49 Good to work out.
Yeah, I was assigned Bonsai to myself, and… I'm gonna reach you to someone. We are also in the meeting right now.
And then we'll.
**Dario Castañé** 30:59 Okay, yeah.
**Azhar Momin** 31:00 And the migration work with that?
**Dario Castañé** 31:03 Yeah. You go… you go forward, and if anybody wants and can help you.
You coordinate, and that we find.
Nice. So… anything else?
I don't know if we have other valid points for the agenda.
**Azhar Momin** 31:25 Yeah, no more topics from my side, but there's, I think, the lawsuit migration still in the meeting notes.
But we need Alibaba people for those.
I haven't turned.
**Dario Castañé** 31:40 Yep.
Maybe something we should price on the… on the slide third.
I'm going to do that.
I'm going to just… Make everybody aware of the decisions from here.
And also, make sure if… if Alibaba people are… are… progressing or not on the long shoot migration, what they… I mean, Datalog is also migrating already.
But it's… we don't have a definitive timeline, so… I'm not going to blame them for not having their own pangolin already fine, because I know they have quite A significant amount of intermissions, too.
Okay, so I'm going to delete this one… And, yeah.
Anybody else has… Any subject to discuss?
I'm going once… Going twice?
Point twice. Okay.
So, I guess we can cut the meeting short.
**Azhar Momin** 32:58 Hmm.
**Dario Castañé** 33:00 Okay, thank you very much.
Sure, I'm.
**Azhar Momin** 33:02 Good, thank you.
**Dario Castañé** 33:03 And thank you for all the contributions. Yeah.
