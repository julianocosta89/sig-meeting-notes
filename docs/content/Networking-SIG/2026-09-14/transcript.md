SIG: Networking SIG
Date: 2026-09-14
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

Stephen Lang (Raintank, Inc. – Grafana Labs) 00:01:39 Hello.
Antonio Martinez (Cisco Systems, Inc.) 00:01:41 Hey, everyone.
Matthieu Noirbusson (Sensor Factory) 00:01:42 Hello?
Marc Netterfield 00:01:44 Everyone.
Giuseppe Ognibene (Coralogix) 00:01:45 Hello?
Sven Cowart (ElastiFlow Inc) 00:01:56 Right on.
I'm gonna bring up the… our board.
In this case, and not everyone has seen this here.
I'm good, show everyone now that we have this. And we should use it like other SIGs do, where we can just prioritize and walk through items this way, and kind of give a status on where things are as well. And this also will be the way that we will triage these tickets and decide on how to move forward on each one of them.
Okay, starting in the top of… well, actually, I'm sorry.
Getting out of myself here.
Hmm.
Okay, we have quite a number of… talking points. Let's triage for… 10 minutes, and then we'll get to the talking points. Does that sound good, Antonio?
Antonio Martinez (Cisco Systems, Inc.) 00:02:53 Sounds good.
Sven Cowart (ElastiFlow Inc) 00:02:55 Alright, let's see. What is this one again?
I'm not sure why this is in progress.
Hmm… Oh, GitHub Automation did it?
Interesting. Don't know why it's in progress. No one else has looked at this, hasn't, have they?
Antonio Martinez (Cisco Systems, Inc.) 00:03:23 Nonly.
Okay.
Sven Cowart (ElastiFlow Inc) 00:03:28 This does relate to some of the DNS things we've talked about, but I don't… Without having looked into it, I'm not gonna know.
How much of a take there.
Okay, this is the one being worked now, Where we have, a open PR.
which I believe is this right here.
The sticking point here is, the guidance that I've written up on how to decide between address port pairs that exist in 3 different areas. Is where that should live.
I originally had it in the general attributes stock.
But no one really likes that that just feels like a dumping place for unrelated concepts, so I moved it, actually, I created in this PR a, An entry point for… The network.
SIG, which would be… It's… the stocks.
Network.
Slash readme.
And, there's still some pushback.
So… The options are the Network Domain Index.
Dedicated doc with the how-to link from the index.
The how-to link.
What he's referring to is there's a how to write semantic conventions.
document.
Okay, to put it in there.
Dedicated page under non-normative or even general.
This is exactly what we're trying to get away from.
Add it to the end of the Network Attributes group page. I don't quite know what this means.
Because, So I need to ask, because I… this, to me, is confusing. There is no network attributes for page.
Dedicated page slash how-to section within the network domain.
That's also, for me, a viable option. Sticking it into the how-to link, just so you guys… Are you guys familiar with what that is?
So… If you go into semantic conventions, And then you go to… All the way at the bottom there, how to write some extensions.
And putting it in here.
I'm not a big fan of this.
It feels to me like… if I'm arriving instrumentation for Network layer, this is… the last place I would go, because I would just look at the existing attributes that exist first. So I try to go into those areas, which is why I like putting in the network.
document.
It is…
Antonio Martinez (Cisco Systems, Inc.) 00:06:22 That's…
Sven Cowart (ElastiFlow Inc) 00:06:23 Yeah. It is somewhat inconsistent. I mean, he is right.
No other domain has a README like this, all others simply provide lists of pages containing the definitions for the domain. IHL pages as a short paragraph.
just because no one else doesn't do it doesn't mean we can't start. Like, I don't think it's a bad… practice to use, and I'm gonna… bring this up in the SEMCON call, because I don't know if there's, like, hard stances around the direction that they want to take those pages or not, but… Anyways… This… he… this fella is a… he contributes regularly, so, you know, it's… he might have very good reasons why… why he feels like this is the best place to put it, that just have not been properly communicated, or I misunderstand. So if anyone has any ideas or opinions.
please, please, speak, speak up in that, PR, because it's been stuck for about a week now, just trying to go back and forth on where this thing lives.
Okay, this… This one here, I feel like this is pretty straightforward.
Now that we've clarified some of the things around the network area, Is this something that, Antonio, you could pick up and look at and try to give your suggestions and make a PR to, Add this.
Antonio Martinez (Cisco Systems, Inc.) 00:07:56 Yep, I would love to. Actually, I had a similar issue with regard to ASM number.
Sven Cowart (ElastiFlow Inc) 00:08:02 Yeah, right, you're right.
Antonio Martinez (Cisco Systems, Inc.) 00:08:03 It was more focused on the… address part, so I think Robert is not here in the call, but he suggested, like, each address, you're gonna have, like, prefix, ES and number, it's a number.
Sven Cowart (ElastiFlow Inc) 00:08:13 Yeah.
Antonio Martinez (Cisco Systems, Inc.) 00:08:14 So, for me, it was more, like, not as a network thing, it was more, like, more related with the address.
But yeah, I… I think we can merge somehow both GitHub issues, in particular direction, so I will… I will check in on that, on that GitHub issue.
Cool.
Sven Cowart (ElastiFlow Inc) 00:08:29 Oh, heck yeah. Alright, sweet. Now that we have that approvers group, we can actually… Take advantage of all these things.
I'm gonna move.
that into to-do, then? Because that's the other one you're talking about, I believe, right?
Antonio Martinez (Cisco Systems, Inc.) 00:08:44 Correct, but I think they are similar. I mean, I'm trying to represent the same, like, which one is the ESN number and organization of an address. I imagine that guy is trying to do a similar thing.
Sven Cowart (ElastiFlow Inc) 00:08:57 Yeah, yep.
Antonio Martinez (Cisco Systems, Inc.) 00:09:00 Yeah, feel free to send to me, I will work on those.
Sven Cowart (ElastiFlow Inc) 00:09:02 Okay, awesome.
June… What is… what is the number here?
1663…
Antonio Martinez (Cisco Systems, Inc.) 00:09:35 Sure.
Sven Cowart (ElastiFlow Inc) 00:09:39 So they're linked up.
Alright, so what else do we have here clarifying? That is… this, We'll… let's just say this will be closed with… 4045.
I don't think there's much to do here after that.
Antonio Martinez (Cisco Systems, Inc.) 00:10:03 But with regard to the… where we put the network, how to use it, my recommendation would be what you just did, put it on under a new network entry point.
That, for me, makes sedation.
Sven Cowart (ElastiFlow Inc) 00:10:16 Okay. It might help to…
Antonio Martinez (Cisco Systems, Inc.) 00:10:18 I will have a comment.
Sven Cowart (ElastiFlow Inc) 00:10:19 Yeah, just leave a comment and maybe explain your rationale of why you feel like that's the best place.
Oh, yeah.
Yeah, and we certainly need this as well.
I don't know why these get moved into in progress.
I'll have to look into that.
Antonio Martinez (Cisco Systems, Inc.) 00:10:42 And actually, for that one, I actually have another ticket, which is quite similar for the Mac one.
Where do you… Let me try to find it out.
Sven Cowart (ElastiFlow Inc) 00:11:00 Should… I think it's this one.
This is actually progress.
Antonio Martinez (Cisco Systems, Inc.) 00:11:31 You can assign to me also the Mac one, and I will try to look for the one that I created and follow the same approach.
Sven Cowart (ElastiFlow Inc) 00:11:38 That sounds good.
Antonio Martinez (Cisco Systems, Inc.) 00:11:45 Actually, there was an action item on… I mean, a topic on… on the agenda, but did you guys talk with the semantic group meeting about… we have a group of attribute of an address, because those two things are related with that topic, about the Marc and about the ESN number, so… we will have to put it as… duplicate everything, right?
Sven Cowart (ElastiFlow Inc) 00:12:10 Thank you.
Antonio Martinez (Cisco Systems, Inc.) 00:12:10 Like, in the pier, on the remote… sorry, not the pier, the pier, the local.
Yes.
Sven Cowart (ElastiFlow Inc) 00:12:15 That's right. So, I did bring that up, and who Melo pointed me, too, and I can… I can send you these. Actually, you know what? I'll do the one better.
Right here.
Antonio Martinez (Cisco Systems, Inc.) 00:12:29 That's the right direction, yeah.
Sven Cowart (ElastiFlow Inc) 00:12:40 That's one.
And that's the other… More or less.
There has been… A desire to do this in the past?
And… I haven't looked into it yet, but I was pointed to these this issue in Weaver, and this issue in semantic conventions, and it got to a certain point where There was edge cases, or… Some things that were holding it up from being moved forward.
But… Folks want it, so… I don't think… like, if we contribute the functionality into semantic conventions and Weaver to add this, I think we could… we could have something going on that… that would allow us to move forward with that idea. So it seems like, yeah, let's just… Figure out why it got stuck in its development over a year ago, and then… See, almost 2 years ago, and then see how we can help move it forward, because it seems relevant enough. I imagine it's probably one of those things where It was just enough work at the time that it didn't make it worth it or something, and it probably just got dropped.
And just some… we just need people to pay more attention to it.
And so…
Antonio Martinez (Cisco Systems, Inc.) 00:14:02 Okay.
Sven Cowart (ElastiFlow Inc) 00:14:03 And for those who don't know, what we're talking about here is, like, if we're talking about things like an address, an IP address, like, that exists in source.address, destination.address, client.
Address, server address, network local address, and network peer address.
There are several other attributes, like, for example.
these AS attributes, like prefixes and other things that you want to add to any one of those addresses, and so how can we create a grouping of attributes saying, if this one attribute is present, all these other ones could also be populated?
Because they all relate on… to the address and provide additional information about something else. So, the idea is that we can either have these attribute groups that are related and relevant when a certain prefix exists, like, for example, network.address, or Or, sorry, network.local.address, or treat them as kind of like, types.
Like, this is the… Attribute type, and the attribute type has all these other attributes on it.
Doom… Okay.
Antonio Martinez (Cisco Systems, Inc.) 00:15:19 before we close… before we closing that, as I mentioned, that won't be solved in the… Short time period.
For my ticket, for the Marc and for the AS, I will add it only to the local and to the PR, or do we want to also add it to the client.address, server.address, and the survey.address, I mean, to all of them, as an attribute.
Sven Cowart (ElastiFlow Inc) 00:15:38 I'm not so sure that it needs to be added to client.address and server.address, but I think we can say that it can be.
Just because that one is a little… Is a little less synonymous than, source.address.
and destination.address, and network.local, and network.appear.address. But I think, I mean, it wouldn't hurt to have it there. I mean, if I have… client or server-based spans, I'm going to get client.address and server.address, so it'd be good to know what AS information relates to that thing. The only reason I say that it probably needs to be optional is because the client.address and server.address now is being treated as it can also be a group of IP addresses, like a connection string.
And if that's the case, then… Yes, we could.
probably still resolve that, but it would not be that straightforward, or at least it would be much less non-trivial than just having an IP address directly.
Antonio Martinez (Cisco Systems, Inc.) 00:16:48 Okay, yeah, yeah, for me it also sounds good as option.
Awesome.
Sven Cowart (ElastiFlow Inc) 00:16:54 Alright, let's go through this then, Antonio?
Antonio Martinez (Cisco Systems, Inc.) 00:16:58 So, for the… for the team, you asked Lyudmila to… to create them. Do we have any update about them? Because there is no pull request associated with that.
Sven Cowart (ElastiFlow Inc) 00:17:09 Oh, it's done. They… and… Let's see, I just didn't see this yet.
Okay, yeah, it… I think she just did it through the UI directly.
So, no PR.
But I guess there will be, based on this conversation.
But it's… I think it's… I think it's there now. Let's double check.
Antonio Martinez (Cisco Systems, Inc.) 00:17:41 Yeah, I can see now. Let me put it here in the chat. I didn't see before.
Sven Cowart (ElastiFlow Inc) 00:17:47 Yep, there it is.
Antonio Martinez (Cisco Systems, Inc.) 00:17:49 Perfect.
Rob Cowart 00:18:01 Is that approvers for things, though, in the semantic conventions repo? Are we… was it clarified whether we're gonna have our own repo, or that…
Sven Cowart (ElastiFlow Inc) 00:18:11 Yeah, there's… We will create our own repo when we feel like we need it.
But right now, we're still working on core stuff.
Rob Cowart 00:18:21 I'm not. I can at least open issues in our own repo for, like, the BGP stuff and whatnot, so at least issues to have points of discussion around, where I've been…
Sven Cowart (ElastiFlow Inc) 00:18:33 You can still do that in semantic conventions Rebo, though, right?
Rob Cowart 00:18:39 Yeah, sure. If that's what we're saying.
The… what, it'll just get moved later, then? Is that the…
Sven Cowart (ElastiFlow Inc) 00:18:51 Yeah, I think we still need to define what the repo's for.
Like, if we're working in the network area, it's… Probably going to be in the semantic conventions repo, since the attributes there in the semantic conventions.
Rob Cowart 00:19:06 Okay, so we're not doing, like, the… the… GenAI repo style thing.
Sven Cowart (ElastiFlow Inc) 00:19:15 I think we still can, but… there's a question that I have not gotten to the bottom of, is what does that mean for everything existing?
Does it just stay there? What's new stuff? Like, where's the line that gets drawn between what goes into the federated repo and what goes into the core repo?
And if someone can give a good answer to that, then… we can make the case, but I didn't… I just haven't put any time or cycles into what that means.
Antonio Martinez (Cisco Systems, Inc.) 00:19:46 I think when things go deeper, like the BEP that Rob was mentioning, like, the interface name, I mean, the interface attribute and metric, for me, that still go to the generic one, the semantic convention one, but the BEP ones, or the SNMP that we were talking also the other day, I think those ones will create a lot of noise on the generic.
and confusion.
But we can do case-by-case, most likely.
Sven Cowart (ElastiFlow Inc) 00:20:16 You have an opinion on an hour.
Rob Cowart 00:20:19 What's that?
Sven Cowart (ElastiFlow Inc) 00:20:20 Do you have an opinion about that now? Like, when the… where the line should be drawn?
Rob Cowart 00:20:26 I'm thinking about my future laziness, and the fact that I would rather put it where it's going to be, than have to put it somewhere else, and then it moves, and then the move creates confusion, because people now want to comment on something that's not where it was before, and… Yeah, you know, so it's like, either… to me, I feel like either we're doing something separate, and let's do it, or we're not.
Like, that's, you know…
Sven Cowart (ElastiFlow Inc) 00:20:51 Yeah, I… I don't think there's, though, any… so… for the same laziness reason is why I haven't done it, because there's… no matter what, we're going to have to manage the network tickets and the semantic conventions repo as well.
So… Like, like this board, right, that we have here?
is at the organization level, so this is any repo, doesn't matter where it is. Like, there's tickets from OBI in here and other things, and we can keep track and work through things that way.
Rob Cowart 00:21:28 Yeah, so to answer your question directly, I don't really have an opinion, I just want to be told what to do, so…
Sven Cowart (ElastiFlow Inc) 00:21:38 let's keep it there for now, until we see a reason that we actually need it. Like, if we have a reason, then… but I don't want to just do it just to do it.
Rob Cowart 00:21:46 then I will try to carve out a little bit of time today or tomorrow to take the stuff I have in and mark down files in that repo in our org, you know, ElastiPlow's org, and and I will create issues for them in the semantic conventions org.
Sven Cowart (ElastiFlow Inc) 00:22:05 Yeah, that'd be great. And, I mean, you can drop code in there, too. Like, there's no reason to not add… the PRs to… the semantic conventions.
Rob Cowart 00:22:14 The reason not to do it at the moment is, especially after my conversations with the entity SIG, is that, like… they don't know yet, like, what… for example, like, what relationship types? Right. I think, yeah, those type of things, there's, like, there's not, like, code to do yet, so it's just gonna be opening issues for discussion at this point.
And then… and then, then… The results of those conversations can turn into.
Sven Cowart (ElastiFlow Inc) 00:22:48 Yeah.
Peter.
Rob Cowart 00:22:50 Here, I mean, this one maybe could be a PR, right off a particular one.
Sven Cowart (ElastiFlow Inc) 00:22:54 But I mean this and, like, the BGP one? Sorry, the Zoom bar keeps getting in my way, I can't get to the other tabs. But the… the… You could add that code to the semantic conventions repo?
And just on a… because you're gonna have to fork it anyways, right? So then you have a fork added there. Or… create the PR and create a draft PR.
That way, it's more obvious, but… I mean, that's what I've been doing, is creating graph PRs for stuff that's not ready yet.
But the great thing, too, now is that because we have that approvers group.
Like, we can actually control All the stuff inside of… GitHub, even though this is the semantic conventions repo.
Okay.
Rob Cowart 00:23:40 Okay, I know I was asked that question in Slack about… about that stuff, so yeah, I'll try to get that moved over.
Sven Cowart (ElastiFlow Inc) 00:23:49 Sounds good. Thank you.
Rob Cowart 00:23:51 Either today or tomorrow.
Tomorrow, excuse me.
Sven Cowart (ElastiFlow Inc) 00:23:56 What is this?
Antonio Martinez (Cisco Systems, Inc.) 00:23:58 So that's your pull request that you had. I didn't have a chance to look at the feedback, there was some feedback over my comments, so yeah, I will… I also bring here, honestly, so people can also review, because it's an interesting one.
So if we have more people looking, it will be better.
Yeah, for example, that comment, I think it's the one that we just discussed here about where to put it, but.
Sven Cowart (ElastiFlow Inc) 00:24:20 Yeah. Yeah, so the other ones I've, resolved and addressed, So, the routing conversation, I created a new issue.
Here.
Just documenting that, deciding on where this actually lives, so this is being informed by the BGP work that you're doing around with the entities there.
So, I created that one.
And then I just removed… I actually just removed the open questions section, because I got rid of all of that portion of it.
So, I actually… yeah.
This was the question about source destination needs direction. Yes, agreed. It… is… I've made a call out somewhere in the doc.
And in the how-to, but otherwise, we're, like, to actually create an attribute, I don't want to add the problem of adding a new attribute to this PR.
Because you're gonna Right, so we're gonna do it when… with the, the flow-related work.
Which is… There is no issue. I needed to write an issue. There's been a bunch of PRs and other things, but I don't think any issues created it specifically for it. I think there is one, but I couldn't get it into this board, but it's in the OBI one, so I need to look up what's going on there.
So, I had made that change.
Yeah, I made the change for this, too.
And then, same with this.
So,
Antonio Martinez (Cisco Systems, Inc.) 00:26:13 I will take a deeper look, yeah.
Sven Cowart (ElastiFlow Inc) 00:26:15 Yeah.
Cool.
Alright,
Antonio Martinez (Cisco Systems, Inc.) 00:26:23 That's already discussed.
And then for the review interface proposal, I have been talking with some folks last week, but you guys were not here, so I think it's a good idea to bring it again. So this is for Robert, for the interface proposal.
I saw that you are using, like, the semicolon in the majority of the example. This is just, honestly, a small detail, but if you could put, like, another example, that would be… Could be great, so in the example column, if you go down.
Rob Cowart 00:26:55 Yeah, yeah, yeah, some of those, they're not all complete on the example values, yeah.
Antonio Martinez (Cisco Systems, Inc.) 00:26:59 Perfect, yeah, I think we are… yeah, those ones. The interface type, MTO, so you're putting… perfect. The other one that they have is Network Interface Bandwidth.
I don't… all of that as an attribute, in my opinion. I don't know if you have any rationale of putting as an attribute for any reason. I see more as a… As a method that we could discuss.
How we… we want to call it, or which… what magic could be, but… AIC personality adopting.
Rob Cowart 00:27:28 the… Oh, okay.
I missed a comment in here. Let me explain real quick.
So, a given network interface.
based on its type, is going to have… let's call it… because I know there's virtual interfaces, but for this… for the sake of discussion, right? Like, a given interface has a… physical capability of what its bandwidth can be, right? A 25 gig per second interface can do 25 gigs per second.
Now, whether it's configured to actually do that amount, or, like, say, a Wi-Fi interface that, you know, can do a certain, amount of bandwidth is, like, physically what it's capable of, that's a little bit different than its actual realized bandwidth, or configured band… and that second value, which is not here, because I was just doing, like, the identifying and descriptive attributes, was not doing metrics yet for all of it, but the idea in my head was.
There would be a separate metric, was, like, the actual bandwidth, or the current bandwidth,
Antonio Martinez (Cisco Systems, Inc.) 00:28:51 Yeah. We need to put that more clear. You said that it's not the configure, but maybe configure war is a good one here, something like, I don't know, network interface configure bandwidth, or… pretty fine, it's not neither a good word. But we should specify that to remove confusion that this is not the actual bandwidth that is going through. This is, like, the… what is expected, or what's the maximum, or… Yeah, we need to iterate.
Rob Cowart 00:29:21 I described that incorrectly here. You're… that was…
Antonio Martinez (Cisco Systems, Inc.) 00:29:24 vulnerable.
Rob Cowart 00:29:25 But that's good input, yeah.
Sven Cowart (ElastiFlow Inc) 00:29:27 Yeah, I think even in the name, right, because this will probably just be the metric name.
Antonio Martinez (Cisco Systems, Inc.) 00:29:32 Yep, yep.
Marc Netterfield 00:29:34 So, another thing that I've run into in the past is that, if you make it an attribute, at least Prometheus won't let you do math on attributes, like multiply them against each other, divide, do a percent calculation.
So, for stuff that I've done, I've had to move bandwidth specifically off of being a label or an attribute to a metric so that I could do math on it.
Antonio Martinez (Cisco Systems, Inc.) 00:29:56 But which kind of math are you thinking about here, Marc?
Marc Netterfield 00:30:00 Like a percent bandwidth utilization, like, if I take.
Antonio Martinez (Cisco Systems, Inc.) 00:30:03 Okay, okay, okay.
Marc Netterfield 00:30:04 Observed bandwidth against the capacity.
Antonio Martinez (Cisco Systems, Inc.) 00:30:07 Okay, okay.
Rob Cowart 00:30:09 You know, that drives me back to this point that I continually find myself I'm not gonna say conflicted, but almost more curious about. And then when I think of OpenTelemetry, I think of it as a spec to communicate information to a sync system.
Not a spec designed to tell the SYNC system what it has to do with the data.
And… and with that… with that definition.
quite frankly, my opinion is, is if they can't do math on attributes in Prometheus, that's their own frickin' fault.
Not… like… and I guess I'm trying to say, like, how… how puristic, Should we be on… fixing the communication standard, open telemetry, to essentially fix downstream systems.
Marc Netterfield 00:31:09 I think that's a valid point, because I just looked it up. I'm like, does OTEL have a requirement about this or not? And I think that's… it is just a Prometheus artifact.
Rob Cowart 00:31:17 So… Hmm.
Marc Netterfield 00:31:22 And maybe other backends, but that's just the one that I run into.
Rob Cowart 00:31:25 Yeah, I just didn't know, kind of, what was the official stance on that, you know?
Because at some point, you're going to get to where, like, someone else is going to say, well, I can only do math on max, you know, interface speed values if they're attributes. Okay, now what do you do?
Antonio Martinez (Cisco Systems, Inc.) 00:31:42 Okay.
Rob Cowart 00:31:43 You know, like, I just feel… I just wonder… and I'm new to this, but I kind of feel that, like, is it really our job to fix the downstream system with the way we communicate the metrics, you know?
Stephen Lang (Raintank, Inc. – Grafana Labs) 00:31:54 No, it's a fair point, and I think the back end is intentionally out of scope. But for the sake of Prometheus, there is a workaround if necessary. You can use, like, metric transformations.
Correct.
Antonio Martinez (Cisco Systems, Inc.) 00:32:05 Correct.
Stephen Lang (Raintank, Inc. – Grafana Labs) 00:32:06 So…
Rob Cowart 00:32:07 Having said that, in this case, though, if the attribute is kind of like.
the max physical capable, and then you have something like bandwidth actual that is the either configured and or… Based on other… thing, like… like, in Wi-Fi, right? All kinds of things, signal to noise and other things that can affect the bandwidth dynamically at a time. That's a different value, and then that would be a metric, and it could be… The math could be done on it, you know.
Sven Cowart (ElastiFlow Inc) 00:32:40 Steven, what did you say that was called?
Stephen Lang (Raintank, Inc. – Grafana Labs) 00:32:44 There's, there's transformations, so you can.
Sven Cowart (ElastiFlow Inc) 00:32:46 transformations.
Stephen Lang (Raintank, Inc. – Grafana Labs) 00:32:47 Yeah.
Antonio Martinez (Cisco Systems, Inc.) 00:32:50 With those, you can convert from attribute into metrics, yeah. We used those in the past.
Sven Cowart (ElastiFlow Inc) 00:32:58 That makes sense. I guess that is their way to solve the problem, which was probably the problem.
Antonio Martinez (Cisco Systems, Inc.) 00:33:05 So the feedback would be, like.
propose a different name, so it's super clear that… okay. Moving on. So here, but here we have…
Sven Cowart (ElastiFlow Inc) 00:33:17 This is why it would be great if this was a… draft PR, because then you could just leave the comment on the code instead of somewhere in some issue that's unrelated to where it actually lives in the code. Yeah.
Antonio Martinez (Cisco Systems, Inc.) 00:33:34 So, the next one is about the network.interface.promiscousmode. Here, my… just in last Monday proposal, sorry, meeting, I proposed, instead of having promiscuous, we could have, like, something like code mode.
I'll name… in the values of that mode, we could be promiscuous on many other. But then I think Mark was mentioning that that data was coming from SNMP, and we didn't have other mode.
There was, like, Wi-Fi mode, but that's a little bit separated. So, also, Giuseppe proposed, like.
on eBPF, you guys are seeing as on-off, so maybe instead of using true-false, we can use on-off to align that, but here I don't have a strong opinion. That was just a discussion that we had last Monday, and I didn't want to… to remove it.
I don't know, I think Guseppe is still on the call, I don't know if you want to add something about the on-off.
Proposal.
Giuseppe Ognibene (Coralogix) 00:34:26 No, no, no, I mean, only because the promiscuous mod on-off is what Linux is doing. So when you set an interface is on-off, just that one.
Rob Cowart 00:34:44 Is that… does that tend to be the typical… I mean, I could see value either way, because… You may have a desire at some point to say, like, on, off, or unknown?
And so, obviously, with a Boolean, you couldn't really do unknown or undetermined or something like that.
So, I'm not married to either one. I could see, like I say, benefit one way or another, if it's,
Antonio Martinez (Cisco Systems, Inc.) 00:35:17 Usually when it is unknown.
Rob Cowart 00:35:18 In my brain, the only thing is I think of a Boolean as probably a smaller value than an on-off is on the wire, so…
Antonio Martinez (Cisco Systems, Inc.) 00:35:28 What I was mentioning is, like, usually when it is unknown, usually the attribute is not Scent.
this is, like, at least the way how it's asked. Is this usually, like, as an optional? I imagine that was marked as optional, I don't recall right now. But if it is not known, we just don't send it. That's what I usually see.
But yeah, I don't have neither sort of opinion about all.
Rob Cowart 00:35:51 Understood. Yeah, I think… I think there's a difference between unknown, like, I just… I don't support doing that, so I… I can't tell you one way or another, and… and unknown… I tried my best to determine this, and darn it, I just couldn't figure it out, and I wanted to let you know.
You know what I mean? Like, I think I could… So I get your point on unknown. I do think there are some valid reasons sometimes where you want to have an unknown, but I'm not saying this is necessarily one, but yeah, I get it. Like I said, I'm… I'm not married to either one here. Whatever is most consistent with where these things are handled elsewhere. I primarily pick Boolean because of the Boolean data type, and thinking that's going to be smaller on the wire, so…
Sven Cowart (ElastiFlow Inc) 00:36:41 I think…
Antonio Martinez (Cisco Systems, Inc.) 00:36:42 Trivia.
Sven Cowart (ElastiFlow Inc) 00:36:43 Yeah, I would lean towards Boolean as well, but… I think let's find some other examples in the ecosystem.
to see you.
Rob Cowart 00:36:52 If they're…
Sven Cowart (ElastiFlow Inc) 00:36:53 There's already a certain broad consensus around that.
Rob Cowart 00:36:56 Shit.
I was just trying to be as consistent as I could be with things where it made sense, but like I said, if the consensus is on-off, I'm open, but I agree, Sam. Let's… let's find more examples.
Sven Cowart (ElastiFlow Inc) 00:37:09 I would be so surprised. I know in the… the, the Linux commands.
You use on-off, but it would be shocking to me if it actually stored that somewhere instead of true-false value.
But it's probably just text config anyway, so it could be that… That's why.
Huh.
Antonio Martinez (Cisco Systems, Inc.) 00:37:32 Okay, so the next ones is… are about metrics. Here, it's more open for thought, honestly. We have… you propose network.interface.byte.
Can we use network.io? Like, if you open the proposal, right, that's… it's gonna be cleaner.
Sven Cowart (ElastiFlow Inc) 00:37:53 What was the myths,
Antonio Martinez (Cisco Systems, Inc.) 00:37:54 Byte, bytes. Yeah, perfect. So it's… a counter that is going to have the direction and the interface name, those two, I really like it, but I… I don't usually see, like, the unit, in that case it's gonna be byte, as part of the name. That was more like a promisios that Mark was mentioning before, logic before, but not… anymore in… OpenTelemetry, so…
Rob Cowart 00:38:17 I'm totally okay with that one. I think when I first brought this up, this was the one I mentioned… I mentioned this to somebody, where I was like.
Yeah, I avoided, like, like the one right below it, for example. The unit is packets. I avoided saying unicast packets, like, for that specific reason, but I was kind of like.
you know, network.interface. what word do I use here? Volume? You know, so… so yeah, I'm open to changing that from bytes to I.O, whatever, whatever we feel makes sense there, yeah.
I also was hesitant because I was… mentioning the units again in the name, but I just couldn't… Come up with anything off the top of my head, so all good, yeah.
Antonio Martinez (Cisco Systems, Inc.) 00:39:03 And do we want to keep interface here? I am saying, because network.io could also be used, I mean… That's…
Rob Cowart 00:39:12 So my only question on this, and I've seen some examples of other attributes that work this way.
But I guess it's from… from things I've worked on in the past. Like, I think of, like, Network.io.
Okay. But then, if that is a value, then that thing cannot have children. Like, if you're, like, marshalling the payload to JSON or something, right? And so that's where, in my mind, I would avoid using you know, one of these parent things, like network.io, is both a value and an object, if that makes sense, you know?
But if that's normal, and I think there are a couple examples of other semantic conventions where that does happen, so if that's normal.
I'm cool with that.
But that's the reason I was… I myself avoided, like, trying to use, like, just Network.io by itself.
Antonio Martinez (Cisco Systems, Inc.) 00:40:18 Yeah, we… as we just said, once we have that request, we can go back and forth if we put interface or not, but yeah.
I don't think that's gonna be a strong one. So the other one is…
Rob Cowart 00:40:30 More general question of, like, are we worried about a payload being able to be marshaled to valid JSON.
Antonio Martinez (Cisco Systems, Inc.) 00:40:44 I didn't got the question, what do you mean here about a payload?
Rob Cowart 00:40:47 Yeah, if, like, the… this record, when it gets sent somewhere, and something reads it, and says, okay, let me just output the… this data in this record as JSON, well, if I called bytes network.io, it would fail, because network.io holding a value would conflict with network.io being an object in JSON, and having things underneath it, like direction and other stuff.
So, so, like, you're basically saying there's… there's some… Record format types or data format types that you're excluding if you make certain naming decisions.
Antonio Martinez (Cisco Systems, Inc.) 00:41:26 Yeah, yeah, yeah, I thought, you know, I thought, you know. Yeah, you are using a namespace, yeah.
Rob Cowart 00:41:32 Yeah, yeah, yeah.
Antonio Martinez (Cisco Systems, Inc.) 00:41:35 That's a valid point.
Rob Cowart 00:41:36 And again, I just don't know. Like, I did try to find out, and I looked around, and I actually think there are some semantic conventions that do the equivalent of just, like, a field like network.io holding a value, even though, like, network.io direction also exists, so…
Sven Cowart (ElastiFlow Inc) 00:41:57 From everything I've seen, I don't think that would ever become a problem.
for… Back to your other comment about OTEL as a communication protocol.
like, this marshalling would only become an issue for downstream consumers that need to JSONify these things and put them into the records, like…
Rob Cowart 00:42:21 I just think that example, while I don't disagree with you, Sven, is not vendor-product-specific problem. It is a… it is a more, like, open… data format problem, you know? So not… not quite the exact same thing, but yeah.
Sven Cowart (ElastiFlow Inc) 00:42:47 But against the spec, I mean, but the hotel spec, though, and how the communication works, no, it will never become an issue.
Rob Cowart 00:42:54 I agree with that.
Sven Cowart (ElastiFlow Inc) 00:42:55 Right, so… and… so it only becomes an issue for downstream systems that.
Rob Cowart 00:43:01 Totally, yeah.
Sven Cowart (ElastiFlow Inc) 00:43:02 Yeah.
But it's… I mean, it's a fair question. I don't… I think that's a good one to raise within the… specification group, like, I'm sure someone has run into this problem before.
I don't know.
Antonio Martinez (Cisco Systems, Inc.) 00:43:22 So…
Sven Cowart (ElastiFlow Inc) 00:43:23 No, because he… I know he's dealt with a lot of this kind of stuff.
Rob Cowart 00:43:27 Can I ask a more general question on that? If we said network.io, right?
I can imagine that could be applied in multiple… in multiple contexts. Like… Network interface. That's gonna be, you know, like, it's in or outbound bytes, you know, based on direction or whatever.
But… a network flow.
Could also just have been network.io, which is the number of bytes traveling across that flow. So are we saying we're going to use that as a gen… as a generic
Sven Cowart (ElastiFlow Inc) 00:44:12 Question.
Rob Cowart 00:44:13 Attribute to hold the bytes, the network-related bytes.
But it could be in a different… it has different context where it applies.
Sven Cowart (ElastiFlow Inc) 00:44:25 That's good, good.
Antonio Martinez (Cisco Systems, Inc.) 00:44:26 In case we're gonna add in several, we need to put the interface, or the flow, or BEP, or I don't know, you can name it in any other context. In that case, we need to separate it, because if not, it will lose… the logic, unless you have an attribute. You will not know what's… you're traversing.
So if we anticipate that that's gonna happen, we will need to keep the interface there.
Sven Cowart (ElastiFlow Inc) 00:44:53 I'm not… I'm not sure I'd agree with that, because… If, for example, I have a… if I have a flow, then I would know that I'm receiving a flow trace.
Or it would be on a spam record, and… There would be no scenario where that would… Be something besides a flow.
And on a metric, if we're saying that we're doing this N22-driven modeling of things.
I would know the metric is describing some sort of entity.
in the actual payload I'm getting.
And at that point, I would know that network.io would be for, like, describing the value I'm getting from Somewhere else, that's not a flow.
Rob Cowart 00:45:42 I think what makes sense here is… So, let me take a step back.
Sven Cowart (ElastiFlow Inc) 00:45:49 maybe?
Rob Cowart 00:45:49 One of the things I actually, once I started to get into this, that I kind of liked, and I think I mentioned this on a previous call, you know, and again, this is my first kind of foray trying to actual create some stuff in the hotel context, but, one of the things I liked in doing it is that A couple weeks ago, was doing something for our own internal schema, and was having the… the naming of the stuff was, like.
if I could have just said, network I.O. direction, and threw that on there, it would have simplified what I was… the weird… names I was having to come up with to keep all this stuff separate, you know? So I think there's a certain, you know, wisdom in doing it that way. Having said that.
I think it's worth taking a look at a bunch of other things related to network and bytes to make sure we're happy that that could be a catch-all attribute for all kinds of different contexts.
Sven Cowart (ElastiFlow Inc) 00:46:52 That makes sense. I think where… where my head was going is… It becomes a problem when you could have for some reason or another, and I can't actually think of one, two byte.
counters.
present on… the same payload?
But I… I just don't know why you would have that. Like, for the… for example, something that's, like, SNMP-derived versus flow to ride, I wouldn't have that. I wouldn't have that problem ever, because they would be reported in different records.
Antonio Martinez (Cisco Systems, Inc.) 00:47:32 The reason why I said we should split is because now if you say that It could be for flows or for interface. Which one is gonna be the attribute key?
Is it gonna be… because most likely later, we're gonna have something with regard to the flow, or it's gonna be also the interface name.
At that case.
Rob Cowart 00:47:57 Okay, so could you also have interface name as a key? Yeah, absolutely.
Yeah.
Antonio Martinez (Cisco Systems, Inc.) 00:48:05 Or that one?
Rob Cowart 00:48:06 thing to differentiate.
Antonio Martinez (Cisco Systems, Inc.) 00:48:08 And then the metric is the same metric.
For flu.
Rob Cowart 00:48:15 Yeah. Well, yeah.
I think Flow has other keys, though, too. That's the thing, right? I mean, and I'm not gonna talk about, like, like, OBI-type flow records, like, generated at the endpoint, or the host, but rather, like.
A flow record going through a router or a network switch is going to typically… you'll have source and destination, and for that flow, those are also keys in that flow, right? But that flow also has an ingress interface and an out… and an egress interface as it's forwarded through that router or switch. And those interfaces… Will also be in the key.
But again, I don't think there's any confusion, because one is the flow span spec, and the other is a… like, in this situation here, this is a metrics You know, a metric.
Payload, or whatever you want to say, right? Record.
Alexa, I think I think we need to come up with some additional examples, because I'm going to tell you… If I was just to search our… our thing for stuff that is… that has units of bytes.
There's going to be a ton.
So, like, when I say a ton, I'm guessing I could probably find 2,000 or 3,000 attributes across network technologies and vendors pretty easily.
So, now, a lot of those will be very similar kinds, but nonetheless, let me come up with some more examples, and then we can make that decision.
Antonio Martinez (Cisco Systems, Inc.) 00:49:59 So, moving on, the next one is a little bit… Bigger change, so you are proposing network.interface broadcast.
The same for unicas, the same for multicasts. This car… I think there was something else, but yeah, those mainly. Can we have something like network.packages? And that would follow the same approach that they have for messaging client metric, like Kafka. They have something called message.client.sendMessages.
I know what we said about packets will be also the unit here, but I couldn't came with a better thing without colliding with the network.io.
But my main comment here also is, like, we should not have, like, four metrics explained kind of the same, because the broadcast, unicast and multicast, or even this car, they are pretty much an attribute. Like, we should came with a better name, like, I don't know, like.
communication way or something, like, we will decide which attribute. And also, for the discard, we should use the content of erotype, which is also another attribute, like, hero type, it was discarded, or… Protocol unknown, I think, was another option that you also proposed… proposed there.
My proposal would be, like, to merge those. I don't know if network.packages is the best way, but the thing here, name is… Challenging.
Rob Cowart 00:51:28 I mean, yeah.
I think before I can answer your question, I need to understand a little bit more of exactly how… The payload here would be getting built.
Cause… and the reason I say that is, like.
Okay, so I'm gonna have network.packets.
Type broadcasts, like, where, like, the packet type is a different, you know, is an attribute that says what network. I'm just gonna say packets, right? Network.packets is. But then I'm going to have another network.packet.
at the same time that I'm… that I would want to be sending in the same… like… OTLP payload to my SYNC system that's also network packets, and the only thing different is the type.
Antonio Martinez (Cisco Systems, Inc.) 00:52:32 Yeah, that's… that's super common.
Is it… Is it gonna be the…
Rob Cowart 00:52:36 That just seems like… you know what sometimes I have is, like, PTSD, that, like, my first computer I ever had had 16K bytes of RAM, and I would never waste that by sending a type field four different times, when if I just named the values specific to what they are, then I save all that space.
Antonio Martinez (Cisco Systems, Inc.) 00:52:59 I can't see that point of view, but now we are… we want to have, like, a metric that consolidates… we are sending packets, and then the way how we're sending, which interface, if there was any error, those will be, like, characteristic of that sent, let's say, and that's why I think we should put this on attributes. I don't know what the rest of the… The attendees consider here.
Sven Cowart (ElastiFlow Inc) 00:53:26 I know that what you're describing is the right way to do it, Antonio, where you have some… Packet type or method, or something like that on an attribute that unifies all these.
Rob Cowart 00:53:42 Oh, so that, I mean, that, that works for me.
There's just a certain part of my going back 30 years that goes, oh man, that's such a waste of space in that payload.
But I get you. Okay.
If that's how it is, that's how it is.
I mean, why not just packets? Network.packets.
Antonio Martinez (Cisco Systems, Inc.) 00:54:08 In my opinion, it's good, but I don't know. Maybe so, so, so generic.
That's the problem.
Rob Cowart 00:54:16 But it is a very generic thing. I mean, it is literally just a count of packets. Yeah.
Yeah.
Speaking of such, I do want to point out one thing. I did stick with counters for now for these.
But, did… did… We do need to make sure, though, if we're… if we stay on that route, that we are… Also, pushing along that initiative to get unsigned 64-bit.
values and the payload. Because if it's… if we don't have that, then this conversation we're having around some of these are… they need to be changed to rates or something, not, Not counters.
Antonio Martinez (Cisco Systems, Inc.) 00:55:00 I mean, usually counters are used for those things, like, Instagram is the other type of metric well used, but it's more for… Duration or timings.
Like, this is, like, a range, and then you see, like, where it's… Spending more time.
So a counter, I would.
Rob Cowart 00:55:18 That might be the other way to do it, too, but yeah, yeah. But…
Marc Netterfield 00:55:22 You're worried about, like, the rollover problem, right?
Rob Cowart 00:55:25 Correct, right. As soon as you go from, you know, the 64th bit becomes a relevant You know, most significant, and boom, all of a sudden, to a downstream system, that's a negative number.
Yep.
And yeah, that… there was a time… where… I mean, we went from 32 to 64, there was a time where people were like, you'll never hit that! Well, yeah, but now we have, like, 1.6 terabit network interfaces.
You know, that counts pretty fast.
Sven Cowart (ElastiFlow Inc) 00:56:00 Rob, you said when you talked to them, they were open to it.
Rob Cowart 00:56:03 Someone else had that conversation, it wasn't me.
Sven Cowart (ElastiFlow Inc) 00:56:05 Okay, I think maybe it was me, because I remember having a conversation about it, and then you and I synced, and I… I mean, I don't know if I can own that, is the thing.
Rob Cowart 00:56:15 I got you.
Sven Cowart (ElastiFlow Inc) 00:56:16 I think…
Rob Cowart 00:56:16 My bigger concern is probably, on that context, is how long would that take?
Antonio Martinez (Cisco Systems, Inc.) 00:56:24 I think the problem is not really on the spec, it's gonna be more on the vendors. Like, if we now support 64, that's gonna be something that we can modify on the spec, but how the… let's say, the collector will adapt to that… I think collector is using today double, honestly, but yeah, we can talk about that later. But I think vendor will also need to adapt.
Yup. That usually takes time.
Rob Cowart 00:56:47 The good news is there are no vendors out there right now, today, that ports, hotel, network, semantic conventions, because there are none yet. Well, there's just that little handful in that one table, but in general, like, I don't think anyone would have encountered this issue yet, so,
Sven Cowart (ElastiFlow Inc) 00:57:06 So where we left that conversation is they're all in favor of it. They asked for… reasons why it's necessary, and I asked you to open an issue inside the spec repo describing the problem.
of, like, how fast these counters can roll over, especially in the networking world.
Because right now, the reason it hasn't happened is because it's just not a problem you commonly run into, and the application space. That was…
Rob Cowart 00:57:39 Oh, in the application, yeah, yeah, yeah. Because I guarantee you, people that have high bandwidth servers probably also have this problem, they just… Weren't managing the network part yet.
Sven Cowart (ElastiFlow Inc) 00:57:51 the… the good thing is, is what can… what could be done is, like, I think it can be pretty easily added to the spec, but then there has to be also the work to follow up with updating collectors and the entire ecosystem around it, including the changes into all the official SDKs.
And… That probably is gonna be a 2-year journey.
That's my.
Rob Cowart 00:58:17 If that's the case, I would definitely want to try to,
Sven Cowart (ElastiFlow Inc) 00:58:22 Well…
Rob Cowart 00:58:23 alternative.
Sven Cowart (ElastiFlow Inc) 00:58:24 Why don't… I don't know if I… I don't agree with that, because if… the change can be made, and people who care about it support it. Like, it's not a breaking change, do you know what I mean? Because it's just adding a type, and if people aren't using it, then you're not using it, that's…
Rob Cowart 00:58:41 I get you. I guess my comment there was more… selfish elastiflow, and that… you know.
I guess we'll just support a draft, basically.
Sven Cowart (ElastiFlow Inc) 00:58:54 Yeah. Yeah, I mean, that's… that's what you have to do anyways nowadays, is support a draft. Most of the attributes are developmental, and people build their…
Marc Netterfield 00:59:01 a lot of people, they get all anxious. They're like, everything in OTEL is still beta, or… like, yeah, man, just get used to it, because, like, five things are actually complete.
Sven Cowart (ElastiFlow Inc) 00:59:11 God.
Rob Cowart 00:59:11 Okay, so we won't worry about that too much, then.
Antonio Martinez (Cisco Systems, Inc.) 00:59:16 But let's create those tickets so we can start moving those things ahead of you.
Rob Cowart 00:59:20 Okay, yep, sounds good. Alright.
Antonio Martinez (Cisco Systems, Inc.) 00:59:27 I know we are running out of time, but the last one was, you have network interface output queue? Here, it just, honestly, I renaming, like, network interface queue packages to follow the same other one, but that's, you know, I have a less… Personal opinion.
And we're also running out of time, but my last comment was, in the last meeting, not the previous… before, I couldn't make it, but I saw the recording, and you guys were talking about network.pr.bep, or network.bep underscore pier.
Rob, have a strong opinion that BEP peer is like a concept on the BEP ecosystem. I think they also go together. It's not like we are… monitoring a BEP on the pier or on the local. It's… it's like a concept. That's why I consider it should go together.
But let's bring in that question, maybe once you create that.
Proposal, and then we don't… we don't have a longer conversation around that time.
God, dear.
Sven Cowart (ElastiFlow Inc) 01:00:27 Mr.
Antonio Martinez (Cisco Systems, Inc.) 01:00:27 That's my peanut.
Sven Cowart (ElastiFlow Inc) 01:00:28 there is, that issue, if I can find it, but… that I created where we can have that conversation asynchronously.
Antonio Martinez (Cisco Systems, Inc.) 01:00:38 I think on the left is the 1419A.
No, not sorry, on the to-do, on the third on the to-do.
Yes. Is that wrong?
Sven Cowart (ElastiFlow Inc) 01:00:48 Yep.
So, right, part of that is… Figuring out where it actually lives.
Another one I thought of, too, is, like, what if you have networked out routing?
Antonio Martinez (Cisco Systems, Inc.) 01:01:00 And then it's not…
Sven Cowart (ElastiFlow Inc) 01:01:02 PGP, all the other ones that…
Rob Cowart 01:01:05 Yeah, on our previous call, I still need to do other… some of the other protocol examples, yeah.
Antonio Martinez (Cisco Systems, Inc.) 01:01:14 Less priority for that. Let's go first with the Networking interface, but yeah.
Rob Cowart 01:01:18 Awesome.
Real quick, Matthew, you were the one that said y'all… you had a bunch of work already that… that your team's organization had done kind of internally around entities, right?
Matthieu Noirbusson (Sensor Factory) 01:01:35 Yeah, we are working on that,
Rob Cowart 01:01:40 If possible, I may ping you to maybe kind of get together and just do a meeting, the two of us, and share some concepts and stuff, and also a little bit of the conversations I've had with the entities group.
Because… My summary would be this, especially when it comes to relationships, they're not sure what relationships they even need yet, and… and… we're gonna… gonna kind of be the first group to really try to use the… or implement entities in anger, if you will. So, you know, like, we need to come up with some type of suggestion of… you know, these are the relationship types we think we need in network, you know, and just facilitate a conversation. And… and I can share what we have a little bit of internal things, some work that I've… that I kind of have in progress.
And then maybe you and me could sync on that first, kind of, draft of ideas there, if that makes sense.
Matthieu Noirbusson (Sensor Factory) 01:02:40 Okay, okay, yeah, for sure we can work together on that, yeah.
Rob Cowart 01:02:44 Yeah, yeah, okay. I will… I will ping you, and we can try to set up a little time to… to talk, so we don't have to do it here with a bunch of spectators as we brainstorm. We'll share the results, and then we can brainstorm from there, so… and if anyone else wants to join that, I'll just kind of put… do it in the Slack. We'll try to organize something, so…
Sven Cowart (ElastiFlow Inc) 01:03:05 Beautiful.
Rob Cowart 01:03:06 Okay.
Sven Cowart (ElastiFlow Inc) 01:03:07 Alright, thank you guys.
Matthieu Noirbusson (Sensor Factory) 01:03:07 Okay.
Rob Cowart 01:03:08 Alright.
Sven Cowart (ElastiFlow Inc) 01:03:09 Thank you, everyone.
Antonio Martinez (Cisco Systems, Inc.) 01:03:10 Yeah.
Matthieu Noirbusson (Sensor Factory) 01:03:10 Thank you.
Marc Netterfield 01:03:11 Have a good day.
Giuseppe Ognibene (Coralogix) 01:03:11 Inc.
