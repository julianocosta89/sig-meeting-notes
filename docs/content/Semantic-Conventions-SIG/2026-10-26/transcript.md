SIG: Semantic Conventions SIG
Date: 2026-10-26
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

Jeff Leva 00:01:01 No.
Martin Kuba (Raintank, Inc. – Grafana Labs) 00:01:07 I wonder if we're in the wrong meeting.
Jeff Leva 00:01:11 Oh, I don't know, this is my first time to this meeting, too, so…
Martin Kuba (Raintank, Inc. – Grafana Labs) 00:01:14 I clicked, yeah, I clicked on the link in the… Calendar, but nobody's here, so…
Jeff Leva 00:01:20 This is supposed to be the Meetings… what time is it? Well, it's 2 minutes past.
Yeah, I don't know. Somebody shared this with me as well, Friday, so it should be a good link.
Martin Kuba (Raintank, Inc. – Grafana Labs) 00:01:35 Yeah.
It's… yeah, I know,
Jeff Leva 00:01:42 I'll give it a couple more minutes myself, but, you know, Bo.
I've heard it's been kind of hit and miss anyway, so…
Martin Kuba (Raintank, Inc. – Grafana Labs) 00:01:52 Okay, yeah.
But I mean, I see, you know, some Trask put in.
Something on the agenda, so I think he's joining, at least.
Trask is one of the maintainers.
Jeff Leva 00:02:13 Oh, okay, okay.
Martin Kuba (Raintank, Inc. – Grafana Labs) 00:02:25 Yeah, that's, okay, here's Trask. We're in the right meeting.
Trask Stalnaker (Microsoft Corporation) 00:02:33 Oh, yeah.
Where is everybody?
Martin Kuba (Raintank, Inc. – Grafana Labs) 00:02:38 The two of us joined, it's like, are you in the right meeting? There's nobody here.
Liudmila Molkova 00:02:54 Hello, everybody.
Trask Stalnaker (Microsoft Corporation) 00:02:56 We are in the right meeting.
Liudmila Molkova 00:03:01 I was in the wrong one, I guess.
Okay.
I think it is my turn.
Great… This is today?
We have a couple of… One's from the next… And… Well, people are joining… Don't forget to put your name.
If you have anything to discuss, please edit.
Let's see… What do we have… Here, quite a few things are waiting on… Reviewers… So it sounds like this one is… Pretty close… this is on the agenda, right?
the…
Trask Stalnaker (Microsoft Corporation) 00:04:16 Yes.
Liudmila Molkova 00:04:20 End user attributes?
Oh… Oh, we have a lot of approvals here.
This is… I think we want Marilia to approve.
Kate needs the second review, where I will take… Oh, look.
So this is the PR that… Was it MongoDB who added the proper context propagation?
Trask Stalnaker (Microsoft Corporation) 00:05:42 It is, who is it? It's Folks… Who are working on… they have a… there's a MongoDB fork now.
That's permissively licensed.
Liudmila Molkova 00:05:58 Oh, MongoDB Event Elastic, or, like…
Trask Stalnaker (Microsoft Corporation) 00:06:02 It's always been Aladd.
Liudmila Molkova 00:06:03 Oh, I see.
Trask Stalnaker (Microsoft Corporation) 00:06:07 And what is the name of… I forget. But there's… Microsoft folks working on it. I don't know if… is it a… Linux Foundation…
Liudmila Molkova 00:06:33 Oh, it's very comment, but the comment is… probably doesn't have the… the… the SQL problem.
Trask Stalnaker (Microsoft Corporation) 00:06:42 Yee… Yes.
Liudmila Molkova 00:06:47 Oh, and it's up thin, anyway.
Let's see.
Okay.
Oh, nice, it's Jason.
Oh, we are overriding the original comment.
Fun.
Clare.
Looks good, and given you already approved.
Let's get it in…
Trask Stalnaker (Microsoft Corporation) 00:07:20 Cool. Thank y'all.
Yep.
Liudmila Molkova 00:07:29 I see Martin here. Is it already on the agenda?
Martin Kuba (Raintank, Inc. – Grafana Labs) 00:07:34 Yes, it is, I bought it, yeah, I bought it there.
Liudmila Molkova 00:07:36 Awesome.
Cool.
This is pretty much ready, just needs another approval rating.
Trask Stalnaker (Microsoft Corporation) 00:07:48 Yeah, I can ask Jack as a… Java approver.
Liudmila Molkova 00:07:55 You… aren't you?
Trask Stalnaker (Microsoft Corporation) 00:07:58 I approved it already.
Shit.
Liudmila Molkova 00:08:03 We can take a look after, just checking if there is anything else we can help move forward.
Oh, RBC Migration Guide.
Yay!
We have it in the agenda.
Trask Stalnaker (Microsoft Corporation) 00:08:21 Yeah…
Liudmila Molkova 00:08:28 Oh, by the way, there is a small… Quality of life improvement that we can probably also merge.
So, there is a friend, this… Table that we have everywhere for error type, and it has a single value.
And this is the… Proposal and templates to not render it, because it's so… Hmm, not very useful.
It keeps the note and everything else just on this front.
And I think it is a good thing to do.
Trask Stalnaker (Microsoft Corporation) 00:09:15 Did you approve? You approved that one. What's the number?
4047…
Liudmila Molkova 00:09:22 Yeah.
I am going to approve it.
Trask Stalnaker (Microsoft Corporation) 00:09:28 Oh, okay. Yeah, Kristoff has approved already, okay.
Liudmila Molkova 00:09:31 Yeah.
But there are some merge conflicts, so we'll… Okay.
I will talk about this, we'll talk about this, and this is on the networking. SIG probably wants my approval.
First.
I'll take a look.
Anyway, let's move on to the agenda, and… We have some PRs from your Trask.
Trask Stalnaker (Microsoft Corporation) 00:10:33 Yes…
Liudmila Molkova 00:10:35 Let me respond to…
Trask Stalnaker (Microsoft Corporation) 00:10:41 Finally sent this PR.
Based on the discussion we had earlier this year.
My interest in moving this forward is, Currently in… the… in Java.
We… we support this on all of our HTTP client instrumentations.
Which is a lot, and we'd have tests for… both. Now, the Old, odd, and the odd.
And I want to… and we have the old one under a preview flag.
And with 3-0 coming up, I want to, if possible, it's not critical, I want to… Drop.
Both of those, and only support.
this one.
Liudmila Molkova 00:11:50 I see Michaela approved already.
And he's interested in this, yeah.
Trask Stalnaker (Microsoft Corporation) 00:11:54 Yeah.
Liudmila Molkova 00:12:00 Service identities, nice.
Cool, I'll… I'll take a look. I think it's…
Trask Stalnaker (Microsoft Corporation) 00:12:12 I did leave one, in the agenda. I left one kind of question there that maybe we could talk about.
Add them, Adding them to the client-server group.
Should we add them to that… those two groups?
So I… it seemed reasonable, the… they're not really… these groups, I don't think, are used anywhere. They're just… For rendering here.
I don't know what we feel it's… I mean, there would be opt-in on… We would make them opt-in on this group, I guess.
Liudmila Molkova 00:13:07 Yeah, so if we… already released it.
Done.
we would only be able to add them as opt-in, but they are opt-in by nature, right? You…
Trask Stalnaker (Microsoft Corporation) 00:13:21 Yeah, they're very much opt-in.
Liudmila Molkova 00:13:25 Yes, but then… It means… Like, adding them to the group would mean that every metric inside up until elementary Semantic Conventions, or outside that takes, that references this group.
Would get that… Metric would get that new attribute.
on this metric, and it's… I think it's expected, that's what we want.
break.
Trask Stalnaker (Microsoft Corporation) 00:14:02 Yeah. Yeah, I think so.
I mean, it's… It's a little noisy, for… Like, for… it's a little bit of an edge case feature in general.
But… It seems… Correct.
Liudmila Molkova 00:14:28 I mean, we can find ways to suppress the noise.
Trask Stalnaker (Microsoft Corporation) 00:14:33 It also makes it… I mean, something nice about actually grouping it here is that it makes… It makes that client.namespace Make, the decision we made to put it under the client.service.name make more sense, because it really is generated from the… typically from the client.address.
So there is a nice…
Liudmila Molkova 00:15:05 Yeah, sure.
Trask Stalnaker (Microsoft Corporation) 00:15:06 Okay, I'll do it. Yeah.
Liudmila Molkova 00:15:13 Okay, and the next one, the first invocation namespace.
Trask Stalnaker (Microsoft Corporation) 00:15:22 So, the fast folks had meant… the context here was they had wanted to try to stabilize stuff, and… And I had pinged them on a Java… Pr.
And so if we're going to… I told them if they want us to change it.
They need to open a PR here.
If we're gonna break… make that breaking change in 3-0.
Liudmila Molkova 00:15:55 Oh, I see.
I'm surprised it passed our checks. Maybe our checks are broken, because there… there is a… Remember, underscore versus dot.
Trask Stalnaker (Microsoft Corporation) 00:16:06 Yes, that's in the, That's in the PR. There's something where you say… I forget.
Liudmila Molkova 00:16:16 No, it's under the Right, yes.
Trask Stalnaker (Microsoft Corporation) 00:16:18 Generation exclude, yeah.
Liudmila Molkova 00:16:20 Okay, okay, cool.
Now it's start time, nice. What, why alpha?
Trask Stalnaker (Microsoft Corporation) 00:16:29 I don't know.
Yeah, makes sense.
Liudmila Molkova 00:17:00 Okay.
And there is a plan to stabilize us.
I've seen the proposal to stabilize attributes, but that's, like, we cannot just stabilize attributes, right?
Trask Stalnaker (Microsoft Corporation) 00:17:13 Yeah.
Liudmila Molkova 00:17:17 Okay.
Trask Stalnaker (Microsoft Corporation) 00:17:17 Yeah, I don't know how… Yeah, I can poke on them a little bit more about their plan to stabilize.
Liudmila Molkova 00:17:32 Awesome.
And other than that, it looks good, yeah, I'll check, I'll… Approve after it's fixed.
Trask Stalnaker (Microsoft Corporation) 00:17:45 Cool.
I think this one… Just needed another approver, or, you know…
Liudmila Molkova 00:17:57 Oh, I… I've been… holding my approval back for a reason absolutely unrelated to this PR.
But… There is a lot of effort.
from different places to adopt these conventions, including, like, Java.
And external, I think RebbitMQnative.net instrumentation also does.
And we know we are going to break it, we know we will remove messaging dot in front of it.
And… It will be much easier to migrate after, because it would be mostly just renames.
But it just feels wrong that we… we know about the problem, we let people adopt the new conventions, and we're going to break them.
Trask Stalnaker (Microsoft Corporation) 00:18:49 Do you want to… I mean, I'm happy to send a PR this week to break them all, and do that rename.
I… somebody had suggested renaming it in here, and I had suggested no, because… it felt… I thought we should do it all at once in the messaging namespaces.
Liudmila Molkova 00:19:20 Yeah.
I mean, if you were up for… would Java adopt it? Would you… you probably already should.
Trask Stalnaker (Microsoft Corporation) 00:19:28 If we can get it in… in… by Wednesday.
or I put up the PR, and we think that we're gonna merge it, then yeah, I'll… I'll… Change them in Java 3.
Liudmila Molkova 00:19:42 I'll approve, we can find somebody else to approve as well, I'm sure.
Trask Stalnaker (Microsoft Corporation) 00:19:46 Okay, I'll send the PR today.
Liudmila Molkova 00:19:49 Awesome.
Thank you.
Cool, I… I think I reviewed it before, and it looked good otherwise. I'll take another look, but yeah.
Okay, so moving on, the RPC.
We have some… Problems in the migration guide?
Trask Stalnaker (Microsoft Corporation) 00:20:22 Just updates, it hadn't, I think, hadn't been updated. Oh, oh, these changes, this is just synced over from… latest that is in the spec part. I guess I should double check to make sure that is, which one we prefer.
We have multiple, we've had some drift in the repo.
Liudmila Molkova 00:20:52 Okay.
So none… comparative is happy.
It probably didn't look into the content itself.
Just a diff.
Trask Stalnaker (Microsoft Corporation) 00:21:08 No, it should look at the other files.
Liudmila Molkova 00:21:13 Hmm, okay.
Trask Stalnaker (Microsoft Corporation) 00:21:16 Yeah, it's not an independent diff, like, it even can… like, I've seen it go and check URLs for other repos in OpenTelemetry.
like, in Java PRs, like, it'll go and check these SEMCONS, For conf- for stuff.
Liudmila Molkova 00:21:34 Nice.
Cool. So you, you want to take some action item and double-check something, and…
Trask Stalnaker (Microsoft Corporation) 00:21:41 Yeah.
Liudmila Molkova 00:21:41 Yeah.
Awesome.
Anything substantial to go out here, just… sinking.
Yes.
Trask Stalnaker (Microsoft Corporation) 00:21:53 No, just filling out, you know, we hadn't updated for, like, the… the address… Server.address being, like, a grouping concept, kind of, and other… just… updating it.
Liudmila Molkova 00:22:13 I wanna talk about something.
If we have time… Cool, and then the stability.
Trask Stalnaker (Microsoft Corporation) 00:22:50 So, gRPC and Dubbo.
No, headers and trailers are still… not stable.
Liudmila Molkova 00:23:06 Because they are opting anyway. Or, like, what?
Why?
Trask Stalnaker (Microsoft Corporation) 00:23:12 We had… said that we weren't, somewhere… we had an issue where I think.
Maybe that was before we renamed. I mean, I'm good with marking them stable.
Liudmila Molkova 00:23:28 Do you remember what is?
Trask Stalnaker (Microsoft Corporation) 00:23:31 Yeah, I can… I can dig. Let me dig that up.
Liudmila Molkova 00:23:40 We can't talk about it on the… RPC call, I think we still have one on Thursday.
Oh, we probably didn't mark them as RC.
Trask Stalnaker (Microsoft Corporation) 00:23:54 Yes, yes.
Cause I think there were some… questions, but I think the questions might have been answered by the discussions we had with the GRPC team and the rename we made around it.
Liudmila Molkova 00:24:12 Okay.
Trask Stalnaker (Microsoft Corporation) 00:24:12 So, let me… I will, I'll research and follow up.
With you on that.
Liudmila Molkova 00:24:19 Cool. Do you want to do it in the same PR? We can also do it in a separate PR. Yes.
is not controversial to Marketam's table. Master.
Trask Stalnaker (Microsoft Corporation) 00:24:35 I guess, I guess I'd probably… prefer to just add it into this PR, if it's… Okay.
Liudmila Molkova 00:24:41 Yeah.
Trask Stalnaker (Microsoft Corporation) 00:24:42 yeah, let me… let me… I had… I think I had just… assumed, since we hadn't marked it RC, but… And we had some earlier discussions, but let me think about that, and I will… I'll ping you.
Liudmila Molkova 00:25:01 That one's good.
Okay, Martin, deprecating on the usernames space.
Martin Kuba (Raintank, Inc. – Grafana Labs) 00:25:10 Yeah, I'm just asking, basically, for approval. There's, we're trying to move it, this namespace, to the client side.
Registry. We already have a PR open there.
I think last week I was asking about the process, so we're just waiting for this to be merged before we can proceed, with RPR.
Liudmila Molkova 00:25:34 Yeah, and you added this for every attribute written.
Martin Kuba (Raintank, Inc. – Grafana Labs) 00:25:37 Yeah.
Liudmila Molkova 00:25:40 Yeah, ugh.
Awesome, and it's also deprecated and moved.
One tiny thing, I think this is not… It makes no sense on the attribute group.
so, look, I think we daunted them, but it's minor.
Nothing depends on it.
Looks great.
And… I mean, we can merge?
Trask, do you have any objections if we just merge it?
Trask Stalnaker (Microsoft Corporation) 00:26:38 Nope.
Liudmila Molkova 00:26:40 Okay, so I'm not even going to apply this, because it doesn't change anything at all.
Okay, great.
Martin Kuba (Raintank, Inc. – Grafana Labs) 00:26:48 Thank you.
Yeah, and we're gonna have a bunch of other ones, after this.
This is the first one.
Liudmila Molkova 00:27:02 Do you… Also on the device names page?
Martin Kuba (Raintank, Inc. – Grafana Labs) 00:27:08 Yeah, that was one of the ones that we wanted to move as well.
Liudmila Molkova 00:27:13 Yeah, I have a PR for this, and I'm interested in what was… Should do… Botted?
So, you know, we are doing this transition to V2.
And in V2, you cannot have entity without identifying attributes.
Okay. And it turns out the device is a very interesting one, because It… first… It does not have identifier and attributes, it was just a resource, and the device ID is also opt-in and sensitive.
So, like, it doesn't fit the entity model.
And in order to, like, be compliant with V2 requirements, I'm converting it into just an attribute group.
But if you're going to bring it to, the client repo.
then maybe we can just deprecate or remove the entity, like we've done, I think, for mainframes, because they will be having it.
Martin Kuba (Raintank, Inc. – Grafana Labs) 00:28:31 Okay.
But we would still have to resolve this entity issue right there.
Liudmila Molkova 00:28:38 you would need to resolve it in one way or another. You can say it's an attribute group, you can model it properly, it was, like, that follows entity model.
But, it would not be in semantic conventions anymore.
Martin Kuba (Raintank, Inc. – Grafana Labs) 00:28:52 Okay. Is there… is there an issue for… That describes the problem with the… Identity.
Liudmila Molkova 00:29:03 There's an issue… There is no issue that describes, like, the requirement to have identity attributes, but there is an entity modeling guide.
You're in the cerebral…
Martin Kuba (Raintank, Inc. – Grafana Labs) 00:29:27 I'm just… oh, sorry, I'm just trying to understand, the issue that… With the identifying attribute for the device, you said that it's sensitive, so, like, it's because… of PII, or…
Liudmila Molkova 00:29:41 I… I think so, so, like, the host name could be… Something, anything.
Yeah.
Yes.
Martin Kuba (Raintank, Inc. – Grafana Labs) 00:29:56 In any case, yeah, we can… we can handle this, so if you want to just, you know, instead of close this and deprecated… Open, yeah.
Then we can… we can have that discussion in the client-side SIG.
Liudmila Molkova 00:30:12 Yeah.
Okay, let me then… Okay, I've lost it, I'll find it, and I will update it here.
On this front.
Okay, thank you.
And this is the PR you have. Do you want us to take a look, or… Any… yeah.
Martin Kuba (Raintank, Inc. – Grafana Labs) 00:31:34 I don't, it's pretty much a straight move. I mean, if you want to look, yeah, we definitely will come to it. I don't think there should be anything… Really… Like, new to review, Now that you've merged the… merged the UPR on your end, we're gonna add that, That commit hash here.
It just pinned to your… yeah, like you said, so… That's the only thing we're gonna add.
Liudmila Molkova 00:32:05 Cool. You have some tests here.
They're tasting templates.
That's interesting.
I'm curious, like, what does do? Maybe we should adopt it in some class.
Martin Kuba (Raintank, Inc. – Grafana Labs) 00:32:26 It's something that Hanson put together, so I'm not… I can't speak to it at the moment, but… Okay.
Liudmila Molkova 00:32:35 Cool, yeah, I… And you're moving to Schema V2, that's awesome.
Cool.
You're… you said you were going to pin… And we should talk about release, we have it on the agenda.
Should we move on?
Yay.
I put it here, I'm kind of curious what's going on with service and deployment SIG, maybe Trask, you know?
Is it active? Is anything going on?
Trask Stalnaker (Microsoft Corporation) 00:33:12 I… Don't know.
If it's… If they're still meeting I can find out. I'm supposed to know.
Liudmila Molkova 00:33:28 I can ping them in the chat and ask, or I can ask Josh.
No worries.
Trask Stalnaker (Microsoft Corporation) 00:33:38 Yeah, I assumed that… They were… Still, unless they're kind of… Yeah.
Yeah, that's a good question.
Was there something you… needed, in particular, or just wondering about some of their PRs?
Liudmila Molkova 00:33:58 Oh, no, we're just cleaning up the TC sponsorship, and we found out that since Josh left.
It does not have a TC sponsor, and we never noticed.
So, I'm just checking for the bookkeeping reasons, nothing else.
Okay. I'll figure it out, thank you.
Trask Stalnaker (Microsoft Corporation) 00:34:24 Yeah, I've seen chatter on the… let's see… Their last, Meeting… I mean, their last, in Slack.
Liudmila Molkova 00:34:49 I think I've seen some PRs to move stability of some.
But I don't remember if it was approved and emerged.
Trask Stalnaker (Microsoft Corporation) 00:34:56 Yeah, the Slack… Channel is active.
So yeah, they're still… they're still discussing.
Liudmila Molkova 00:35:05 Cool.
Oh, that's clear.
Awesome. And… that's the release. We've been holding release for a long time. I'm sorry, this is unexpected.
So, I cannot open Slack right now, but I imagine somebody is asking about the release, and I think we need release, definitely need release, because we have a bunch of… RC… unstable things.
So maybe we can spend a little bit of time here to go through the open PRs and mark them, add them to the milestone, and… Done… R…
Trask Stalnaker (Microsoft Corporation) 00:35:52 Yeah, I'd love to get, RPC in and released.
End of the week.
Liudmila Molkova 00:36:01 And I think there is more. There are some, yeah, this fence RC… Oh, wow.
This is important for Java 3 release, right?
And we've talked about, the messaging. Not this one, but the one you will send.
Right. And… do we need this?
Trask Stalnaker (Microsoft Corporation) 00:36:36 That would be nice, yeah, yeah.
Liudmila Molkova 00:36:38 Yeah.
Okay, so let's mark this as, the new milestone.
What is the version that we have? 144? Will be 145.
And as soon as… 135… That shows 145… Which one?
I'll pause on Slack and say that we are going to release Either this or early next week. Let's try this week.
And I think at least all of the things that I found so far Are either very close or can be, with some reduced scope.
And… Yeah, I can do the release.
Martin Kuba (Raintank, Inc. – Grafana Labs) 00:38:22 Out of curiosity, how often do you do releases, and how do you decide when to do a release?
Liudmila Molkova 00:38:30 Oh, we try to do monthly, but sometimes it's just that somebody asks, and we… So, sometimes we forget, and somebody asks, and then we do it.
But actually, for people who might be listening, if you ask for release, and especially if you're a prover and haven't right access to the repo, you can initiate release yourself. I mean, we can just talk about it and say, okay.
We are ready. And it's just, you don't need… you don't need the maintainer to actually start the release.
But yeah, monthly is the desired state. The reality differs.
Martin Kuba (Raintank, Inc. – Grafana Labs) 00:39:14 Take care.
Liudmila Molkova 00:39:27 Okay.
So, I still have… time, and I have a couple of things I want to bring up. This one is some distant future, maybe I should talk about… mmm… this.
And… first.
So… we are adding span type to the spec, and spend type will be… will become, like, a metric name. So it would need to be stable, and we would not… it would be part of stability guarantees.
What we have today in the spend types is… Well, there is some system to it, but I'm proposing to a line of these metrics.
So that, for example, we have HTTP client request duration, and the spend type would do the HTTP client request.
It means that, like, the client, it's currently the last segment, or client, server, producer, consumer.
It would move and become the second segment.
Here… And for… internal things.
Following the precedent we have in GenAI, which is don't define.
We don't put the internal inside the spend type.
So, just follow the GenAI lead, and do this.
And after that, we should be able to survive the introduction of the spend type and semantic conventions.
Trask Stalnaker (Microsoft Corporation) 00:41:18 Yeah, definitely, that sounds like a good idea.
Liudmila Molkova 00:41:36 Oh, there's… there are also collisions.
Cool.
Okay, nice. Then it's actionable.
And we'll do a work on it.
And… The other thing I wanted to bring up that maybe we should put into release or resolve… Relatively soon is… TB… We do… There is an interesting question here, those databases, So I don't know the shape of this PR now.
But… let's take a look at this pants.
So what we used to have… We had… a span for the base DB client.
I'm trying to find it… yes, this, this front. It was a span.
And… This was also an independent span.
And, the plain sequel was also an independent spin, and all of them were… independent spans.
we… In V2, they are not independent spans, they are refinements.
And then there is a question of what refines what.
So there is a DB… And there is an interesting… limitation that we have, that might be lifted in the future, but from… we were… we kind of… we don't want to lift it yet, is that refinements cannot refine refinements.
So, it leaves us with this, that the sequel is… a refinement of DB.
and Mongol, and… SQL Server as well.
So, SQL Server and SQL are kind of siblings.
And this is essentially all undocumented explicitly.
Is it called DBs.
And so on.
It might not be awesome. So, like, if I just want to treat SQL Server as SQL span, there is nothing in the schema that tells that.
I think it's… Fine?
For now, and I think making SQL Server refine SQL in the long run Would not be breaking.
Because they are both database spans anyway, and nothing for the telemetry that would change based on this.
So I kind of want to start flat.
Trask Stalnaker (Microsoft Corporation) 00:45:06 Yeah.
I don't… seems fine. I don't think we need to block on moving that forward.
Liudmila Molkova 00:45:14 Yeah, and I think what… James was suggesting is that we're… Keep the attribute group.
We probably fixed it. Okay, he removed it.
Oh, sorry, that's the wrong PR.
Anyway, I'll check, I'll follow up, on this and see if we need any other discussions.
Okay.
Okay, so then the final thing I wanted to share, and it's some early prototype I kind of want to just, show… And get higher level feedback.
Sorry, maybe.
So we have a project in OpenTelemetry that's just started, and a tab that's merged, telemetry Policies.
And it kind of intended for the collector and SDKs to, describe what… how to transform telemetry.
And it's not OTTL. It can… it's… it's specified.
VR, this schema, and it's been actively worked on.
And I was thinking, They're already fighting the language.
That would say, okay, match this attribute and do this with the signal.
And it's exactly the transformation language.
the in… That could replace the current schema transformation that's very limited.
The benefit is that we get something that can do the transformations already.
And we can test it, we can leverage the work that other people are doing instead of inventing our own schema that would do pretty much the same.
And… I've been trying to put together a set of examples that would demonstrate our migration guides.
As a proof that we can… do this.
And maybe I'll take a look at the… the Gen AI.
So, this is the wrapper around schema, around the policies.
And it tells from what and to what.
And then there are a bunch of policies, and they say, okay, if… This attribute exists.
Then rename it.
And so on.
Of course, there are things we cannot express.
But it is much… already much more expressive than, like, oh, they have regex, they have a few more things that we can reuse, but essentially, it provides way more Extensibility than the current schema transformation.
And there is an assumption that we can do more. I got some initial feedback from David Ashpole, who works on the project, and he's kind of supportive of having more things, but we need to bring it up with the policy project as well, and see if they are Like, would be open to expand this list in the future of supported operations.
But this looks promising, and… we can… do more with that. So, for example, we can express the… If we define the gRPC schema, the native gRPC schema in Semantic Conventions language.
Then we can also say how to convert one to another. This is invented.
And this is still something I'm working on. So, like, It's useful to see that you can… what can… what is supported, right? We would put only transformations that are supported.
But we can kind of generate this part and say what's missing after.
Still.
And assess if it's, like, critical for, migration.
So, if we look into databases… Like, we would see a lot of gaps, because we added a lot of things in DB Conventions.
But if we look into Gen AI… Well, there are some gaps.
But they are mostly minor, so, like, there are some missing attributes on this metric.
Or some detailed attributes are missing. But, like, from general dashboard perspective, We… so far, didn't break much. It's possible to transform one version into another.
And all the general dashboards and alerts do still work.
Trask Stalnaker (Microsoft Corporation) 00:51:19 Can you go back to the database gaps?
Liudmila Molkova 00:51:25 It didn't have the metric. Imagine that. I don't remember.
Trask Stalnaker (Microsoft Corporation) 00:51:31 Yeah.
Same with, no, no, RPC, we did have the metric, yeah.
We renamed it, I think.
Liudmila Molkova 00:51:40 I think it was poorly defined, it didn't have a lot of attributes, it had them in Markdown, but not in YAML.
Trask Stalnaker (Microsoft Corporation) 00:51:46 So, gap means you can't, go two ways. You can't convert it in backwards, or…
Liudmila Molkova 00:51:58 Oh, so in this version, it's directional, right? So, it's from this version to that version.
And you can go back.
Trask Stalnaker (Microsoft Corporation) 00:52:07 Why would that be a… why would that be a gap when you're going in that direction?
Liudmila Molkova 00:52:15 So when you transform this version into this version.
Oh, I see what you're saying, so if nobody could build the dashboard, for… The database operation duration.
Trask Stalnaker (Microsoft Corporation) 00:52:33 Right.
Liudmila Molkova 00:52:35 I see for the previous version, yes.
Yeah.
Trask Stalnaker (Microsoft Corporation) 00:53:01 And I was wondering if that applied to some of, like, the missing attributes, if also… but I wasn't… Sure, so, like, spans… Missing attributes…
Liudmila Molkova 00:53:14 Yeah.
Trask Stalnaker (Microsoft Corporation) 00:53:17 Yeah, like, it seems to be describing… Problems, gaps of going in the other direction.
Liudmila Molkova 00:53:27 Not really, because… Well, yes, you cannot go in the other direction.
But you can, and you can keep metrics. So, like, when you downgrade, you can keep everything you had.
And it's still… not incompatible.
That's a good question about the gap.
Trask Stalnaker (Microsoft Corporation) 00:53:50 Can you go back to the 124 to 1… yeah, this one, yeah.
So, like, the line 30… These look like new… most… mostly new attributes that didn't have, anything corresponding to them in the old So it feels to me like… not a gap, if you're going in that direction. Like.
Liudmila Molkova 00:54:22 Yeah.
Trask Stalnaker (Microsoft Corporation) 00:54:23 You didn't have… you don't… you don't have any telemetry to start with.
Liudmila Molkova 00:54:27 Right.
So it's… Probably more like, okay, I am building telemetry against this version.
I cannot, if I'm trying to upgrade the old version to this, it wouldn't work.
Trask Stalnaker (Microsoft Corporation) 00:54:49 You wouldn't get conformant, or you wouldn't…
Liudmila Molkova 00:54:53 You wouldn't get even… like, it depends, but yeah, in this case, you wouldn't get anything meaningful.
Trask Stalnaker (Microsoft Corporation) 00:55:02 Yeah.
Liudmila Molkova 00:55:04 It's probably worth explaining.
Trask Stalnaker (Microsoft Corporation) 00:55:07 Yeah.
Liudmila Molkova 00:55:08 Presenting in a different way.
Trask Stalnaker (Microsoft Corporation) 00:55:10 Yeah, because when I think of schema transformations, and when I think of gaps, or things that can't be represented. I don't think, you know, Users who have the old… Have old telemetry coming in and want to transform it to new telemetry.
And what they care about is that they didn't… lose data.
Like, that we have someplace to put all that data.
Liudmila Molkova 00:55:44 Yeah.
Trask Stalnaker (Microsoft Corporation) 00:55:45 In the… in the new schema.
Liudmila Molkova 00:55:49 Yeah, and it sounds like there are two scenarios. The first one, I'm… Migrating my instrumentations.
And then doing transformation, and don't want new dashboards… oh, sorry, old dashboards to break.
There's a separate keys that I have, I'm trying to normalize up.
And then…
Trask Stalnaker (Microsoft Corporation) 00:56:10 Right.
Liudmila Molkova 00:56:12 I will have some gaps in the old telemetry that would not let me update my dashboards to the new version.
And… but yes, it's hard to explain.
Trask Stalnaker (Microsoft Corporation) 00:56:24 I forgot, Jeff asked if he could have a couple minutes at the end, to ask some questions.
Liudmila Molkova 00:56:32 Oh, yeah, thank you, sorry, I didn't notice it.
Jeff Leva 00:56:34 Hi, yeah, sorry.
Trask Stalnaker (Microsoft Corporation) 00:56:36 Hey. No, no.
Jeff Leva 00:56:37 Hi, Trask, yeah. Welcome. Yeah, I bumped into you guys last week or so, and I was on the wrong meeting, for some GenAI attributes.
discussion, so I think I'm finally in the right spot. So, I work with OCSF and COSI, and we have some security attributes that we want to get aligned with OTEL as best as possible.
So, I think I answered my first question. Is the Gen AI, the correct… I guess, format, or repo for that.
the conventions.
For, like, security attributes and so on.
Liudmila Molkova 00:57:23 Is the secu… yeah, go ahead.
Trask Stalnaker (Microsoft Corporation) 00:57:25 Go ahead.
Liudmila Molkova 00:57:27 Is the security attribute specific to GenAI or not? Probably not really, or maybe sometimes.
Jeff Leva 00:57:34 Yeah, they should be. I can share a doc. I didn't know if I should just open… I guess two things. If I do figure this out, which we… I'm sure we can, do you guys want an issue and a PR? Or just PRs, or how does that work with you guys?
Liudmila Molkova 00:57:52 It would be nice to start to create an issue, And, like, if we're not sure, maybe in the Semantic Conventions repo.
Or GenAI, we can transfer. But essentially, to lease the scope of things you would like, to see.
Jeff Leva 00:58:10 So, for example, let me… So yeah, we have, like, That was the first thing, but yeah, I think most of these… would probably fit in the GenAI Conventions. Is there security… basically, attributes. Like, one of them is the hotel underscore trust level. We want some… we want to build some attributes into things like that. The hotel security guardrails, those type of things.
Does that sound like the right arena?
Liudmila Molkova 00:58:46 And we haven't… if I… if I'm honest, that it… it… It would be difficult, because we don't have people who used to work on the security Semantic Conventions.
And… It's just… we, at least from my side, I don't have enough expertise in the security to give you any decent reviews.
I think there could be other people who are interested.
But it might take a bit.
Jeff Leva 00:59:23 Okay.
Trask Stalnaker (Microsoft Corporation) 00:59:23 There's… there's also, I mean, I think part of what we're hoping out of the COSI and OCSF folks was, is that group of people who have that domain knowledge, and So, you know, the… We… the question is, sort of, do we integrate that into… the OpenTelemetry SIGs, in which case, you know, we kind of, would want you all to come to these meetings and these, you know, discussions and have that here. Okay. The other option is the federated Semantic Conventions.
Where you all could own, sort of, a… A domain of things that You know, you define… using our tooling and our, you know, we have… Kind of how GenAI is already a federated, repo. You can have those outside of OpenTelemetry completely.
But I would love to have… I think we need a lot more time to discuss this. Why don't you open, and I… I think this might be a good… because part of the problem is also, like, secure… we don't have a base security domain.
And so probably a lot of the things, even though they're… that you want to do Gen AI-specific stuff, we may… some of that stuff might be… Mmm… we might need a security-based domain also, and again, that's kind of where, you know, we're looking for, the OCSF folks, potentially, to provide that base domain.
Yeah, I'd also be happy to, if you want to have, like, a separate meeting.
Jeff Leva 01:01:26 Okay.
Trask Stalnaker (Microsoft Corporation) 01:01:27 If you wanna… if you can pull in, you know, like a… somebody from OCSF, and… We could have, you know, more discussions there, kind of figure out you know.
How… how the jigsaw pieces can fit together.
Jeff Leva 01:01:45 Yeah, okay. I did share a doc, I know it's getting late, and I have another meeting as well.
But maybe I'll come back… Should I put something on the agenda and I can come back next.
Trask Stalnaker (Microsoft Corporation) 01:01:57 Yeah.
Jeff Leva 01:01:57 Some folks, and we can hash this out a little bit better, and…
Trask Stalnaker (Microsoft Corporation) 01:02:01 That'd be awesome.
Jeff Leva 01:02:02 Okay, alright. Well, thank you for your time. Sorry, this is… this is something we've really been trying to get to do, and I… I'm both OCSF and COSI, so I can help straddle the fence, but I'll invite more, because they have a lot… there's a lot more depth that we can bring in here.
Trask Stalnaker (Microsoft Corporation) 01:02:19 Okay, yeah, and even if we just… the initial discussions at a surface level is fine also.
Jeff Leva 01:02:25 Okay, alright, sounds good. I did put that doc in there, just kind of so you know what I'm after, and some of the attributes.
Anyway, you guys can look at it and be prepared a little bit, so… Alright, well, thank you, Trask and, team, so we'll talk.
Trask Stalnaker (Microsoft Corporation) 01:02:43 Yeah, put it on the agenda, and maybe if you can attach that doc.
Jeff Leva 01:02:46 Yeah.
Trask Stalnaker (Microsoft Corporation) 01:02:47 To that doc in the agenda also.
Jeff Leva 01:02:49 Okay, sounds good, thank you guys.
Liudmila Molkova 01:02:51 Cheers. Are you at the KubeCon by any chance, Jeff?
Jeff Leva 01:02:55 I'm sorry?
Liudmila Molkova 01:02:56 Are you going to the KubeCon by any chance?
Jeff Leva 01:02:58 No, no.
Liudmila Molkova 01:03:00 Okay. If anybody from the team is going, we can have an in-person discussion there.
Jeff Leva 01:03:06 Okay, I'll find out. I have an OCSF meeting tomorrow and COSI on Thursday, but I'll put it in the chat and see if I can get some, answers from some folks.
Liudmila Molkova 01:03:17 Awesome, thank you.
Jeff Leva 01:03:18 Thank you very much. Goodbye. Cheers.
