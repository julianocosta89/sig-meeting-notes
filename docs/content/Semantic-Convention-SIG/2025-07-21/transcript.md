SIG: Semantic Convention SIG
Date: 2025-07-21
Duration: 62 minutes
Zoom Recording URL: https://zoom.us/rec/share/WB1lcm_lb2ul9la0pQEtcjb1ZJ8hiko1lkmALb40la8Fu5pbEZOODHnZLWBavdGZ.BNdpOZJaAkph60mN
============================================================

## Zoom Recording Transcript

Liudmila Molkova 00:00:40 I'm of the day.
so let's get started, and some triage or people are still joining.
Please add your name to the agenda to the attendees list, and if you have anything to discuss, please.
and your topic to the agenda.
Okay, let's take a look at the triage board.
We have some pull requests that need more approvals.
including some trivial ones. Please take a look. There are a bunch of things that are blocked.
let's see?
I remember, we've been chatting about user actions and the currency things.
Trust, Dan. Do you know, if if that's
stalled, should we close it as anyone where is working on it.
Trask Stalnaker 00:02:35 hey? Don't know.
Yeah. Go ahead.
Daniel Dyla (Dynatrace) 00:02:38 Yeah, during the the browser sig last week
or 2 weeks ago. I don't remember which meeting we went through all these old Prs that had been a little bit stalled from the previous client, Sig
and I think the
the general feeling was that most of them are still good, but they just kind of lost momentum
and the new browser Sig is intending to
follow through on most of them. I don't know about this specific Pr, but there's a
you know, we're we're going through the process right now of assigning who's going to work on the various some com things, and whether it's, you know, the the particular owner of the user action event? Which I think
I expect that to be an important one so handled. Soon.
I they will decide whether to revive old Prs or open new ones, I think, but it's being.
It's being tracked. I think we're just in the early stages of trying to figure out what the State will be here.
Liudmila Molkova 00:03:53 Wonderful. And it is. Go ahead.
Trask Stalnaker 00:03:57 I was gonna suggest, maybe just clear approvals and move it back to waiting for Sig approval.
Liudmila Molkova 00:04:05 Okay.
Trask Stalnaker 00:04:06 Because they're kinda I think stale at this point.
Liudmila Molkova 00:04:14 Awesome. Thank you.
Okay,
just a quick check, because it's always in the blocked, and maybe we should close it. Move it somewhere
convert it to draft to ask, do you know what is the progress in the Graphql world?
Trask Stalnaker 00:04:36 Yeah, it's continuing but slowly, we meet once a month. yeah, I wouldn't.
What should we do?
There isn't. I mean, there is sort of a sig, if you consider it now, the external Sig.
So maybe just awaiting Sig approval.
Liudmila Molkova 00:05:00 Sounds good.
Let's spend a couple of more minutes on the block on the trash and the blocked Prs. I didn't follow up on this one.
I've blocked both dB system and the systems and messaging dot systems, James, if you want to talk about it, let's add an item to the agenda.
James Thompson 00:05:23 Yeah.
Liudmila Molkova 00:05:30 For this one.
I there is some feedback. There are some discussions. I would really laugh if somebody from Jcp. Pointing to Josh right now could take a look, and we would consider it as a Sig approval or
Do we consider Gcp a covered area that we, a wolf.
Josh Suereth 00:05:59 I mean, this is about anyone who uses Gcp client libraries. So I think this would impact all observability and opentelemetry, especially if our client libraries come with opentelemetry instrumentation out of the box. So that's kind of what this is about. What I think we want here is we want the Gcp client, library teams coming to opentelemetry and saying, here's what we, you know. Here's the best practices we'd like to provide and get some comp to be like, yeah, this is good.
If you'd rather have the Gcp client library teams kind of own this independently somewhere else. Once we get things set up more with our tooling. That makes sense to do. I think we can decide that. But this is more like a we'd like to advertise what Gcp client library team should do I can talk to Michael about this one specifically. It might be a bit early to put in open telemetry. We we can decide.
But yeah, this is, this is intended to be a Gcp client. Library teams had open telemetry instrumentation, and they provided out of the box spans. What should they be that provides the best ecosystem experience for all of open telemetry.
Liudmila Molkova 00:07:06 I am supportive of having those. We have some azure equivalents listed in semantic convention. So I'm supportive of adding those. Why I didn't review is because I would like Gcp. Folks to
make a pass on it first.st
Josh Suereth 00:07:23 Yeah. And for that, we're still having internal discussions. So this is a we. We could. I can ask Michael to move it to draft that actually might be better. And then we'll go from there.
Trask Stalnaker 00:07:36 Or awaiting Sig approval.
Josh Suereth 00:07:40 Yeah, we don't have a Gcp Sig. But that that is something we we could think about doing. Yeah. So maybe instead of blocks we can. We can put a waiting Sig approval.
Trask Stalnaker 00:07:52 Maybe maybe we could change awaiting Sig approval, to like awaiting experts.
something more generalized to cover both sigs like active sigs, and
things like Http, where we don't have an active fig anymore. But
we still have people who are who own that area.
Oh, yeah.
like that.
Liudmila Molkova 00:08:30 Cool. So we are out of our triage box. Let's move to the
agenda and have a couple of items that remained
not discussed in the last meeting. So let's take a look at the sequel commenter. Sam, I think you're here.
Sam 00:08:56 Okay.
Liudmila Molkova 00:08:56 And unfortunately I didn't check your last changes. Do do you want to discuss any specific items.
Sam 00:09:03 Oh, yeah. So instead of bring the service down. Name propagator. I I would like to introduce a service propagator. It's more like a list of string that can be propagated by the text map
carrier. I also provide the example so well. Users could just
proper cable they were they want, instead of just tied to our
like predefined service down there. I feel that could be more general.
and I also moved the propagator out of the instrumentation.
I rolled it to this should be defined in the language control. But I didn't make changes about their service.name part.
and I I think I should discuss in the sick meeting first.st
Josh Suereth 00:10:08 So
for context here for everybody who might not know in SQL commenter, it doesn't just pass the trace id
and the span id. It passes like service name. I believe it. And and Sam correct me if I'm wrong. It was like something like controller in action where the original thing, and then we we change it to be service name to match open telemetry and I can't remember.
I I feel like there were 2 things being passed that were not just span id context. Id
So so everybody understands like, that's 1 of the things SQL commenter does. The problem. We have an open telemetry is actually service name. There is no Api access to it at all.
Like right now, service name is part of resource, which is part of the SDK,
and there's not a way to get access to it in an Api as part of instrumentation, which is where context propagation lives. And so for SQL. Commenter to get service name. It actually has to go directly at the SDK.
Now, Sam, I think this is a general problem with open telemetry Apis.
If we are planned to propagate a service name, we need a place to put service name that can participate in propagation kind of similarly to context. And so my question on your proposal here is, are you proposing to use opentelemetry context to write service, name.
to propagate between components of instrumentation. Are you trying to do something more general, of propagating the whole freaking resource? So people have access to it in instrumentation.
Sam 00:11:52 Well, in the example, I don't use the context. I just provide a way. So user could use the propagate Api to
propagate a list whatever they want, and
it probably just leveraged. Inject, Messer.
and it doesn't use the contacts.
I I've put that in the comment.
We can see if you scroll up a little bit.
Yep.
Liudmila Molkova 00:12:32 So this aligns with what we discussed on slack right, that
you can give a propagator to the instrumentation.
and it would use it. But instrumentation doesn't care what you propagate.
and there could be a country component.
That depends on the SDK, that
inject service name, that that propagate service name.
Sam 00:12:58 Yes.
Liudmila Molkova 00:13:01 The question they have is.
if this is the case, then why do we need any of the service? Name things in the database
conventions?
Sam 00:13:14 So the because people don't usually open 100% sampling, and that means even the
the database propagated trace contacts.
It. It might not be
easy to correlate the the data we fetched from the database side and correlate that with the client side, because
the
we we have we sample the trace twice. We sample it in the client sign once, and when we got the trace information from the server side, because we only can get the current running query, that's
second sampling. So the the chance to connect these 2 is not very, not very high. So.
having a service name at this we could 100% know that. Where is the client? Where is the client service.
Liudmila Molkova 00:14:23 For.
Sam 00:14:23 Right? Yeah.
Liudmila Molkova 00:14:25 My comment is not about, why do we need to propagate service? Name.
My comment is whether, if we why we have this
in this document, it can be in a different document.
because the database instrumentation doesn't care what you propagate right?
Sam 00:14:49 Yeah, I,
yeah, you're right. I just feel like this may be a related topic, but I can move to other place.
Liudmila Molkova 00:14:57 Absolutely. It's a related topic, but my suggestion would be.
There is a similar document that describes some specifics of Aws context propagation.
If if I will find it.
No, no, tiff somewhere here.
And if we put the document well, I don't know if this is the right place, but for the one for service, name, propagate there that if we put some document
in this place, we can link to those documents from here saying, Okay, maybe this is the propagator. You might want to use.
This would make more sense to me, but they would do it as a separate Pr.
Josh Suereth 00:15:52 I, yeah, I agree on separate. Pr, I also think, Sam, that this problem you probably want to take to the Spec Maintainers meeting to talk through all maintainers about, because you need a hook
to get servicing to propagate through
to context propagation across all sdks to make this work.
And you don't have that today like like, I think I understand why you're trying to make a semantic convention and put it somewhere. But I don't.
I don't think the span semantic convention is the right place, agreeing with Lydmilla there. But I think you need a place to put that, and so I think we need to keep having that discussion
with with folks who own sdks. Because, you know, foundationally.
this is not a thing we do today is put service name in context and propagate it and then use it later. That is something that SQL commenter wants. And if we're adding SQL commenter capabilities in
everywhere, then we'll have to figure out how to do that or push back on that feature of SQL. Commenter. And I think we want to have that discussion kind of quickly, because I think that could take a while to do so and sort that all out. So I would recommend talking about this in the specification meeting about
generally what you're trying to do, a SQL commenter and the challenge you have, you know you need service name
to propagate into the database.
You need it context to do so. And there's not a consistent or clear way to do that across sdks. And you would like to have a a at least a specification. So you can write context propagation.
That is general, that that will work, no matter how people decide. They want to deal with service, name
right across all the sdks. Yeah.
I don't see how you can do that today with the specification of open telemetry, you'll have 20 different implementations that rely on non specified behavior of sdks. That doesn't seem like a great state. So I think that's a question for the spec meeting. And I think that you probably want to take. Take some time to write down that problem at that level just explicitly that part of it, so that you can have a very optimized discussion. There. Does that sound good.
Sam 00:18:08 Okay.
Liudmila Molkova 00:18:19 Okay. Thank you. So if
does it, would it work for us if we either remove this for now?
Or if we leave it as completely optional example, without any normative language.
Sam 00:18:45 And we don't. Meanings. Only suggestion.
Liudmila Molkova 00:18:53 Yeah. So this is could be an example.
A dear.
like, if you, if you want to start implementing it, I personally, I'm open to hear from other maintainers. I personally don't see a problem if
we leave it as an example. And if there is some country component somewhere that actually implements it.
But this should not include any any normative language, and it should be a pure example of what you can do with this.
Sam 00:19:24 It is like, if it is more like, Oh, if you interesting, you can just pull the propagator into the I mean language contribut and do this pulling stuff. But this is not kind of like enforced by this fact. Right.
Liudmila Molkova 00:19:41 Right?
Yeah. So I think it's pretty much like
how it's done today. But maybe if you emphasize it, I'm I'm looking at Josh, currently because I think you have opinions, and I'm not sure if you would agree with this.
Sam 00:19:55 And.
Josh Suereth 00:19:56 So. So my my opinion is,
I think I think you're right that we can do this without specification. Put it non-normative. Take out the maze.
I would still like to see a canonical way to do this in open telemetry that's consistent across sdks, but I do think that that can be a that's like a side task, you know, like writing down what you want and how people do this can be. Step one step, 2 can be figuring out how to make sure this is consistent. But, like Lydmila to the point of like context, propagation for SQL. Commenter, I still don't know how you write that thing
unless you know that service name is in context today.
And there, since there's no specification on, like what is in context
across things like, I don't think you can actually write a propagator today.
Sam 00:20:46 In our spec.
Josh Suereth 00:20:48 That uses it. You could write a propagator that only does trace Id, and you'd be fine
in the spec. But you could not write one that includes service, name.
Liudmila Molkova 00:20:58 Sam, do you have a prototype for this.
Sam 00:21:01 And no, but you, you just okay.
Josh Suereth 00:21:06 Sorry what I mean.
You can write one using only the specification you have to rely on contrip components.
That's the bit that I think is worth talking about in the specification meeting.
Sam 00:21:17 -
Liudmila Molkova 00:21:19 Yeah, I I think we're over over time on this one. Someone. I'm sorry. Could we maybe just scope this Pr down to the
the rest of this document.
and then we can keep talking about the service name and finding the reasonable way to move forward.
Sam 00:21:39 sure and.
Liudmila Molkova 00:21:41 Yeah.
Sam 00:21:42 And another little time it's just. There is another discussion about whether we should use the pretend or append. I feel like we we don't need to decide that in this. Pr, we can
like kind of skip this, because I feel like there's a lot of different opinion about this.
Liudmila Molkova 00:22:06 I I left the comment that I I think that we leave the freedom to append or pretend it does.
It's not. Is it necessary to give freedom? If you just say, Okay, it's always a pen. I don't care a pen to pretend.
But if you say something definitive, then the chances are everybody would implement it in a consistent manner. If we leave a freedom they will implement it in different ways.
Sam 00:22:31 Yeah, the.
It's just like 2 master have their phone comes. I already don't know.
Liudmila Molkova 00:22:41 Can you just pick one, whatever it is?
And if it turns out to be the wrong choice, we can always revisit this.
Sam 00:22:50 Okay, okay, thank you. I have no other questions.
Liudmila Molkova 00:22:58 Yeah, thank you. Sorry. It's taking a bit and thank you for working through the feedback.
Sam 00:23:04 Okay.
Liudmila Molkova 00:23:07 Okay this one was left from the last meeting. Nick, are you in the call?
Nick Moore 00:23:13 Yes. How's it going.
Liudmila Molkova 00:23:16 Great do you want to present? Do you want to talk about it?
Nick Moore 00:23:19 If you just want to open that link, it should be enough context here. So this is about the the security addition, so adding security
components to to the
to the open telemetry, semantics, conventions. And so I was looking over the vulnerability one recently. And
I noticed that actually, there are a number of the parts of the spec which are actually quite tied to a particular version of Cvss. Cvss. Is a standardized way of sharing information about vulnerabilities. And it was tied quite clearly to Cvs
3, which is now actually updated. Everyone's not. Everyone has updated. Lots of people still use. Cvs. 3 Cvss. 3. But Cvss. 4. Was released released 2 years ago. Now, and changed some of the naming conventions and things like that. And there's a kind of question there about how closely do we want to tie to an old version of standard?
Should it be something that's specified, kind of generically kind of, can you have just a high, level kind of vulnerability, scoring object that has custom attributes based on whichever scoring approach you want to use.
or something different completely. I don't know.
Trask Stalnaker 00:24:43 Alexandra, do you wanna.
Alexandra Konrad @Elastic Security 00:24:44 Yeah. So 1st of all, this. This was a part of our donation of the Ecs elastic common schema to open telemetry and like this was
this vulnerability component has been created back then. So that's why it doesn't cover like the latest change in this version of vulnerability. Standard.
We, if you, if you have looked into the comments there we have discussed
how to cover not only Cvss. But also other standards that.
Nick Moore 00:25:31 Yes.
Alexandra Konrad @Elastic Security 00:25:32 So that we are not picking only one standard of particular version, etc, so that you could describe which standard you want to use. And how you what data belongs to the standard. But this is in about this particular pull request. And if
have seen, it's now in in kind of frozen state. Because we had some time ago another meeting together with Ocs
team to
maybe work together on this. And there was a new group created inside the Ocs community which is not quite active, as I would like them to be. And I also like it's good that you raised this
pr again. Maybe I should just let's say, continue on introducing this particular vulnerability namespace in a, let's say.
update, yeah. Updating into the Ocsf standard, because I I think it might take some like quite a while until we have anything from the ocs group. But this is probably yeah, more question to Josh or Trask. So that let's say, we could proceed within the semantic convention. But I could look into vulnerability component and make it as close as possible to the Ocs.
Trask Stalnaker 00:27:23 Have you? Have there been? I'm sorry I haven't been following. Have we? Kind of kicked off work with the Ocs community?
Alexandra Konrad @Elastic Security 00:27:34 There. There was one meeting. Guy was there where? We just discussed that
we might work together on it, and they have created. a group in slack channel but there were like no other meetings, because, like those people, they want
probably to have more meetings not only with me, but with other folks from semantic convention like, including like you trust, or maybe Josh and decide, let's say the common course on how we proceed, because from what I understood, they want different things than we do, because they want still, just to use the
protocol and deliver Ocs over the protocol, but not updating the semantic conventions to to support security standard as well. So it's it's as I said, it's not active as I
would like it to be. Yeah. So that's why I thought, maybe I will.
not to break anything in the Ocs. If there will be any merge later, but make the vulnerability component as close as possible to the Ocs, because they are very close to be honest.
And this would probably solve a bit. This question, because, they have their way of
selecting the standard.
Trask Stalnaker 00:29:19 So you're thinking that we could
just basically go ahead and align our semantic convention security semantic conventions with the Ocsf
naming kind of treating that as the standard and just
Alexandra Konrad @Elastic Security 00:29:39 I think it's it's just about this particular component, this particular namespace.
Because we need any way to like to check it one by one. Yeah. So it's not like we just take everything and adopt it. But with vulnerability it is possible, because they are
pretty close. Let me send the link.
Trask Stalnaker 00:30:14 Yeah, I mean I that would
I. I would support that if we can take
if we think it's close enough to just
bring the, you know. Treat the Ocsf vulnerability
as the standard, and just see snap to that.
Alexandra Konrad @Elastic Security 00:30:36 Yeah, I think we can adopt
or like merge it, and I can send it here in the chat. So we
like they have more fields there as we do, but some of them are like similar
from what we have in the Ecs. Or what we could add to the open telemetry.
Trask Stalnaker 00:31:03 Nick part of the issue we've had with
the vulnerability. The security domain here in open telemetry is we just haven't had traction of sort of domain expertise to have staff, a group to do that and develop that
and so that's sort of where
we had some discussions with the Ocs folks. I think our preference would be to lean on that group as the domain experts.
And just pull either.
Yeah, if they're not interested in doing semantic conventions like defining these things in our semantic convention format.
That's
okay. We were. We were kind of hoping that they might take a more active role in that
but if not, if we can
just kind of treat that as the
domain expertise than the standard. And just basically say, our semantic conventions are modeling the Ocs domain.
Nick Moore 00:32:25 I think that would be a good place for us to be, I think. Yeah.
I had also noticed it wasn't progressing very quickly. I guess. Yeah.
they would seem. I'm just filling in a slack request now to join the Ocsf group. So yeah,
you're happy to participate either way. Really.
Alexandra Konrad @Elastic Security 00:32:47 I can add you to the Ossl group as well.
You can find me there because oh, you can find the group about
it's called hotel collaboration. So
yeah, you can join there. But again, it's not very active in the way that we need it. Semantic convention. So that's why I saw that. I might just go along and try to adapt or merge this particular. Let's say namespace with Ocs Namespace. And
yeah, proceed with it.
Liudmila Molkova 00:33:36 Yo.
it would be wonderful if we can develop a principle if we just say, Okay, we we represent one
thing from all Csf. And semantic conventions. It's awesome. But I think we need to have a principle on how we do this, because there are things that are
very similar.
But then we we need to say, Okay, do we flatten what those Csf says? Or do we record it as the whole object which we can do now.
I think we kind of need to figure out how we do this in general, and then, if we
adopt vulnerability, are, we should establish how we adopt other things.
That that's the only thought that I have on the topic.
Alexandra Konrad @Elastic Security 00:34:26 This could be a starting point where I could, let's say, invite people from that group to collaborate within the semantic convention on this particular topic.
And maybe then there will be some yeah.
more more life in that group. We could proceed from that point, make sure that.
Liudmila Molkova 00:34:47 Okay, yeah. Sounds good.
cool. So moving on to the next topic, I think it will be short there. Apparently I have some issues on up in telemetry. I/O, because of the of us using
HTML links to Markdown files.
Still, I need to understand what is the problem, but somehow, what we have in entities.
an entity is problematic.
Let's open it up
entities.
Yep, okay. So this table creates some problems on up and telemetry. I/O,
apparently because of the combination of
HTML tables and HTML links, or just HTML links. Not sure we need to find a way to rework it. But unfortunately, Josh has left. I think he had some reasons to create this table this way.
just probably because he wants to render
things in a certain way.
It might mean that we cannot use rich HTML features in this file or anywhere else.
Anyway, it's somebody. It seems somebody needs to dive into this and figure it out, and this will be the
something that we need to fix by the next release, so that up on telemetry I/O
can be fixed.
I wanted to raise awareness. I cannot jump on it this week. I'll see what they can do next week, but if anybody.
Trask Stalnaker 00:37:02 You can assign it to me. I I won't be able to look at it this week, either, but I can work on it next week.
Liudmila Molkova 00:37:08 Okay, sounds good.
Thank you.
It's actually my fault. Because the Ivan we were releasing I noticed that
the open telemetry I/O check fails, but it made no sense to me. So I said, said, Okay, I don't care. We are releasing, anyway.
Okay, send task.
Trask Stalnaker 00:37:38 Oh, I I good. I got the assign. Yeah.
Liudmila Molkova 00:37:45 Okay, thank you.
Let's move on to the next topic. James, do you want to present about the namespace?
James Thompson 00:37:55 I will see if I can let me try screen.
Say, can you? What can you see?
Okay. So what we've got here
is following last week's discussion about the namespace
and how we can document things.
Okay? And following the discussion we've had in a couple of issues, I've just gone through
and put together a sketch of what it could look like.
Liudmila Molkova 00:38:42 A quick, quick note. We didn't have a discussion on namespace. We had a discussion on events registry.
James Thompson 00:38:48 We last week we discussed having a general page to show events, and all the different signals is what we spoke about last week.
Liudmila Molkova 00:38:56 Wonderful. So maybe we can start a bit earlier, and you can guide us into how you see this.
James Thompson 00:39:02 Yep, yep. So what? So what I'm think thinking is currently, if you go to the page, there's a couple of pages that you look at. So you go, Jen AI, you have a page now for your events. You have a separate page for your metrics. You have a separate page for your spans. Right? What the idea here is we move to a single registry right? Which is what I'm referring to this in the Namespace Registry.
which is grouped based on the namespace. All right. So, for example, Gen. AI,
right, when you open that page, you are greeted to a page like this one here.
where you see what what namespace you're looking at. You have a summary of the namespace. You have your header or
another message at the top to describe. You need to follow this migration strategy
as well as a general description.
Right? So that becomes your header. Right for the name, please, and underneath that
you have some tables showing you everything that's available in that namespace, be it attributes, entities, events.
The metrics spans
right? So you have all these tables here showing you what's available as part of Gen. AI, for example.
right? And then what you can do is if you click on something, you are then taken to the page that's describing
what you've selected. So here I'm having a look at one of the entities. I can see the details of it, and I can see what attributes there are.
Okay. Alternatively, a, we can do the same approach here
for metrics. So you can go to the metric. You can see the details of the metric, and you can see all the attributes, etc.
So the idea is, we're bringing things together to have a single namespace where you can go to see everything that's in the namespace.
Liudmila Molkova 00:40:57 Essentially, it's the readme page, but it lists all the definitions.
James Thompson 00:41:03 It's it's a readme page for the for that namespace.
Liudmila Molkova 00:41:09 Yeah. So like, if you look into the Gen. AI page, there is a readme, and it it has links to the other documents.
James Thompson 00:41:18 Yep, right? And actually lists out what metrics you have available, what events you have available, etc.
Liudmila Molkova 00:41:28 So the proposal here is to refact their readme pages and automate their generation.
James Thompson 00:41:36 Yes.
Liudmila Molkova 00:41:38 And it's not the proposal to put everything into their registry or change the content of existing documents.
James Thompson 00:41:47 It comes down to how we, where we put
do we have the have the namespaces in the registry, so have your registry as your 100 auto generated documentation
right? Because what we discussed last week is moving the events to being generated as part of the registry
alright, and seeing what the gaps were right.
So for me, it makes sense. If you go to the registry and you click namespaces, and you can see what namespaces are available.
Liudmila Molkova 00:42:24 The the thing is that oh, if you look into most of our namespaces, they only have attributes, and they will never have any other signals.
James Thompson 00:42:35 Yep, then we just don't show the entities blocks. We don't show them that can be managed
so that way if you go. So the rather than having ideally, rather than having a separate entity registry for attributes, and a separate one for namespaces or entities. You have one registry called namespaces, and then you can select it, and then you can see what's in there.
Liudmila Molkova 00:43:06 It would be nice to kind of see the how it works in the real life
if we can generate something, but also
I'm curious about all the details. So if you show, let's say that Jenny has span called Foo
when you click on the spam folder. Does it bring you.
How do we solve the coherence? Like today? We have a document that describes Http spans. Less than half of it is auto generated.
and taking the definitions away from it doesn't make sense.
But having a link from this document to the actual definitions in the semi-handwritten file makes sense to me.
James Thompson 00:43:53 Alright. So I think that more ties into what I didn't touch on was, how can we describe
the these implementations should be implementing these events, these spans right?
And that's where
I've I've sketched here. You, you have a package, right? So this is where you can specify. These events must be implemented. These metrics are implemented this span. So that way, you could see, okay for Gen. AI. I have
my clients. But client package right?
Or my tool package, for example. Okay, what do I have? Okay, these events will be produced and they span will
be produced all right.
And then you can also see that. So that's already documented in the example.
The other thing I've done is to further address the feedback from you is this file here? So this is an implementation page.
Alright.
So you can see this is very similar to what you have now.
So you can see what it is, the implementation and what events, what metrics, what spans.
So that's also there as well.
And then you can also click on it and see the connection.
Liudmila Molkova 00:45:21 I kind of feel we're going in some directions that it. They're very far from where we are today, and it's hard to have any opinion on this. It sounds like there's a lot to to discuss. So my 1st reaction is that let's try to template this readme page, and let's see where we go without introducing any new concepts.
James Thompson 00:45:44 What's so? Isn't that what we have here already? All right.
Liudmila Molkova 00:45:50 It's very hard to tell, because it.
Trask Stalnaker 00:45:56 Are you able to? render like, show what it really will look like?
Right? We're seeing it with all these templated
parameters, so it's hard to sort of visualize. I'm having a hard time visualizing it.
James Thompson 00:46:15 Yeah.
But yeah, so I can certainly put in alright. I can migrate one
one area, for example, if one
all right, and because and replace the custom. Attribute types.
I can. That can be done. But the idea is
having a single spot you can go to and see what attributes are in that namespace, what entities, what events, etc. What metrics! And then clicking on that, and seeing the details of what you've just selected.
Liudmila Molkova 00:46:48 So if we scope it down to this, and let's say, try on Http.
James Thompson 00:46:52 Yeah.
okay, like won't.
I'll bring across 1 1 of the metrics examples so effectively, I'll just fill in these pages. But
bringing across 1 1 attribute, but filling the table of attributes, for example, is what you're saying.
Liudmila Molkova 00:47:18 Alright, so.
James Thompson 00:47:21 All right, so effectively you'd have a list of this table here would list all the attributes, and then you click on the attribute, and it takes you to the same attribute definition just
to save the time of manually copying across.
Liudmila Molkova 00:47:37 I I'm not sure I I don't know what the the vision you have, so I I don't know what is the best approach
James Thompson 00:47:46 The the vision is, you can go to the website. You go to the registry and and see, okay, what's in my Gen. AI namespace.
Trask Stalnaker 00:47:56 It. Would you be able to do like a a you know, just a mock up
that we can select?
I see your vision like I. I like your. I like
the idea of your vision, like I like, you know, putting effort into the docs and organizing it better. But I I think if you're asking for you know, opinions on this on specific
proposal.
Having, you know, like a wireframe, a mock up of what the website would look like
would be really helpful for for me.
James Thompson 00:48:38 I'm just trying to think of the best way to do that. All right. Kids
like the website structure wouldn't change. It's just the pages on the side is all that would change
right.
Liudmila Molkova 00:48:58 Yeah, you can just put the mock up on the report. Okay, go ahead. Trust? Sorry.
Trask Stalnaker 00:49:03 Just taking ht, I mean that that helps even just to understand. So there'd be no change to the table of contents on the website.
And so the change would. So maybe just
mock out Http, as Linla suggested, to show, you know what it would look like.
so we can get a feel for that.
James Thompson 00:49:31 Yep.
Liudmila Molkova 00:49:33 I'd like to call time on this. We have a few more items on the agenda.
Let's
great. Thank you, Alexandra. Do you want to talk about it? Or do you just want asking for reviews?
Alexandra Konrad @Elastic Security 00:49:55 Yeah. I just ask him mainly for reviews, because we have discussed that. We proceed as this. I finished it until let's say the end. And we just need. Yeah, I just need more reviews there from
stakeholders. And Peter.
Liudmila Molkova 00:50:13 This is like literally the same thing. It's just in Yaml.
No changes.
Alexandra Konrad @Elastic Security 00:50:19 I think there there is like no major changes. There are some small like rewarding, etc, but there should be no changes. Yes.
Liudmila Molkova 00:50:29 I mean from the naming, from something that would show.
Alexandra Konrad @Elastic Security 00:50:33 Yeah, things things that we discussed like, dot value against just just a name like I haven't changed it. So it means that my second Pr, for example, which checks if we have metrics with this namespace in issue, this would fail on when this pull request will be merged.
So that's why I haven't changed anything there. If you want to change it later, let's do this. And most of the requests that were discussed within. Like in comments, we have deferred it to further pull requests until this one would be integrated in our system.
Liudmila Molkova 00:51:18 okay, sounds good. I, I started looking. But I got scared of the amount of changes I didn't realize, how many there are. But thank you.
Alexandra Konrad @Elastic Security 00:51:29 Yeah, I think
most of like most of the changes are in the Yaml file, because Md file are mostly auto generated.
yeah, only a few boarding CAD about particular metrics, but all tables are auto generated.
Liudmila Molkova 00:51:52 Okay, sounds good.
I'll take a look. Thank you.
Okay, James. Which one is this.
James Thompson 00:52:06 Or or Braden can go first, st because I'm just mindful of the time.
and we can push this to next week.
Liudmila Molkova 00:52:17 Okay, thank you. Brayden. Do you want to talk about the last one.
Braydon Kains 00:52:20 Yeah. So the the scenario that I want to ask about is we got a metric
that is like, maybe she could like, I mean. This is a metric that is still theoretical, but like in a scenario where this is a metric that would be shared across different conventions. So we have
these conventions for nfs, and there would be some attribute like network protocol name
if I want and and like, if if the protocol name was Nfs, then we'd want
different, like semantics, or like like explaining how it works differently, or how it's instrumented on nfs. I don't know how to make that work, because the current way is proposed in the Pr. Is that the things are in the Nfs namespace, and that's all the things related to the semantics of how they're instrumented. All those descriptions, all the schema for what you would expect for nfs. Metrics are all
in this namespace. But if we're going to start unifying them across storage and only differentiating nfs from something else based on an attribute value. I no longer understand how you would
document and validate schemas and things like that.
Liudmila Molkova 00:53:37 Can you give an example of what would be difficult.
Braydon Kains 00:53:41 I'm just not up to the 2 year speed.
So the the linked comment is an example, because
that is a fine. That's fine, for like the final usage pattern. But like how we actually document that is unclear like we wouldn't have
a spot for like
when it's nfs. And the value is this, this is how you do things versus when the value is this. This is how you do things.
Trask Stalnaker 00:54:11 In the past. We I mean, I feel like we have examples of this where we just put it in the
notes.
But I mean that to your I think your point is, how do you? Then automatically, you're worried about automatic verify validation.
Braydon Kains 00:54:30 I mean, there's yeah, there's no, there's no verification in that case. And also like, if if it goes in the notes of the original definition spot. Then suddenly network.protocol.name has a bunch of or like.
maybe it's sorry. The store, the the metric, the storage volume operation count suddenly has a bunch of like cluttered like this is what it is when it's nfs. This is what it is when it's xyz other things. What it is when it's
whatever like the like that would get cluttered in that spot. And there is now and now, all of a sudden, if there's no it like. If all of the Nfs metrics are shared. Where do we document like this is how you use. And this is what Nfs metrics are
like. We can't. There isn't a way for us in the current tooling to say the Nfs metrics are these metrics when the values are for this.
when the attribute of said value is this.
because currently it's organized as a namespace. All the Nfs stuff is under the Nfs namespace. Now, it's going to be shared across storage or Rpc. Or whatever, and differentiated by an attribute value. And all of a sudden we lose our way of documenting nfs. Specific stuff.
Liudmila Molkova 00:55:43 So you're right. There is no way to do it today, and the notes would probably be the best
and best of your friends
the future that you can outbuilding. Is that 1st there is a work item, and I think somebody Jeremy on who works on weaver is looking into this and how we can say, Okay, let's let's take. Or maybe Alexandra is working on it. How we can take.
When you say this only applies to the specific value, like a limit in enum
types. For the instance of.
let's say, metric or span, it does not solve your problem. What might solve it is that you have a base metric definition, and then you kind of reference this metric and slightly refactor, its description
or additional properties, and then you can render those metrics separately, like 2 different
tables, and then you can narrow down the original metric definition to your use case.
That's what we do for database spans because we can
right? So there is a base database span. It looks like this. And there is, let's say,
radius database span that looks slightly different.
They are compatible, but they are not the same
metric referencing is something that we are looking into
into in in weaver in tooling group.
It's not something that materializes tomorrow.
The
approach that we've been following in some other places. Let's pick.net is ugly, and you will hate it.
But I'm going to show it, anyway.
So this is a document that describesnet Http. Metrics.
and it covers Http. Server request duration.
It says, you know.
it follows that metric. And here are the freeform notes on how it slightly deviates from the original definition.
I wonder if so. Yeah.
I promise you're going to hate it when you do.
Braydon Kains 00:58:18 If if I was the one who wrote the Nfs. Pr. I wouldn't care, because I would just redo it. But this is someone like a coworker of mine who I guided through getting this whole pr written with nfs stuff. And now, all of a sudden, I'm going to say.
actually, all of these are going to be Rpc. In storage, and you have to rewrite this as a handwritten document like that really sucks.
Liudmila Molkova 00:58:41 Yeah.
James Thompson 00:58:43 But but I think a good example is if you scroll up right, you can see into the client metrics. So that's pulling in the the automatic automatically generated tables
alright and just above the automatic tables. It has the additional information.
alright, all right. So between the title and there you can put your notes in
alright, so the rest is.
Braydon Kains 00:59:09 Well, no, that that's it's okay. It's like, I.
I know that some of it is automatic. It's just the whole thing has to be Redone now is all.
And and like we're we're blocking a bunch of work on getting that pr merge. And all of a sudden I'm gonna upend the whole thing.
Liudmila Molkova 00:59:24 Do you have to? You can still like, describe the variations and flavors inside notes.
Good year.
Braydon Kains 00:59:35 Well, well, I mean the the Pr. Right now is a bunch of new yaml files and new generated documents.
and instead, it's going to be. We're just going to rewrite in a yaml. I'm sorry. A markdown document to pull from standard definitions and put it like it's it is a rewrite of the whole Pr.
Liudmila Molkova 00:59:55 Is there some.
I think, like we, we can do better in the short term, like one suggestion I would have is to help us drive the tooling, but it will be even more work.
Braydon Kains 01:00:09 It's.
Trask Stalnaker 01:00:11 Yeah, I mean, that would be one thought Brayden is if oh, but you said it's blocking other things because I was gonna say, like, you know, we could just put this on
hold and for a while, until the tooling catches up.
Yeah, there isn't.
They're rewriting.
Braydon Kains 01:00:34 I don't know if there is
a solution to this other than
like, probably what I'm going to do is I'm going to rewrite because I feel bad making him do this whole thing. And now the whole thing's like, I'm I'm just gonna tell him, like.
sorry, too bad it doesn't work anymore.
And so whatever I'm complaining, I'll do it. It's fine. It just sucks.
Bertrand (MetricsHub) 01:00:58 Or we just mentioned the pull request and then change it afterwards. So it seems like a success, and then an evolution right.
Braydon Kains 01:01:07 But there's also. Then the host metrics receiver is going to merge this. And then the host metrics receiver is entirely going to change everything that it's doing, so we might as well do it right the 1st time. I I would prefer to just merge the thing.
Excellent
I also, but I'm also of the opinion that the unification is barely worth it like this has been going with like nfs and raid conventions.
anyway. Sorry we're out of time. It's fine.
Bertrand (MetricsHub) 01:01:35 So. By the way, I have a question. Why do we.
Liudmila Molkova 01:01:38 Sorry we we are out of time. We have to drop now, so you can post in the semantic conventions chat. Here.
Yeah, thank you.
Have a good day.
