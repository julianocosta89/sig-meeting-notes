SIG: JavaScript SIG
Date: 2025-07-30
Duration: 59 minutes
============================================================

## Zoom Recording Transcript

**Marc Pichler (Dynatrace)** 00:53 Hello!
**MG Marylia Gutierrez** 00:58 Hello!
**David Luna Bistuer** 00:59 Right.
**Marc Pichler (Dynatrace)** 02:09 Yes, we can start it on.
Welcome, everybody. Let's jump right into the 1st topic, which is from Marilian.
**MG Marylia Gutierrez** 02:23 Yeah, I feel like it's on me today. But.
**Marc Pichler (Dynatrace)** 02:26 It's okay.
**MG Marylia Gutierrez** 02:26 And so the 1st one. Yes, I've been getting just random questions like from community in general, just asking for, like the state of logs, because we show that it's not market stable So just wanted to get a sense. Anyone working on this any plans to when we plan to market stable. I don't know. Just in general the current state of it.
**Marc Pichler (Dynatrace)** 02:49 I guess there's no concrete plans right now. Svetlana has been chipping away on some of the oh, things in the milestone which see f here somewhere.
Oh.
**Trent Mick** 03:13 That's for Lincoln. Chat.
**Daniel Dyla (Dynatrace)** 03:14 It's 9 team. Yeah.
**Marc Pichler (Dynatrace)** 03:16 Oh.
oh, just being confused by zoom for a bit one second.
Yes, that is the one.
Yeah. There's some things in there that still need to be done. But overall there's yeah.
I don't think there's a whole lot still that needs to be done for it to be stable. It's just not a priority topic at the moment. And I think we should 1st tackle the topics that we have committed to already, which is the Http stuff and database. Simcomf updates.
But yeah, that's 1 of the topics. I think we have already noted it down somewhere in the focus topics here.
Stabilizing this something that we can pick up once we're once we're done with the other things.
Yeah, I know for a fact that a lot of people are waiting for this. Because I also had a bunch of people asking me about stabilization on that.
and it would also make stabilizing.
The export is a bit easier.
Because the exporters are like they depend on the on the logs package, and if we depend on an experimental package, it's very difficult to like. Also make the exporter package stable.
So not sure on like the ordering here. We could, of course, go with this. But yeah. So blocks stabilization would be something that we would have to look into eventually as well.
**MG Marylia Gutierrez** 05:26 Thank you.
Next one is just me asking for reviews. So I did the first, st just the initial structure kind of like preparing for the declarative configuration. So this one is just creating a different package and setting up. Just I think I put it just a couple just to get the sense of how this is gonna work. And since we mentioned the prior weekly that we might want to get rid of Core, and I did have a few dependencies that I was going to use on core. So instead of using those which was just the getting the environment variable, like values and the at the log level. So actually, what I did. Instead, I copied those things to this, so we can eventually get like, delete them from the core. And don't have that dependency anymore. So those files. Yeah, the environment one and the DC log levels are exactly the same as they were on core. And then I just created, then the config provider with the config objects, and so on.
So the only thing that is weirder is the package lock that is showing tons of difference that yeah, it's not even gonna load here. But it's just that thing that keeps adding the like, the permissions and version of stuff. I don't know how to solve this. If anyone has any idea, every single time that I try to fix, I just created more lines.
**Trent Mick** 06:57 Get a job with Microsoft and get on the Npm. Maintenance team and fix their package lock system.
**MG Marylia Gutierrez** 07:05 Okay, busy. We'll be right back.
**Marc Pichler (Dynatrace)** 07:09 I think. I'm not sure which which version you're running for on your on your local machine. But there was one thing that caused a lot of package lock churn in some versions of Npm.
**Trent Mick** 07:28 Yes.
**Marc Pichler (Dynatrace)** 07:30 I added, where was it this constraint here? In renovate that should avoid this?
like adding the like license fields and stuff which, like usually causes a lot of churn. I don't think we've seen that happen in the core repo anymore since I added this, but I'm not sure if we just got lucky.
**MG Marylia Gutierrez** 07:55 Yeah, I'm just checking. I'm using version 9.6. So I might try to just update my Npm and run again.
**Trent Mick** 08:03 Is that cause you're using? Do you typically use? Note 18, then, is that way?
**MG Marylia Gutierrez** 08:08 Let me see what I I am.
**Trent Mick** 08:10 Just think.
**MG Marylia Gutierrez** 08:11 Yeah, my own, 19.9.
**Trent Mick** 08:13 Yeah, okay, I think it's No. 20 updated to Npm, 10.
**MG Marylia Gutierrez** 08:18 Okay, yeah, I cannot all do the all the updates. Yeah.
**Marc Pichler (Dynatrace)** 08:23 Yeah, that's that could help. And yeah, I'm not sure what the fear in the package lock actually is. So I'm not sure if there's other things that been moved around and are not related to this. But if it's like the license fields, and there's some other one that keeps popping up all the time. If that's the 2, then.
**MG Marylia Gutierrez** 08:47 Yeah, those were yeah. Were those the ones you add a couple of extra thing, of course, because I just add a new package. But besides that, all the others, for just those same fields.
**Marc Pichler (Dynatrace)** 09:01 Yes, I will review this one. I have already started with having a look at that one a few comments that I have right away is, I'm not sure if, like copying for getting started is the best approach right now, for.
like these things, because yes, we wanna remove it eventually. But it is stable. So it's not gonna go anywhere for sometime, at least until we pump to 3 dot O, which we haven't like, define the plan yet for and if there's any needs in this package that we change these these functions or add new ones. We can just add them to the package here instead of core. And then eventually, once we pump to 3 dot. O, we can just move these over.
Okay.
I guess I'm not sure if if anybody has suggested any other things before. But that would be my personal preference on on these things.
Yeah. But I will post my comments anyway. And then from there, anybody else has input on this Pr, please, or like, wants to get involved with this, please have a look. And then, yeah, we can get this.
We can get this going.
**MG Marylia Gutierrez** 10:31 Yeah. And once I have this, that is like structure ready, my goal is to create like separate issues of all the things that are required for this.
and so that I can share. If anyone is interested in also working on this, we already have, like a plan of what to do.
**Marc Pichler (Dynatrace)** 10:47 Okay 1. 1 question that I have is, have you looked into any way of generating code from the definitions in the I think it's Jason Schema definitions, right? Or something like that.
**MG Marylia Gutierrez** 11:03 Yeah, so haven't looked into that one yet. That is my goal. So I have one file that already left it like separate, that is called like just the config and that is kind of like a copy of the thing I've been using, like the same comments that they put it there. So my idea is to kind of have at some point similar to what we do like semantic convention that we just generate, based on. Then have it here. So that is the end goal. But I haven't got to that point yet.
**Marc Pichler (Dynatrace)** 11:35 Alright, sounds good.
**MG Marylia Gutierrez** 11:41 Next one me again. It's just from the consumer experience saying that we were looking at like some responses from some of the service we did some people. Sometimes they complain about like time to reply from Prs and stuff like that. So I was not aware that this existed. And then I was looking specifically like, even look like the Javascript. So for the core one, I think we are good. We are like less than 3 days, considering that also counts for weekends, I think, makes sense and then I noticed on the contrive is a little higher, is like 5 or something, 5, 6, with sometimes being like over a week to reply to comments.
So maybe that is something to keep an eye and be a little more attention on the contribut as well cause. I know that a lot of them is just. We tag the owner, and the owner don't necessarily look.
But yeah, just wanted to bring this.
**Marc Pichler (Dynatrace)** 12:49 Yeah, in in contribut, there's yeah, as different sorts of ownership. I guess that's also why why we see that discrepancy here.
because everything in in in the core repo we assume, like as is owned by everybody who is with on the on the approvals or maintenance or creators list and back to country people is more of a like. There's smaller groups that are kind of assign this owners for the different packages.
**MG Marylia Gutierrez** 13:29 Yeah.
**Marc Pichler (Dynatrace)** 13:30 And there's sometimes some some differences in like the response there. So yes, it's definitely something that we.
But look into getting getting reduced somehow at of any.
**MG Marylia Gutierrez** 14:03 And this is the end of my Ted Talk.
Okay.
**Marc Pichler (Dynatrace)** 14:09 Okay, Does anybody have any anything they would like to add, or any additional topics that they would like to bring up this week?
**Hector Hernandez** 14:25 Just one quick thing. Sorry I missed the lock stabilization question. I think it will be good to go through the board of the remaining things we have been.
We left this unattended for a while. There has been some progress in several locks related. Prs, I also have this huge change to basically move locks Api into the actual main Api package as experimental. So we're trying to push this for stabilization hopefully soon. So it will be good to to start talking about it more often.
**Marc Pichler (Dynatrace)** 15:00 Yeah, the.
This is the pr you were talking about. Right?
I think. Yeah, Dan commented. Here. Anyway, that we'll probably need to get all the other things done 1st before we can actually move the the thing over.
**Daniel Dyla (Dynatrace)** 15:26 To be clear. I don't think we absolutely have to get everything done before moving it over. I think we just wanna make sure anything that's a that would be a breaking change. We do just to avoid threat. This is moving it as experimental. We can change things, and I don't think we need to treat it as like a hundred percent stable when we do it. It's just we want to get as close as we reasonably can.
Api is still usable without integrating it into the main Api package. So there's no like really strong motivation to move it over that I'm aware of.
If this is a blocker for something else. Please let me know But also there's no, I think, reason to wait for it to be perfect, either. I think we just wanna make sure we get the low hanging fruit, the breaking changes. We know we need to make like adding event name and stuff like that but I don't think we want to necessarily hold this forever.
**Marc Pichler (Dynatrace)** 16:28 Yeah, completely, agree.
**Hector Hernandez** 16:30 Yeah, yeah, I would prefer to not hold it forever.
**Daniel Dyla (Dynatrace)** 16:33 Yeah, okay.
**Hector Hernandez** 16:35 Marriage is not easy. But yeah, yeah, it's not that I'm pushing to move this right away. It's just I thought it was part of the stabilization plan. So I'm just trying to to push that forward right.
**Marc Pichler (Dynatrace)** 16:48 Okay, yes, that makes sense. Yeah. The I think there's just few things that still need to be done before this before this becomes very actionable. And once we have these things sorted out I guess there's nothing that speaks against actually moving this along. A bit quicker is the the few things that I'm talking about is exactly these breaking changes that Dan mentioned earlier. That, I think we should get in and test drive. We have one more experimental release before actually migrating it to the Api package.
But once that is done, I think there's nothing that speaks against like moving this along and anymore, topics that you would like to bring up.
Okay, not then. We'll move on to back triage for now and if you if you have a topic that you would like to discuss that's not related to bug triage, please just let me know, and we'll go back to discussing the topics in between.
All right.
The 1st bug here open 3 h ago session related type error from Grpcjs.
We're using honour frame, but never seen that before on Bun.
Oh.
I wonder if this is a button?
Something that happens on button, but not anywhere else errors are killing the process.
**Daniel Dyla (Dynatrace)** 19:33 Yeah, I would add the runtime bond label.
**Marc Pichler (Dynatrace)** 19:38 Hmm.
**Daniel Dyla (Dynatrace)** 19:39 If it's killing the process, it's p. 1. But it is an unsupported runtime.
**Marc Pichler (Dynatrace)** 19:50 Or put a comment here.
**Daniel Dyla (Dynatrace)** 19:53 It also needs a reproducer.
**Marc Pichler (Dynatrace)** 19:55 Okay.
Nowhere.
**Trent Mick** 20:47 Super.
**Marc Pichler (Dynatrace)** 21:12 Script producer on here.
I will actually assign a p 1 laborious way. Seems to be that this would be somewhat easy to reproduce, though, with, like all of that here.
just copying together and running it find some time I will look into trying to reproduce that here.
Yes.
Also, the way that they could go is not using the Grpc exporter and switching to the Http one. We recently merged the change. And I think it's released there already. As well. That removed some old quote that wasn't used anymore in Nodejs. That should sort some issues in buttons where?
yeah, let's see what they come back with here.
Copy moving on to the next one.
Ignore urls for the domain name work or xhr. Requests.
I'm not fully up to speed on how to configure the this package here.
**Daniel Dyla (Dynatrace)** 23:17 I don't see the patterns that they're trying to let's see. Get some relative ignored by so dude pattern they're using is like dot star my app.
But I guess that would only work if relative URL is passed to the open mission matched against ignore Urls.
Yeah. So oh, it's the relative path is ignored. I got it so. The absolute path is, is properly ignored. If they use dot star my app, because that's part of the the domain. But the relative path is not so. I guess we want to make sure that we're always matching absolute paths. So if you call.
if you call Xhr with a relative path. We have to run the matcher, not with what you called, but with the absolute path. I think that's a reasonable call out and probably a p.
**Marc Pichler (Dynatrace)** 25:12 You, too, I guess.
**Daniel Dyla (Dynatrace)** 25:14 Yeah.
**Marc Pichler (Dynatrace)** 25:23 Right?
yes. But then do you want to add a quick comment, saying, like, just reiterate, reiterating what you said right now to this issue.
**Daniel Dyla (Dynatrace)** 25:41 Sure.
**Marc Pichler (Dynatrace)** 25:42 Okay, thank you. And then if somebody has time, they can. Look into picking this one up it's a bit more clearer for them what to do.
**Daniel Dyla (Dynatrace)** 25:53 I can't get to the bug because you removed the triage label.
**Marc Pichler (Dynatrace)** 25:56 Oh, no! It's 5, 8, 10.
**Daniel Dyla (Dynatrace)** 25:59 5, 8, 10. Thank you.
**Marc Pichler (Dynatrace)** 26:08 Alright we can move on to contract.
Examples. Express cannot work.
I think they are somewhat outdated if I recall correctly.
if they trust the order comes from this.
Yeah, that would make sense, because it initializes the the thing later.
Since this is back in the examples, I would put a P. 4. Here copy and put the express label on here.
call me alright phone.
And I think it's it for a contribut as well.
alright phone, so we can move on to pr triage.
yes, I haven't been. I've probably noticed I've been on vacation for the past 2 weeks, so I might need some help in getting up to speed on. What's going on here the 1st one. I think if I recall correctly, David, you've been working on another pr, that was.
**David Luna Bistuer** 29:34 I have a similar one that that actually so I split that specific one. I split it into the 1st one is already merged, the second one is waiting for review I didn't want to.
**Trent Mick** 29:46 My bad. I said I was gonna review that. Yeah. So I think I think we get David's in and we can say it closes or obsoletes this one as part of that committed it'll close this one.
**Marc Pichler (Dynatrace)** 29:58 Alright. Yeah. Sounds good. Then I guess we can skip over that one. Yeah, as always, if anybody has.
and please review. If it's Pr, and then so that would actually improve the developer experience quite a bit.
Alright. Send this one here.
Seems like Jonathan, is unresponsive here.
it's the specified behavior that seems to be bit larger to be reviewed here right now.
But I guess we could also just review this one and getting get it in like I did marched I actually put a note for me to reach out to them on slack and see if there's anything going on that's out of the ordinary that would cost them not to be responsive.
And let's hope that we can get this on the way, because the Pr is actually up to date just missing the reviews from the component owners.
Right? And the next one is react native Pr, that I guess it's also kind of client instrumentation stuff related. So I guess that's on hold still, right now.
**Daniel Dyla (Dynatrace)** 32:32 Yeah, I think so.
**Marc Pichler (Dynatrace)** 32:34 All right.
The next one.
**Trent Mick** 32:38 Had the last browser Sig meeting. Had they talked about like saying, Hey, this, the whole new event space world is. Gonna take a while. Let's move forward with the instrumentations in the meantime or not. So like, I don't know if this is it actually on hold. I didn't make the last meeting, so maybe I shouldn't.
**Daniel Dyla (Dynatrace)** 32:56 Yeah, I went to the last meeting. We didn't talk about any of the existing instrumentations. But I think the the last time we talked about it. We talked about completely, essentially rewriting them from scratch.
I think it's not going to take a while. I think it's going to be one of the 1st things the browser Sig works on before doing any like Api or SDK changes.
**Marc Pichler (Dynatrace)** 33:36 All right.
I guess we can continue on right away with the next browser related thing.
the status on this one here is okay, with putting it on. Hold right now.
The things are the the instrumentation work, is it? Is it blocked on anything right? Now then, do you know, is there like some comp work that goes first, st or it should go 1st before the actual instrument.
**Daniel Dyla (Dynatrace)** 34:25 And they should.
**Marc Pichler (Dynatrace)** 34:25 Mprs, come up.
**Daniel Dyla (Dynatrace)** 34:27 I think they will want instrumentation as prototypes for the semantic convention work, anyway. So I think it will happen kind of at the same time, I don't think the semantic convention work is blocking it necessarily.
I think that.
Yeah, I I wouldn't add a new page view instrumentation right now, without having the people from the browsers take. Look at it.
**Marc Pichler (Dynatrace)** 35:03 Okay, and
**Daniel Dyla (Dynatrace)** 35:06 What is the comment that I linked there? 2386.
**David Luna Bistuer** 35:11 It's me talking, I think. Yeah.
Talking about the fact that there are semantic conventions, and there was a Pr. I don't know if the Pr. Is closed.
some of them are closed, but not preopened, so we would talk about this this in the process sake would like to reopen it and start the discussion. But I have no no permissions to do to do so.
Yeah.
**Daniel Dyla (Dynatrace)** 35:34 I'm not sure if Abnette has been joining the browser sig I think maybe this points to. Maybe we need to add, like some approvers from that browser Sig into our contrib approvers list?
So that they can.
Because right now, we we just don't know what to do about these browser instrumentations.
**Marc Pichler (Dynatrace)** 36:10 Yes, I think, having some more people here that would be interested in reviewing these things would be very helpful. It seems that. Martin approved this, but quite a while ago, and I guess there's been some some changes to like how things should look like It would definitely be good to have some involvement in Semconf as well, so that the instrumentation is actually working towards like being a prototype rather than just being a standalone instrumentation.
**Daniel Dyla (Dynatrace)** 36:51 Yeah, I think that's kind of the way I feel about it, too.
**Marc Pichler (Dynatrace)** 36:55 Hey!
Oh!
**MG Marylia Gutierrez** 36:59 Also, I don't know the focus of March now I have changed. He's a grafana now, so depends on what he's looking out. If there's anything in particular can all can also let me know I can message him.
**Marc Pichler (Dynatrace)** 37:20 Oh, that this is the the person that opened the Pr. Just to clarify right? I just know them by the name Ebbinette.
**MG Marylia Gutierrez** 37:27 No, I'm talking about because I talking that Martin reviewed the stuff.
**Marc Pichler (Dynatrace)** 37:31 Martin. Okay.
**MG Marylia Gutierrez** 37:32 Yeah. And then he opened the other yard that got close No. He just joined a grafana.
**Marc Pichler (Dynatrace)** 37:43 Yes, I think if if Martin is interested in getting this moved forward. Then yeah, if you if you ask him, I think it would be would be helpful to reach out and see what his priorities are on this. And if that is something that he is interested in. I think another review would be.
oh.
would be good here, or if he's interested in driving some of the same conf efforts probably or so
**MG Marylia Gutierrez** 38:16 Yeah. Can I can message him.
**Marc Pichler (Dynatrace)** 38:19 Okay.
**Daniel Dyla (Dynatrace)** 38:21 Yeah, they should be done in parallel with some comp, though I don't think it should just be like, Oh, well, there isn't some Comp. So I made this.
**Marc Pichler (Dynatrace)** 38:37 I will just put a comment here that we discussed this in the Sig meeting today, and that we are looking for.
when when there's browser instrumentations being added that they go hand in hand with an effort to also drive Sam conf in that regard and then we'll see if the person that opened this Pr is interested in doing that. Otherwise, I think eventually, the client the the browser sig will also end up working on something like this in probably near future.
right.
That was this one. Then we can move on to the next one, which is sequelize it's been has been a review here.
Almost.
It approved this. So my comment is near looks like got it?
No conflicts right now. So that is something that I will have to have a look in a bit more details, not something that we can just simply push through on the call here today. There's a lot of dB, Sam Confin use. So we wanna make sure that this is also up to date with the stable ones.
I think.
Wow.
seen usually does a really good job in making sure that everything is started out when he updates and comes. So I wouldn't assume that to be any large issues, but still need some more thorough review there.
Alright, this is It was a forced push. Unfortunately, so makes everything a bit more difficult. Otherwise it would be fairly easy to just merge this in right now.
I guess.
Reception hook.
It's in types, so it will be automatically exported as well.
I think this one is actually good to go. It seems very.
very much in line what we what we saw here before.
See if the pipeline passes, and then we can get get this merch soon.
Alright!
Next one this is the bye.
pretty close to 7 min ago. So just gonna refresh my page. Then.
Oh, the next one is web exception, instrumentation.
I have.
which is requested here. But this, Bot didn't volunteered as a component owner still doesn't seem to be edit here.
I guess there's there's nothing yet, but if there's, I think, the onus we should be strict on requiring at least 2. There.
**Daniel Dyla (Dynatrace)** 45:03 Hmm.
**Marc Pichler (Dynatrace)** 45:08 Oh, yes.
I mentioned that I was going to review this one, but went out of office for a while. I'll put this on my list again.
**MG Marylia Gutierrez** 45:28 Does this get affected by the changes that risk was doing about like tokens and permissions.
**Marc Pichler (Dynatrace)** 45:36 Yes, we I don't think it would be affected, since it's a new workflow, but we should at least review it in with that in mind. To make sure that we have the proper permissions in place, and limit everything that it can do as much as possible.
Alright, The next one.
It's conflicts and missing tests.
So we're actually close this Pr here closed.
Oh, we can move on to the next one.
This was the Gcp. Detector thing.
9, 23rd that was last week where I wasn't here. There seems to be. Have.
**Trent Mick** 48:06 Yeah. So we did. We discussed it. Aaron, that's that's mess github user. Yeah, basically what? The last comment is. So it's on him to come back, and it's only been a week so.
**Marc Pichler (Dynatrace)** 48:19 Okay, leave it in its current state. I think.
**Trent Mick** 48:22 Same with the next issue.
**Marc Pichler (Dynatrace)** 48:24 Okay.
**Trent Mick** 48:26 Same with the next issue on your triage board. It's related to this one.
**Marc Pichler (Dynatrace)** 48:31 Okay.
Oh.
**Trent Mick** 48:49 I'd reviewed this one. It's on newly out of. Follow up. I don't know what we do for an activity.
**Marc Pichler (Dynatrace)** 49:02 or put the comment here.
**Trent Mick** 49:10 Next week and ask if she's gonna have bandwidth to come back.
Yes.
**Marc Pichler (Dynatrace)** 49:43 I'll put the comment here, and then we can wait a few more weeks, and if the person that opened the Pr. Doesn't come back then can close it again.
Then the next one is acting full container id from Ecs. Fargate Group.
Oh, Jonathan actually commented. Here monthly, push 2 commits which I would assume.
Oh, still to do what Jonathan suggested here. So we can leave this for a bit. This was just last week oh, 7 days ago, so can still be some that's still some time for them to come back and review it again right?
This one is in draft, so I guess we can skip it.
**David Luna Bistuer** 51:12 Yeah, skip it, please.
that this needs to have the.
**Marc Pichler (Dynatrace)** 51:20 Wrong, one.
**David Luna Bistuer** 51:21 Okay.
**Marc Pichler (Dynatrace)** 51:22 Sorry.
**David Luna Bistuer** 51:22 There's the actually once understood, is a requirement for this one too.
**Marc Pichler (Dynatrace)** 51:38 Alright And there's renovate Prs, which I guess we don't wanna merge, anyway.
because they're breaking tests right now.
So close this and there's Oh, I got confused, and which one was the latest that I was looking at this one.
and this one here seems to be.
**Trent Mick** 52:32 That job failure was just for network connectivity. I just restarted it.
**Marc Pichler (Dynatrace)** 52:36 Okay, awesome. Thank you. And believe that running and see what happens.
Then the next one's a real Pr again.
Oh, this is type support in instrumentation.
**Daniel Dyla (Dynatrace)** 52:57 I think if you look at the comments you'll see people, possibly even me tagging a Becky saying, please review this.
I know that you reached out to him to, and he said he wanted to still be the owner of these components, but he's not responsive. I think we need to.
Somebody needs to take these over.
**Marc Pichler (Dynatrace)** 53:28 Yeah, it seems that this has already been 3 weeks ago, I were put another thing on my list of action items to reach out to Obekney and seeing them again about if they have time to be involved still.
Oh, then we can get some clarity on the ownership situation of this package.
Oh.
oh.
this happened last week. Has owner approval.
I'll give this a quick look as well, just to make sure that everything's okay overall from a high level perspective. And then this can also be merged. Just won't merge it on the call right now, because needs some more time to for me to like grasp fully what's going on there.
perhaps, and 2 more renovates. Prs, and this is the Pr. That If it was talking about with the test services. Scripts person needs some more time to you rebuilt but bye set release. Pr.
Seems to be that I would actually wait until tomorrow morning, when I'm actually in the office to merge this to deal with any issues. If that that happens to be a problem with one of the Prs that could merge domain.
if anybody is interested in like learning how to handle contract releases or like core releases, for that matter. As well. Please reach out to me. If you're at least an approval, then I have, and then you have necessary permissions, or that can get you the necessary permissions to walk through the process. And we can also get releases out a bit more quickly. When people are on vacation and whatnot. So if that's something that you're interested in, and you are an approval. Please reach out to me.
And yeah, I walk you through it. It has gotten fairly simple over the past 2 years or so more more automation. So it's not as involved as it used to be.
only renovate again, renovate again, and then there's a Kafka, Js, tr.
instrument transaction sentencing seem already approved. This one. So just have a quick look at this same just here to make sure that nothing is doing sketchy things so that we can improve the workflow and run it, and once that is done, this should be good to merge.
Then I think we're pretty much out of time now, anyway. Alright Nobody has anything they would like to bring up. Then. Thank you, everybody for joining
**Daniel Dyla (Dynatrace)** 59:05 Thank you.
**Marc Pichler (Dynatrace)** 59:06 Have a nice week and see you next week.
**Daniel Dyla (Dynatrace)** 59:10 Have a good one. Guys thanks me, too. Amelia.
**David Luna Bistuer** 59:13 Bye.
**MG Marylia Gutierrez** 59:14 Thank you.
**Marc Pichler (Dynatrace)** 59:16 Okay.
