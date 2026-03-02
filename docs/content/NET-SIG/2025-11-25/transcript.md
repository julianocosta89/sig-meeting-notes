SIG: .NET SIG
Date: 2025-11-25
Duration: 32 minutes
============================================================

## Zoom Recording Transcript

**Piotr Kiełkowicz** 00:57 Hey guys, can you hear me?
**Martin Costello** 01:01 Yes.
**Piotr Kiełkowicz** 01:02 Gross.
**Rajkumar Rangaraj** 02:11 Hello, everyone.
**Martin Costello** 02:13 Arash.
**Piotr Kiełkowicz** 02:14 Any rush.
**Rajkumar Rangaraj** 02:38 I think we have more topics added. I think we could get started. Piotr, you want to go first, and you want to drive it, or you want me to share? How do you want to take it?
**Piotr Kiełkowicz** 02:47 I think you can share. I'm not sure.
How… how you usually handle public.
**Rajkumar Rangaraj** 02:54 Thank you all.
**Piotr Kiełkowicz** 02:55 So, if you can, it would be great.
**Rajkumar Rangaraj** 02:57 Sure, just one second.
They were even able to see my screen.
**Martin Costello** 03:20 Yep.
**Piotr Kiełkowicz** 03:21 Yes.
**Rajkumar Rangaraj** 03:22 Good. I think,
The first thing is the, like, Pietro brought a very good point about releasing the stable version of the classic ASPNET instrumentation.
we both felt it's an apt to do the public API review here before the release. So let's… we could take a look at the public API and see if everyone is in…
agreement on what it is being there, and if it's fine, I think we can proceed with the,
the stable release. So, even before that, just want to check if anyone has any concern before we get into that part on this topic.
**Martin Costello** 04:07 And for me.
**Rajkumar Rangaraj** 04:10 Cool. I think we could, only one second, this…
I think we have…
This is no different, than if we look at it,
the class of the ASPNet code, this is no different than that. Is that correct, Piotr? All of this?
**Piotr Kiełkowicz** 04:40 Yes, it is more or less very similar. Okay.
The naming patterns… the naming patterns are exactly the same.
They can…
There may be some differences related to the…
real classes used under the hood because of the HTTP request or response can be in the different… different class, to be honest, but in general… in general, it should be the same.
**Rajkumar Rangaraj** 05:08 Okay.
So, should we take a look at both the places together, or…
Let's bring up, like, instead of, like, doing that, I'll bring the contrary report.
Let's verify how different it is. That's the only way we can…
Compare and see how people are going to see the difference here.
It's almost same. I don't see any concerning APIs here that we should be worried about. Piotr, you have any
Any issues with any of these, that we should be getting in detail?
**Piotr Kiełkowicz** 06:15 I think…
it is pretty staked. It is… last significant changes was done one month ago, and it was released then.
So, in my opinion, it should be safe to release.
**Rajkumar Rangaraj** 06:30 Okay.
So, I have a one question. It's not related to the public APA, rather the binding redirect. So…
if someone takes this package as it is, this with the HTTP module, both of them, it's not going to work. Immediately, it's going to…
Throw them some could not load… like, file load exception is what they're gonna get into it.
So, is that a place that we have any documentation on how do we… how the customer should handle that?
**Piotr Kiełkowicz** 07:05 Now, there is no documentation for bind… binding redirections. I never met this issue, to be honest.
**Rajkumar Rangaraj** 07:13 So you say, like, if you… if I recall correctly, right, if I create a plain vanilla classic ASP.NET app, and if I install this instrumentation library, you say without any issues it worked?
**Piotr Kiełkowicz** 07:28 I'm checking the source code, give me a second.
**Rajkumar Rangaraj** 07:32 It never works that way, if I recall correctly. Even if you look at the example app, which is over here, you will see a lot of
A binding redirect in it.
I don't even know whether all of this binding data… okay, it looks like it's all been updated to 10 here.
**Piotr Kiełkowicz** 07:52 Yes.
**Rajkumar Rangaraj** 07:54 Yeah, so these are… these are all that are recommended, so…
We… at least… if… it's not a very big blocker, but somewhere we need to document that… what redirections are needed, especially for that,
D.
Classic ASPNET Core… sorry, Classic ASPNET Instrumentation Library. If not, customers are going to struggle to find the right versions to place there.
**Piotr Kiełkowicz** 08:24 Okay.
I can try to create a documentation for this making panels for myself, so… so it is the last blocker, in your… in your opinion.
**Rajkumar Rangaraj** 08:33 It's not a blocker, but it's good to have a documentation update. Just to reduce the supportability burden, if not, people are going to come back here later and say, I ran into, like, an exception adding this one.
I think that's all. I think we are good here for the stable version. I don't have any… I don't see any other thing, because it's in RC for…
passed.
few weeks, so I think we are good to go.
**Piotr Kiełkowicz** 09:06 Cool. I will check what I can do about binding redirections, and then, when merged, I will…
Trigger the release process.
**Rajkumar Rangaraj** 09:17 True.
Anything else from you, Pietro, or…
**Piotr Kiełkowicz** 09:25 No? That's all, thank you.
**Rajkumar Rangaraj** 09:27 Cool, yeah, thanks, Piotr. Martin, you have a topic,
**Martin Costello** 09:33 Yeah, so this one's potentially a can of worms, so I wanted to try and explain the problem, and then see what people's thoughts are. So, there was an issue, a couple of weeks ago. Someone said that the EF core instrumentation doesn't work.
correctly if you use the Cosmos provider for EF Core, and that's because the Cosmos provider isn't a relational EF Core implementation, it's a non-relational one, and all the relevant hooks
sorry, all the relevant events for that distinction, the EF call provider does not listen to, so you don't get any of the instrumentation, it just doesn't work properly.
They reported it as a bug. I don't think it's strictly a bug, I think it's just something that was never implemented, and the library isn't stable.
But then, I sort of went off to the EF Core repository, and
found an old issue that's about having native OpenTelemetry support.
And Roji works on it at core, and he was… gave me some hints as how we could do it if we wanted to, but what he's essentially getting at is…
If you want Cosmos, or Mongo, or whatever instrumentation. You should use the support in the underlying providers.
And EF Core is more of a higher level, I'm doing the query.
Kind of level, rather than the database-level semantic conventions.
And the current implementation of the EF call provider is sort of…
floats in the middle. It's not fully doing a high-level EF core.
metrics and tracing. It's trying to also be, like, the SQL client instrumentation, and giving you, like, database semantic conventions.
But…
that now means it's sort of in this weird hybrid place, whereas if we went to make it generic EF core.
Then we'd remove most of the functionality from it and, like, refactor it to move to a higher level of abstraction.
But then, that undercuts the idea of being able to give a package to people.
that then works with lots of SQL-like providers without having to go into the nitty-gritty of which specific one it is, so you get your database semantic conventions.
But, if you then want to…
say you want to keep doing that, but you want to support non-SQL-like implementations, that now means there's basically an unbounded number of things that the EF core provider instrumentation doesn't do, that now needs to be implemented.
to support things like Cosmos, which is then kind of duplicating stuff that's already present inside the Azure libraries. So now it's sort of in this weird middle place, where it isn't really one or the other.
So is kind of like, what do we do about that? What's the path forward?
**Rajkumar Rangaraj** 12:51 So, let me ask a question. I don't… I need to look into in depth on this one. But, today, we are saying the Cosmos is here and saying if we support it. Tomorrow, some other provider comes back and say that, hey, it's not working for me, so we cannot
keep on tweaking this for every providers, right? Is that correct, in my understanding on that?
**Martin Costello** 13:14 Yeah, it's because, like, it doesn't work at all. Like, if you don't turn on the instrumentation in the Azure SDK for Cosmos itself, you get nothing if you use the Cosmos-specific EF Core provider, but, sort of.
the EF core instrumentation implies it will work with it, but it actually doesn't. It doesn't explicitly say it does, and there's no tests for it, and the only mention of Cosmos in the whole codebase is just the semantic convention attribute for the DB system name.
Where it just goes, oh, if the assembly's this name, then it must be Cosmos.
But because it's not a SQL provider.
The code to do that never runs, so it's kind of dead code.
**Piotr Kiełkowicz** 14:02 Martin, maybe it is… in general, not worth to invest in EF core instrumentation package.
Yeah.
Spend this time for adding…
tracing functionality directly to Entity Framework Core.
Natively.
**Martin Costello** 14:26 Yeah, that's potentially… that's potentially one option, it's just the only downside to that is then nothing… like, even if I did all the work tomorrow, nothing will happen for a year, because it will be part of .NET 11.
**Piotr Kiełkowicz** 14:39 I know, but… I think it is the… in general, it is the recommendation from OpenTelemetry for .NET.
To make instrumentation native as much as possible, to avoid any additional Right.
library dependencies, especially that Instrumented libraries does not need any additional reference except diagnostic sources.
**Martin Costello** 15:07 Oh, yeah, yeah, I agree. It's just that if we did go down that route, we'd still
Potentially have to support the current one for another, like, 2 years.
Because it will only be usable for people from… from next year for 11.
**Piotr Kiełkowicz** 15:22 I agree, but we do not… never… there is no need to probably
We do not need to stabilize, ever, so we can keep it as a better version, and…
Do not care so much about the backwards compatibility.
**Rajkumar Rangaraj** 15:42 Yeah, I agree with Peter. The end goal of this repo, especially the Contrib repo, is not to increase the number of the instrumentation or keep adding the features. The goal is to get the native instrumentation done in the products itself, and reduce the number of the
Like, products that we maintain in this contract.
So, if we need to keep to that principle, the path is clear, as what Piotr explained.
**Martin Costello** 16:13 Okay, that's… if that's the direction we want to go in, that's fine. It's just… if I… if I just unsolicited, just put a comment on the original issue and go, oh yeah, we're not going to do this, close.
It's probably not what you… it's not what… it's not what users would want to hear.
**Piotr Kiełkowicz** 16:34 In general, we can accept Kind of interim solution.
Even for the Cosmos DB, if it is strong demand for this. Maybe we will be probably not invest our time for this. I… at least I would try to avoid it, this kind of investments. But we should be fine to review and tell that this will be… clearly tell
that this version will be supported for .NET 8, 9, and 10, but there is a long-term plan to move all this instrumentation natively to EF Core, and then you can expect breaking changes.
In the level of… traceability.
**Martin Costello** 17:19 Yeah, I think that's fine, because it's,
Because, yeah, I looked into how much work it would do to make it work just for Cosmos, and it wasn't a trivial amount of work, and I didn't particularly want to do the work.
Especially given that they could just turn on the Azure SDK tracing.
**Piotr Kiełkowicz** 17:39 Thank you.
**Martin Costello** 17:44 Yeah, I think the only benefit… the only nice thing the EF core instrumentation has that,
We would lose by getting rid of it, is the fact that you can plug in one thing and get lots of observability on lots of different things at once.
Like, if for some reason you had, like, an application that used MySQL and Postgres and SQL Server all at the same time.
you can put one thing in and see all of them from the same library with one set of configuration. But I think that's the only…
positive.
It has of being, like, a person in the middle.
**Piotr Kiełkowicz** 18:28 Agreed.
**Martin Costello** 18:34 Okay, if everyone's in agreement, tomorrow I'll put a comment on the original issue.
that says, we're not gonna add support for Cosmos and non-relational, I'll then do a PR to update the README and point that out. So, if other people read it, they don't waste their time and then open an issue saying it doesn't work.
And then I'll… See if the EF core team are in…
active enough to be interested to review PRs, to maybe look at putting it in and get them to give some more concrete details on how they'd like it implemented.
**Rajkumar Rangaraj** 19:14 Yeah, and also try to route the users to the actual repo where they can go and request for the native instrumentation that might act as an unblocker for them.
**Martin Costello** 19:25 Yeah, if you just scroll to the top of that issue, Raj, I think it's quite old. I think it's just… it's constantly got punted out… yeah, 2022. It just keeps constantly getting punted out of their backlog.
**Rajkumar Rangaraj** 19:35 Okay.
**Martin Costello** 19:38 So I think they're… they're on board with the idea of doing it, it's just never important enough that the team itself actually does it.
**Rajkumar Rangaraj** 19:46 Got it.
**Martin Costello** 19:50 Maybe, maybe Aspire will,
Be the carrot that finally gets it done, even if we end up doing it.
**Rajkumar Rangaraj** 20:01 This may not be true, if I understand if the currently with Azure SDK stuff… yeah, let's push it back and see how it goes.
Yeah, I see the next issue here.
**Donald Hanson** 20:25 Yeah, this one I was, I met with some of you guys about 2 or 3 weeks ago about this one. This was around being able to modify a scope's attributes.
Before it got exported.
And so I took a stab at making a,
a change to support that in the SDK.
so, the suggestions and such that were in this original,
issue, I didn't follow through on, but the core of it was still somewhat similar.
**Rajkumar Rangaraj** 20:57 So, if I recall.
I don't… I did not get engaged much in the conversation, but when I… if I recall the discussion, the recommendation that was provided was to use the
the techniques in the iLogger itself, instead upon relaying upon something in the SDK, or do changes to the SDK.
Right.
write a, like, iLogger-based processor or something like that to.
**Donald Hanson** 21:24 That was one of the two.
**Rajkumar Rangaraj** 21:26 Yeah.
**Donald Hanson** 21:26 I guess I didn't… Okay.
**Rajkumar Rangaraj** 21:30 Martin, I think you were driving that conversation, that correct? Like…
**Martin Costello** 21:35 That was my suggestion, yes, because we did something similar to that at a previous job of mine.
**Rajkumar Rangaraj** 21:41 Yeah, I think we need to figure out if iLogger can help, if… only if there is no solution in the iLogger, we should be exploring something in the SDK.
**Donald Hanson** 21:50 Okay.
Okay, I'll need… I gotta go back and look at that then. Okay.
I don't know how that would work.
**Rajkumar Rangaraj** 22:03 Yeah, take a look at it, bring it back, like, then we can explore and see if there is… if you're hitting a roadblock, then we can think about what's.
**Donald Hanson** 22:10 Okay, yeah, I mean, I just… just knowing how the internals of how this stuff works, I don't see how that can work.
But okay. I'll go back and revisit it then.
**Martin Costello** 22:18 I did… I did a quick skim through your PR just now. I… I think as it is, it wouldn't be…
We couldn't take the change because it was making breaking changes to the interfaces.
**Donald Hanson** 22:32 Okay, that was the one thing that I wasn't sure on.
Which part of that is the concern? Is it the type change on the struct?
Or is it the signature on the foreach?
Or boy.
**Martin Costello** 22:47 Let me look at it again.
It was certainly the type change, I think, is one.
**Donald Hanson** 22:53 It would make sense, yeah.
Because it's only, effectively, two changes.
So, okay.
That was the concern that I had on it, was whether or not it would even be acceptable, so…
**Martin Costello** 23:13 It's a bit hard to read because of the diff. If I, like, opened it properly and looked at it, it would maybe look…
**Donald Hanson** 23:19 Yeah, it's pretty straightforward. Effectively, it's a scope, a log record scope was just a holder for an object, a bag for an object, and then you could enumerate it. And the problem with that is that you can't modify that bag.
Right.
And that was what I was looking at trying to do. I have a scope that's held onto, you know, 5 layers up. As I'm writing a log record, I want to modify the attributes that are going to be in that bag, just like I can modify to log record attributes.
So in my processor, I'm able to modify a log record attributes, but I can't modify scopes attributes.
So the general idea was…
To basically have the log record scope hold onto, its bag, and let you modify that inside your processor.
To overwrite what the attributes are.
**Rajkumar Rangaraj** 24:10 Do you know from a benchmark… did you benchmark this change and see…
**Donald Hanson** 24:13 the… there was an allocation difference. There was a 144-byte allocation that wasn't there originally.
So yeah, that was the other concern, I just didn't get to put them together in a way I present to you guys yet.
**Rajkumar Rangaraj** 24:25 Yeah.
Yeah, just try out the other approach. If not, we… I would still… my recommendation still remains the same, then only we should go this route.
**Donald Hanson** 24:35 Okay, sounds good. That's… I just wanted to get an opinion from you guys before I spent more time on it, so… sounds good.
**Rajkumar Rangaraj** 24:41 Thank you.
**Donald Hanson** 24:41 Thank you.
**Rajkumar Rangaraj** 24:45 That's all the… topic that we have, does anyone have any other things, topics to discuss here?
Okay, cool.
There are a lot of pending PRs here. Most of them are really pending on me to take a look. I have a goal to clear off all the aged PR here.
before the second week of December, so you might see some traction from
me in this area. I'll try to take a look at it.
So, nothing new here, it's most of them are, like, all world peers.
I think that's all we have for today. Is there any other topic or anything else anyone wants to bring in now?
**Martin Costello** 25:38 I pinged Alan on the issue to look at as…
He was the main person driving it, but
I remember we had a discussion a couple of weeks ago about we weren't going to make the sanitization opt out, and it always be on.
And someone's opened a pull request proposing that we make it opt out.
**Rajkumar Rangaraj** 26:02 Which one is that?
**Martin Costello** 26:04 It's in Contrib, it's… Which… where is it again?
It's issues… it's the top issue in Contrape.
**Rajkumar Rangaraj** 26:18 I'm sorry.
**Martin Costello** 26:27 I remember at the time, we were like, let's just always have it on, and then see what happens.
And now we've had a request that someone wants to turn it off.
**Rajkumar Rangaraj** 26:40 The sanitization, it always makes sense to keep it on, if you ask my opinion.
**Martin Costello** 26:45 But, as you and Alan are driving it, if it can wait for a week, I will… Oh, yeah, it's not urgent, I just thought I'd…
bring it up as it's something we'd specifically spoken about. The use case in the issue is it strips off some, something EF Core uses, which is related to…
Logging or tracing.
So then it, like, makes that less useful.
And this particular user's like, I know what I'm doing, I want to, like, remove the safety net.
**Piotr Kiełkowicz** 27:18 Martin, what's?
What is stated in this semantic convention?
**Martin Costello** 27:25 I think it just says, should.
I don't know, I did… I did quickly look at it after I read this issue, and it wasn't… there wasn't… it wasn't immediately obvious that it should absolutely, definitely never be ever to be turned off.
**Piotr Kiełkowicz** 27:39 Okay.
**Rajkumar Rangaraj** 27:42 The only thing is that the story will remain the same if we speak from an HTTP and the SQL perspective. HTTP, by default, it has sanitized the URLs. So here, if we're having a different story.
will cause a confusion, so having a single story to explain across the OpenTelemetry.net would be the right thing to do.
**Martin Costello** 28:04 I think all they're asking for is the ability to turn it off.
**Rajkumar Rangaraj** 28:08 Yeah, that makes sense, yeah.
**Martin Costello** 28:12 Yeah, I think they're perfectly fine with the fact that, by default, it does do that. I think they're just like, if I know, or I want to take the risk, I want to be able to turn it off.
**Rajkumar Rangaraj** 28:25 Yes.
That makes sense, a lot of sense.
I'll bring this up in the… sorry.
**Zach Montoya** 28:39 Sorry, I'm about to change subject.
Go ahead.
**Rajkumar Rangaraj** 28:42 Nothing, I'm just going to bring this topic again next week. I'll just give a heads up to Alan about it.
Okay. Yeah, go ahead.
**Zach Montoya** 28:53 Yeah, my question was, is there, any specific PR, that,
you would like… like, maybe I could help… I could review?
**Rajkumar Rangaraj** 29:03 If you can, in the OpenTelemetry, if you go and touch any of the long-pending PR, if you can take a look at it, it would be very helpful. Mostly the one with the,
There is a, I already have the tab.
open here. So if you look at the MTLS support, these are all the very important ones, if you can take a look at it, and ZZip compression. So if you can…
If you have a bandwidth and would take a look at it, it would be very useful.
**Zach Montoya** 29:37 Okay, yeah, I'd like to take a look, although I will be taking a holiday almost the rest of the week, so I wouldn't be able to take a look until, like, either this afternoon, or if I don't finish reviews then.
**Rajkumar Rangaraj** 29:46 No, no, no. Yeah, that's why I said, like, even… for the same reason, I said, just going to take time till the mid of December. And these are all pending for a very long time, too.
**Zach Montoya** 29:57 Okay.
**Rajkumar Rangaraj** 30:04 And I saw… Jack, I saw your message on one of the other
some issue, I think you were responding to, Sejo, about OTLP.
If I recall. I would say,
Just hold on to that till January. We will try and bring down our backlog, and then we will say anything that can get new that needs to be added to the ordeal.
**Zach Montoya** 30:31 Okay, yeah, that one was with the OTLP, the HTTP JSON, serialization format, so I was just,
I'd like to contribute that, but, if, you know, I want to make sure that there's bandwidth for reviewing and maintaining that before I…
**Piotr Kiełkowicz** 30:46 Exactly.
**Zach Montoya** 30:46 do anything?
**Piotr Kiełkowicz** 30:47 the protocol unit, it's Datadog, or it is just.
**Zach Montoya** 30:50 No.
**Piotr Kiełkowicz** 30:50 random.
**Zach Montoya** 30:51 No, it's not. There's… I mean, there's the question that one of the users on the issue was trying to get support for Datadog intake, which is already supported with Protobuff.
So they should just use that. I did comment that. But just for adding the additional serialization format,
that's something that I could do, so I was offering to…
**Rajkumar Rangaraj** 31:12 Still, I would say that we will wait for it and see if there is really a need for it, how many, like, customer reports it. The reason is, if we do something and if no one uses it, we'll be just maintaining it for no reason.
**Zach Montoya** 31:26 Exactly, yeah.
I understand.
**Piotr Kiełkowicz** 31:32 Like, if you can kind of create simple…
Implementation and prove that it is More performance? Yeah, we should.
invest in this. Otherwise, I do not see any reason to do this.
**Zach Montoya** 31:48 Gotcha.
Okay.
**Piotr Kiełkowicz** 31:55 I think your user wrongly understands the statement on your page, and tried to use wrong.
**Zach Montoya** 32:06 It's possible, they're also… I don't know when the person last responded, but they might have not.
Done some updates to our documentation pages as well, so it might just be a simple,
**Piotr Kiełkowicz** 32:19 I'm confused.
**Zach Montoya** 32:20 Yeah.
**Rajkumar Rangaraj** 32:30 That's all I have, Ert. Thanks, everyone.
**Piotr Kiełkowicz** 32:33 Thank you.
**Rajkumar Rangaraj** 32:34 built.
**Martin Costello** 32:34 Bye.
