SIG: .NET Auto-Instr SIG
Date: 2025-08-06
Duration: 21 minutes
Zoom Recording URL: https://zoom.us/rec/share/0QsgsbjC47jUEfibjw0LYIph1RfnXmT-R0G8A6eDDiMyM7MmqP6M8wPHvhAIfq19.H9sAoHBu4aNyhnN1
============================================================

## Zoom Recording Transcript

**Yevhenii Solomchenko** 02:16 Right.
**Chris Ventura** 02:18 Give me a moment. I can get set up to to run the meeting.
Okay, so pull requests.
So adding analog instrumentation.
Okay, so I believe this is a follow up from what was done for did we support Log 4 net previously?
So this is looks like the analog version.
I say, yeah, let's take a look at this.
I don't know if anybody's had a chance to look at it yet.
so we'll follow up offline.
Okay?
And we got the next.net monthly bump.
Let's see rapid. Mq. Bump, Github action bump.
Okay, let's talk about this one.
Zack. I'm assuming you're still waiting for some sort of repro.
**Zach Montoya** 05:00 Yeah. So on this one, I I can try and repro. I just haven't had time to do that. So I think I should reasonably able to do that.
So that's the next step. I just haven't had time to do that.
**Chris Ventura** 05:14 Okay?
And then file-based configuration.
Any updates on this one.
**Rasmus Kuusmann** 05:29 Yeah. So I added some comments there you can also review if anyone else likes to wait.
I think it's the last one. So this one is old.
Yeah, this one.
**Chris Ventura** 06:18 Anything you feel worth discussing in the group, or just offline.
**Rasmus Kuusmann** 06:24 Yeah, I think you can look offlines.
**Chris Ventura** 06:28 Chat.
And then I assume there's been no updates on this with pure out.
Yeah, added a comment.
But yeah, Peter won't be back for a while.
Okay, so discussions?
Oh, quite a few.
Oh, no, this is something else.
I thought. I clicked on, never mind new issues.
So open last week.
Okay, so we're still waiting for logs in order to figure out what's going on.
And I believe they're they were running into a permissions issue with writing logs because they were trying to get the logs written to the program files Directory.
So we'll keep this open because there's been some response.
Okay?
And then onto the bytecode instrumentation for SQL. Client.
Couple of us have put some comments out here.
It's worth having. Others take a look at it.
I would still prefer to minimize how much bytecode instrumentation we need to support.
especially when there's existing instrumentation out there.
So my preference would be to only support the the minimum amount here, but there may be some difficulties with that.
So read through it. If you have additional ideas, please share.
Okay?
And this is a discussion we brought up previously about testing package versions that have some known vulnerabilities in them.
So this came up specifically for some of the bytecode instrumentation that we support.
and wanting to have tests to ensure that we still work with those older versions.
So take a look, share your thoughts.
and I believe we're still waiting for this person to come back from their vacation.
Maybe we'll give it another week and then close it.
**Zach Montoya** 10:25 That one. Also, if you go back to the new issues, it seems actually pretty similar. To the latest one as well. So maybe making progress on either of those 2 will help get to a resolution.
**Chris Ventura** 10:39 Okay.
no new discussions.
nothing needing to be added to the project board and don't.
Well, actually, there's the analog story.
Do we have that in here. No.
yeah. I don't think there's any updates for any of these stories.
anyways, any other topics that we want to bring up.
**Rasmus Kuusmann** 11:48 I have a quick question about the Http request names in So the same Comp. Page defines that the name should be the method plus is that we wrote, but that gives us like to different display names.
It does it?
Is it like correct or something wrong with the simcom?
**Chris Ventura** 12:26 Okay, is this in the trace semantic conventions.
**Rasmus Kuusmann** 12:30 Let's make.
**Chris Ventura** 12:32 Or do you want to share.
**Rasmus Kuusmann** 12:38 I can give you the link.
**Chris Ventura** 12:42 Okay.
**Rasmus Kuusmann** 12:45 So let's this one.
**Chris Ventura** 13:03 Okay, so spend name, specifically.
**Rasmus Kuusmann** 13:22 You know specifically, if you look at the target, it should be one of the following Http road for Http. Server. So the road is like 99% of the cases like controller action.
**Chris Ventura** 13:37 An index.
**Rasmus Kuusmann** 13:40 And previously, I think, we used to replace a controller and action with actual values.
And now it seems like this is like the pure template. There, in the activity, name.
**Chris Ventura** 13:56 Now, is this just for the Instrumentation library? Or is it for the built in instrumentation in dot net 10 or 9.
**Rasmus Kuusmann** 14:13 I think it's in.
**Chris Ventura** 14:17 In the contribut.
**Rasmus Kuusmann** 14:18 Instrumentation. Yeah. Instrumentation library for spnet and the spnet core.
**Chris Ventura** 14:25 Okay?
yeah. 99% of routes in aspnet and aspnet core. These days are controller slash action. So it doesn't provide a lot of value.
**Rasmus Kuusmann** 14:42 Exactly so, and if you look at another link.
let me send this one also.
I think this one should be the raw specification page where the main page should take information.
And here you can see, the table makes much more sense. Now.
this is definitely not like
**Chris Ventura** 15:14 Right.
**Rasmus Kuusmann** 15:15 Wrote, here is so.
**Chris Ventura** 15:19 Yeah, this was the intention.
**Rasmus Kuusmann** 15:22 Yeah, which means like, for me, it seems controller should be replaced, and maybe even action.
**Chris Ventura** 15:30 Perhaps open an issue for that instrumentation to to start a discussion.
**Rasmus Kuusmann** 15:39 Yeah, I was just double checking. If you think it's like correct here, or is correct in the same con page.
**Chris Ventura** 15:51 I think what most people want to see is this type of name.
**Rasmus Kuusmann** 15:59 Yeah, that makes much more sense. Here.
**Chris Ventura** 16:02 I don't think people want to see this.
I think people would tolerate this.
But I I do think that this is what people would expect want to see with a route based name as opposed to the the literal route. Definition.
**Rasmus Kuusmann** 16:27 Yeah.
**Zach Montoya** 16:29 Is this one right here? The one they highlighted? Is this the same as like, if you go back to the semantic conventions page? For is this not the URL template.
**Rasmus Kuusmann** 16:38 No, this is, if you look@thehttp.route definition, then it's like pure template there.
And that's what we get at the moment.
**Zach Montoya** 16:51 Gotcha. Okay?
Yeah. I mean, I.
**Rasmus Kuusmann** 16:55 Yeah, you can see that.
That's the template usually comes.
**Chris Ventura** 17:01 Gotcha.
**Zach Montoya** 17:02 Okay, yeah.
yeah. I mean, I think most people like you're saying would prefer to have the like controller resolved. And then a template for the Id, or something like that.
Yeah, that's what I've seen.
**Chris Ventura** 17:19 Now.
with that being said, I guess an argument could be name could be made that if that is the parent span for the for the Controller span.
Then maybe that's okay.
If there was a span created specifically for the Controller that gives the the more specific name.
But I yeah.
**Zach Montoya** 17:55 Yeah, I mean, I guess if you have.
I think, the auto instrumentation or or sorry the contrib for asp, net, core and asp.net. They probably have attributes where, like Controller is equal to this action is equal to this. So at least you can filter down from like the super low cardinality to a good query, but still.
**Chris Ventura** 18:17 Yeah, if they do have those attributes, then it's probably fine.
But I suspect that there's a bunch of tracing uis out there that it.
It'll make it cumbersome for people to find what they want.
**Rasmus Kuusmann** 18:39 Yeah, so exactly, we have our client brought up this issue. So.
and I used to remember that we replaced Controller in action. But no.
and didn't notice that it was changed before releasing this table version of spinet instrumentation.
**Zach Montoya** 19:00 Yeah, that might have happened last November, or whatever. When the Htp. Was stabilized.
**Chris Ventura** 19:09 That would make sense.
So hopefully, that means there's attributes for that data.
**Rasmus Kuusmann** 19:17 Just URL dot path. I think no controller, no action.
Okay, this is.
**Zach Montoya** 19:26 That's a problem.
**Rasmus Kuusmann** 19:27 Yeah, that that's dot net, dotnet specific. No.
and the SIM con is pretty much like, why, there.
**Chris Ventura** 19:36 Yeah.
Yeah. And depending on where that spends created.
the resolution hasn't happened yet. So it'll make it hard to enrich.
**Rasmus Kuusmann** 19:57 I think the sad part is, even if you use, enrich to overwrite the display name, then it's still overriding in the instrumentation site.
**Chris Ventura** 20:10 I was thinking more about adding additional attributes.
**Rasmus Kuusmann** 20:13 Oh, okay.
I was suggesting the customer to overwrite the display name, but seems like this is also open bug.
**Chris Ventura** 20:28 Yeah, I I'd say, bring it up as a discussion.
**Rasmus Kuusmann** 20:35 Okay.
**Chris Ventura** 20:41 I don't know if there'll be a lot of traction, especially with that instrumentation being moved natively in aspnet core.
But it's still worth trying.
**Rasmus Kuusmann** 20:57 Yep.
**Chris Ventura** 21:04 Anything else.
Okay?
Well, that's all I've got.
So yeah.
**Zach Montoya** 21:18 Thanks. Everyone.
