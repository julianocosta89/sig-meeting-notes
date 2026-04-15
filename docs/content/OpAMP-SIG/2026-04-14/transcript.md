SIG: OpAMP SIG
Date: 2026-04-14
Duration: 52 minutes
============================================================

## Zoom Recording Transcript

**Tigran Najaryan** 00:20 Hi, Andy, how are you?
**Andy Keller** 00:26 I'm great, how are you?
**Tigran Najaryan** 00:29 I'm good.
**Andy Keller** 00:34 I just responded to your PR, I'm sorry it took so long, I had… PTO.
**Tigran Najaryan** 00:38 Yes, I saw that, thank you.
I'm actually… I wanted to maybe chat a bit about it, because I'm… I'm having second thoughts here.
I don't think what I'm suggesting… is, this is the right approach. The problem is that essentially, I'm saying here the capabilities can't change arbitrarily.
Trying to maybe have some sort of control over what the state changes can look like in the implementations.
**Andy Keller** 01:11 Yep.
**Tigran Najaryan** 01:12 The problem is that I don't think… It really works.
it creates an illusion of a control. I think the reality is going to be that, especially with HTTP transport.
From request to request, The server, at least, has no way of Knowing that… The client was not… Update it, for example, upgraded to a newer version between the requests, right?
And… I don't think we can prohibit the client Hey guys, I don't think we can prohibit the client from changing its declared set of capabilities between versions.
So, let's say I'm an OPAMP client, I'm implementing a particular subset of capabilities in version 1, then… the software is modified, now it's version 2, and it implements other, more capabilities, right? Or removes some capabilities even, right?
**Andy Keller** 02:15 Yeah.
**Tigran Najaryan** 02:16 And those… I mean, they, they, like, the upgrades can happen, like, I'm sending a request, an open request, then… immediately the client is upgraded, the next request comes with a completely different set of capabilities. It is a reality, like, there's… I don't see a way to prevent that, to be honest.
as much as I would like to constrain, have some.
**Andy Keller** 02:39 Yeah, no, I think the HTT case… You raise a… you raise a good point.
**Tigran Najaryan** 02:45 With a WebSocket, at least there is some control, like, there has to be some sort of disconnection probably happening for you to do an upgrade, but for plain HTTP, like, there's no way. You have to be prepared for that to happen.
**Andy Keller** 02:59 Yeah.
**Tigran Najaryan** 03:00 And so, if you have to be prepared for that, I don't see how… Prescribing it in the specification is going to change that, to be honest.
**Andy Keller** 03:09 Yeah, I… I mean, my first instinct was actually that… this was a limitation of the AppAmp Go implementation that we were… Codifying in the spec?
**Tigran Najaryan** 03:21 Yes, it's more like that in my mind. It's probably a limitation of the particular implementation, where we simply haven't tested for all the possible combinations of capability changes in the middle of an exchange.
And we just don't know if it works at all, right? Which is fine, an implementation can have some limitations. We can even enforce those limitations explicitly, like we have in Opamco implementation.
**Andy Keller** 03:51 Right, right.
**Tigran Najaryan** 03:52 But I don't think it belongs to the spec.
**Andy Keller** 03:56 Yeah.
**Tigran Najaryan** 03:58 That's what I'm seeing at the moment. Like, I've been thinking about it, trying to figure out why. It felt a bit weird to me, so I think… Maybe… maybe let's… let's… Think it through, but it seems to me we should maybe get rid of that in the spec.
but still have it in the goal implementation, or any of the implementations. It's okay to have that.
particularly, I'm not too worried about enforcing some limitations in the implementations, because There's no need to have that sort of fluidity in the capabilities.
if you change the capabilities, it's likely going to be a result of a restart or something like that. There's no need for a dynamic change like that. The only use case that we're aware of is what Jacob needed for for the particular… for the particular scenario in the operator, that's fine. If those come up, we can… remove some of the existing limitations in the implementation, nothing wrong with that.
**Andy Keller** 05:02 Yeah.
Just to catch one up, sorry, we… Tina and I started talking before everybody joined, and… Tegan had a PR, it's been open in the spec for a little bit. I owed him feedback.
As a… as we were discussing.
My feedback was pretty minor, but, Yeah, there you go, it actually is the first… okay, perfect.
It is the first agenda item, we just got started.
Before I finish pretty point, you know, I think my… I guess the question is, you know, we're trying to drive toward 1.0, on all these different components, do… do we feel like… if… there's limitations in the OpAmp Go implementation about something like… Agents changing their capabilities.
that that, therefore, precludes the OpAmp Go from Like, is completeness a requirement for 1.0?
**Tigran Najaryan** 06:23 Yes, yeah.
I think it doesn't.
Because the spec doesn't… let's say we don't measure this PR. In that case, the spec doesn't have an opinion about whether the capabilities can change or no.
call it unspecified, right? So you can go either way in your implementation. But then in the implementation, I think it's okay to have some limitations that you can later remove.
So, nothing breaks, really, you're just expanding your use cases. If we feel the need that it needs to be specified in the spec so that different implementations behave similarly, or there is a need to do that because of interoperability reasons between the client or the server.
it needs to be an amendment to the spec in that case, right? But I don't feel like that in the situation where the spec has no opinion, and the implementation has limitations, that's somehow a problem. I might not think that's okay. Especially because, practically.
we don't have that problem. I look at least at the supervisor implementation, and it doesn't do anything like that. The supervisor is… pretty static in the set of capabilities. It is, it is enabling.
So, in practice, I don't think it's going to result in a problem of any sort.
I'll give it a bit more thought, maybe, and… but I would also very much like other opinions on this one.
I'm… I'm not entirely sure what is the right way. I'm inclined now more towards not changing the spec and just Can be some sort of supplementary guidelines which say that implementations can do this or that, have this sort of limitation, or anything like that, maybe.
Okay, I guess for the sake of time, unless someone else has… Thoughts on the topic?
**Evan Bradley** 08:36 I just have a question. What's the motivation for restricting the capabilities that can be updated?
**Tigran Najaryan** 08:43 The motivation was that Without understanding the consequences of allowing unlimited changes in the capabilities dynamically.
it would not be possible to know in what state the implementation would end up. Let's say in the middle of a sequence, right? So let's say the client and the server are exchanging messages that are prescribed.
as part of a particular sequence, let's say remote config update. So the server sends remote config offer, the client applies, then sends back the status update that it is applied, right? Something like that, or a package update. There is a prescribed sequence that that only is meaningful if the particular capability is enabled on the client side, or on the server side. Now, imagine in the middle of that exchange, the client changes its mind, and says, no, I don't support that capability.
You may end up in some unexpected state in the implementation of both the client or off the server, because now the message that was supposed to be delivered is not delivered, that the capability has changed.
or the client is in some sort of weird state now, we have never tested for that. That's the problem I have, in particular with the implementations. I don't know what will happen if that… that is actually enacted at runtime. Now, it's possible to do that. You can Call set capabilities anytime in the client.
Including when it's in the middle of an exchange, and what will happen, I just don't know, right? So we would… Potentially, at the very least, would have to test for those situations to see what we end up with. Is it causing trouble? Is it okay? I just don't know, right? So, out of, I guess, to be careful.
I thought that it would be good to just have a limitation of what is allowed, and what is allowed we would explicitly test for.
And everything else we would prohibit.
But now I'm… I'm not so sure that it's a very good idea anymore.
Precisely because we don't necessarily have control over what can happen, especially with playing HTTP requests.
The spec can say that you can't change capabilities, but… The server at least still needs to be able to… to deal with that situation, because the client can be upgraded to a newer version that supports a different set of capabilities. So there's no way to enforce this, in my mind.
No matter what the spec says.
We can have an enforcement in the implementation, that's fine, but when it's in the spec, somehow there is an expectation that you… You can enforce it in the protocol that the peer is behaving in a particular way, from the server's perspective.
Which is not the case, you just can't do that. There's no way.
**Evan Bradley** 11:50 Yeah, I see the concern.
**Tigran Najaryan** 11:52 Sorry, I didn't mean to stop that.
Okay, maybe if you guys have any thoughts, comment on it, I don't want to use all the time, let's maybe move to the next one.
I think I also have the second one, it's about the… guidelines for the SDKs, so… A few folks here at Splunk have been working on adding the ability to do the configuration of SDKs using GoPump.
We have been discussing this as a possible option for a long time. Seems like there's now an appetite for multiple language implementations to adopt it, and so this doc essentially brings some sort of guidelines on how to apply OPAMP, or how to use OPAMP for OpenLeentry SDKs, how you're supposed to do that, what the What the identifying attributes are supposed to be when you're using I'll pump.
with, OpenTeLentry SDKs.
Take a look at it. We have… multiple languages?
I think, already, trying to implement this, I think Java.NET, there's one more, I think.
So, we do have maintainers from the languages, but… It wouldn't hurt to have more eyes on this.
For now, it's basically about what do you want to put in the identifying attributes, and… Well, we have a section about that… about the collector in the spec. I think that also needs to move out of the protocol specification into this additional guidelines for the… specifically on how to apply OPAMP to open planetary components, to SDKs and collectors. Once this piece is accepted, I can also file another PR to just move that from the spec document into this document.
**Andy Keller** 14:06 Degran, I… I wasn't sure about… I know there's some… already some conversation here about, identify… identifying versus non-identifying, and the new entity concept.
I guess it… My initial reaction… To the non-identifying section, was… you know, just… but didn't… it caught me off guard a little bit, it wasn't what I expected.
**Tigran Najaryan** 14:35 In this document, in this PR, you mean?
**Andy Keller** 14:38 Yes.
**Tigran Najaryan** 14:39 Doing what?
**Andy Keller** 14:39 Language certification agents should leave this empty?
**Tigran Najaryan** 14:43 The reason for that is because there is nothing else remaining, because we're saying everything that is in the resource, you put it.
**Andy Keller** 14:51 Yeah, I guess, right, so… so why should… why… What is the thinking for putting everything and identifying?
**Tigran Najaryan** 15:01 The thinking is that you need to have something that uniquely identifies the SDK, In theory, it could be a subset of resource attributes, but there is no way to know which subset to use.
And so we're saying, to be safe, you just use everything.
**Andy Keller** 15:18 Okay.
**Tigran Najaryan** 15:19 thinking here, basically. If we had the entities, we would say that you use the the union of the identifying attributes of all the entities. That… in theory, would be sufficient. But because we don't have the entity, that's what we're doing here.
**Andy Keller** 15:36 Okay, that makes sense.
Yeah.
**Tigran Najaryan** 15:40 I don't know if there is a… there is a way to… Future-proof this… somehow.
So that we don't have to… I mean, if we later decide that doing what I described with entities is the right approach.
If we change to that, That would be a breaking change.
Because you would… Now have fewer attributes in the… in the identifying attributes.
So… That closes that door, in particular, right?
**Andy Keller** 16:14 Right.
**Tigran Najaryan** 16:15 I don't know if there is a good way to avoid closing that door?
Yeah, it's kind of an unfortunate situation.
**Andy Keller** 16:21 Because I think it was smart in OpAmp to separate these things.
Even though they weren't separated.
Upstream in the hotel.
**Tigran Najaryan** 16:31 Yeah, yeah. And it matches very well the concepts that we have in the entities. It's exactly conceptually, the same thing. So if we had the entities, it would be a no-brainer. We would just use exactly that here. Unfortunately, we don't, so… I don't know if we have much options here.
Is there… is there a way we can phrase this in a way that says… Once the entities are there.
Could we phrase this to use the… use the… only the identifying attributes from the resource?
And then, because there's no way to know which ones are not.
You just include everything in the implementation, but once you have a way.
It's still kind of… it's going to be, in practice, a breaking change if we do that.
I don't know if there is a good way to read it here.
Okay.
**Andy Keller** 17:33 Yeah, I'm fine with it. I agree that there's not a good solution.
**Tigran Najaryan** 17:42 Alright, yeah.
Let's move forward.
Michael, you have the next one.
**Michel Laterman** 17:48 Yeah, so… This is more of a question to the group, if… There's… Any other interest in getting extension support in the supervisor?
Or what a good starting point for that is, because I saw this as an open issue, and that elastic we're interested in.
Building out support specifically to you know, storage extensions, auth extensions, and… Such, and we'd be willing to sponsor work for that, and get me or other… me or one of my colleagues to start working on this.
I know that this was called out as something not in scope for 1.0, but, We have wide security use cases that… Need some things which would be easiest to… Put in through extensions for both the supervisor and collectors.
**Andy Keller** 18:47 Yeah, it's… there's a certain irony here in that… Dakota and I talked about putting this on the agenda, and then saw that you had already put it on the agenda, but, It's also really important to us, And, we were considering doing the effort as well, so… I don't know… What your timeline is, or when you… When you'd hope to do this, but we definitely… Are eager to… To tackle this, and Could help, or could… take it, or could just, you know, review and help test your implementation?
**Dakota Paasman** 19:35 Yeah, and… A little bit more context for our interest in it.
we're specifically interested in the auth extensions, like it was mentioned in that issue. And so we also have work that we need to do in the extension auth package as well.
She'll be focusing there, and then also… how you actually use these extensions in the supervisor. It's another aspect of it that… We'll have to figure out a good… A good mechanism so that things like the storage extensions that you want to use are… usable as well.
**Tigran Najaryan** 20:14 Are the… are the extension implementations sufficiently decoupled from the collector codebase? I imagine they would be implementing these interfaces and the extension component interface, right? Which is probably fine.
I'd imagine there's nothing else they are coupled with in the collector codebase, so we could actually reuse them.
They're, they're separate, they're separate, modules as well, right?
If I look at the… for example, what do we have?
**Evan Bradley** 20:46 all separate modules. We'll need to re-implement our own host, but that won't be that much of a problem.
I… the biggest challenge I see with this is figuring out how to jam them into the op-amp client and the requests it makes.
Are we able to put middlewares into the HTTP connection that the client makes to the server?
**Dakota Paasman** 21:09 So… I think… not to… More generally, answer your question about, like, how this is done, So, a couple years ago, a former engineer was working on this, briefly, and at the time, there was initial buy-in from one of the maintainers of the extension auth module to add a new interface to the To the client, which would basically just generate WebSocket, or just generate headers for a WebSocket request, and then, once we generate those headers, at the time that we're instantiating the WebSocket client, we would just assign those and use those headers.
Which, there are some drawbacks with that, especially if those headers change over the lifetime of the WebSocket connection, which they did discuss at the time, but, it seemed to not be… big concern.
And that original issue.
**Evan Bradley** 22:08 per OI.
**Tigran Najaryan** 22:08 We would have to… sorry, we would have to somehow expose the round tripper in the open client, right?
**Dakota Paasman** 22:16 No.
**Tigran Najaryan** 22:17 And then… Oh. No.
**Dakota Paasman** 22:19 No, I would be adding, like, a new interface here, so it'd be, like, a WebSocket client interface that implements a… a header, or a function that generates headers for the WebSocket client.
That was the agreed-upon solution with the extension off.
maintainer.
**Tigran Najaryan** 22:38 So it needs changes to the extension implementation.
**Dakota Paasman** 22:41 Yeah.
**Tigran Najaryan** 22:41 Not just… There's no way we can use them as is without changing anything there.
Could we plug into the existing, like, little round tripper?
**Dakota Paasman** 22:51 There is a way.
So that was part of the initial discussion. Again, it's kind of tricky because this was an effort that's almost 2 years old at this point. So, at the time.
they implemented, a short-term solution that would use the round tripper. However, they identified that as not ideal, and so they said once the extension off module was stabilized, they'd like to go back and revisit adding a new Interface, which, at this point, that module is stabilized, so… That was… my thinking.
**Tigran Najaryan** 23:28 Yeah, the reason I'm suggesting that is because it means that we won't have to change anything in the extension implementations, it's just easier.
**Dakota Paasman** 23:35 Logistics.
**Tigran Najaryan** 23:36 Exactly, right? So we make changes on our end, and that's it.
**Dakota Paasman** 23:39 Yeah, no, that's, that's really…
**Andy Keller** 23:41 I do remember this conversation.
before, but I wasn't close enough to it to remember the details on why If the round tripper was just considered… Hacky, or if it was really.
**Dakota Paasman** 23:52 Yeah.
**Andy Keller** 23:53 If it's… You know, and that's… that's.
**Tigran Najaryan** 23:59 I just, I just, yeah, I just don't know whether we'll be able to convince every extension Owner here in the country to make changes to their extension, so that It can be consumed by.
the supervisor, or biopanko.
**Andy Keller** 24:18 I mean, if…
**Tigran Najaryan** 24:18 So it's a… it's a harder…
**Andy Keller** 24:20 I would like to avoid that.
that requirement. I think if we couldn't avoid it, you know, we can always test for that interface and only support extensions that have been updated to.
**Tigran Najaryan** 24:34 Sure, yeah, yeah.
**Andy Keller** 24:35 to include…
**Tigran Najaryan** 24:35 It still would be nice to support them all out of the box without any extra effort.
**Andy Keller** 24:39 Slavery, yeah.
**Tigran Najaryan** 24:41 Yeah.
I would try to do that first, and if that doesn't work, do what you're saying, test for the support of the.
**Michel Laterman** 24:49 Yo.
**Tigran Najaryan** 24:49 Whatever it is, the WebSocket version.
**Michel Laterman** 24:53 Is the open issue where you described… is there an open issue, or an… sorry, an old issue where you described Adding a new interface, because…
**Dakota Paasman** 25:04 I just… I just linked it in the chat.
**Michel Laterman** 25:06 How could…
**Andy Keller** 25:07 Why don't we just add it as a comment on this?
**Dakota Paasman** 25:09 Yeah, I'll do that too.
**Michel Laterman** 25:11 Yeah, cause… Not looking at that other issue right now, it seems like it would be pretty straightforward to ex… To add some way to specify Round-tripper support in… op-amp go instead of extending extensions.
**Tigran Najaryan** 25:33 Exactly. I'm willing to accept a bit more work for us at Old Pump, so that we can then benefit from the existing extensions.
Rather than… try to go and convince the extension authors that they need to change their extension. It may be just… Harder to do.
If there is a technical way for us to do it, from our side.
That would be my preference. I think it's just easier to do.
**Dakota Paasman** 26:05 Yeah.
**Tigran Najaryan** 26:05 the reason I'm saying. Not necessarily the best from technical perspective, but maybe just… Easier as… from a logistics perspective.
**Dakota Paasman** 26:16 Yeah, I… I do agree, it's definitely easier, and I… from all indications, it does seem like The concern with the round tripper was just it was considered hacky.
So if we're okay with that, and prefer that for, you know, time constraint, then… Yeah, that definitely…
**Andy Keller** 26:36 It sounds like there's… there's interest in doing this from… You know, all of us, so… We should probably… Put together a proposal for an implementation and figure out… What the solution should look like, and then… And then do it.
How do we want to… Proceed.
Who wants to take the lead?
**Tigran Najaryan** 27:03 Would this… would this be… would this be, essentially… Just for the supervisor, in practice, or… How are we seeing this?
Or maybe even for the opum extension in the collector, Or is it…
**Andy Keller** 27:18 extension already supported auth extensions.
**Dakota Paasman** 27:21 Yeah, it does already use the round tripper.
**Andy Keller** 27:26 Yes.
**Tigran Najaryan** 27:27 Say that again?
**Andy Keller** 27:28 The auth exten… the op-amp extension already… supports auth extensions.
**Tigran Najaryan** 27:33 It does?
**Andy Keller** 27:34 It's the supervisor itself that's missing support.
**Tigran Najaryan** 27:38 How is… how does that work? They are using the same old pumpko client, right?
**Dakota Paasman** 27:44 They're… they're using the round-tripper, approach, so before creating the client, it's, You can configure the op-amp extension with an auth extension that it references, and then it'll use the round-tripper method on it to generate headers and use those.
**Tigran Najaryan** 28:00 Okay, then I'm not sure I understand. Why does this exact same approach doesn't work for the supervisor?
**Dakota Paasman** 28:09 It's not that it doesn't, it's just that it wasn't implemented in the supervisor at that time, and then there's been so much time that's passed since then that, you know, that original agreement, or decision, I should say, that was made,
**Tigran Najaryan** 28:23 Okay.
**Dakota Paasman** 28:24 You know, let's up.
**Tigran Najaryan** 28:25 Seems like, since we have that in the extension, we just maybe copy the implementation?
Shouldn't be that hard.
**Dakota Paasman** 28:36 Yeah.
**Andy Keller** 28:36 I think it's a matter of understanding, if there's limitations to that implementation. You know, do we want to propagate those limitations to another implementation?
**Tigran Najaryan** 28:49 Yeah.
**Andy Keller** 28:50 And I don't… I don't have a good understanding of If there are limitations, or what those limitations are.
I would agree that if it's already implemented that way in the op-amp extension.
just implement it the same way in the supervisor, and we should be good.
Because they're both using the same client library, and Again, I'm not close enough to it to understand the nuance.
Right.
**Tigran Najaryan** 29:19 Evan, what do you think?
Would you be willing, interested?
**Evan Bradley** 29:25 Yeah. No, the… use… wrapping the round tripper like we're doing… I don't understand what the… the caveats are here, but that would be, like, my first way of doing this, just because it leaves the extensions alone. As far as copying things from the extension to the supervisor, I agree, I think that just makes the most sense. I mean, they're… I think from a user perspective, they're so tightly coupled that I feel like the… any… You know, caveats for one would apply to the other.
**Tigran Najaryan** 30:00 Yeah, and also using collector auth extensions in the collector supervisor feels just natural, right, for the users as well. The same configuration settings.
All the… the… the same set of… of… methods available. I think it just feels right to me, doing it that way.
**Evan Bradley** 30:22 Yes, I mean, at least for the foreseeable future, it's the supervisor just for the collector, so I think that reusing things from the collector and in the collector ecosystem makes sense. We've also talked about this for confident providers.
**Tigran Najaryan** 30:36 Yeah.
So, I guess what I'm hearing is… we think this is the right thing to do. It's a matter of… Who wants to take in?
I just do it.
**Dakota Paasman** 30:59 Yeah, I can, I guess, do we need a design doc, or do you think we're ready just to maybe outline this in an issue, but then start implementing?
**Evan Bradley** 31:10 I'd say… I really don't think it's gonna be that complex.
Like, it's just a matter of, you just have to make a host in the supervisor instantiate the extensions inside of that.
The problem is, though, that we could… we would have to include them out of the box. Yeah, maybe let's do it in an issue.
Because we don't have the collector's, like, plug-in model. We would need to say that, you know, the supervisor now ships with these extensions at this version, you know, with these, you know, you know, possible vulnerabilities and things like that.
**Tigran Najaryan** 31:46 Yeah, yeah. That would be my other concern, I guess. We're, we're… Adding some more blood to the supervisor. How many… how many do we want to bring there, really? And how do they… what sort of transitive dependencies they bring? That's… that's a lot of new stuff that we add to the supervisor.
Maybe we need to be a bit more selective in what we want to bring, and not bring everything at once.
**Evan Bradley** 32:09 Yes. Secondarily, do we, how do we feel about… this in relation to 1.0.
I guess I'm concerned if we keep… if we want to set a scope for 1.0, but we keep adding things, I feel like we're just never gonna… that's what is happening in the collector, we just… we never.
**Tigran Najaryan** 32:31 Yes, yes, yeah. I wouldn't make this… this definitely shouldn't be a prerequisite for 1.0 in my mind. And I don't think… adding this later is a problem. There's nothing that we would break if we bring this as capabilities. It's okay if someone probably wants to work on it, I definitely wouldn't make it A required thing to be done before 1.0.
**Evan Bradley** 32:56 So, my… my concern is more so, if we add this now, and then we say we want to go 1.0, how do we… Tell users what's 1.0 and what isn't.
**Andy Keller** 33:08 I mean, I…
**Tigran Najaryan** 33:09 Yeah.
**Andy Keller** 33:09 We… we need this to happen now.
like, in the next month, and that's gonna be before 1.0, so it's… it's gonna go into 1.0.
if we do this now, I think, is… So, I don't think it needs to be a requirement for 1.0, but I think realistically, given the timeframe.
of… the work that we need to do, and I think, It's gonna end up in 1.0.
**Tigran Najaryan** 33:39 So, I think then the question is that the extensions themselves may not be stable. So, if you're declaring the supervisor 1.0, But you're including some off-extensions which aren't stable themselves, then we have a problem, right?
That's… that's what… that's what you're concerned with, Evan, right?
**Evan Bradley** 33:57 Yes. Yes.
**Tigran Najaryan** 33:59 we would maybe would make a call about including only a small subset of extensions, which are stable. I don't know if there's any at the moment.
**Evan Bradley** 34:09 If there are stable extensions, I think that's… what do you call it? I think that would be fine. Otherwise, how would you guys feel about a feature gate to enable these?
**Tigran Najaryan** 34:21 Yeah.
**Michel Laterman** 34:23 Yeah… we've… Generally, prefer feature dates for anything that might be Might interfere with how something runs on a customer's system.
So, big support for that over here.
**Dakota Paasman** 34:40 Yeah, I think… Same… same for us. I think that would be acceptable.
**Evan Bradley** 34:45 Cool. Okay.
**Dakota Paasman** 34:47 Yeah, I can… I can write up an issue with a lot of what we've just discussed, and… We can go from there.
**Evan Bradley** 34:58 Thanks.
**Dakota Paasman** 34:59 Diff.
**Tigran Najaryan** 35:00 Okay.
Good. Thank you.
Which one's the next one? No, this is the same one.
**Michel Laterman** 35:09 Yeah, so… This, so, a bit of context is, last week we have Big security use cases, and we really want to prevent duplicate agent IDs.
So… In the spec right now, we have a section on detecting duplicate web sockets for an agent.
I'd like to know if there's just general support for making that They basically use the same wording for duplicate.
duplication detection based on agent IDs.
Not just for WebSockets.
Yeah.
**Tigran Najaryan** 35:56 I guess that the problem… the reason that the spec says this is done for WebSockets is that there's a reasonably easy way to do it for WebSockets, right? You're just observing two connections at the same time using the same ID.
for the…
**Michel Laterman** 36:13 You only have one server, though.
**Tigran Najaryan** 36:16 Yeah, I mean, even if you have multiple, still, you can have some sort of a logic which tries to detect that by exchanging that information between the servers. For plain HTTP, it's harder, because you may just see… regular requests coming, let's say they are alternating from different agents, but they are using the same ID.
How would you detect that they are actually a different agent using the same ID? You would have to use some other.
**Michel Laterman** 36:46 Yeah.
**Tigran Najaryan** 36:47 way of understanding this is coming from a different place, right?
**Michel Laterman** 36:51 Yeah.
**Tigran Najaryan** 36:51 address or something like that.
**Michel Laterman** 36:53 Right now, the wording of the spec… Users should allot, so we can… We can use that to say, like.
your server doesn't have to do… like, at Elastic, we're gonna require authorization letters.
So, it's pretty.
**Tigran Najaryan** 37:12 You're gonna… you're gonna require what? Sorry, can you say again?
**Michel Laterman** 37:15 Authorize… authorization when using Allbound.
**Tigran Najaryan** 37:18 Okay.
**Michel Laterman** 37:19 you're gonna need some kind of API key.
And eventually, we'd like to, you know.
Offered connections, and then we can associate one ID with one API key.
**Tigran Najaryan** 37:34 Right.
**Michel Laterman** 37:35 And that would be really easy for us to do, and it would be really easy for us to say.
Agent D.
**Tigran Najaryan** 37:41 You'd have the same problem, you're back to the same problem where the two different agents may use the same API key then.
How would you ensure that they're using the different API key?
**Michel Laterman** 37:52 If… We have a… so, at Elastic, we have a specific Enrollment process, so the initial connection would use a pre-shared key.
And then once we build out management, the server would offer each agent a unique API key.
**Tigran Najaryan** 38:18 Sure, but if the agents have the same ID, how would you know to offer them different API keys?
But you're back to the same problem then, right?
perspective, it's the same.
**Michel Laterman** 38:29 What do you mean, when would the agents have the same ID?
**Tigran Najaryan** 38:33 And that's exactly the question to ask, in my We have to start there. How do you end up with agents that have the same.
**Michel Laterman** 38:39 So, if we designate an enrollment, like, our initial key as a shared secret, We could say… offer connection settings, and force a new agent ID from the server, with the I don't know what the message is called, but I know it's specifically something that these Service can offer.
And then from that point forward.
Whoever receives that message needs to use… that ID authorization key combo.
**Tigran Najaryan** 39:16 Yeah, I think we have that as a flow here, somewhere here.
It describes how you… registration or first? I think that's what you're describing.
**Michel Laterman** 39:28 Yes.
**Tigran Najaryan** 39:29 Which is fine.
**Michel Laterman** 39:32 Stop.
This would be specifically just saying, instead of… having duplication detection only apply to WebSockets, where… If a duplicate WebSocket comes in.
you can either respond with a, please change your ID, or a 401 or something. We can apply it to HTTP as well, where if we detect a duplication, we can either say.
here's your new ID, or absolutely not here for 401, don't talk to me.
**Tigran Najaryan** 40:04 Yeah. I'm fine with that. My only concern is that, I guess, I don't see a good way to implement it. How would you go about detecting.
**Michel Laterman** 40:15 It would be…
**Tigran Najaryan** 40:15 Duplicates.
**Michel Laterman** 40:16 It would be service… it would be service-specific, for sure. But I think the spec at that point just needs to recognize that of a client.
if you're… If you're connecting HTTP or WebSocket to a server, and you have a duplicate ID or a collision.
You might just get a 401 back.
Or something… something depending on the server bag. Right now, it's not clear in the spec that that's an option.
**Tigran Najaryan** 40:55 Okay.
I guess with an existing implementation, if the server detected that, and there's… there's a… it's supposed to return… it's supposed to offer a new UID, I think, right? That's what we're doing there.
There's a… There's a way to do that in the protocol, let me see, where is that?
new instance… yeah.
Supposedly, that's what the server is going to do. If you return this to an existing HTTP client, it would just work with existing GoPAMPGO implementation, I think.
I'll need to double check, but I think this should still work. What you're saying is you want to see that reflected in the spec as well, clearly.
**Michel Laterman** 41:42 Yeah, I've… yes, yes, because right now.
Right now, it's based on WebSocket.
And…
**Tigran Najaryan** 41:55 Yeah, this is what it says, right? See here, it says it should generate a new instance ID and make it… offer it in the new instance UID of the message.
So you want this to be essentially extended to the plain HTTP connections. Yeah, to be honest, I don't see any problem with extending it. My only concern would be that we're essentially making a recommendation that is not easy to follow. That would be my concern here.
because I clearly see how you would do it for WebSockets, I don't…
**Michel Laterman** 42:27 Yep.
**Tigran Najaryan** 42:28 so easily see how do you do that for the plain HTTP connections. You would have to have some sort of heuristics in place. Like I said, maybe you look at…
**Michel Laterman** 42:36 For more truck.
**Tigran Najaryan** 42:37 IP address or something like that.
**Michel Laterman** 42:38 Yeah, you, you, you… That would be… implementation-specific.
on the server side. Okay.
**Tigran Najaryan** 42:48 So we… we can say, I guess, If the serv… I don't know if the exact same wording is… is good for deploying HTTP connections, we could… I guess it would work, should detect, should means if you can do, if you can't, then you don't, I guess. Yeah, probably works.
**Michel Laterman** 43:09 Should… should on your response, also.
**Tigran Najaryan** 43:11 Yeah.
**Michel Laterman** 43:12 Gives us an option of, instead of… sending a new instance ID, we can send a 401.
Because we… we also want to stop .
**Tigran Najaryan** 43:28 Okay.
Do you… but by the way, this particular issue that I opened was… a slightly different thing. It's about… malicious behavior.
**Michel Laterman** 43:39 Yes.
**Tigran Najaryan** 43:39 impersonating a different agent, so this would be a different thing, in reality.
**Michel Laterman** 43:46 Kind of why we want to be able to respond with 41s, because for our use cases, we don't want Someone pretending to be a customer endpoint, and…
**Tigran Najaryan** 43:56 Yeah.
**Michel Laterman** 43:57 Interrupting a control flow.
**Tigran Najaryan** 44:04 I think I'm fine if we want to make that change.
I don't really see that… as a problem. As soon as the wording is shewed.
If the server is able to detect it, Fine.
**Michel Laterman** 44:19 Okay.
**Tigran Najaryan** 44:20 Let it do it?
Yeah, I'm… I'm okay.
Can't do that.
**Michel Laterman** 44:28 Yep, all live.
Got a PR up sometime this week.
**Tigran Najaryan** 44:35 Okay, sounds good.
Okay, I think we have the last one from Stanley. Is Stanley here?
**Stanley Liu** 44:46 Yep, right here.
Hi, I'm Stanley, I'm an engineer from Datadog. I'm new to the SIG, so just wanted to introduce myself.
**Tigran Najaryan** 44:57 Oh, welcome.
**Stanley Liu** 44:59 Yeah. So, basically, if you guys remember Jack Peterson, he was previously working on this proposal for adding a root certificate signing chain for message verification. Just wanted to apologize for the delay, and we are intending to pick this work back up, so… If you guys need to be refreshed on this, basically we want to add the X509 trust chain signing.
Which would allow customers to have full trust in the artifacts they receive, that they are received, that they are provided by the vendor itself.
This will prevent, in the case that an op-amp server is compromised, for, these compromised configurations and binaries to not be accepted at the client side. It's just something that we feel that op-amp is lacking.
And we feel that it's a large risk at scale that could lead to remote code execution or data exfiltration.
And we want to implement this as an opt-in capability, so that it would be backward compatible, as well as optional.
So, yeah, I just didn't know the current state of things, what people think about this. There's also a document proposal that Jack wrote that I linked in the meeting notes, so I was wondering if anyone has any opinions or feedback.
But additionally, we are working on a POC for this, so I think once we have alignment from everyone that we want to proceed.
We can either expand on this document to have, like, a more detailed RFC, if you guys want, or we could go forward with the, the proof of concept.
**Tigran Najaryan** 46:50 I think we'd want a bit more eyes on this. Like you said, it definitely needs to be some sort of an opt-in behavior. It can be the only way.
If someone doesn't need this extra… Verification, then they use just what we have today.
I would also like to understand how much complexity it adds to the implementation.
I understand it conceptually.
But in practice, how much more complexity it is bringing to the code base would be also good to know.
If you do have a prototype already, or did you say you're a working guy?
**Stanley Liu** 47:31 Yeah, we're working on it. It's like…
**Tigran Najaryan** 47:32 Okay.
**Stanley Liu** 47:33 mostly in place, we have, like, an end-to-end test, but, in terms of complexity, I can definitely get back to you on that, like, sizing and stuff, yeah.
**Tigran Najaryan** 47:42 Yeah, it would be great to see it if you have… when you have it, and are you doing it on a fork of a… of a… what is it, an open Go fork? Is it for the Go version? How… what are you doing exactly?
**Stanley Liu** 47:53 Yeah, we have forks… we have forks of OpenGo, OpenSpec, I believe Contrib as well to, fork the supervisor, so we have some changes there, and, like, an end-to-end test, so… Yeah, once we have that all ready, I can present it, and you can see how complex, what things are being added, and etc.
**Tigran Najaryan** 48:16 Do you… do you have the spec changes in place already, or you're still working on those as well?
**Stanley Liu** 48:23 I believe they're committed, but I don't know if they're, like, finalized yet. It's pretty, like, in progress.
**Tigran Najaryan** 48:29 Okay, it would be, I guess, useful to start early, so that you don't do all the work, and then we end up saying no, or we end up saying significant changes are needed.
So… As soon as you have something that you would like.
to get some feedback on, maybe poster links here, and let's take a look, and I think we should take it from there. I think I… I think the concept is reasonable, it would be useful to have. However, I think we would need to balance that with how much more Complexity of the implementation we're ending up with.
If it's too complex, I would even consider it being some sort of an extension to the specification, and… have some sort of a flaggable behavior in OpenGo, which would allow you to Booking to the… whatever exchange is happening there to, essentially, Have this as an extra.
extra, sort of, implementation, which is not there by default.
But if it's simple enough, then maybe we don't have to go to… Don't have to go there, right?
So, let's do that. When you have something that is reviewable, it would be good to take a look at it and see where it takes us.
**Stanley Liu** 49:52 Yeah. No, that sounds good. Definitely agree. I think, so I'm working with one of my teammates on this, and, he was working on the implementation, but last time I checked, it wasn't very complex, so, we'll definitely share when it's ready.
But, from what I'm gathering, it seems like, the current proposal and, document are… Maybe detailed enough, so, maybe we can move forward with Getting feedback on the proof of concept, and then proceeding from there instead of, like, writing a more full-fledged RFC.
Because this, document that Jack wrote is already pretty detailed.
**Tigran Najaryan** 50:32 Yeah, yeah.
**Stanley Liu** 50:34 Okay.
Cool. Yeah, thanks a lot.
**Tigran Najaryan** 50:36 Yeah, I'll take another look.
And maybe the… the community can also take a look at it.
An implementation would also be really helpful.
**Stanley Liu** 50:46 Yeah.
**Tigran Najaryan** 50:54 what is… what's the… is this supposed to be diagrams, I guess?
**Stanley Liu** 50:57 Yeah, there's definitely diagrams.
**Tigran Najaryan** 51:04 Let's see if refreshing helps. Now they are.
**Stanley Liu** 51:06 Oh, okay.
**Tigran Najaryan** 51:07 What's going on here?
**Stanley Liu** 51:09 Yeah, I'll try to…
**Tigran Najaryan** 51:10 Can't fix them.
**Stanley Liu** 51:12 Maybe I'll copy it into, like, a… Another document to fix it.
**Tigran Najaryan** 51:18 Okay, thank you.
**Stanley Liu** 51:19 Yep.
Okay.
**Tigran Najaryan** 51:24 I wasn't…
**Stanley Liu** 51:24 Oh, sorry, is the.
**Tigran Najaryan** 51:26 Go ahead.
**Stanley Liu** 51:26 to share it, just the CNCF Slack channel, like, Alta…
**Tigran Najaryan** 51:30 The Slack channel and the issue, I guess, it would be useful to do both.
**Stanley Liu** 51:35 Okay, sounds good. Thanks.
**Tigran Najaryan** 51:39 Okay, thank you.
Anyone has comments on the topic?
Yeah, that was the last topic in the agenda. Anything else, anyone?
Alright, thank you all.
**Andy Keller** 52:12 Bye.
