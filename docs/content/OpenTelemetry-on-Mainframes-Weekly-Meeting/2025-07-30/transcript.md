SIG: OpenTelemetry on Mainframes Weekly Meeting
Date: 2025-07-30
Duration: 26 minutes
Zoom Recording URL: https://zoom.us/rec/share/0p8Un0nQSHgcA0-F_0PryMWEW3wbW17nJbNOQFZjuloKHN6hPSTUSiVnRn95ECvb.-XqsteyCkJPrQKOw
============================================================

## Zoom Recording Transcript

**Ruediger Schulze (IBM)** 01:46 Hey, Craig! Hey, Jim!
**Jim Porell** 01:49 Hey! Roger! Hey! Greg!
**Ruediger Schulze (IBM)** 01:52 So.
**Greg Shriver** 01:53 Hello! Hello!
**Ruediger Schulze (IBM)** 01:57 Hi, there. So hold on back here.
Think we have a couple of things to just follow up on.
We started to put some agenda items on the.
**Jim Porell** 02:15 I noticed you were already editing.
**Ruediger Schulze (IBM)** 02:18 So alright, let me just bring up the screen.
Okay?
So the yeah, let's just add, also, if there's a this attendees.
Okay, on the survey and Actually, I wasn't sure. We we had, I believe, looked at these recites some time back, but it's actually good that you went over them again, and probably had similar observations than than we had. In fact, we, when when Aaron was, was still, you know, part of this effort here. We also had a presentation at the virtual Gse Uk.
and this is where these charts have been actually being created. So it was an effort that we had a, you know, a couple of weeks ago to put these materials together, and essentially also what we mentioned here as key insights that that was something that we, you know, in the preparation of this presentation, had been formulated.
If you had, you know, any observation in the discussion last week. And you would like to add this here, let's do that. If if there's any conclusions that you know beyond what is already captured, or we can also capture things under under the questions. If this is specific.
There were a couple of interesting observations. Why, we had kind of like randomly on the, you know.
This was put out on the on the block of the mainframe project. This was on the block of the open telemetry project. In the end we had quite some participation from experienced mainframe persons, anyway.
And also, as you may have noticed specifically, I think I mentioned it somewhere. These persons also have been asking them for performance system metrics in a telemetry format. That was one of the indications from the data.
Another interesting indication was also that you know, there's obviously, I think it's down further down here. There's a consideration about having batch information exposed. We we are open telemetry format. It was kind of like interesting observation as well. I think this came like twice from the data.
So just giving some examples here. So I think there's still space to to add some additional information to these, so feel free to to add that in I would like to still like, go for vacation out at the end of next week, but I still would like to hand this over to to the Omp project and the open telemetry project by the end of the week.
**Greg Shriver** 06:04 End of this week or end of next week.
**Ruediger Schulze (IBM)** 06:06 And the end of end of next week.
**Greg Shriver** 06:08 End of next week. Okay.
**Ruediger Schulze (IBM)** 06:10 Yeah, yeah.
**Jim Porell** 06:12 Greg. Greg and I had an observation. We both nailed open telemetry has the opportunity to save the mainframe from executives that manage by magazine, and are invisible to mainframes.
In the sense that now you start looking at things end to end by any tool like today, you're really limited in the in the range of tools you can use.
the the interesting thing will be, you know. How do they account for this? But They'll see that the mainframe is relevant and important to much of their business.
which could be a really good thing. It's it can't be ignored because it's hidden behind some black box.
**Ruediger Schulze (IBM)** 07:08 Right, right.
**Jim Porell** 07:09 It could be. The depth of the mainframe, too.
**Ruediger Schulze (IBM)** 07:12 People start looking.
**Jim Porell** 07:13 The cost.
No.
but but the reality is, there's a lot of good stuff here. What the the interesting aspect! And I'm thinking about it from the cost is a lot of the resilience and security is built in.
Where, when you're doing traces on a distributed application, you're getting one flow, you're not seeing the necessary redundancy. You're not seeing necessarily the servers associated with security. You're not seeing the floor space cost, you know, and the and the environmental cost that.
you know, are are pretty easy to account for on Mainframe. So it's not a perfect world, but it it should open. I would think it would help open up people's eyes.
**Ruediger Schulze (IBM)** 08:00 Right and as you just mentioned, carbon. And as I also see this here, this was interesting, I would have to go back to the data. But if we.
while processing the data, you know, we always had the questions formulated in a way, and what else? Right? And carbon. There was one company who was actually or looks like, you know, it was just a single person. But that was actually very much focused on the carbon. And that's why you see this somewhere here. I don't have it on the screen right now. But here, right this is was one of those examples then.
And I think this is not to be underestimated. So this this visibility aspect to to bring this in to.
**Jim Porell** 08:51 Yeah, once we figured it out and it was, I'll give Greg full credit. He figured it out. So I'm like what I'm thinking. It's like angular or some type of ui thing. I'm like, what And when you start thinking about carbon credits that gets into the cost accounting side. So, that is kind of interesting.
**Ruediger Schulze (IBM)** 09:08 Yeah, yeah, right?
Yeah. So so feel free to to still add on and probably in the in the middle of the next week I I will write to me, and then also put this on top to to get it. Get it out there.
I think the observation.
**Jim Porell** 09:27 I just made. You know we made last week is probably more relevant to the Ompe folks, but might be helpful on the open telemetry side, too.
**Ruediger Schulze (IBM)** 09:36 Right. And in fact, the open telemetry public relationship. They they, you know, they have been asking on this, on this, on the channel about this. So we want to get this. So we also be recites being published there right?
Then the other topic that we had is, you know this metric, semantic conventions table here, and maybe let me let me just walk through this a little bit. And then I think you had also suggested we can take actually what we produced at the beginning as a starting point to take it over. But essentially the idea is that if you look at these variety of metrics that we have on the platform.
We need to come to A to a way of modeling them. And also we need to account for that, you know, we are now moving to to entities from a specification point of view which in the end will help us. In fact, because then, you know, we we get the the possibility to also associate these metrics with a proper entity on these entities. We will have, it's not as clearly called out here, but we also will have a discussion around what are the identifying attributes versus what are just descriptive attributes? Possibly this will also help us, then, to to clear some of our questions that we discussed earlier on A, on A, on the ontology discussion.
And the idea is that you know, we we may start with Hmc. Metrics, because, you know, from the lowest layer. Obviously this will help us to already come up with a naming scheme for some of this, and just again taking it as different CPU types as an example.
Back. Then we, I think, introduced, and might might actually be in here right? We back at that time we introduced kind of like we were thinking to introduce attributes like CPU type, and and also CPU mode. And the way is, how does the spreadsheet is being linked? It's kind of like cross linked with validation. So if you don't have your attribute here on the on the registry being defined like like these that I just mentioned. And then, you know, you can examples, or actually, probably we wanna specify a full list of what can be given here.
But then, we can also. We have already 1st validation. Do we have all these attributes probably added, and that helps. Then, when we need to put the Pr in place.
Right and you know. As I said, it's probably a good place to start with. The Hmc. Metric groups could be an example to go.
But also, as we know, there's there's more, you know, on the Hmc. Api, there's more. It's kind of like more configuration information, but also may serve as as metrics. Think about weights, for instance.
L. Par weights. So and yeah, taking what we, what we started with is probably a good good good place to to get into this.
**Jim Porell** 13:18 Yeah, what I was wrestling with.
Hmc. Metrics. That tab makes sense. That's hardware related as I started looking at the other tabs with attribute. I mean, it sounds like we need to add more tabs and then attribute and entity and relationships and metadata are basically kind of summary from those individual tabs. I mean, they're like you, said Cross Link. Is that a.
**Ruediger Schulze (IBM)** 13:47 Yeah, yeah, this is. Hmc, is just an example here. So.
**Jim Porell** 13:51 We could have the same for Cvm. Metrics, for instance.
**Ruediger Schulze (IBM)** 13:55 You may have that for maybe we had this discussion. Is this Cos, or is this workload manager? We, you know this is then where? Where? Probably we, we also will figure out what you know. What's what's this? What what we really want to express or transport as a component or entity. Again, owning these metrics.
**Jim Porell** 14:21 I'm thinking out loud. Here, I I can see each operating system having a tab.
**Ruediger Schulze (IBM)** 14:27 Right.
**Jim Porell** 14:28 But then I can see as we get into the individual process, models.
kicks, Ims batch unix system services. dB, 2. Store procedures.
They might have their own tabs, or they get into. You know they're not quite the same.
Their process is not quite the same as a unix Linux windows process.
and maybe we have to call them out differently.
**Ruediger Schulze (IBM)** 15:01 Right.
**Jim Porell** 15:01 So I can kind of see.
And again, I'm I'm kind of thinking the way you did with the Hmc. Metrics, where you had as attributes on the far right, you know. System CPU. But then you brought it back over into the attribute to show it. You know, in that column I can see in Zos. When you start thinking about process, a process type will be kicks. Ims, dB, 2, you know. Then you bring it over here underneath that attribute, and maybe that's when you warrant its own page or its own its own tab.
I don't know. I'm just. I'm trying to think about how to do this logically.
**Greg Shriver** 15:42 So are we. Are we thinking that each tab could be its own sort of namespace? If you will.
**Jim Porell** 15:50 In some respects. Yeah, maybe.
**Ruediger Schulze (IBM)** 15:53 Or sub namespace. So if if it's I mean, you know, obviously, system is already predefined by the semantic conventions. And some of this. What we have on the Hmc. Is we probably want to map back to system.
But if we can't find an existing namespace, then probably we would go with this mainframe on.
**Anand Somasundaram** 16:21 Thinking out loud, This is more like a layer. Right? We start with the Hypervisor prism.
and then we go into the operating system.
and then we go into the Middlewares applications on top, but that will be more on the trace side. So the rest is all metrics right.
**Ruediger Schulze (IBM)** 16:42 Think so? Yes.
metrics and the there's maybe small portion related to logs.
But the the system more on the level of resource or entity definition.
**Greg Shriver** 17:02 Right I was. I was just gonna say, I think you just have to be careful.
Anything that that that exists in the resource cement, the resource subset of semantic conventions that would cut across all those you know, metrics, logs, and trace signals.
**Jim Porell** 17:25 Yeah, actually, I wasn't appreciating the namespace reference. But system is already like you said a defined namespace. So we're just adhering to that mainframe is a new namespace.
**Greg Shriver** 17:36 Yeah, and.
**Jim Porell** 17:36 Yeah. And because virtualization.
When Anand said what he did, you know, virtualization is probably a known namespace. But we have different entities within that.
**Ruediger Schulze (IBM)** 17:48 And it's I think it's not yet a namespace, as far as I'm also not aware of. Think activities in the spacer. But it's something as we discussed the ontology which we we probably want to bring in. Then, as we go up the stack.
**Greg Shriver** 18:10 Right. And and as we discussed before, you know, if it's something, if the like, going back to Jim's point with the process, models being different potentially between, you know, traditional mainframe and unix Linux windows.
If if there's a direct mapping between those 2, then fine, if we can fit into the existing semantic conventions, the way they're currently namespace. That's great. But if we're gonna have to sit the thing on its ear to say, well, but in a mainframe. You might have to go through this flow diagram to figure out what it is. I think we're better off just to to have a if we're going to add that add it in its own appropriately namespace thing that's specific to me, to the mainframe.
**Ruediger Schulze (IBM)** 18:57 Right. And this actually reflects one of the observations that that I also had recently. So, as we now get more and more into these discussions around. You know, how can we map Isle to generic concepts which are across different platforms, and also what is, you know, commonly defined on the semantic conventions versus mainframe specifics.
We we start really to step into these different namings, or different also concepts that we have on the mainframe and we had discussed. We had an internal discussion, for instance, about something that is on the mainframe called a connection, but effectively, it's not a connection in the network term.
But a mainframe. Sme will will understand this as a type of connection.
So I think we will also step into interesting discussions around this terminology. As we move forward. And I think I said this earlier, we had some. So other discussions around how to deal within terminology. But I think this effort can actually help us also to identify these clashes.
And it's not just the sysplex sysplex versus cluster example that we that we already referred to once right?
**Greg Shriver** 20:27 Right.
**Ruediger Schulze (IBM)** 20:28 Yeah, so
**Jim Porell** 20:33 Yes, I'm I'm looking at the opentelemetry dot I/O right now, and it looks like I don't know. Maybe I'm wrong. But you know, system, runtime environment. Rpc.
Object stores. Http, are these all namespaces? Maybe database cloud providers, azure.
**Morgan McLean** 20:54 Effectively, yeah, yeah.
**Jim Porell** 20:57 Okay. Alright, that's cool.
Alright, that's good to know.
**Greg Shriver** 21:06 And Rudigo. Where? Forgive me. But where? Where is do we? Is there a link to this particular is, I assume this is a Google Sheet.
**Ruediger Schulze (IBM)** 21:15 Yeah, it's here. It's it's okay. It's in the in the.
**Greg Shriver** 21:19 I got it! Got it! Got it? Got it?
Thank you.
**Ruediger Schulze (IBM)** 21:23 It's yeah, right?
Okay, yeah. So maybe you know, if you could, maybe, you know, take a look at this and maybe we can start to to populate that And and then, you know, try to bring some some basic.
you know data into this. And then we can also start to to look at.
You know how to use this, then to formulate prs based on that as we enter the holiday season, it's probably fair to say that there will be not so much happening on in August. But, I see this as one of the activities to focus on for September, October timeframe to kind of like. Get to it.
1st of all, you know, on this, secure to get to a common view of how to name some of these.
you know, metrics, most common metrics which we obviously have on the platform starting from the Hmc. But then going up to the other layers, as we said.
and then I think we can work on the on the pull request as well.
I'm trying to actually bring somebody in to help with the pull requests. Still need to have a couple of, you know internal discussions on that, but that may then also help on the execution side. On this right?
Then at last, at least, from from what I added to the agenda, just very briefly. So the the Community day at Tech Exchange, Omp.
I think I got 30 seconds of I think we had done that. We had listed what we submitted.
but in the end I was asked just to merge the the architecture session and the Sig update into one session for 30 min.
And essentially, what I would do is, you know, talk about this on a.
on a, on a, you know, for the for the architectural session. Obviously there was also this this idea of of doing more in the education space about how mainframe architecture works from typical perspective of how transactions are being processed, what kind of components you have, protocols, communications in between and then leading this over into, you know the current work that we are that we are doing here, and then probably this sort of minutes will be past. But that's the plan for the year for the Omp session.
And I think, Richard said. I think he's not on today right that he would be as well there. We'll definitely contact Richard.
So maybe we do this as a as a joint presentation of the sick. I will reconfirm that was with red shelter.
Good!
Any other topics.
**Greg Shriver** 25:01 I don't have anything else for today.
**Jim Porell** 25:03 Not be there.
**Ruediger Schulze (IBM)** 25:06 Right.
I will be still available next week. Then I'm off for 3 weeks, and then back in September.
**Jim Porell** 25:17 Yeah, I'm I'm off the night the near 1st week, 9th to the 16.th So.
**Greg Shriver** 25:25 I'm off from now till January.
**Jim Porell** 25:29 What's your name?
**Morgan McLean** 25:33 One? Do this.
**Greg Shriver** 25:37 I wish that were true. Actually be careful what you wish for actually.
**Morgan McLean** 25:41 Yeah, actually, yeah, yeah, fair enough can happen very quickly.
**Jim Porell** 25:46 Hello, Greg! You have a.
**Ruediger Schulze (IBM)** 25:48 Yeah.
Okay, then. Yeah. See you. Next week, right? We'll see you whenever.
**Morgan McLean** 26:01 See folks.
**Greg Shriver** 26:03 Bye-bye.
