SIG: Semantic Convention SIG
Date: 2026-05-04
Duration: 79 minutes
============================================================

## Zoom Recording Transcript

Liudmila Molkova 00:03:53 Hello, me, Kellyanne too butts.
Michele Mancioppi 00:03:59 It is a lonely thing, and I am not about.
Liudmila Molkova 00:04:03 Sorry, I can't hear you, give me a sec.
Hey, can you hear me now?
Michele Mancioppi 00:04:27 Yes, I could hear it all along.
Liudmila Molkova 00:04:30 Awesome, yeah, couldn't.
Michele Mancioppi 00:04:31 I was saying it's just me and other bots.
Liudmila Molkova 00:04:36 No, no, no, you lent two butts.
Michele Mancioppi 00:04:41 How you doing?
Liudmila Molkova 00:04:42 I'm good, how are you?
Oh, did he… Kick them out.
Michele Mancioppi 00:04:51 I don't know, why do we allow them in the first place?
Liudmila Molkova 00:04:56 This is a public call. We allow everybody in.
Michele Mancioppi 00:04:59 Hello, everybody.
Liudmila Molkova 00:05:16 Oh, I'll trust.
Trask Stalnaker 00:05:20 books.
Liudmila Molkova 00:05:28 Okay, I don't know whose turn is it to run the call, but… I can…
Trask Stalnaker 00:05:39 Probably not your turn.
Liudmila Molkova 00:05:41 Do you want to take over?
Trask Stalnaker 00:05:45 Sure, unless Armin wants to.
Armin (Dynatrace) 00:05:49 I'm trying to figure out what to do with this firefly thing.
Liudmila Molkova 00:05:54 Tell them…
Trask Stalnaker 00:05:55 Ignore it.
Liudmila Molkova 00:06:00 Oh, you gave up, Trask.
Trask Stalnaker 00:06:03 I… I did.
Armin (Dynatrace) 00:06:11 Are we familiar with the second one as well?
There's two of them.
Trask Stalnaker 00:06:21 Some of them… Have, like, polite, like, you can comment.
To it, to leave, but some of them you can't.
Armin (Dynatrace) 00:06:36 Alright, let me take care of the other one in the meantime.
Trask Stalnaker 00:06:43 Oh, you, you can't drive the meeting.
Armin (Dynatrace) 00:06:46 I can as well. Would you then to the… the host? I'm already there.
Trask Stalnaker 00:06:53 Do we… do we… do we really care?
I've given up on… Doing the whole host thing.
Armin (Dynatrace) 00:06:59 Maybe it's a one-time thing.
Let's see…
Trask Stalnaker 00:07:03 No, they just keep coming back. I've… I've done it… I've wasted enough meeting time looking up the host code and going in and kicking them out.
Armin (Dynatrace) 00:07:14 I'd even left voluntarily. Nice.
Right…
Christophe Kamphaus 00:07:25 Is there no Zoom feature to ban a certain user?
Trask Stalnaker 00:07:30 I've reported them so many times to Zoom, and they always give me the same answer, which is that it's a public meeting. If you don't like it, make it a private meeting.
Armin (Dynatrace) 00:07:56 I think it worked, because it even left after I declined the permissions.
And I also said that it should remember it for our future meetings, so maybe that… That helps.
Liudmila Molkova 00:08:22 It starts with the trash.
Armin (Dynatrace) 00:08:29 Should I share the screen? I'm getting it ready now.
Liudmila Molkova 00:08:33 Yeah, if you run the meeting, you should probably share the screen.
Armin (Dynatrace) 00:08:37 Just a second… Right, there we go.
Is there any of these which you would like to discuss specifically?
Or should we just triage the ones?
Liudmila Molkova 00:09:20 So we usually… I think take a look at the blocked ones, there is no change since last time.
If I remember correctly, so probably nothing to discuss. Maybe we can check if there is any new development at browser resource timing event?
Because I think it was on hold, it wasn't, like, blocked by the reviewer.
It was mostly…
Armin (Dynatrace) 00:09:50 Can close this one, okay?
Should we go ahead, then?
Doing so?
Liudmila Molkova 00:10:00 I've already released an instrumentation with this convention, I'm… I mean, I don't mind closing it, but at the same time, I also would rather merge it if it's already implemented.
Armin (Dynatrace) 00:10:15 Leave a comment.
Oh, I saw you.
Christophe Kamphaus 00:10:18 as I understand it, they will use different ones.
Yeah, I think…
Daniel Dyla (Dynatrace) 00:10:23 the one that…
Christophe Kamphaus 00:10:24 up here.
Armin (Dynatrace) 00:10:25 Do you see…
Daniel Dyla (Dynatrace) 00:10:26 The released one is temporary.
Armin (Dynatrace) 00:10:29 Okay.
Liudmila Molkova 00:10:30 Okay.
Armin (Dynatrace) 00:10:32 So these are not as in the proposed ones here, but a different set?
Daniel Dyla (Dynatrace) 00:10:41 I don't know what instrumentation he's talking about. The… Fetch and XHR instrumentations use… the regular HTTP convention right now.
I don't know if there's a separate browser… Instrumentation at this point or not.
Liudmila Molkova 00:11:02 This is browser resource timing, so it should be…
Daniel Dyla (Dynatrace) 00:11:06 Yeah, but I don't know if it's been added to the existing… fetch XHR, or if there's a new instrumentation.
Liudmila Molkova 00:11:16 Okay.
I'm going to leave a comment saying that if this is capturing something actual, and there is no plan to introduce something new in the next few months.
I think it would rather make sense to be documented.
Done.
But that's up to the browser to decide.
Let's move.
Armin (Dynatrace) 00:11:52 Not good.
And for the other one, no update there, so that one will be out to closed, I think.
And… Swan.
Anything you'd like to cover there? We don't have any agenda items today, so we can also spend a bit more time on triaging the issues and PRs if you want.
Alright, I bet.
Trask Stalnaker 00:12:28 drink.
Armin (Dynatrace) 00:12:28 yours.
Trask Stalnaker 00:12:29 I have a couple agenda items above, under next.
Armin (Dynatrace) 00:12:34 Alright.
Din… Let's put them down here, I didn't see that.
Right, do we have Scott with us? Yeah, we do.
Scott Gerring 00:12:51 Hello. All right.
Armin (Dynatrace) 00:12:52 Then I'll pass it on to you.
Scott Gerring 00:12:54 Sorry, I probably put it in the wrong place in the meeting notes. I've not joined this sick before.
Armin (Dynatrace) 00:13:00 Oh, it's fine, no worries.
Scott Gerring 00:13:02 So we were chasing some high-level guidance here for something we're working on primarily in the profiling SIG.
For a quick high-level overview, there's these two OTEPs here.
that let us, from the profiler side, read out information about the SDKs in eBPF, essentially. So the first one gives you context about the process, like the resources. The second gives you context about the running request.
To connect the two together, we need an identifier that we can use with the process context as an extra attribute that we can share some configuration information behind.
We think that this is something that probably matters to the semantic conventions, but we're not really sure.
And I guess the question is, what's the easiest way to go about figuring out what we should call this? Should I cut an issue or a PR? Should we discuss it now? How would these things normally work?
And let me know if I can give more context. It's quite a rabbit hole, so I don't want to waste everyone's time.
Michele Mancioppi 00:14:11 Could you maybe give us… A quick overview of what kind of semantic conventions you would need that are not in the process or host namespace already.
Scott Gerring 00:14:21 So, in the process context, you, as a SDK, expose your resource to the profilers, you know, you have your environment and all those sort of things, but to configure the thread context.
We need to provide a bit of extra information that basically does some key mapping and whatnot, so that when the profiler comes in and sees that there's thread context being exposed, it knows how to interpret that.
So what we would put in the process context, it's not really a resource in the open telemetry sense. We'd probably hang it in the extra attributes section that the process context facilitates, and its configuration for this other mechanism that builds on top of it.
So it's a bit of a funny one in terms of what would normally be modeled in the conventions, I suppose.
Michele Mancioppi 00:15:08 But, why do you need… Semantic conventions to apply to effectively inter-process communication with these attributes.
But it's conventions is what the profiler will end up emitting.
Scott Gerring 00:15:21 So there's communication between the SDKs themselves and the profiler. If it is the case that this doesn't need a semantic convention, that's also fine.
Michele Mancioppi 00:15:32 I don't think it does.
Trask Stalnaker 00:15:36 Initially, it sounds more like a spec.
thing, just check out that inter-process communication. The semantic convention.
Michele Mancioppi 00:15:46 fortunes.
Trask Stalnaker 00:15:47 are… More about things that… telemetry that gets emitted And consumed by users.
Scott Gerring 00:15:57 Cool. I'm happy with that as well. We were pointed over this way by some feedback on the second OTEP behind some discussion here link.
So there might be a bit more nuance to it, but again, like, we're perfectly happy to not put it in the semantic embraces if it doesn't make any sense.
Trask Stalnaker 00:16:14 Could… could you pull up the comment so we can see?
Maybe that would help.
Christophe Kamphaus 00:16:22 Yeah, the question was whether it was already discussed.
With, semantic conventions.
And it might make sense, I guess, if we want to document it, so it could be easily found.
If you search through someconf, But if you start from the spec side, and it's already documented there, That would be fine as well.
Armin (Dynatrace) 00:16:52 Yeah, I think if it's in the spec, that should be sufficient, because if it's in Senkov, it could give the wrong impression, as if that is something that a consumer would end up seeing.
And something that would be interested there, rather than some intermediary one.
Michele Mancioppi 00:17:07 Okay. So it doesn't matter if it's downstream, then it should be in semantic conventions, ideally. In interprocess communication.
No.
Scott Gerring 00:17:17 Cool. And it absolutely doesn't escape between the conversation between the SDKs and the profiler here, so I… I think we're all agreed that it doesn't need to go in semantic conventions, which is probably great for everyone.
Armin (Dynatrace) 00:17:30 Yeah, if you need some, like.
something to compare it to in your discussion. You could bring up the collector, which has this internal P data format, that Is what the collector uses internally, and that's also something that's not… documented in SEMConf, and not even in the spec, because it's just… Internal and stays as such.
Scott Gerring 00:17:54 Cool, that's a great tip, thank you.
Michele Mancioppi 00:17:56 I'm, I'm commenting on the thread.
Trask Stalnaker 00:18:00 Thanks.
Christophe Kamphaus 00:18:01 questions. Should, then, this namespace be reserved for this usage? Just like the OTA namespace is reserved?
Trask Stalnaker 00:18:11 namespace.
Sorry, go ahead.
Liudmila Molkova 00:18:16 These are not… attributes, in a sense, of semantic conventions, right? This is something that's put in the threadlock or some context. It's not going onto the telemetry, is it?
Scott Gerring 00:18:29 It's… it's both, to be confusing a little bit. So, on the process context, the context exposed is modeled as a set of resources and a set of attributes using the OTEL Protobuf types for that.
So it's… we model it in those terms.
But it's not escaping this conversation between the two components.
So I suppose… if there was some future semantic invention thing that wanted to use thread local dot, or TLS thing. or whatnot.
There would be the convention, the potential for conflict at that point, with us in our internal interface.
Trask Stalnaker 00:19:12 Sure.
Liudmila Molkova 00:19:13 which is.
Trask Stalnaker 00:19:13 You're actually putting it directly on the… it is a resource attribute in…
Scott Gerring 00:19:19 But there's, if you jump to the… this is… this is a bit of a rabbit hole, but if you open the link that went to the… OTEP for the process context.
Which is… it's actually linked… I've linked it further down there in my message in 4719 process context, a little bit up and to the left.
Armin (Dynatrace) 00:19:39 This one?
Scott Gerring 00:19:39 Yep, that one.
You can see how it's modeled here. If you jump down… yep, this should do it. So, yeah, exactly that. So we have both the resource and a set of attributes. The idea at the moment is that we would model it as an attribute there.
But… So this is… Sorry.
Michele Mancioppi 00:20:02 this is proto that is not part of OTLP.
Scott Gerring 00:20:07 No, it's using the same definition of resource from the OTLP spec, and it's just re-exposing the resource to the eBPF profiler, but it's not getting into OTLP, absolutely not.
Michele Mancioppi 00:20:18 Yeah, it has inter-process communication between different OpenTrendry components, but doesn't go downstream, so… I think what we said so far is correct.
Scott Gerring 00:20:26 Cool. Yeah, it's a piece.
Trask Stalnaker 00:20:28 that I'm missing is, I think was what Christoph was asking, is if The… if we had a… thread local namespace in semantic conventions in the future, would that cause a problem for you?
Scott Gerring 00:20:47 I suppose it could, but it also feels very theoretical to me, in the sense that Based on what we're talking about now, it seems very unlikely that things expressed in that terms would end up in the semantic conventions?
Michele Mancioppi 00:21:00 How about the answer.
Trask Stalnaker 00:21:01 relying… Sorry, Michelle.
Scott Gerring 00:21:04 Yep, we would be relying on the uniqueness of that name.
Michele Mancioppi 00:21:07 there would be entirely different bags of data. I mean, the profiler would not go and look for the thread local information in the resources. It looks in the thread local context.
Scott Gerring 00:21:18 No, it looks in the process context. It would look in this attributes thing here.
But yeah, it would require many things to line up for it to be a problem that we use that name.
Trask Stalnaker 00:21:31 Do you need… I mean, can you, like… So if there was something with that name in the resource there.
That would cause a problem for you.
Scott Gerring 00:21:42 Yes, I was…
Trask Stalnaker 00:21:43 Users can put anything Into the resource.
Scott Gerring 00:21:47 Not on the resource, it would have to be in this extra attributes thing here. So the things that are in the user's resource are fine, we won't look there, we would look in that repeated attributes section.
Trask Stalnaker 00:21:56 Oh, okay.
Scott Gerring 00:21:57 It's worth mentioning that the implementation of this in the SDKs hasn't got very far yet, but it's hard to imagine that users would be putting things in there explicitly directly into the attributes. So again, I think that you could imagine some complicated situation where it became a problem, but it feels rather… abstract to me.
Trask Stalnaker 00:22:20 But in that case, it's not conflicting with semantic conventions, it's… conflicting with.
Something that you all are giving users access to do internally.
Scott Gerring 00:22:33 Yep, I think that's fair.
Trask Stalnaker 00:22:34 Okay, yeah, that was the part… that was the only part I wanted to clarify, was that if we added, or a user added resources with that specific name, if that would cause a conflict for you or not.
Michele Mancioppi 00:22:48 Let me share the screen so that before I press the send button.
We can all agree on the answer.
Armin (Dynatrace) 00:23:07 Sounds good to me.
Scott Gerring 00:23:09 Maybe it does not get emitted downstream by the profiler, I think?
But no, otherwise, I think that's perfect. Thanks all.
Michele Mancioppi 00:23:21 And one, and two, and done.
Trask Stalnaker 00:23:26 Chip it.
Michele Mancioppi 00:23:29 shipped it.
Armin (Dynatrace) 00:23:31 All right. Thanks, Michaela, then. Back to Trask.
Trask Stalnaker 00:23:38 Yeah, yeah, I can share.
Armin (Dynatrace) 00:23:43 You can, or I can?
Trask Stalnaker 00:23:44 I can share. Yeah.
So, as… let's see, oh, Armin, you have permission to approve this.
Admin…
Armin (Dynatrace) 00:24:09 In the admin report?
Trask Stalnaker 00:24:10 Quest? Yeah.
So that I can get that repo created and start populating it, so, I… did put up a draft of what this would look like, removing it, from the Semconv repo.
And basically… It just, find one that's easier to… look at… This is a nice short one. So it just, blanks out all the pages and adds… oh, here, we can look maybe this way… Hads, you know, moved.
header… Everything is… the YAML files are all moved to deprecated pieces, So, I… So, it'll be great to, you know, have a look there.
From… coordination perspective, this will need to happen after we, populate the… Repo, or at least have it, because it links to it.
Lyudmila, I saw that you have… A… Have cleaned up the… V2 schema…
Liudmila Molkova 00:25:53 Yeah.
So, let's, let's talk about it. I have the… There are some… some complicated… list of reasons and why I moved everything to V2, including templates.
But essentially, I have templates in this repo now.
Trask Stalnaker 00:26:20 I think.
Liudmila Molkova 00:26:21 Yeah, we can keep them here. I can send a PR to Weaver Packages.
But, there are a couple of relatively small bugs in Weaver that I'm also fixing that, result in some minor diff, not, not awful.
But, other than that, yeah, there is a… I flattened down the nested groups, and I created this skill to transform, but skill should probably go out from this repo to the semantic conventions.
Trask Stalnaker 00:27:02 Yeah.
Liudmila Molkova 00:27:02 Beaver packages.
We can go through it just for others to see V2 schema, or we can… Move 1 was the… Discussion.
Trask Stalnaker 00:27:17 Let's spend a few minutes.
Liudmila Molkova 00:27:21 Yeah, so maybe then I can share, you can go to some place, let me share.
Trask Stalnaker 00:27:29 Okay.
Liudmila Molkova 00:27:42 Hey, So, let's take a look at… oh, okay, so some interesting things to discuss. I think we should remove deprecated things from this new repo.
They will stay in the original one.
Trask Stalnaker 00:28:04 Good idea.
Liudmila Molkova 00:28:05 Yeah, so if I take a look at spans… So, important things.
from the most important to the least. We now have… span refinement. This is a new thing introduced in V2. So we have… genAI inference client, right, that describes any GenAI inference call. And then there is a refinement of it called up an EI inference client.
it can modify attributes in certain ways. I don't think it can change stability, but I'll need to check.
But, important part, it's… It says I am the same span.
And it's… you can think about it as a group extension from the previous world, but it inherits more than just a list of attributes. The group extension was just the attributes, even if you extended the span.
Same mechanism.
Trask Stalnaker 00:29:19 It's like, it preserves identity, or the span type.
Liudmila Molkova 00:29:24 Yes, future one. The same thing exists in metrics.
So, we have Gen AI operation.
Let's say GenAI token usage as a metric defined here.
There is an OpenAI version of it that introduces a couple of OpenAI-specific attributes.
So the… some, other things I've done here, Or… how we define… sorry, how we define These groups, and actually, the groups have slightly different usage comparing to V1. So, here I'm introducing this group, that describes GenAI-specific error type, and now I can… Include this group everywhere.
without an inheritance. I can include multiple groups. So, for example, if I'm… Looking at… OpenAI in France… Quiet?
oh, maybe I can flatten it more.
But the goal is to keep groups flat.
this one, for example, it includes the… Some common client attributes, it includes some usage attributes, it includes content as a group.
So now we can combine multiple groups together.
Instead of building very deep hierarchies of groups.
And this allows us to flatten them down.
I think we can polish this even more, too.
remove these groups and include them on spans. But anyway… So, these changes don't result in any markdown changes.
And yet, I do have some markdown changes in my PR.
Which are coming from… I have a new way to express snippet. The old snippet mechanism still works.
But the new snippet mechanism is actually… it's a JQ filter.
You can, polish it in many different ways.
So if I probably look… Here, there could be an example.
Cheer.
Yeah.
This is a trick, I don't know if we need it, but anyway, we don't usually include GenAI provider name.
And, system-specific spans, because there's just one system name, and we don't have good means yet in semantic conventions to express it, so here I'm just excluding this attribute using the filter.
Here, in this snippet.
I don't recommend writing the snippets by hand.
But just tell your AI that it's a JQ filter and what you want to achieve, and it will do it for you. But if you're a JQ specialist, I'm jealous, but… yeah.
This links… I've changed the template, because I changed the template, it's ever able to fix.
Yeah. This as well.
Trask Stalnaker 00:33:08 Cool.
Liudmila Molkova 00:33:10 Yeah.
And I think this is pretty much it. There are some changes like this, which are bug and Weaver. There's a dedicated place for this now, in the schema.
And V2 schema for spam name format.
But it's not propagated properly.
To the resolved version, and, it's just a link to the issue that tracks it.
Finally!
Trask Stalnaker 00:33:39 On… on that, I'm just trying to evaluate if that's fine for us for now, or if we need to block on that.
X.
Liudmila Molkova 00:33:52 You can always return this node back to the node, and… We can't… yeah.
We should probably block on it.
Trask Stalnaker 00:34:03 Okay.
Liudmila Molkova 00:34:04 And the workaround could be either we release an urgent version of Fever, which is possible. The other possibility is that I'll just return back this text, and I will remove the template that renders the structured Thank God.
Trask Stalnaker 00:34:22 Okay.
Okay.
Liudmila Molkova 00:34:24 That's another comment.
Trask Stalnaker 00:34:25 We have op- we have options, okay.
Liudmila Molkova 00:34:35 And there is one thing I wanted to… it's probably not a burning need, but I wanted to get your thoughts, since we're here.
So… it's usually difficult to look into YAML and say how exactly the final span or metric would look like.
V2 makes it easier because of flattening, but still… reading Markdown burns my eyes, so, what I've added here is A possibility to… generate… So, this is the generated YAML schema, was everything.
It's giant now, because I've just generated it for the first time, right? But normally, if you, let's say, change one attribute, you would see the…
Trask Stalnaker 00:35:29 Oh…
Liudmila Molkova 00:35:30 see if, like, what we see in Markdown today, when we.
Trask Stalnaker 00:35:32 Change something.
Liudmila Molkova 00:35:33 But this is in YAML, and it's a little bit easier on everybody's eyes.
Trask Stalnaker 00:35:38 That's… that's nice. Yeah.
Liudmila Molkova 00:35:42 Yeah, and we can play with it, we can drop it, it doesn't change anything that users see, so if we don't like how it works, that's fine.
Trask Stalnaker 00:35:50 Yeah, no, no, no, that does address, like, my primary problem with the hierarchy previously, was just understanding how it resolves, so… Feels like it's something worth trying out.
Liudmila Molkova 00:36:04 Yeah, and what I want to do with it, so sometimes when I use AI and they give it the markdown files, it's too much, it's hard to read, it needs to discover the relationship, now we can give it the, okay, here is the… the whole thing… well, you can use MCP Server from Weaver, or you can just find things using Grip and this file, and then discover the rest.
Trask Stalnaker 00:36:30 Cool.
Liudmila Molkova 00:36:34 So then, Trask, how do you want me to do this? This is a giant PR? I can't break it down, or…
Trask Stalnaker 00:36:42 No, don't.
Don't… I will, I'll look over, everything, And, yeah, it sounds like, yeah, I'll… Yeah, I… my preference would be less just as one big PR.
Liudmila Molkova 00:37:00 Okay, awesome.
Thanks.
Trask Stalnaker 00:37:06 And if it looks, I may go ahead and… Well, I'll chat. We'll chat this afternoon.
Helping you.
As far as merging it, because it… it would… I may merge it, even with a couple of to-dos in it, in there.
Because I'm also, I'm replaying the semantic convention repo history, filtering that out, so I'm gonna change… I'm gonna re… basically force push to main on my repo to bring over that history, and then have a couple of layered things on top, so including… I want to include your PR on that.
Liudmila Molkova 00:37:53 Nice.
So… And we have a plan for this one. Do you want to take over?
Aye.
Trask Stalnaker 00:38:06 I think that's everything, let's see… Yeah, Armin, if you can… Look at this one.
Since you have… permissions… To approve, and that will… Let me go ahead and start staging things in OpenTelemetry.
Armin (Dynatrace) 00:38:31 Sure.
Trask Stalnaker 00:38:34 Whoa.
Liudmila Molkova 00:38:41 Jaw!
You're next! I haven't seen you in this call.
For a long time, welcome back!
Joao G. (Dynatrace) 00:38:50 Welcome back. Hope you can hear me. Microphone likes to play. Okay, looks like it works.
Liudmila Molkova 00:38:56 Do you want to present?
Joao G. (Dynatrace) 00:38:59 No, I don't think there's… there's much to… I don't think there's much to present, let me… pull off my camera. Yeah, so I… I came back, and yeah, this was something that I… I wanted to work for quite a while, and since I had a clean slate, I took it, so… And because there was some issues with the out-of-sync markdown on our side with out of sync metric names on the markdown, and then I also noted that this will still do manually.
So… I worked on adding this to Weaver, so now it's possible to define the, metric requirement level in the YAML.
also for V2, and then, yeah, so this is merged in Weaver, we need, a release, but I started working on, now, sameconf to be able to, modify all the AMO files to add this, and then… Hopefully fix or make the entire metrics markdown auto-generated, so we don't have this… Don't have to put these snippets anymore, so it will generate, because then we have all the information we need.
To generate an automatic, so that's… that's just an update. There were… the only thing that I'm slightly concerned, or will need people's eyes and attention, is that there's quite a few Metrics that don't have the, you know, the hard-coded manual, requirement level.
I'm doing my best to look at them, and then find online, or… there's a lot of them for, for example, AceNet Core.
and Castro and Signal are, so I'm looking over the documentation for those, and then, you know, try my best to see what they are. For example, for Aspenet ones, I believe all of them are recommended, because They're collected by default, so… You have to opt out, by, opt out from the meter, yeah.
Liudmila Molkova 00:41:02 I think pretty safe to assume that if there is no requirement level, it's recommended.
Joao G. (Dynatrace) 00:41:06 Yeah. Yeah, that's what I'm going, so I will… I collected the names for the ones that I don't have, they don't have, so I can, you know, put in the PR so people know which ones to look, but the rest is all, you know, one-to-one mapping from the… For the markdowns.
Thank you for it.
that we are this week, I think, and then we just need to wait for a release.
We were released through, so we can merge it.
That's it.
Liudmila Molkova 00:41:35 Nice. It sounds like we have a couple of reasons to release Weaver as soon as possible.
Joao G. (Dynatrace) 00:41:41 Yep.
Yes.
Liudmila Molkova 00:41:45 And for the things that are not in the… Yamongyad are also the histogram boundaries, right?
Joao G. (Dynatrace) 00:41:53 That's true, yes. Then I can also… I think the discussion…
Liudmila Molkova 00:41:57 What's that?
I think Josh didn't want them in the YAML, like, the strict YAML, but more, like, in annotations, because it's an advisory thing, it doesn't… really go over the wire, and there's nothing would need to happen in Weaver In order for it to be fully completable.
Joao G. (Dynatrace) 00:42:21 So it just is this metadata thing that we also have for… for… Is it spans? I forgot now. I saw them somewhere in the… In the YAML model, yeah. Okay. Yeah, and then there's also this discussion with Dashboll, with Ashpole, about the, you know, like, the mapping.
of the optional… Option T, but it doesn't seem that it moved anywhere, right?
Recently. Somewhere linked in some other, oh, yeah, that one, exactly.
Okay.
Yeah, I guess it is still… can be… can be done in parallel, or won't affect, Addition of this. If we change later, then we can change.
Yeah, that's it for what I wanted to know.
Bring up today.
Liudmila Molkova 00:43:41 Oh, thank you.
Finally, metrics in YAML.
Joao G. (Dynatrace) 00:43:45 Yes.
Well, it took a few years.
Liudmila Molkova 00:43:50 Sorry, I'm taking… I took over the screen sharing. Carmen, do you want to take it back?
Armin (Dynatrace) 00:43:56 Yeah, sure. I think the next one is yours anyway, and there's no… no visual from what I can tell.
Yordis Prieto 00:44:04 Right? Hello, Sorry, I need your help with a few things that I don't know how to think about it. May I share the screen?
Liudmila Molkova 00:44:16 Chris!
Armin (Dynatrace) 00:44:17 True.
Yordis Prieto 00:44:17 Okay.
Alright, so… the f… First thing that I would like to understand is the linguistic aspect.
A service is a component of an application, but then if I go to the application, then it says one or more services, or, like, okay, how can I define what a service is?
And the reason I care about this is because it's related to this here, as well, where, okay, I can see some logical namespacing for multiple services, but does that mean deployable things, components in my system, and so on?
And the reason I say that is because I… I have an existing monolithic deployment of Elixir, but inside, everything is extremely distributed, right? There are queues all over the place, and event stores in between, and stuff like that. So, like, I don't know how… I should think about it.
unlike… What goes where and why?
And related to that is because when I go to… oh no, I closed Datadog.
When it goes to Datadog… give me a second… Alright, hold on.
How can I stop sharing now? Share, share, share?
How do I stop sharing?
Oh, here. Sorry. So, when I go to Datadog, which I don't know if it's a Datadog issue, or, like, something that, like, supposed to be my taggings… I ended up with not an explosion of services, but, like, there is a lot of linkage of what things feels like a service.
So, when I go to my dependencies, right, they're… these are a… This is an even sourcing command boss, right? Which basically rehydrates the event store, apply it, and stuff like that, right?
So… But their one per command, which I think is somewhat, like, intentional in my end, because they could be just deployed independently as well.
But… okay, should there be a service under namespace, or a component in the service, and stuff like that. So, like, I'm trying to figure out what I should be doing around All that.
And one, maybe, mistake I made is that… the package that I… maintain. I tag it with like, message queue, right? All this information that Datadog allows to look at this beautiful GUI, or whatever, right? But, like, should I be doing that? Should this be a… And messaging, right, with all the stuff or not.
So…
Michele Mancioppi 00:47:01 Let me try to take this. There is a lot to unpack. First of all, you are right in that slightly linguistic confusion, where we tell you that, first, the application is made of… is part of a service, and on the other side, it looks like it's a group of services that ontologically doesn't match.
Now, the service itself is a logical component, and Different end users may have different trade-offs about what they want to call a service.
There is, If we talk about Datadog, there is the concept of resource, which is not unloaded resource, it's more like an API endpoint.
And it feels that your different commands may want to be different operations in Datadoc. So, sorry, different resources. In auto, we do not really have a concept of operation as such. However.
The term operation is creeping into semantic conventions at different points, so there is messaging.operation, database.operation, open tracing, and light step, which are progenitor of OpenTender, had the concept of operation in them.
Some tools out there use the concept of operation, overlaying it on top of OpenTelemetry, and ultimately, the span name Should be something very close to what logically, we would consider an operation. Now, this being said.
I understand that you're providing a library, right?
Yordis Prieto 00:48:38 Yeah, part of it is the library is, like, doesn't know about any application yet.
Just try to make a difference.
Michele Mancioppi 00:48:44 The government should not set the service.
The service is something that the application using the library should set.
Yordis Prieto 00:48:53 Yep.
Michele Mancioppi 00:48:54 So that is… the biggest, like, higher level thing, I would say, ideally, so depending how you implement the library, I'm assuming that you're using the OpenTelemetry API, To create spans.
Yordis Prieto 00:49:08 Yeah, yeah, I'm not setting the service, but I'm setting the, like, namespace, the messaging, right? So, should my command boss in memory, sometimes, because it's not always, be the messaging?
Michele Mancioppi 00:49:21 That, so, is it… okay, more, more to unpack. The messaging, the messaging semantic conventions are… to my understanding, and Ludmila Trask's administrative face tray, are mostly about external messaging queues. Think of your Kafkas, think of your active en queues.
It sounds like you're using it… using them as internal job queues inside your monorith as well.
Additional.
Yordis Prieto 00:49:53 Well, the tricky bit is, like, is… in Ireland, everything goes a little bit off the water, because, like, Architecturally speaking, right, the whole point is, is… transparent, location transparent, so all this in-between thing goes off the water. So, like, yes, it's in memory, but no, it's not even in the same node, could be some time, so, like, it's the tricky situation. And I don't have any strong opinion, but this is where, like.
why I started with, I have a monolithic deployment, but with a really fully distributed, like, components behind the scenes.
Michele Mancioppi 00:50:27 I did not realize they were on the Beam VM, then in that case, my objection about using the messaging namespace is moot, because in reality, you're not going to know really, if it's here, if it's there. So, let's say that my personal opinion is the messaging semantic conventions do apply in your case. I have no idea what you're going to set as messaging.system, because I don't think we have anything in the accepted values that would actually work, but also, I think it's an open enumeration, so… If you add something there, it's unlikely that anybody dies, or something explodes.
Yordis Prieto 00:51:04 Right.
Michele Mancioppi 00:51:04 Going back to the service.
Did I actually answer your question?
Yordis Prieto 00:51:10 Yeah, yeah, you're clarifying a lot. Like, the namespacing as well, for example, is like… okay, I have one service, it's a monolithic, but that means that the dimension is somewhat meaningless, so what's the point of the namespacing then, right? Because in my… like… monolithic deployment, but with, you know, the distributed architecture, what do I do?
Michele Mancioppi 00:51:35 So, again, this is my personal opinion, and other people may disagree, and then send me straight. Service is what you make of it. Effectively, these semantic conventions offer you a mechanism to have two logical levels of grouping your spans.
for lack of a better term, your telemetry. One is the logical component, and the other is the service.namespace. People that use my tool, I see them sometimes using the service namespace in the way that you propose.
So inside the monolith, to split the component, like, the single monolith in multiple smaller components.
More often than not.
It's used in a distributed system where every application may have the front-end component, and you won't disambiguate which one it is.
Again, using service.namespace and service name is something that the person who deploys the application, including your library, will elect how to set.
using, for example, the auto underscore service name environment variable, auto underscore associates environment variable, declarative configs, and there's probably 50 other ways, depending on the SDK. So, there is no hard and fast rule about what is a valid service and what is not.
In my experience, the right, compromise depends very much on the backend that you emit telemetry to. Some backends, they do not know anything and want to know nothing about surface namespace. Others treat it semantically, so your mileage may vary.
Yordis Prieto 00:53:13 Okay.
Michele Mancioppi 00:53:14 And I'm sorry I cannot give you an actual answer, it's one of those things that, you know, it depends.
Yordis Prieto 00:53:18 Yeah, yeah, no, I'm okay with it. Like, my… primarily, I want to gather, you know, opinions, and ideally, from the, like, semantic convention, kind of like… hopefully be a little bit more opinionated, I think, or, like, the very least give options to people like B and C, primarily because I trust you guys to be, like, more, like, expert than me, you know? So I'd rather just follow than, like, make a major mistake, and then I cannot backtrack out of it.
Michele Mancioppi 00:53:46 Seth, I, so, am I to understand that you, publish a library that has built native OpenTelemary instrumentations?
Yordis Prieto 00:53:57 Yeah, it's event sourcing, so basically all the… projections out of the event store, right? Is that consuming from the messaging? I guess my event store is a messaging at that point.
But then in… that's in the consumption of the messages, that's somewhat obvious to me, but in the command side is where the other side of it, right? Like, you dispatch the command, it may or may not be in the same node or whatever, right? Like, it doesn't really matter, and… That's the other side of it.
Michele Mancioppi 00:54:26 I have a little something I would like to try with you. So, when people say, this library, this framework, this piece of software supports OpenTelemetry, it's very much a spectrum.
So, it goes to something as easy as it shoots out OTLP, with some level of quality and consistency in terms of metadata and integration with each functionality, too, it's something that this highly enlightened group put wow at it. And there are 50 shades of gray.
Yordis Prieto 00:55:00 In this particular case, because I'm also maintaining the Elixir OpenTelemetry stuff, is 100% semantic convention, plus the stuff that I put here that are custom. So I'm trying to document all the custom stuff, so I eventually figured out how to bring it into a group like this. So…
Michele Mancioppi 00:55:17 Enterprise.
Yordis Prieto 00:55:18 Yeah, so across the Elixir, at least the stuff I'm maintaining is, like, semantic convention, or, like, a little emojo that you could go there and see exactly what I have custom, so I can bring it up, which I also have another PR audit, the… yeah.
So… Yeah, so, like, these are the custom ones, and… the rest is just, like, like I said, like, I really tried to… To be cementing convention.
Michele Mancioppi 00:55:46 I have something, it just came to me, since we're talking about you deploying on Elixir and the VIN VM.
Maybe it can help figuring out what is a service and what is not.
The fact that, there is an additional semantic con… this initial attribute in the service semantic conventions is service.instance.id.
Now, canonically, that should be the identifier of the VIN VM.
Or at least that is how I remember the specs calling it out.
Which implies that each instance of the BMVM should have the same service name, because otherwise we'll end up with different service names having the same service instance ID.
Which is invalid.
Yordis Prieto 00:56:33 Right. Which, related to that, is my every actuary service, or namespace, or component. It's like, in the Veeam, everything's just so, like…
Michele Mancioppi 00:56:41 I feel you may be going a little too granular by naming every actor a service, because in my experience, most actors in BVM, they're still packaged in an application, and then the first instinct would be to say, okay, the boundaries of that application is a service.
Yordis Prieto 00:56:58 Well.
Michele Mancioppi 00:56:59 Collectors do different operations.
Yordis Prieto 00:57:01 Yeah, but you could form clusters… you could join two clusters, and they're completely different actors in completely different clusters, and you don't even see that. So, it's like… kind of.
Michele Mancioppi 00:57:12 But you still deploy them as a deployment.
Yordis Prieto 00:57:15 No, no, no, no, completely independent deployments, you form the cluster, just let the Veeam to actually do the message passing. So you could have, to make a point, a front-end edge… deployment service that former cluster with the backend storage deployment service, and then let Erlan to actually do the message passing, so you're not doing your PC in between, you know, HTTP, none of the stuff, it's just Erlan, you know, pass the message, and then let the cluster to figure out where the things are. So, it's blurry, so it's not the exact same deployment.
Michele Mancioppi 00:57:47 Then in that case, you could still decide to go… to give a different service name to each actor, but then would need to effectively use the prefix of the service name and slap it into the instance ID, which then causes some very interesting questions about how does the Erlang SDK work in terms of resources, because you effectively… I don't know, do you use different placer providers, metric providers, logs providers for each agent?
Because the resources at the level of the tracer provider.
Yordis Prieto 00:58:16 Yeah, I haven't got to the point where I treat every actor that special, to be honest with you, because right now it's like, you know, it's too blurry, and like, at what point I don't gain any benefits, right now. So that's the honest answer, and that's why I've been trying to figure out, okay, what should I be doing here? Like, how should I think about it, right?
So, that's…
Michele Mancioppi 00:58:35 I see an interpretation where, saying every actor is a service.
to be valid in your scenario. I think you will find that exceedingly hard to do with the SDK, because ultimately, I mean, things are changing somewhat, also with the entities coming in, but still… Currently, you define, effectively, the resource up front, and it's immutable across the lifetime of the, of the, in your case, the BMVM, unless you unload and reload the SDK.
You go down the very complex and resource-intensive route of having a tracer provider, a metrics provider, and logs provider per agent, and then each one of them can have a factory, its resource. So… I don't know, honestly. I think it may be a bit too… a bit too yay to go one agent, one service.
Yeah, definitely.
Yordis Prieto 00:59:36 Yeah, which is why I started with, like, the cyclic between applications and services, like, okay, I just want to figure out how to get out of it, so, like, split things and say, okay, here's… here's a guideline for people that care. Like I said, right now, no big deal, I'm not… I'm not actually going that crazy, like, anywhere I don't find that much value right now. But, yeah.
Trask Stalnaker 00:59:55 I mean, I can agree.
I like what Michelle said earlier about, it sort of is what you make it. You have two levels.
of breakout, maybe, I mean, 3 with the instance ID, and so, like.
If you go too granular with your service, then you will… you only have, like, one level above. You're kind of, you know, you're… Only hurting yourself, but it's just… you have those three levels.
use them in the best way that makes sense. Yeah.
Yordis Prieto 01:00:33 Yeah, is the messaging to being in memory okay to use as a tagging for my command side of things?
Liudmila Molkova 01:00:42 At this point, you are building something relatively custom we didn't design for, so if it works for you, then yes, if it doesn't.
Then… sorry.
Yordis Prieto 01:00:53 Oh, yeah, then…
Trask Stalnaker 01:00:54 Messaging is really more around… message queues, and I don't know, like, we were not thinking actors, messaging between actors. That feels like somewhere in between RPC and messaging, but…
Yordis Prieto 01:01:11 Okay, yeah, yeah, no problem. I'm gonna… I have one more thing that… it is related to messaging that I couldn't figure out what to do about it.
I… needed help, like, I'm contributing to the Broadway… Package?
Right? And in the Broadway package, I came across the need to… So basically, Broadway, from the component perspective, I can have… The bashing and the single messages are at the same time in the situation, because it goes into a single message where you can actually, like, transform data or whatever, and then goes into the bashing in some cases.
When I go to the bashing.
I found a need to know how many successful and failure from that given batch.
I made up these two values, again, like, in a module or whatever. I don't know if there is an attribute for that, or… Or, like… No, okay.
Liudmila Molkova 01:02:11 Thursday's done.
Yordis Prieto 01:02:13 Should I open an issue related to this, or do you think it's, like, a strong reason for that not to be there?
Liudmila Molkova 01:02:22 It's not a strong reason to be… it's not immediately, because we… our messaging SIG is on pause, and there is no one to actually look in the PR if you send it, and it will probably be automatically closed, because this area is effectively on pause.
If there is some interest to resurrect it, I… Personally, don't think we will be able to resurrect until 2026, but maybe 2027.
If AI heat goes down a little bit.
But yeah, so for now… I mean, you're already contributing to the instrumentation, and if you think it's commonly applicable to other instrumentations.
Then maybe the message, it should be called differently, but if it's just for this instrumentation, just keep whatever you have today.
Okay, good.
Yordis Prieto 01:03:20 Yeah, and in this particular case, that package is basically the, like, one of the top ones from Elixir, so everybody's gonna be using it, and I… we definitely use this a lot in our observability, right, to know, hey, what's going on with the batching situation.
So…
Michele Mancioppi 01:03:37 I have a couple of questions on the matter, because batching is, bar none.
The most, misunderstood aspect of how to create instrumentations, like, from the semantic convention perspective. And, at least in my experience. And, the cardinal sin was, span links.
Being something that you could not add after the spam was created.
Yordis Prieto 01:04:05 Yep.
Michele Mancioppi 01:04:05 Now… I am thinking at your scenario, and… I am wondering why do you need to expose it as an attribute if you are collecting span links for it?
Yordis Prieto 01:04:26 no strong reason other than I think that's what is the correct thing to do, so I am actually collecting all the spang links, and… Basically, you know, the reason is because normally we just look at, like, from the, what is it?
Where's it?
split. We just get the split back of, like, here's the success for, here are the failures, and, like, how we documented for… That situation to know what's going on at the batching level.
But no strong reason whatsoever, just… what I thought it was proper.
Michele Mancioppi 01:04:58 Yeah. Do we actually have, so more than, thinking about… effectively, the way I understand this is that, you are, you want to document on the consumer span.
like, how many it has consumed, right? And we have something in semantic conventions called messaging.batch.message underscore count.
Yordis Prieto 01:05:21 Yeah, that's here. So that's the total, but then in the total, which ones are failed and which ones are succeeded. So that one, I already have it here.
Michele Mancioppi 01:05:28 Exactly, so that's a Fatherian extension.
Yeah. The, how do you represent?
on a message-by-message basis, whether it's consumption in the batch succeeded or not. What do you put in the span lick?
Yordis Prieto 01:05:44 Oh, and this panel link, I don't put anything in this panel link.
Because this…
Michele Mancioppi 01:05:49 do not have a status code. They're just a link to a different span, and they will link to the producers.
But those have their own status code.
Yordis Prieto 01:05:58 Right, right, yeah, I just link them, but I don't do anything with it. So I go through every single message, and then just collect them, and then make the link.
And that's all I do in the consumer side. Other than that, when this finishes, it just gives me the, like, list of successful and failure messages, and then that's what I use for the attributes.
Michele Mancioppi 01:06:18 Okay, sorry to jump in.
Trask Stalnaker 01:06:20 in here, but we're over time. We should probably, continue the discussion either async or next week.
Michele Mancioppi 01:06:28 Do you mind if we stay… I mean… Yeah, do you mind if we stay here, Jortis and I?
Yordis Prieto 01:06:34 Alrighty.
Armin (Dynatrace) 01:06:35 I can leave the call open for you. All right, then thanks, everyone.
Yordis Prieto 01:06:39 Thank you.
Trask Stalnaker 01:06:40 by…
Michele Mancioppi 01:06:41 Bye.
Yordis Prieto 01:06:42 Sorry about that.
Michele Mancioppi 01:06:43 No, it's a fascinating use case. So, from the top of my head, more than saying how many succeeded and how many did not, as a user, we prefer to know which one succeeded and which one not.
And in that case, I would expect some way of annotating it on the span link itself.
But I don't know anything in semantic conventions.
That, actually, food… I mean, you could put…
Yordis Prieto 01:07:12 link itself, not to the original Spanish?
Michele Mancioppi 01:07:15 Yeah, because think about it. So, as a… the…
Yordis Prieto 01:07:18 Wait, is that possible? I didn't even know you could actually annotate links.
Michele Mancioppi 01:07:21 Yeah, of course, they get attributes. You're also supposed to put the message, that message again in there.
Yordis Prieto 01:07:27 Okay, today I learned.
I didn't know that. Wait, wait, wait, what?
Michele Mancioppi 01:07:32 Good value.
Can we have an attribute.
Yordis Prieto 01:07:36 No, no, no, no, no, that solves the problem. I mean, I don't know if Datadog is gonna like that, but, like, that's a second problem. Okay.
Today I learned. I didn't know you could actually attribute this links. That totally makes sense. That's where I would put it then.
Michele Mancioppi 01:07:52 Yeah, and you're supposed to put the messaging ID in there. And I was wondering.
Yordis Prieto 01:07:56 So this is not something that is a.
Michele Mancioppi 01:07:58 semantic conventions, to my… to my knowledge, allow, but I, as a, like, if I put my… throwing away the semantic conventions I had to put on the… the instrumentation author, I would use the error namespace to put it on the semantic link. I said, this succeeded and this one didn't.
Yordis Prieto 01:08:17 The, the what namespace?
Michele Mancioppi 01:08:19 Error.
Yordis Prieto 01:08:20 The error. Yeah, yeah, yeah, yeah.
Oh, okay.
Well, dude, today I learned, like, I didn't ever, ever knew that. Now that fixes us all this, because for me, I have this end-to-end all over the place in architecture.
Okay, okay.
to the link itself. Interesting.
How do you deal with… oh, wait, oh, I added to the link, because in this particular case, I also have situations where… like, the way Brightwood works is, like, there is a… You actually produced One per message, and produce the bash.
So… Is that okay? I guess it's okay, right? Like, depending on which level…
Michele Mancioppi 01:09:08 At least what per message?
Yordis Prieto 01:09:10 Okay, so in Broadway, you have the concept of the producer, which is like, you know, taking a bunch of stuff and then dumping it into a module. That module can decide to have either one at a time or a batching. But, here's the thing, they also have something called prepare a message.
which is one at a time, where you do marshalling and then put the data, you opt in into it. So, like, basically, one component have bashing and a singular one, all at the same time.
Michele Mancioppi 01:09:38 So the, the, the, as the… As an instrumentation author, there can be the, the temptation Of, creating spans in the situation of just one message consumed, or a patch of them differently.
The, I advise against it, because it's a very slippery slope. And the… imagine this case. So, your library is the one that, kind of.
Is the first span.
In the request. So you have, like, you have a queue, and you connect, and that connection, the consumer span, is the first one on your side.
By the time you create that span, you do not know which trace it is.
Right. Even if you need to consume only one span, then you need to delay the creation of the span.
Knowing which trace contest continues. Don't do that.
Create always a new trace.
And then use the span links. For the end user, it's gonna be mighty confusing if sometimes it continues in the same trace, sometimes not.
Moreover, you may not know… so you can code for it in the instrumentation, it gets even more complicated the moment that you have a parent that triggers the consumption of the span. In that case, the trace ID is already set.
And it's going to be a different trace than the one coming in with the trace context of the message. So my advice is, in any case, you just either continue the trace that you have in your application as the active span, or if you're about to create a root span, then create a root span, and then just link.
So start with a new span, which means that consistently, irrespective.
Or whether you want to consume one span or many, the trace shape is always the same, and it always uses span links. Now, this being said, I am the head of product, former head of product, I'm the chief architect of a tool that does very well with span links.
That is not universally true.
Yordis Prieto 01:11:44 Which one is that one?
Michele Mancioppi 01:11:45 That's zero.
Yordis Prieto 01:11:47 Okay, I… wait, dash, dash, zero, hotel.
Michele Mancioppi 01:11:51 I don't want to chill, but I don't know how many other tools do as well with span links.
Yordis Prieto 01:11:56 This one?
Yeah, I mean, that's it, like, you are the perfect person, honestly, to tell me what to do, because, like, I don't feel an expert, and… like, I feel, like, alone in this, like, situation. The beam is, like, so much all over the place, like, okay, everybody expects single deployment, or things like that, or, like, no, really.
kind of, like, it doesn't apply to me. Yes, they're monolithic, but the architecture is so distributed, and locations are post-transparent, and, like, things like that, that I get lost. And for me, and Michael's like.
I just… tell me what the strong opinion is, you know? I just adjusted to whatever you do, you would troubleshoot or whatever, because, like, I have all this stuff to do.
Michele Mancioppi 01:12:40 Yes. So, let the user control the service, the service name, Think hard whether you want to burn the service name for the agent, or instead group it around the operations, which is in this case.
And, yeah, I think we're clear about the, the, span links. And remember, put on the span link, the message ID.
Yes.
Yordis Prieto 01:13:07 Yeah, no, no, no. I'm gonna go back to all my, like, consumer side and figure out where I actually put in the wrong thing, because that exactly… you told me today what was the biggest gap for me. I didn't realize that the link was the one, hey, you should have this data.
Now, the second part is hopefully Datadog is useful.
But that's a V2 Pro.
Michele Mancioppi 01:13:30 It's not… I mean, they say they're alternative, so you can open a feature request and say, hey, how about you, I can be supported?
Yordis Prieto 01:13:38 Yeah, yeah, yeah, yeah. It's one of those, like, maybe you know the answer, because I don't. It's like, you know, okay, why this thing here, I think, is a resource? Like, sometimes they tag things and confuses me, because I don't know if it's open telemetry.
Michele Mancioppi 01:13:51 I don't… no, no, it's… this is Datadog, effectively translating what they get in Auto into their own proprietary format, and I am guessing so that Umbrella is a service?
Yordis Prieto 01:14:03 It doesn't deployable thing.
Michele Mancioppi 01:14:04 Outside this namespace, and that this is an operation.
Yordis Prieto 01:14:08 Yeah, that's technically… yeah, this is technically one operation, so… yeah, so, I don't know, like, sometimes that's the tricky bit, that's, like, confuses me, so… so you're saying that in here… you see, they don't… they don't allow me to see attributes here.
which now, I'm worried, because most likely, if I put the span links attribute.
They should show me here, as a whole theme for.
Michele Mancioppi 01:14:33 If you're able to traverse from this span to the one that you link, I mean, that's good.
Yordis Prieto 01:14:40 They do allow me to traverse, but not to see attributes in here.
Michele Mancioppi 01:14:44 It traverse, can you traverse both directions?
Yordis Prieto 01:14:48 Yeah, yeah, yeah, it goes back and forward, so if I come here, there's a back… backward one.
Michele Mancioppi 01:14:52 Okay.
Oh, that's.
Yordis Prieto 01:14:54 So I can go back and forward, but I don't see anything here that will show me attributes for that given thingy.
But again, it's like, that's just a Datadog thing. So, yeah, so for me, it's like… when I come to… here, like, look at all this. Technically, all those… actually, let me group it. All these things, AODM, is the exact same deployment, it's just like… a domain, right? Like, a domain-driven design, like, command handler, so it's every single operation, so… Is it rye? Is it Rona? I don't know.
Michele Mancioppi 01:15:25 It depends, and it gets even more interesting the moment you start thinking about RAD metrics.
So, rates, errors, and duration, although I think of them as requests, errors and duration. Some tools will want to actually calculate the material of the service.
So if you go to granular, They lose every meaning.
Right.
That's why in this video, we actually literally implemented a concept called operation.
with a name and a type that is based on the attributes and the name of your spans, because that kind of level is missing in OpenTelemetry.
Yordis Prieto 01:16:04 maybe that is the answer of my situation, because all these operations are technically the exact same domain, right? It's like, as if it was gRPC or PC operations, right? But, like, it doesn't look like that in here.
Right, which, But if I give up to them, I do like that it gives me all the, you know, latency error requests. Like, I like that, because that's why I'm keeping it, because it's useful to go there.
Michele Mancioppi 01:16:32 It would do it also for the, it would allow you to do it also for the resources, right?
Yordis Prieto 01:16:39 Put the resources… So every single thing would be a resource, or would be the seller review.
Michele Mancioppi 01:16:44 It's, umbrella process or site reviewing eligibility something.
That, I would call an operation in their serum. I would call it a resource, as far as I know.
You would still be able to see the latency, not on the service map, because the service map will aggregate by service name.
Yordis Prieto 01:17:03 Yeah, let me find… because… okay, this one. That's an operation, technically.
Michele Mancioppi 01:17:08 Yep.
Yordis Prieto 01:17:10 So that's an operation, the… the… it's no, like… could be grouped logically.
Michele Mancioppi 01:17:15 But in data, they're gonna offer you the service.
Yordis Prieto 01:17:19 I mean, I don't know why they do that.
Michele Mancioppi 01:17:21 Because of the way that you are notated, I assume.
Yordis Prieto 01:17:25 So.
Michele Mancioppi 01:17:26 If you give, if you give… This… this umbrella.solarreview command something, if you set it as the service name.
Yordis Prieto 01:17:33 I'm not, the service name is Umbrella.
Michele Mancioppi 01:17:37 I'm so confused.
Yordis Prieto 01:17:39 Yeah, the service name is only one, it's the umbrella, but I don't know what they're doing in here.
That is taking it from… oh, here.
Yes.
Michele Mancioppi 01:17:50 But that is missing the service name, doesn't it?
Yordis Prieto 01:17:54 I think they put it here.
Michele Mancioppi 01:17:57 Oh, no, it should be also in the tags.
Oh my god.
Yordis Prieto 01:18:01 Yeah, I, like… this is… Yeah, like, do you see now why I'm getting so confused is, like, sometimes it's like, okay, what am I doing wrong, per se?
Michele Mancioppi 01:18:11 Yeah, that's…
Yordis Prieto 01:18:12 I'm gonna connect it to your service, then, and see how it's gonna look.
Michele Mancioppi 01:18:16 Yeah, let me know how it works in that case.
Yordis Prieto 01:18:18 Yeah, yeah, I'm gonna connect my local development and trigger the whole workflow, because honestly, like, I cannot tell what is… Datadog telling me, hey, doing whatever they want, what is me tagging it wrong, and, like, you know, I want people like you to tell me, hey, do this, do this, do that, and here's how you learn how to observe it that way. Because, like, yeah, I know that it depends, but, like, just tell me how to work.
Michele Mancioppi 01:18:41 Here are a couple of… a couple of tips. So, if you want to see what you actually send.
You would, for example, be able in their zero to go to tracing.
then get a span, and then there is the source tab, and this shows you a, always, it will always show OTLP JSON, even if you send OTP protobuf, because nobody can read protobuf.
But you will see what you're actually sending, and you're able to explore the stuff inside. Like, let me get something with links.
Something of this.
And you're able to see, the links, you'll be able to inspect also the attributes.
To all of this.
Works.
Yordis Prieto 01:19:28 Got it.
Michele Mancioppi 01:19:30 And that is… hopefully it helps to make sense out of it.
Yordis Prieto 01:19:33 No, this was really helpful. Like, thank you so much. Like, I'm gonna go back to it, especially that gap of the link, I didn't know that, so now I need to revisit that absolutely everything. Thank you so much.
Michele Mancioppi 01:19:44 You're welcome. Have a nice day.
Yordis Prieto 01:19:46 Alright, you too, bye-bye.
