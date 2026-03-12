SIG: Rust SIG
Date: 2025-06-17
Duration: 25 minutes
============================================================

## Zoom Recording Transcript

**Cijo Thomas (Microsoft)** 01:03 Hello!
**Anton** 01:06 Hi heid.
**Cijo Thomas (Microsoft)** 01:08 One second I will share my let's give one to 2 min to see if anyone else joins.
I think we can get started. I don't see anyone else messaging about joining or joining. So we should be good.
Yeah, I missed like last couple of weeks not quite sure if there was anything we discussed last time. I don't even see a notes from the previous week. I completely missed the last one the previous one. We it says, no one else joined. So we did. Okay, young Yang and Pol were the only ones.
Yeah, there are like topics to discuss. We can add it to the agenda, or like, since it's just a small group of people we can just probably start talking without having to put here. I have a very skewed ask which is to help review the donation or contribution. However, you want to put it so. This was a tower instrumentation. It's doing metrics only right now, but it can be in the future in which to add traces also.
So this was maintained in a personal report by someone in Grafana.
So we have asked them to contribute it to open telemetry.
Country people. So this East up here believe this is mostly ready. There are like couple of like linked issues, and like some minor comments about adding a readme.
Because this, this has a very detailed example. Node.
like the typical examples we have. This has a full blown example, including deploying collector Prometheus Grafana, including Mimir.
and even like pre-built dashboards. So it's a bit more than our usual examples.
Oh, yeah, excuse me, yeah. Please help review this one.
I think I might have requested Anton to review the a similar Pr in the Demo Report open Elementary Demo where we are now using the newly donated Instrumentation Library. So we got this instrumentation for Actix Server a few months ago.
Now the Demo Project Open Elementary Demo Project. There is rust component. It's now rewritten or refactored to use the Semi Official Instrumentation library.
So I expect that once, though the tower one is done, we might be able to showcase that in the demo itself Demo already has Docker compose, and even Kubernetes file to deploy application along with collector dashboards and everything. So we don't need to.
We don't have to like, maintain all the details from this contribution. But it's okay to go in asses.
Yeah. Just one ask to review for this one.
My only other topic is about the next release. We didn't have a chance to review what was spending.
So I think I just created a new milestone. It was point 3 0. So I added point 3 1 to decide like. I mean, I wasn't sure whether it should be a point 3 1, or it should be a patch one.
So, depending on how much progress we make. This would end up being a patch one, if you're all adding, like minor bug fixes or things like that.
But if we end up making breaking changes for tracing or something, then we may want to put this one. So I just opened this one like, if there are anything which you are working on. Please feel free to add to the milestone, so we'll keep it updated so people can see what's coming in the next release.
It's quite lightweight, as you may have already noticed, there isn't much plant except the Tokyo tracing one, which then we can talk about next. But everything else is either a work in progress, Pr, or like very simple removal of feature flags. As things are getting stable.
this actually has an interesting thing. So a couple of days ago. Copilot has been enabled for the report. I did try to use copilot to do the job. Unfortunately, it couldn't work. It didn't work, so I'm hoping that this gets fixed by the Cncf copilot account team.
Okay.
have used it in like other places. It it works like, very good. Of course we had to review it and all but generally. If you give like detailed instructions, including exit criteria like how to validate corporate has done a job. It does a very decent job of doing all kind of this kind of like somewhat trivial jobs.
Expectation is almost all the issues marked as good. 1st issue could be easily covered by co-pilot. If it if you get the seat from Cncf co-pilot thing.
Okay, yeah. Now we can go back to this 9, 6, 2. Let's play it.
Excuse me, yeah, this was open for quite a while, I think. Jungyang reviewed it recently.
I see.
**Zhongyang** 09:28 Think just in case anyone want to take a look before I merge this.
it is, after all, Api.
**Cijo Thomas (Microsoft)** 09:36 It was a breaking change. Right? Yeah.
**Zhongyang** 09:38 Yeah, it's where it can change.
I didn't merge it. Figure I can give people some time to review it before.
in case there's something we're missing.
**Cijo Thomas (Microsoft)** 09:48 Oh, this is just adding, Okay, this is, there is no feature flag. So it is directly modifying the existing interfaces. Okay? Got it. Yeah, we'll definitely need a change log entry.
Yeah, I'll just add a comment right away.
Yeah, I think we need to any any. Was there anything like worth discussing now, or like young. And you said you already reviewed it so like. If there is nothing which requires discussion, then we can rely on offline reviews.
There was a similar pr which is to add on ending that's under feature flag, because spec is under feature. Flag or spec is experimental. Yeah, this one.
that one. All I did look at it. It looks good, except I left a couple of comments about examples, not the actual code itself.
Oh, but if this looks good, these 2 can go in the next release.
I mean, obviously more things can be added because we only put August end as the date for next release. So we have plenty of time.
Okay, nothing else in the agenda, like, I think it might be a good time to discuss or rediscuss the tracing integration thing beyond. You're also here. You mentioned that, like again, like background, is like we were trying to contribute to tracing open telemetry, but unfortunately beyond Spr. Did not get any review.
Except some one started reviewing it right now, or okay. David has asked to review it. Okay.
**BA Björn Antonsson** 12:00 Yes, exactly so, David, who was involved in the discussions and on on the open telemetry Repository is now a maintainer of this great. So he has started reviewing, and I'm gonna move the the Pr. Forward a bit and and.
**Cijo Thomas (Microsoft)** 12:23 Okay.
**BA Björn Antonsson** 12:24 This.
**Cijo Thomas (Microsoft)** 12:24 Was there any mention about like long time maintenance? Or, oh, okay.
okay, nothing. It's more like technical questions like, because he wanted to like, make sure like one.
There will be like someone actively maintaining it cause we it took like approximately a month and a half to get someone to review it. So.
**BA Björn Antonsson** 12:49 Yeah.
**Cijo Thomas (Microsoft)** 12:51 Okay, good. Okay. This is the case. Then we just need to like, wait for them to adopt these changes. And then, like, do all the breaking changes which we've been like holding off in the tracing thing.
For the milestones. I I really think, like we should have a sooner milestone where we can declare the tracing Api's table.
There are a lot of things here, I mean quite large number of issues, and most of them are relying on the this Pr. Because once that Pr is done, then there shouldn't be any need of all this. Non standard ap, so we should be able to clean up all of those things, but I don't think that's the only thing remaining like. There are few more things here, so we'll need to take a look at this one by one and see if we can put a target date for tracing Apis table, and then, of course, followed by tracing sdks table. That also has.
Oh, quite, not that much. But yeah, there are like some issues.
Yeah, I don't have a timeline in my mind. But I think we should try to put some timeline because we did the same for metrics and logs last year, even though we were off by thing 3 months. We only declared it a stable on like May End instead of February or something. We were off by a few months, but at least it gives people some rough idea so like, since at least like couple of maintenance and approvals are here. Maybe it's a good time to put some tentative date. Anyone wants to propose something, I would say, this is already June, so I don't think we can make anything happen in next one to 2 months, or maybe sometime in September, would be reasonable again, like this is completely depending on how quickly this we are progress, because that allows us to do a bunch of cleanups.
Is everyone. Okay? If I put a 10 day to you, timeline like September end, that would be 3 months.
June, July, August, September. Yeah.
**BA Björn Antonsson** 15:18 That that sounds reasonable. I think I mean, I actually hope that the tracing open telemetry Pr. And and work will move fast now, because he, he seems very active.
**Cijo Thomas (Microsoft)** 15:32 Okay, yeah, yeah.
yeah, even when when I joined the open elementary investor for like, we were having discussion to do, yeah, this one. I think there was a issue to sorry declare traces as stable in 2020, I think 2,020, not this one. There was an issue. But like, it's almost 5 years.
we are not yet in a shape to declare.
which is why I think, oh, yeah, maybe this one.
Yeah, this was started like, in 2020 so we thought, like, we were very close. But then it didn't happen. So it's okay to like slip, at least we. If we have a rough idea, then we can keep this in mind.
Now, for.
**BA Björn Antonsson** 16:20 That that sounds very much like the next version of Tokyo tracing, which has been near release.
**Cijo Thomas (Microsoft)** 16:29 Yep.
**BA Björn Antonsson** 16:30 For 5 years. So.
**Cijo Thomas (Microsoft)** 16:32 It's not just the next version. I think they have plans to do one dot 0. That was also similarly stuck.
Yeah, okay, yeah. For Api like September. Then this would be like, probably end of year is more realistic.
Just put like exactly the last day of this year. I'm hoping that, like once the Ap. Side of things are done, it should be relatively easy, through easy to go through the SDK. Once, because we have already done stable release for logs and lot of things in logs were originally copied from tracing SDK itself. But we did improve things in logs. So we just need to like apply that learning back to the SDK, so it should be, I hope, relatively small. But yeah, we'll see.
There could be like some things which are improperly triaged.
for example, like this one is about Yeager. So this should be like completely removed from SDK stabilization. Those are part of exporters.
Yeah. And then, like, resource is more like a common thing not really tied to tracing. It's more like a neutral thing notated. So there could be like some re retry of issues as and when we find it okay, with that.
yeah, beyond, like, now that I think we have good set of people here I want to like, discuss something we briefly covered in one of the Prs. Which was about adding some capability to the apprender for tracing. Create let me open it. And oh, you know I won't be able to find it. Maybe it's in a believe this is the Pr where we discussed.
Yeah. So there was a feature. Ask to modify the tracing integration, the purely on the logging side. I'm not talking about span at all, so purely on the logging side. There was a feature asked to enrich the log records by getting all the attributes from the parent span and the chain of parent spans, and then attaching it as attributes to the logs.
This is, I would say, a very common ask from what I gather, because some people don't even use distributed tracing, they are only relying on logs. So unless some changes like being proposed here is done.
Any information which is captured in the parent spans are completely ignored.
I think this is a reasonably good feature. Ask again, it's opt-in basis, so no penalty if users are not opting in. But if they do opt in what this does is, instead of just converting the tracing events into open telemetry log records, it will also look at the parent spans and get all the attributes, and then store them as attributes in the logo code itself.
On one.
**BA Björn Antonsson** 20:08 Just a quick question. There this walks, the this walks the hierarchy of Tokyo, tracing spans right.
**Cijo Thomas (Microsoft)** 20:18 Yep, yep, exactly. Yep.
**BA Björn Antonsson** 20:21 So that that means that it will miss things if we if people create, I mean with the new integration. If people mix open telemetry and and tracing spans. In the code. Things will not be there.
**Cijo Thomas (Microsoft)** 20:40 Yeah, the attributes from spans created using open delimitry will not be captured.
Yeah, that the reason I believe I I've been asking, or I've been asked about. This thing is lot of people use tracing and they use the tracing spans purely to get enrichment to their logs, not with the intent of viewing those spans in here.
**BA Björn Antonsson** 21:08 Yeah, yeah, absolutely. No. I I complete completely understand the use case. It's I. I just wanted to make sure that I understood what's being asked. So yeah.
**Cijo Thomas (Microsoft)** 21:19 This is something which I believe we discussed quite quite a while ago. So there was a proposal in open elementary. The report is now archived. But there was a proposal in open telemetry about in process context which never got merged. There is a lot yeah, in this is inter process.
I need to find where that it was quite heavily discussed. Yeah, I think this was context scope attributes, which is something which open telemetry currently does not have. Because if you put something in baggage, that's the typical place where people can put arbitrary Qalu pairs, it escapes the process boundary.
There was a proposal to do something like if you, if you're doing like some logs, do you want to add some key value pairs, you want it to be associated with the entire logs within that process.
So that's what this proposal was. It never got merged, even though a lot of support it. I got asked about this like very recently. Yeah, I think I did mention oh, this in our report. So so that that's the main reasoning why such a capability is desired. So I'm hoping it's something we should be able to add without like confusing the users, because this would basically mean that anytime you create tracing span, you are doing it with the intention of enriching the events. Slash logs, not with the intention of producing a full blown span, so we cannot make a assumption about what users want, so all of this would have to be opt in users by default, gets nothing. They only get events converted into log records. If they opt in to this feature they will get log records, interest with attributes from span. And then there is the extreme case where people would get tracing spans converted into auto spans by virtue of using tracing open telemetry.
So there is this late different variety or or different category of scenarios or use cases. So we just need to be somewhat neutral in the default. Like, don't do anything by default and let the user pick what capabilities they want and enable it.
Oh, yeah, I'll I'll anyway, like, wait for the test to settle on the tracing open elementary before trying to do it here.
But yeah, just a heads up.
Okay, yeah. Any other topics which we want to discuss a few open prs, unfortunately, we don't have that many reviewers these days. So if any of you have bandwidth, please help review.
I'm hoping that, like the copilotting will help with few of the issues once it is enabled.
it's to be seen.
Alright, anything anyone wants to discuss beyond Yong Yang or Anton. Any topics you want to discuss other ways. We can end early.
**BA Björn Antonsson** 25:03 From my side, so.
**Cijo Thomas (Microsoft)** 25:07 Alright! Thanks everyone.
**Zhongyang** 25:09 Okay.
**Cijo Thomas (Microsoft)** 25:10 Yeah. Thanks. Yong. Yang. Enter anything.
**Anton** 25:13 No, no, all good, all good.
See you later. Bye.
**Zhongyang** 25:17 Okay. So bye.
**BA Björn Antonsson** 25:18 All right.
