SIG: OpenTelemetry C/C++ SIG
Date: 2025-06-16
Duration: 52 minutes
Zoom Recording URL: https://zoom.us/rec/share/ZasfGTWPDb70YjIyKUYs_YPNCbnpm_G8gABze2SbM2_80GsRlOFp1ZLxXzE72ov9.7xullNS7qhXqIWvg
============================================================

## Zoom Recording Transcript

**Rafael Roquetto** 01:12 Hi! There!
**Marc Alff [MySQL]** 01:17 Oh, Hello! Raphael!
**Rafael Roquetto** 01:19 Hi! How are you?
**Marc Alff [MySQL]** 01:20 Not too bad! Thanks for joining.
**Rafael Roquetto** 01:24 No worries. Yeah. So I'm not directly involved
with the the c plus plus stuff. I'm working on the evpf side of things.
But yeah, my, my background is you actually embedded in C, plus, plus, I thought I would join
and see what's going on around this site.
**Marc Alff [MySQL]** 01:44 Okay.
Hi, Tom.
**Tom Tan** 01:49 Hi! Mark Hey Russell.
**Rafael Roquetto** 01:53 Hi.
**Marc Alff [MySQL]** 02:04 I think I saw a message from Pranav that he cannot make it today.
**Tom Tan** 02:11 Yeah.
Yeah. Assume that Lita will join.
**Marc Alff [MySQL]** 02:15 Okay, yeah.
Highlighted.
**Lalit** 02:33 Hi, mark.
**Tom Tan** 02:42 You are on mute, you are muted. But
**Lalit** 02:48 Yeah, I'm I'm audible right?
**Tom Tan** 02:50 I can hear you. Yeah.
**Marc Alff [MySQL]** 02:52 Yes, we can.
**Lalit** 02:53 Yeah. Yeah. Yeah. Okay, thanks.
**Marc Alff [MySQL]** 02:58 And I don't know if
and Asan can make it so I guess we can start.
**Tom Tan** 03:07 Okay.
**Marc Alff [MySQL]** 03:11 Raphael, since you just joined, do you have any specific topic or questions for us? You want to cover.
**Rafael Roquetto** 03:19 No, I just thought I would, you know, join to see what's going on. I eventually I wanna get involved.
But for now I think it just. I just should. I just watching
and see how I can help. Yeah.
**Marc Alff [MySQL]** 03:33 Okay.
Hi, Duke.
**Doug Barker** 03:36 Hey! Mark! Hey! Everyone.
**Lalit** 03:40 Part of.
**Marc Alff [MySQL]** 03:43 Okay, well, I guess we can. We can start here then. I don't have any specific points to discuss. Usually I had a couple of things in that list.
But today I don't have a lot.
One thing. So on the issue side, things has been very quiet except for a few issues that I just raised. So we can go
quickly.
And I guess the main discussion would be on code reviews.
Does any one of you have any specific topic or or
area that you want to discuss before we dive into details.
**Lalit** 04:26 No! From my side.
**Tom Tan** 04:29 And I have a quick one. Do you have an like any? Apply for new release? I think it.
We end of June or.
**Marc Alff [MySQL]** 04:38 I think we just made one in
yeah end of May. So I guess end of June or early July, we should make one.
**Tom Tan** 04:59 Okay.
**Marc Alff [MySQL]** 05:03 Yeah, we are a few commits already. So yeah, we can.
And beside, there's also some deprecations which have been announced for a long time which are coming.
especially this one.
So I guess we should make a release. Just that.
we'll remove this thing and and
do the removal as planned. Otherwise, if we wait, if we wait for too long, I mean people will never get rid of us.
**Tom Tan** 05:34 Okay.
**Marc Alff [MySQL]** 05:35 Yeah, it was.
And for July.
do you have any specific constraints on when or this is needed, and possibly with what content.
**Tom Tan** 05:55 I think I I don't have. But maybe we, we can create an issue on the new release and then add items. There.
**Marc Alff [MySQL]** 06:02 For for central tracking.
Yeah, I I will do that. As for the previous releases. Yes.
yeah. So yeah, I guess we can. We can do something like early July, and then I don't know for you. But typically this is also the period of summer vacations. So I don't know if we will have a lot of things for August. Maybe we can wait on for September for the release. After that
we'll see depending on the.
**Tom Tan** 06:31 Okay.
**Marc Alff [MySQL]** 06:31 On the changes that we have.
**Tom Tan** 06:35 Sounds good.
**Marc Alff [MySQL]** 06:36 Okay.
sorry about cough.
as I said earlier, we don't have any new issues. The only thing we have is things I filed just to get rid of very old preview flags that we have.
typically, these preview flags have been there for quite some time, and I think it's it's time to basically promote them.
So for all of them, the the ideas that
so some feature was added a while ago. In that case, like, yeah, 2 years ago.
but the feature this thing in C make is disabled by default. So one thing we can do is enable that by default.
So it's a it's a minor change. And
so people will see the feature. If they don't do anything, and if there is an issue they can still
change their their microphone and and disable that.
So it's not that that risky, I think.
And then what we can do is mark the flag itself as deprecated, and then merge later remove it.
And upon removal, of course, we need to make sure that everything is stable and that we don't have
bugs reported against that feature, and people complaining that hey? When it is enabled, I have this blah blah, and
just make sure that everything is stable and and fine when by the time we finally remove the flag itself.
So I just find a couple of
issues for a couple of flags. There are. There are more flags that exist, but those are the oldest one. I think that we have
2.
I'm suggesting that we we enable that at some point
any comments on or concerns on that, or
and the follow up question would be
Do you think we can do that for
basically the next release? If we if we ship something on in July.
like only those flags enabled by default.
**Tom Tan** 09:05 What is the 3rd one for? I'm wondering I haven't checked and transact secure logging.
**Marc Alff [MySQL]** 09:11 Yeah, this was a feature that was enabled in, implemented in curl itself to log when things are.
What was that?
I think it was basically to print things in the log file to explain what is curl doing, for to debug things like when there is a failure, say, Oh.
curve failed failed because of that because of.
I don't recall all the details. But it was basically a debugging feature.
**Tom Tan** 09:49 I see.
**Marc Alff [MySQL]** 09:50 So that when you have basically typically, you have an exporter, an Otlp exporter that fails in Http, and you know that. Yes, it failed. But you don't know why. And with this feature you can have more details about what exactly, was the problem.
So it's mostly to debug things
print like print the error receipt from the server things like that to see if it contains information explaining the the failure itself.
**Tom Tan** 10:22 Okay? Or I think you you may be more familiar on this one, or like does enable it by default. No
looks good to you. Well.
**Lalit** 10:31 Let me just have a look into that. I did review it. But probably
if we I mean okay, like to see like.
sorry if we enable it by default. It won't.
It won't add some enable some debugs right to get printed by default. It's still we still need to enable those right.
**Marc Alff [MySQL]** 10:55 Yes, so to. If we enable the feature, flag, it just compile the code.
But if I
correctly, there's still a runtime flag to say whether people want to debug in debug information or not, and this one is disabled.
so I don't see any any risk with that.
**Tom Tan** 11:15 So you option enabled we just build like by default. If the user don't make any code change.
there will be no behavior change. And just to get some more of your functions compiled into it right.
**Marc Alff [MySQL]** 11:29 Alright!
**Tom Tan** 11:34 Okay, which? So we just make the function ready for the user to call.
**Marc Alff [MySQL]** 11:38 Yeah, so this, this is from memory, because this is.
**Lalit** 11:42 Quite old, also.
**Marc Alff [MySQL]** 11:45 Yeah, November last year.
But from from what I recall, it's it's debugging code that also needs to be able at at one time.
**Lalit** 11:58 This condition check is not under any mutex or anything like that, whether it's log enabled or not.
**Marc Alff [MySQL]** 12:04 No, no.
**Lalit** 12:05 What was it called?
At least add some conditional check
just want to ensure that that won't change the performance of anything like that.
**Marc Alff [MySQL]** 12:17 Not that I recall.
**Lalit** 12:19 Okay.
**Marc Alff [MySQL]** 12:22 So of course, for each
basically for each of those flags we can, we can discuss if there are any risk, like okay or
yeah, or mutexes or whatnot.
**Lalit** 12:34 Yeah, let's probably discuss in these issues here.
**Marc Alff [MySQL]** 12:37 Okay,
Http compression. This is also just to add support for code, which is to do some Jz compression and things like that. That was not implemented earlier.
So it's a
likewise it's a new feature. I mean, if you don't use compression today, there is no reason why this code would introduce some some bugs and unstable things.
Likewise the job. PC, this is to have more security features in
in in the socket connection itself.
But if today, if you have an application running, it is not using that.
So the the code added will be just that code. I think.
So. Yeah, let let's
if there are any specific risk, we can discuss that in every issue, but from memory for those I don't think there are any
this is assigned to me currently. So we'll probably do a Pr. For for each of those things.
So expect to see a couple of Prs coming.
**Tom Tan** 13:58 Okay.
**Marc Alff [MySQL]** 14:04 And this is it for new issues. So I guess we can go through Pielsman.
Oh, by the way, I saw that a couple of Prs got merged today as well. So thanks for that.
this one. So this is typically an example of some old feature flag that we just forgot about
like this feature flag was there, but not used anywhere. So it's a
and and beside, it was still experimental. So this is safe to remove, and we should, we should do that just to maintain the code base.
**Tom Tan** 14:37 Oh, like, I have a question like, How do you really
remove the preview flag like we have a process like to promote preview feature into stable, and then maybe we should mark the option as deprecated for one or 2 releases or notify the user.
**Marc Alff [MySQL]** 14:57 So in in general. Yes, except that for this one this preview feature affected the Abi, and this was done before the Abi v. 2. Flag.
So, in fact, this this preview feature was later replaced by the Abi v. 2, so it never got promoted to
to an official stable flag that need to be deprecated and removed. It stayed experimental from the from the start.
**Tom Tan** 15:26 Okay.
Okay. Yeah.
**Marc Alff [MySQL]** 15:41 Do you have any preference for which order to look at the the Prs that we have?
So basically, we have a lot of configuration ones that we can probably discuss together.
and some scenic changes from Doug.
**Tom Tan** 16:08 Unless they make changes during draft.
Maybe we should.
**Marc Alff [MySQL]** 16:13 Yeah, that's right.
**Doug Barker** 16:16 Yeah, I moved it back to draft based on the last meeting. So I'll break that up into smaller Prs and leave this one around.
**Marc Alff [MySQL]** 16:22 Oh, yeah, that was due to due to size.
**Doug Barker** 16:26 And since then it looks like.
**Marc Alff [MySQL]** 16:29 Oh, yeah, this is the. This is a minor collision on the setup team make, I guess, but also changed recently. Yeah, so should be trivial to to fix.
**Doug Barker** 16:39 Okay.
**Marc Alff [MySQL]** 16:40 Okay.
so I would like to discuss file configuration in general.
So I saw that you had some
comments on Vspr, but it's a comment which is general in general.
Yeah, which which apply to the whole schema. So it's a general comment.
**Lalit** 17:08 Yes.
**Marc Alff [MySQL]** 17:11 So for the let's see for the context.
basically, there is a yaml schema with a given structure. And this Pr introduce introduces some files
which are c plus plus classes that represent the yammer nodes that were in the schema.
So the top top level node in the schema is the open telemetry configuration as a whole.
and the C plus plus representation for it says, Okay, a configuration consists of
some properties like for the file format, which is saying, there is a disabled flag.
and then all the different nodes that are below it. So obviously the configuration from the entire SDK consists of the tracer provider, configuration for traces, then likewise for for metrics, likewise for loggers, and so on, and so on.
So this was a minor comment with
with the concept in general, that of O. 2. Instrumentation in all the Sigs, which is why it is present in the schema.
But, as far as I know c plus plus doesn't support auto instrumentation. So this is why I chose to not parse that part of the schema. So if there is any node that describe auto instrumentation.
it will just not be passed. And the other reason for that also is that I'm focusing so far only on the all the attributes in the schema which are marked as stable.
because we know of that structure which will stay, as is but other nodes are also marked in development and may change. So it's more risky to to implement code for that right away.
Let me show you.
**Lalit** 19:02 No, actually, I thought, it's basically instrumentation scope. That's what I commented on that.
**Marc Alff [MySQL]** 19:07 Okay?
Oh, wow!
So this is the schema report itself with a schema.
And this is the instrumentation. So the schema define an instrumentation node, which is oh.
well, I don't remember where my name is, but it's it's flagged as experimental and as experimental in the name. And then there are some placeholders for every
yeah, every
seek there. So we can have general properties to that, apply to everyone. And then C, plus plus specific properties for C plus plus instrumentation.
Java properties for Java, specific instrumentation, and so on.
**Lalit** 20:01 Okay.
**Marc Alff [MySQL]** 20:03 But the idea is that there is no point in passing that part of the schema, because we will do nothing with it anyway.
**Lalit** 20:09 Yeah.
**Marc Alff [MySQL]** 20:10 And if later that that becomes important, then of course, we can add that.
**Lalit** 20:15 Make, sense. Yeah, thanks.
**Marc Alff [MySQL]** 20:19 And the other big big thing is
So yes, as you have, as you have noticed, the c plus plus class to represent a yaml node
very is very resemble the yaml node itself, which raise the question whether we can and should generate this automatically, as opposed to write manual code for that.
Typical example like this is a span limit. There is a yaml node that contain exactly those
those attributes.
So we can never define a class like with 10 lines
with a couple of attributes in it, or we can
find find a tool and have a process to generate that code automatically from the the spend limit configuration. Let me see if we can find it.
So this is the schema for the spanimeter, and you see.
It says, we have an integral which is attribute, length, limit, attribute, count, limit, blah, blah.
and those are exactly the same one that we see here.
So no story short.
I consider to generate that automatically. But I think it will be actually very complicated to actually get that working. To start with.
**Lalit** 21:56 Okay.
**Marc Alff [MySQL]** 21:57 And also
it might not be flexible after that, because once we have generated code, it becomes much complicated to to address special cases, because there is always something that just does not fit in the schema.
**Lalit** 22:11 Yeah.
**Marc Alff [MySQL]** 22:16 So I think, yeah, this is basically my my comment here.
**Lalit** 22:22 Okay, yeah, thanks. I think that should
probably let me go through that. And I think I agree. I mean, it's probably automating. It will not be very smooth process.
In general, we do have have lots of conditionals, and in general.
**Marc Alff [MySQL]** 22:39 And also, even even if we can do that.
One thing that I found working on that whole thing is that the C plus plus world in in general is extremely poor when it comes to when it comes to Yaml.
I found only 2 parsers written in C plus, plus.
and one of them does just doesn't work. So
there is only one password which is suitable that can be used. So if we.
**Lalit** 23:08 Yeah. So yeah, now, I remember, I think we did discuss about this, and probably you did shortly some past parsers. Yeah.
**Marc Alff [MySQL]** 23:16 Awesome.
**Lalit** 23:16 Oh, yeah. Yeah. Oh, yeah.
**Marc Alff [MySQL]** 23:19 So I've not looked at tools. But, -
the issue is 1st 1 1st to find one which might not be simple, even if we find one. I'm guessing that the generated code will come with dependencies at one time
asking the dependency on that parcel or this parcel, or those classes which also is the question of whether the code is good enough to be in open elementary. Cpp. What are the license there? What are the dependencies? And so on. So it's a
it's a it's a big black box. If we opened it, there's a lot of voice calls over.
**Lalit** 23:58 Okay.
**Marc Alff [MySQL]** 24:03 So yeah, take take your time to to look at the comment. And
**Lalit** 24:07 Sure.
**Marc Alff [MySQL]** 24:08 And see if you have a
if you if you agree, or if you have a proposal for a tool or things like that.
**Lalit** 24:16 Yeah, sure.
**Marc Alff [MySQL]** 24:23 But yeah, we, I guess we need to decide on that, because, obviously, it affects all the older classes for the model. So
not not only those those Prs, but everything else which is coming with it.
**Lalit** 24:41 Yes.
**Marc Alff [MySQL]** 24:54 Oh.
so, Doug, I know that you you looked at that code already because you approved it. Thanks for that.
Tom, did. You had a chance also to look at the the configuration thing or or not. Yet.
**Tom Tan** 25:10 Hello, not yet. Yeah.
I will get some time to look. Look. Maybe some of this.
**Marc Alff [MySQL]** 25:16 Okay.
can, can you?
So basically, because this is a big thing, I I'm waiting to have
consensus and many, many approvals on the on the Claire itself.
So do you know when you will have time to look at it of land and Tom to
to see basically what I'm looking at is
to to decide if we can merge it or not.
**Tom Tan** 25:52 And do this like the series of this Pr peers have a dependency.
or like either one can be merged, and should or should- should one or
all of them like, if we merge one, should we novic
all of them before the next release?
**Marc Alff [MySQL]** 26:08 No.
they can be merged independently and even out of order, because it's only adding files which are not used yet.
And so it's basically adding a file which will be that code in the in the Gitry, because no, nothing is using it yet. So there is no risk for that.
The question is especially for the decision to generate code or not.
I guess we have to take it soon, because otherwise it needs.
There's some more work. If we if we decide to try to generate code, for example.
**Tom Tan** 26:43 Okay, that sounds good. I think.
**Marc Alff [MySQL]** 26:46 Okay.
**Tom Tan** 26:46 So yeah, from my side, I think I can. This week or the next week I will try to get some time to
to to more review on this this series. Prs.
okay, not sure, Nandi, or comment.
**Lalit** 27:01 Yeah, I'll at least go through this just to, because it's important to at least have an agreement on whether we need auto generation or not that probably I'll do it hopefully in couple of in these couple of days. Just go through this and apart from that, on this Prs, I mean, what exactly should you think that we should focus? It's basically ensuring that this, that the schemas are in sync with the code or.
**Marc Alff [MySQL]** 27:26 This is exactly what the Pr is about is to say, we have. We have a schema that says we have a simple span processor.
And then we have a class that describes a similar span processor, and the only thing it contains is an exporter.
**Lalit** 27:43 Okay.
**Marc Alff [MySQL]** 27:44 So
it's it's basically to make sure that if there is a schema that says, Oh, there is a property named Foo.
then we have the C plus plus class that contains a member to represent food. This is about it. Those classes are just pure data. They contain no load.
**Lalit** 28:02 Yeah, yeah. Got it? Yeah, sure. No problem. Yeah.
Got it. I think I should be able to see by this week.
by end of this week should be able to review them.
Prs. Which you have created as of now.
**Marc Alff [MySQL]** 28:21 Okay, thanks.
So this cover was 4. This one
it's approved. Already I saw that you had a comment that we need to
put a workload changelog entry with a migration step, which I think is a good idea. So I will do that.
And the the good thing is that since it was documented earlier in the deprecated part, we have that.
So we have. Yeah, we have the the migration step. So.
**Lalit** 29:01 Yeah, you too.
**Marc Alff [MySQL]** 29:03 Yeah, I will just pick that and put that in as an important note in the change log.
**Lalit** 29:09 Yeah.
**Marc Alff [MySQL]** 29:16 So
yes, now we get to see make so yes, so so, Doug, if you, if you can split that into independent parts that will simplify the review a lot
as well as we discussed earlier.
**Doug Barker** 29:36 Sounds good.
**Marc Alff [MySQL]** 29:37 Okay, and what else do we have?
So those 2, I recall, are related
**Lalit** 29:51 So.
**Marc Alff [MySQL]** 29:52 No, maybe not those 2. But so this one.
So was it a Ci check?
Yeah, it looks like it.
So, Tom, I don't. I don't remember. Do do we still need this, or is it?
Was it to debug a bit failure? Only.
**Tom Tan** 30:26 I think we still need this, still, some cases not covered by existing pipeline. So I just need to have some more time on this.
**Marc Alff [MySQL]** 30:36 Okay?
So yes. Well.
whenever you feel it's ready, just hmm.
Change the draft status, then, so that we can, we can review it.
**Tom Tan** 30:50 Yeah, sure.
**Marc Alff [MySQL]** 30:51 Okay.
this is a change for a moment.
And
yeah, it's totally ready to see make. So it's a good thing that Doug can comment on that, because I don't. I can't.
**Doug Barker** 31:25 Yeah, I've just requested those changes, so I'll try to get owent on slack if he doesn't reply soon, and.
**Marc Alff [MySQL]** 31:34 It's so.
I guess it's very unlikely to get it on slack.
1st of all, there is a huge time difference, because it's in China, and
so he's pretty good at replying and discussing things as in comments, I mean as comments on an issue.
I don't think I ever discuss things with him in slack, directly or
so. Yeah, there's the the time zone, for one thing, and also
is so. His English is sometimes a bit would be tough to understand.
So sometimes you have to wait between the lines to actually see what you what you actually mean.
But otherwise it's a i mean, he's
He has a lot of from from experience. He has a lot of skills and and can can detect things. Sometimes it's hard to see what he means if he makes a comment. So keep keep that in mind also.
**Doug Barker** 32:46 Okay, sounds good. You have
put a pretty comprehensive comment there and then requested these specific changes. So I think if we're able to agree on that. Then we can get this merged and hopefully this week.
**Marc Alff [MySQL]** 32:57 Okay, good.
So this one was related, I guess.
So what's the plan? Is it? V. So this is Ci, only, you know. Vcc.
so do you plan to add that Ci changes to the main Pr for moment? Or
or is it just to debug things so.
**Doug Barker** 33:36 Yeah, I'm expecting that once once his change gets merged, then we'll close this. So he already cherry picked, I think, one of the commits from this Pr.
**Marc Alff [MySQL]** 33:46 Okay.
**Doug Barker** 33:48 This one is definitely not intended to be merged. It was really there to demonstrate the problems.
**Marc Alff [MySQL]** 33:53 Okay, sorry.
So
yeah. And so much flag. I was about to ask about that. But I I saw that it is there already. So
that's great, because it's otherwise. It gets confusing. I mean, looking at this externally, you don't know which Pr is doing what and
it's harder to follow sometimes so great
term. So this one was also so it is a very tiny change, like one line.
**Tom Tan** 34:37 do so.
**Marc Alff [MySQL]** 34:38 Which would we do with it?
**Tom Tan** 34:43 Excuse me,
I haven't been. Follow up this one, maybe if it let me close this one, for now I think I haven't assigned any need for this one, for now.
**Marc Alff [MySQL]** 34:54 Okay.
**Tom Tan** 34:55 Yeah.
**Marc Alff [MySQL]** 34:56 Because it. It's it's so simple that if we need it again, we can, we can create.
**Tom Tan** 35:01 Yeah.
**Marc Alff [MySQL]** 35:02 And and have it reviewed and merged. It's a
what I would like to try to avoid is just having this one hanging forever.
**Tom Tan** 35:10 Okay, yeah, yeah.
**Marc Alff [MySQL]** 35:22 this one. So I've seen some some. Well, I've seen some change in dates where it was recently changed, but I haven't seen what the change was about. Exactly.
Lali, do you know, have you made any comment on this or.
**Lalit** 35:38 I? Yeah, it's it's on me, I mean, I have to kind of persuade this author of the Pr
to to fix the merge conflicts I pinged him. I think he's very busy, so probably let me remind him once again.
**Marc Alff [MySQL]** 35:55 Okay.
**Lalit** 35:56 So. So I thought of taking this Pr, because this is an important change to make
cardinality limit, as at least in C plus plus. We don't have the support of having a cardinality limit as configurable. Right now we have a hard coding of 2,000
attributes, and it's important change, and let me see if he can. He still agrees on
completing it. Otherwise, at least I can pull one of the one part of this Pr.
Of making this configurable and raise up here, let me let me just check with him once more.
**Marc Alff [MySQL]** 36:35 Okay.
**Lalit** 36:36 Yeah.
**Marc Alff [MySQL]** 36:38 Yeah, because I mean, when it comes to the metrics code.
it's I guess you're you're the one who knows that part of the best. So.
**Lalit** 36:48 Yeah, yeah, let me let me just
have a check with him. Otherwise I'll I'll take it up.
**Marc Alff [MySQL]** 36:54 Because if if I try to merge that, something will happen.
**Lalit** 36:59 Yeah, yeah, no, no. Let him do that. Yeah, that's that's probably good to get it done from him.
**Marc Alff [MySQL]** 37:05 Okay.
Sounds good.
Oh, by the way, I don't know if you remember. But what was it?
We had a Pr, some from someone complaining about some
we had someone who raised the Pr. About some race conditions recently, and the CAD for that was approved and the Pr. Was merged. I cannot.
I cannot find it right now. I don't remember which one it was.
See?
Yeah, this one.
**Lalit** 38:01 Okay.
**Marc Alff [MySQL]** 38:02 So yeah. Cla was approved, and so the fix was merged.
It's so.
The good news is that 1st of all, we have a fix, but the the even better news.
**Lalit** 38:13 Similar changes required.
**Marc Alff [MySQL]** 38:16 Yeah, so we can, we can. We should look at similar changes but also now that series signed, I'm hoping that we may get some over contribution from that guy.
**Lalit** 38:29 Okay. Yeah.
**Marc Alff [MySQL]** 38:32 Well, you never know, but that's it's always easier when all the yeah.
But paperwork butternuck is is cleared.
Anyway. That was a side note.
testing framework and.
**Lalit** 38:50 No, no, we need not open it here.
See.
**Marc Alff [MySQL]** 38:54 And and this one. So for those who don't know. So
this one is a huge Pr that contains a lot of work.
and what I'm doing is I'm taking bits and pieces of that huge Pr to make small ones to merge it by part.
So all the file configuration, something. The code which is there is, in fact, extracted from this one and this one. So if you, if you want to do code, review, you can look at the small part. If you want to do testing or
look at execution in a debugger, or execute some unit tests, you should look at the big one, because then this one will. The big one will build and run
with all the make files and all the all the tests. But but are there.
Just so, you know.
**Lalit** 39:43 Okay. Yeah. Thanks.
**Marc Alff [MySQL]** 39:47 And I guess this is it, for all the Pr's
Anything else you want to discuss in general.
**Lalit** 40:01 Not not from this, but probably I had some sort of question for Raphael, I mean just in case, I mean, if he has an answer like he's. You're from Grafana right, Raphael.
**Rafael Roquetto** 40:14 That's yeah. That's right. Yeah.
**Lalit** 40:15 I mean, I just wanted to check like I know that Grafana has done lots of work on auto instrumentation in Bela. Is it something
which has some support for C plus plus and trust in general, where we can auto instrument, an application written in c plus plus and trust. If the symbols.
Dude, you know.
**Rafael Roquetto** 40:35 To an extent I think the C plus plus, or any like native application in that regard.
You would get metrics, and you would get very elementary.
maybe traces very limited instrumentation. The biggest issue
is knowing to which symbols to hook yes, to extract things, and because.
you know, in C plus plus. There is no such like standard framework, like, for instance, we support Nodejs. We don't support Javascript or.
**Lalit** 41:10 Okay.
**Rafael Roquetto** 41:10 Support Java, because there is some sort of standard Api that everyone is using when it comes to rust and C plus, plus, you know it's all over the place
but it's you know, if you have anything in mind in that regard, it's you know, we could look into supporting it.
**Lalit** 41:30 Okay, no. I mean, I was just thinking like, in case there is an application. I mean the release which has a symbol. I mean symbol table coming part of the application. But or maybe externally, if it is supplied.
can those symbols be, or to be instrumented into instrumented using Epp, or something or not.
**Rafael Roquetto** 41:50 Yes, I mean, we would need to do some work to improve.
Got it? Yeah.
But yes, yes, we do that. For go, for instance.
**Lalit** 41:58 Okay? And how about in go like Google already? Has some some metadata for the symbols? Right? Even though it's a compiled.
So.
**Rafael Roquetto** 42:05 Yes.
**Lalit** 42:06 And that is being that. Okay.
okay, so that is that is utilized by Bella. Is that.
**Rafael Roquetto** 42:16 Yes, so for go we so bela
for go it. It has its like own subsystem, and we call it tracer where we. It does its own thing. And we use those symbols for a lot of our other things. And that would include like C plus plus programs.
We mostly rely on on the kernel stuff only. So we're not really looking to symbols
from a particular software. But we most of Bela work, especially for metrics. Does a lot of a lot of that data get gathering at the kernel level. So it really doesn't matter which application you or you're using. It's more when it comes to traces and face contacts. Propagation. That's when we need a little application. Specific knowledge
**Lalit** 43:06 Yeah, exactly. Yeah, yeah. I was more interested from distributed, distributed tracing perspective. And at least how the context gets propagated across the network. But I think that's a different discussion, probably. I was just thinking I was interested how we can do that for C, plus plus and rest. But it all depends on again, probably, which Http framework is being used, and we have to even instrument that. But yeah.
**Rafael Roquetto** 43:32 Exactly.
**Lalit** 43:34 Yes.
**Rafael Roquetto** 43:34 Even like with Node Nodejs. We we just replace the code. Because, you know, no Js is written c plus, plus, and they do export symbols.
But okay, a lot of.
And we had like new probes that would
correlate the requests at the C plus plus level. But they changed everything recently, and a lot of the work is doing into the Javascript individual
engine. So we had to like use Javascript ourselves, and kind of inject an agent inside a node binary.
So there's all kinds of different techniques.
**Lalit** 44:08 Okay.
**Rafael Roquetto** 44:08 To achieve that for a very simple application like C plus plus, it would probably work out of the box because we could just correlate like a thread, is reading from the socket. And then it's writing all these many requests. But you know, probably doesn't apply to real words.
**Lalit** 44:22 Yeah, yeah.
Okay, yeah, thanks. Just just wanted to check the current states where exactly it is. Yeah, thanks.
**Rafael Roquetto** 44:30 Yeah. No worries.
**Lalit** 44:39 Yeah, Mark, nothing more from my side. Yeah, that's up.
**Marc Alff [MySQL]** 44:43 Okay, and well, I don't have any anything else myself. Tom do, maybe.
**Doug Barker** 44:54 I was thinking of putting in a Pr to start tackling some of the claim. Tidy warnings. Do you guys have any preference of doing like one Pr for category of
of warnings or putting them multiple together because some of them you can fix automatically with the with client.
**Marc Alff [MySQL]** 45:13 One thing that I noticed and I was thinking with sanctide is that
today we breed all the code with Synctid, including all the unit tests, and
to my understanding, sin and tidy is just about style of
specific construct in in the code itself.
So I don't think it makes sense to clean up all the unit tests themselves, because that would be 1st of all extremely tedious, and it doesn't add value to the product, because if we fix some warnings from Selectadi in a unit tests. The likelihood that this would actually detect a bug in the main code is very low. I think
so I guess we can start to fix all the warnings 1st in the main code in the production code.
and then when that is done, then we can see where we are and see if we want to
transverse. You need test or not.
So I'm wondering if we should
scope down the Crm. To only cover the production code and not run the unit test with sent Id
at least in as a 1st pass. So that we we fix
basically this is to give priority to the fixed information code and not fix in unit test.
**Doug Barker** 46:37 Yeah, I think that that makes sense. And we, since we're running claim tidy and see make, we can also fix by either by target or by folder and enforce warnings as errors. Kind of, you know, incrementally, if we'd like to do that.
So are you proposing, Mark, that we disable cling tidy on the test to start.
**Marc Alff [MySQL]** 46:56 At least to start. Yes, it would make less noise.
And what forces forces us to focus on the areas which are important at least 1st
as to how to do that.
No idea. One thing to remember is that the list of warnings which have
so there is a configuration file somewhere that should list. What incident, id warning, are to be reported or not?
This thing? I think so.
Just no voice, way, voice checks.
Wusse came up came out of some
basic try to see, to try to get some select working.
but those are never been discussed in depth to see. Oh, do we absolutely need read this of art.
So if we find
what what I'm getting at is, if we find some sedentary warnings that makes no sense. Instead of fixing all the warnings to comply with this list, we may as well
make changes to this list instead. If we, if we think it's better.
**Doug Barker** 48:16 Yeah, that makes sense. I was thinking of starting with the the ones that are where we have methods that are throwing have the potential to throw exceptions. So there's a i think it's a bug prone
something about exceptions warning that's catching some of our methods that are calling other methods that can throw, even though our methods have no except and we're not catching exceptions. So I think that would probably be a good one to start with. But I think that would also depend on. If you guys agree that that should be fixed. Yeah.
**Marc Alff [MySQL]** 48:45 But this is a good one to start with, although it might affect the Api itself.
so it can be touchy. Another one to look at also would be like all the performance issues, for example, like, Oh, sync, tidy, saying, Well, you are making a copy of an object where you should have a cross reference instead, and things like that risk should be
trivial to fix and and not trigger a lot of discussion, because we we know that the fix is better anyway. So
it would be.
It should be straightforward, for example.
**Doug Barker** 49:26 Makes sense. I'll I'll try to get 1 1 pr up this week, and then maybe we can see how that goes with fixing some clink, tidy warnings.
**Marc Alff [MySQL]** 49:39 And from from past experience, because I've done a lot of work on on include what you use.
The code base is actually quite big with a lot of
code, with a lot of compiling options and things like that. So it's easier to say, fix like 2030 whatever warnings at once, merge it, and then try again. If you end up with a big big pr that hangs forever, it will die by its own weight, and will never be merged, because it's
there are so many things at once to fix. But we cannot do anything, everything at once, and also the good is moving in the meantime, because there is also some overpr being merged. So it's
even though it
creates a lot of Prs. I think it's better to just address areas one by one. So at least we know. Okay, this
say, traces are clean. And now let's do. Metrics and metrics are clean. And now let's do logs and things like that.
For example.
**Doug Barker** 50:46 Okay, yeah, I'll take a look and see if it's possible to just fix all the warnings like in the Api folder or something like that, and and then turn those on as warnings, as errors. And maybe that would be a approach that we can take.
**Marc Alff [MySQL]** 51:08 So that was saying, Tony, anything else.
And which reminds me.
yeah. And the code of well, so
include what you use is pretty much done, but she needs some cleanup. I'm hoping that I would have some time to actually do the last pass on that
ceiling. Tidy is a big area. There is another one which we have never looked at, which is basically to get a good oxygen build to make sure that
everything is documented correctly.
when we document a functional method, parameters and whatnot, I'm sure there will be a lot of surprises there as well.
but that can. What can come much, much later.
Okay,
In any case, if we don't have anything else when, thanks all for joining and this and hope to
see you soon, either online or or at the next meeting. Then.
**Lalit** 52:33 Thank you.
**Tom Tan** 52:35 Run.
**Doug Barker** 52:36 Thanks guys.
**Lalit** 52:36 Yeah.
**Marc Alff [MySQL]** 52:37 Thanks, thanks. Everyone. Bye.
