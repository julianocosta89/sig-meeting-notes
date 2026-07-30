SIG: Agent Management WG
Date: 2025-12-10
Duration: 57 minutes
============================================================

## Zoom Recording Transcript

**Tigran Najaryan** 01:50 Hi, everyone. Hello.
**AK Andy Keller** 02:00 Whoa.
**Tigran Najaryan** 02:38 Okay, we probably should start, we have a few things in the agenda.
Jade, I think you have the first two items.
**Jade Guiton** 02:46 Right, yes.
So first to introduce myself briefly, I'm from Datadog. I was working with Jack Peterson.
And, yeah, for the past 2 months, I've been working on, building a prototype op-amp server.
And, while it seems to be working in the common case, there are a few edge cases that I don't think are mentioned in the spec that I wanted some advice on, or, like.
Question what the mental model for them should be.
The first one was, dealing with duplicate, instance UIDs. So the specification mentions… that WebSocket servers should detect duplicate UI at ease, which is possible because you can kind of tell when there's multiple connections at once.
But for the HTTP protocol, or HTTP transport, it's not… really easily doable.
But there are some possible ideas, like… If there are multiple sequences of sequence numbers.
for the same UIDs, you might, assume that these are duplicate UIDs, and so… I was wondering if there had been some thought put into the best way to do this, and whether it should be recommended in the specification?
**Tigran Najaryan** 04:12 Yeah.
I don't think I have a great suggestion. In the past.
with the solutions I work with, not all pump.
The way that we did is we used some sort of heuristics to see if what the data is coming from Looks like it's coming from different agents.
One approach was that if you see alternating source IP addresses with the same UID, then it's probably different agents that are reporting.
there may be other heuristics are possible there as well, right? I don't know if there is a great solution to this.
Probably you can come up with this sort of Possibilities there that can be not terribly robust, but maybe detect significant number of cases.
I don't know, MD, if you have any more specific experience with, with this, with your implementation.
**AK Andy Keller** 05:09 A bit. The other thing we've looked at is the other set of The attributes, the identifying and unidentifying attributes, if they are different, You can often look at headers, like the… You know, maybe the remote address or something like that, but if that's… That might not be different if it's coming through.
A little balancer or something like that, and they might all have the same address, and so that's… even though they're distinctly different agents.
Yeah.
I don't remember if the MAC address is usually in there as an attribute. By default, I believe our… our our distro includes MAC address as an attribute, and we've used that, It's very unlikely to be duplicated.
So… It…
**Tigran Najaryan** 06:02 It only works if it's on the same network, right?
**AK Andy Keller** 06:04 You can't have it for containers. So…
**Tigran Najaryan** 06:08 Yeah. Yeah.
**AK Andy Keller** 06:09 If you've actually duplicated a container, so… We haven't found a completely foolproof way of doing this, but, I, I think if… if you… It might be useful to have a discussion around this and, When I say, you know, like, open an issue, and let's get this… figure out if there's some language we want to add to the spec.
That would… that would help people in this fashion, because there's… You know, we've had… We've had some… we definitely have had some experience with this. We… we're primarily using WebSockets, and it's a little bit easier in that case, because Usually they're… they're both connected, but they're… could be connected to different nodes, and so that's… it's honestly not that much different than HTTP, because even though you've got a persistent connection.
You still need a backend database and some… To really track a list of connected agents, their latest message.
Number and, and attributes, and then compare.
**Tigran Najaryan** 07:18 Yeah, you're essentially looking at some sort of fingerprinting of the agents, right, to see if it is the same agent, does it look the same, or it looks different, but also allow for the possibility that agents obviously can change over time what they report.
And so… Some of those… flip-flopping from this to that maybe is sort of an indication, if it happens more than once, maybe an indication that this is actually two different agents using the same UID. Again, like, it's probably not going to be completely Reliable, but maybe can serve… 90% of cases, hopefully.
**AK Andy Keller** 07:59 I will say that we've had… we have had this pop up many times.
It does happen in the wild. Ideally, the answer would be, you know, you're doing it wrong. It should never happen when the spec says that the UID uniquely identifies an agent, but it definitely happens.
**Tigran Najaryan** 08:19 I saw this happening, Andy, when people cloned VMs. You have a VM with an agent running inside, you just clone it, and it's the same agent, same UID, nothing changes there. It happened in… I saw it in production, actually, happening.
**AK Andy Keller** 08:34 Yeah, we've seen it with… somebody creates a… An agent that, you know, feel good about this installation, they want to use this as now a template to… deploy lots of agents that look just like this one, and it turns out that they, you know, all include the same UID, so…
**Jade Guiton** 08:52 Okay, it's helpful to know that this is something that happens, and that, yeah, I should probably implement a heuristic for.
**Tigran Najaryan** 09:02 Probably not very often, though, right? If you're managing your infrastructure properly, Shouldn't happen, hopefully, but it.
**AK Andy Keller** 09:10 Yeah, like I said, we've definitely seen it quite a bit, and we are, you know, tracking telemetry on behalf of those agents, and it gets Really bad when you… because you… you get, like, multiple counter resets and things like that.
When you have different agents reporting, different calendar values, and… It can… it can really be a problem, so…
**Jade Guiton** 09:35 Hmm.
Okay, that makes sense.
And the second topic I wanted to bring up, I know it's something the spec specifically says is out of scope.
Which is, detecting whether an agent is active or not.
And, like, to be able to… to, handle the op-amp protocol, we need to keep some states, but probably not indefinitely. There needs to be a TTL.
But, the spec makes no guarantees about how often an HTTP agent will pull the server, so it's hard to set the TTL On that data in a… in a useful way.
And one way to potentially get around that would be to impose a polling interval using the report's heartbeat capability, but I'm wondering if that could be a… A problem for some users, or simply for agents that don't implement that feature.
Perhaps, like, would it be reasonable to… add… Some way for the agent to report its own polling interval?
Instead.
But that… Sound like a good idea?
**Tigran Najaryan** 10:57 So the spec today says, what the default value should be, but then it… I think it says the server shouldn't rely on the default, because the agent may choose to do something differently.
And then the server… can also instruct the agent to use a particular Intel vial, I believe. But then, you're right, If the server doesn't do that instruction, and the agent chooses not to use a default.
then the server has no clue, right? There's no way to know.
I guess we could, maybe, for the agent to tell what is it precisely that it's using.
it's gonna be based on some heuristics, again, anyway, right? Because you may lose a heartbeat, right? You never know Whether you're always receiving everything, so you probably are going to set your inactivity time.
To be a multiple of the heartbeat interval, anyway.
**Jade Guiton** 12:01 It's something I thought about, detecting the interval, but the problem is that this requires you to hold some state.
To detect the interval between the two messages.
So if the goal is to… know the TTL of your data.
there's kind of a chicken and egg problem. You need to know the TTL before you can set that state.
Otherwise, there's the risk of just keeping it indefinitely.
**Tigran Najaryan** 12:32 Right. I mean, you wouldn't choose it to be indefinite, right? So you'd put some upper bound on that, anyway.
**AK Andy Keller** 12:37 Yeah, an hour, or something like that, but I… but that… that would be another… another option would be to specify a… An upper bound, or at least, you know, highly recommend. You know, because at some point, I… you know, you're just gonna… you're gonna end up with a lot of latency if polling is once a day or something like that, you know, that's not…
**Tigran Najaryan** 13:01 Yeah. At some point, you're going to consider it inactive anyway. If the agent reports once a day.
Is that an active agent anymore?
Probably no, right? If it doesn't report within a few minutes.
I would call it an inactive agent. I don't know why would anyone choose the heartbeat interval to be, let's say, more than a few minutes, right? Why would you want it to be once a day?
And if you do, then the notion of activity is probably Not very interesting concept anymore, right?
So… That's a… that's a possible way to treat it that way, right? Set the… your default inactivity period to be 5, 10, whatever minutes, half an hour.
Then, if you want to be more precise so that you detect it earlier, you can watch the intervals between the hot pits that you observe on the server side.
and set that as a multiple of that observed number somewhere. We could look into adding that as a number, so that the agent specifies in its request that This is the anticipated next.
request that I will be sending, we could do that.
I don't know if there is a lot of value in doing that, because this is going to be, anyway, not a guarantee of what the server is going to see there anyway.
And what if the agent then decides to change that, because it was reinstalled, and it now has a different configuration suddenly?
And your server expects it to report when it doesn't report anymore.
So… Is it going to be a whole lot more reliable if the agent reports it? I don't know, I'm not… I'm not sure about it.
I would opt it… it's gonna be a positive decision anyway on the server side, right? No matter what you do. There's no guarantees.
And if you have to have some sort of fuzzy logic on the server side, maybe you just do that. You rely on just that fuzzy logic, and… Don't do anything special on the agent side.
**Jade Guiton** 15:06 Right, so I guess one way of dealing with that… Would be to… Impose a maximum value for the polling interval.
Which I guess can be just a requirement for a particular endpoint. I guess that could be a… That could be, one way of doing it.
**Tigran Najaryan** 15:27 If you control your agents, then you do that, right? You can probably impose Some sort of maximum reporting interval.
If you don't, then… who knows, right, what they are reporting. But if you have the control, then… then… You choose whatever number you feel comfortable with, and then on the server side, you now know what to expect.
**Jade Guiton** 15:51 Right, yeah, the problem is that in my case, I would not have control over the agents, so… It would be a matter of saying, if you want to use this endpoint, you have to set your polling interval to something not ridiculous, like less than an hour.
**Tigran Najaryan** 16:06 Yeah.
**AK Andy Keller** 16:08 I guess what it comes down to is what… What is the goal of, of… Identifying what's active and not, and is it considered active if it's pulling Once an hour, or once a day, or something extreme like that.
**Jade Guiton** 16:25 Right, yeah. In my case, it's just a matter of showing to the user, like, their agents, essentially.
**Tigran Najaryan** 16:34 Which is that, like, it's a soft requirement, right? You just can decide that something is active, it has reported At least in the last 5 minutes, then it's active, right?
probably if the only purpose is to visualize that somewhere in the UI, that may be good enough, right? Because you're not making any… Part decisions based on that state.
Anyway, so… who cares, right?
**Jade Guiton** 16:59 Yeah, it's definitely not… extremely critical. It's just that there's a… a balance, I guess? If the…
**Tigran Najaryan** 17:07 If the, the, the…
**Jade Guiton** 17:09 the period… Between heartbeats that we expect is too high, then an agent can linger for a very long time in the visualization, even though it's no longer here.
**AK Andy Keller** 17:21 And vice versa, if it's too short, you can have agents pop in and out.
**Jade Guiton** 17:25 But, yeah, I think… I think it's pretty reasonable to use a detection method, like you recommended.
**AK Andy Keller** 17:35 Yeah, we do the same thing, by the way, and it is helpful to… people want to know how many active agents I have, and if I'm going to deploy a configuration, how many agents are going to get this configuration, and if… You know, you… It makes sense to track this.
I don't think I have an easy answer, though, on… You know, on what… what heuristic to use, and I think it's pretty subjective.
**Jade Guiton** 18:06 Yeah, that makes sense.
Do you think there could be, like, potential… complaints about egress costs if the server enforces a polling interval that's too short. I… Doubt it, since it's not… it would still not be all that often, but… I'm not sure if there is a…
**Tigran Najaryan** 18:27 It depends how often it is, right?
**AK Andy Keller** 18:29 That's good.
**Tigran Najaryan** 18:30 If the agent to report every second, then that can add up.
**Jade Guiton** 18:35 Right, right, and nothing like that, but, yeah.
I guess… Since the… the client has a configuration to set the polling control, I'm not sure if Users expect That to be enforced.
at the expense of what the op-amp server says, but I guess the op-amp server has the ability to reconfigure the agent anyway, so…
**Tigran Najaryan** 19:02 Yeah.
I… I don't really know… What are the use cases where people would choose to use a different reporting interval than the default?
without understanding those use cases well, it's a bit hard to answer this question, right? When does that really happen? When do we see that? Is that… Is that 30 seconds?
what does that become? Is it a minute? Two minutes? 5… 5 hours? A day? Why is it then happening, right? A solution to those may look different, depending on what exactly is the reason for changing the default.
So, I would say… I would stick to the simplest approach here. If it were me, I would just go and just set some fixed interval in my backend and say if I haven't seen the agent reporting anything in the last 5 minutes, I'm gonna consider it inactive. And if I haven't seen it for 24 hours, I'm going to just remove it from the list of agents.
Completely. Something like that, right? Just… I would just keep it simple until… I have evidence that that's not good enough, and I need to do something more about it.
**Jade Guiton** 20:17 Hmm. Yeah, that's very fair.
I think that's…
**AK Andy Keller** 20:23 WebSockets as well.
**Jade Guiton** 20:25 Sorry?
**AK Andy Keller** 20:26 Are you doing… are you implementing WebSockets as well?
**Jade Guiton** 20:29 Yes, both. In the case of WebSockets, yeah, there is an easier solution, because as long as the WebSocket is connected, we can assume that the agent is live.
**AK Andy Keller** 20:40 Dear.
You'll want to just watch for reconnects, because that's pretty typical.
So give yourself a little grace period for a reconnect.
**Jade Guiton** 20:50 Definitely.
**AK Andy Keller** 20:55 Otherwise, you have your agents going inactive.
You know, it all depends on how your load balancer's configured, but, I think we.
**Jade Guiton** 21:05 Of course, two and a half.
**AK Andy Keller** 21:06 workbook.
**Jade Guiton** 21:10 Makes sense.
I think we can move on to, Bundes Point? I don't know if that's how it's pronounced.
**JM Juande Manjon** 21:22 One day is fine.
**Tigran Najaryan** 21:26 Okay, go ahead, Grande.
**JM Juande Manjon** 21:28 Okay, let me… I'm gonna look at the document… So, I think we have these… feature request for, providing Docker images for the PAN survey and agent example. Thank you, Tigran, for the feedback. I'm gonna… Follow up after the meeting, but this is pretty ready to go.
The second thing is I want to work, on… the example is focused on providing custom messages demo, where, the community can see how we can leverage custom messages. So, looking at that, I realized that the custom messages doesn't fit very well.
In my use cases, because currently the spec said that we can handle the version, the data schema version of the payload in the So, in the capability, but I think this is not right, because, like, imagine I have 10 different schemas, so I need to have capability B1, B2, V3, B4, and this is not scalable. So, in order to solve that, I was thinking that we can provide a schema version In the same payload, so the agent or the server can identify With data and which format it comes from, and we don't have to overload the… the definition of the capabilities. We can have just a single capability and different schemas.
I think they will fit very well in my use case.
**AK Andy Keller** 23:09 I looked at the issue this afternoon before the meeting, but I didn't have a chance to comment, but my concern with that idea is that the capability is intended to be, like, a contract.
Between the agent and the server to say that you support this capability, and that implies all of the messages that are involved in that capability.
And so if you have an… let's say you now introduce a new schema version of a message.
Now, now the server, or, you know, maybe some of your agents are… are producing messages with schema version 3, but the server doesn't know.
how to parse schema version 3, it doesn't know what that means.
Now it doesn't actually support that capability.
We can't parse that schema version, so… So then I think you end up kind of back in a loop and saying, well, how do we say that the server can support schema version 3, and it's by creating a capability with version 3 that this… and now the server and the agent both agree that they… they can parse both of these messages. I think one thing you might want to consider if you're… if you find yourself… I'm not sure how you're doing your encoding.
And if it's rapidly evolving, and you think that there's going to be many different schema versions, but you could… Include in your… in your payload, the version.
And have your kind of an initial payload be just the version and the data, and then you have to, you know, parse that again, essentially, based… now that you know what the version is, now you parse the payload based on that version.
You're still going to end up You know, in your own situation, with… Servers that can't handle those versions.
Or vice versa. But, you know, that might… I guess I need to understand Your use case more, to understand how the message is evolving.
And… and how… But, but it's somehow still compatible. Makes sense.
**JM Juande Manjon** 25:24 So Medicare is simple. So, we have, different medical devices that is sending, custom messages. So, let's say you have different robots, A, B, C, D, and now you have to have you need to have capability A, capability B, capability C, but all of them are the same functionality that the comp says is they are sending a custom heartbeat to the server, but each system, each robot, has a different schema.
So I need to handle at this capability level, when actually the capability is just Harvard, and I can't decode the information because its schema and format are different.
So now, if you said I need… I can add… the schema into the payload, but I need to decode the payload to know the schema version.
And there.
**AK Andy Keller** 26:18 That's where I was suggesting, you know, like a double encoding. Basically, you have…
**JM Juande Manjon** 26:22 your initial encoding, maybe it's a protobuf, and the protobuf is just schema version.
**AK Andy Keller** 26:27 And… the payload.
And now that.
**Tigran Najaryan** 26:30 The data field is opaque binary sequence, right? So you can put the schema there inside the data field, essentially.
**JM Juande Manjon** 26:36 Right, so you rely on implementation for that. It's better that part of the spec identified that you can separate the consent, so you can have… and involve the category of… the concept of the feature in a different way that involve the schema.
Because they are different, so I think it's… the concept of the capability is a high level.
feature, and the schema is very low level. I'm forcing that the schema cap has to be part of the capability, I think it's not right.
To enforcing the spectr.
**Tigran Najaryan** 27:07 Yeah.
**AK Andy Keller** 27:08 Another way you could solve this is with… sorry, Tigran.
**Tigran Najaryan** 27:11 No, no, no, go ahead, go ahead.
**AK Andy Keller** 27:12 Would be to… Support, you know, more message types and encode the version information into the message?
Type itself, so the capability is, you know, robot heartbeats, and the message is heartbeat… Slash schema version.
And you have, you know, from the message type, you can basically determine what schema version the payload will be.
But that sort of double encoding, is a pretty common pattern, where when you receive a payload.
A lot of times, you'll see… A pattern where you have maybe a type.
and you see this, like, in Go when you're deserializing objects. You might deserialize into something that has a type, and then it just… you deserialize the rest of it into, like.
of string any, and then you… now that you know what the type is, you deserialize that map of string n using map structure into… into an actual thing, now that you know what you're actually trying to decode into.
**JM Juande Manjon** 28:16 Right, but that's the reason that always a payload has a payload and header.
Right? And this version schema could be considered part of the header. So if the concept… so we can discuss that. You can have a unique payload and pull the header inside the payload, and have the double decoding. That's a… that's a workaround. But I think we should separate the payload to the versioning. In general, I mean, like.
Common forms.
**Tigran Najaryan** 28:41 That's the… that's the question, why do you want to separate that? OPAMP doesn't care about that separation. OPAMP… the generic OPAMP implementations will not know what to do with those two separate fields. They don't care about that separation.
**JM Juande Manjon** 28:54 in…
**Tigran Najaryan** 28:55 You have the data field and the schema that describes the format of the data field. Now, if you combine those into one data field, you have the exact same functionality, right? Nothing… nothing changes there, really, unless… You have somebody who has no idea about the format of the data field, and somehow they need to know the schema. But who is that? We don't have any implementation like that who doesn't know how to decode the data field, but somehow cares about the schema field. Why would… why would anybody care about that schema field?
Right, so that's the distinction there, right? The separation of those two pieces of information into two distinct fields in the protocol message.
Achieves nothing compared to having that as a single paragraph message, because there's no one who is interested in the schema field separately without knowing how to deal with the data.
If you can pinpoint to a use case where it matters.
then we can consider it. But so far, it seems to be… it's my custom implementation of an agent. I control the format of the data field. I design it. I know what the format of that field is.
In that case, you can choose to include the schema as the header of the data field. The first byte is the version number of the schema, whatever. Your choice, right? So, why do you need it separately?
**JM Juande Manjon** 30:21 Mesu is we need to add a new capability for that.
Right? And that's my major concern.
**Tigran Najaryan** 30:29 I don't think…
**AK Andy Keller** 30:30 I think you need to add a new capability if you can use a single capability and then… Add your schema version into your payload.
Right. I think there's a risk that you're going to… Add the… add a… Handling for a schema version in one place and not the other, and now you're going to actually be incompatible, but that's… You know, that's something… That you'll need to solve.
In your…
**JM Juande Manjon** 30:55 Okay, we should, we should update the spec, not to recommend to do, add the schema up into the capability.
**Tigran Najaryan** 31:06 I think that's a fair… yes, we say that capability must specify the format.
maybe it's… I guess maybe that… that is what is too prescriptive, in a way, maybe, in the specification. We can say that the format is… agent-type specific, right? It's up to, essentially, whoever designs the custom message to choose the format of that data, and whether it's fully controlled by capability, or in addition to capability by some other aspects, including maybe a leading portion of the data field.
That's, again, it's none of the old pump specifications concerned, right?
**AK Andy Keller** 31:46 Opam doesn't care about it.
**Tigran Najaryan** 31:48 There's nothing that all pump implementation.
**AK Andy Keller** 31:49 Is there language in there that says something about the encoding?
**Tigran Najaryan** 31:52 It says, we say that, the data field description says binary data of the message, the capability must specify the format of the content of the data.
For each custom message type it defines.
So we're essentially hinting that all you need to know is just the capability.
Which is true, I guess, but then, sort of.
Obam doesn't really care about it at all, right?
What you do with your data format is up to you.
whether it's capability controlled, whether it's, I don't know, JSON data, which contains whatever you care, doesn't really matter. OPAMP has no… reason to deal with that field. It's just a sequence of bytes. We don't care from our perspective.
**JM Juande Manjon** 32:48 Okay.
**AK Andy Keller** 32:49 Yeah, and I guess I don't… maybe I… just reading it… I mean, I did write it, so I guess maybe I'm reading it the way I wrote it, but the… I think it… what I… what I intended here is really just that any capability can use any format it chooses. It could use protobufs, XML, JSON… And the capability should just document As part of the capability, what… Format those messages are in, so that The… anybody implementing that capability Knows what to expect.
And that's where I… that's where I think we run into compatibility issues, if you… If you have a new field that has a schema version.
and you say, I support Capability X, but now you get a message With a schema version, you don't know about or know how to parse, and now you don't really support capability X anymore.
And that's why the intent was to make it a new version the capability if there's a breaking change. Now, often in practice, we have a couple of these custom message implementations.
you know, we're using something like Protobuff or JSON, either of which is pretty flexible in terms of You know, adding fields, and we can say, you know, if we don't see this field.
that it defaults to this value, and therefore we still support the capability. But if… if the lack of that field really means we don't know what to do, then that would be a new version of the capability. You know, if it's a breaking change that requires that you have knowledge of all the fields, then it's a new version.
And I can imagine that… at some point, this scales… Where you might support 100 versions of a capability, and then… You know, that really was never the intent to grow like that, and… because these messages of support and capabilities will be quite large.
But… But I sort of plan to solve that when it comes up, I guess, and…
**JM Juande Manjon** 35:00 Okay, that's good stuff, thank you. So, Andy, so I'm gonna focus on custom messages, I think you have great experience on that. Can I follow up with you.
**AK Andy Keller** 35:09 Sure.
Yeah, hit me up on the Slack.
**JM Juande Manjon** 35:12 True, thank you.
So, that's all for me?
**Tigran Najaryan** 35:19 Okay, thank you.
That's all we have in the agenda. Anything else, anyone?
**AK Andy Keller** 35:25 There was something else that Dakota and I were talking about this week. We didn't… we were thinking about posting an issue, just wondering… Want to get a sense of the appetite, so… we've run into some… Issues with the supervisor, as a deployment model.
Where our current agent is capable of hot reload, and now we're moving to a supervisor-based Implementation, and this extra binary is causing issues with things like Windows services, you have The binary is actually the supervisor, and there's questions about logging, and… Memory usage and all the things that you might expect from a process.
And it's… it's presenting some challenges, and… I think… the sort of… the hot reload that's been added upstream since we came out with Supervisor, or since the Supervisor was designed, you know, mainly the SIGHUP and reload configuration, would make it possible to support… Modifying the configuration via an extension alone.
And so we've thought about, you know, extending the existing extension to support modifying configuration, or creating a new extension.
that was, you know, kind of a separate read-write extension, but I'm just curious what your thoughts are on an extension-based… approach.
**Evan Bradley** 37:11 So, if I understood… If I understood right, you were saying have the extension send SIGHUP to the collector process?
**AK Andy Keller** 37:21 It's, there's no reason.
**Evan Bradley** 37:22 Shouldn't work right.
**AK Andy Keller** 37:23 Yeah, essentially because there's no… programmatic hook. We could either add a programmatic hook that an extension would be capable of reloading configuration, but another way to do that is to… Send a SIGHOP to yourself, which… We've spiked it out, and it… it… You know, seems reasonable.
**Tigran Najaryan** 37:44 My opinion is the following on this topic.
**AK Andy Keller** 37:48 Yeah.
**Tigran Najaryan** 37:48 There's a possibility for things to go wrong.
During that process, right? The config is incorrect, and the collector no longer starts.
There is no good way to revert that anymore without a supervisor.
The purpose of the supervisor is primarily that, to isolate complicated stuff from the simple stuff, essentially. You keep the simple things in Supervisor, you make it as reliable as possible, and things that can go wrong they go inside the collector's a separate process. If it crashes, it burns, doesn't really matter. You still have your supervisor, you can roll back to all sorts of things.
That, in my mind, is the important distinction there.
Can you do what you described? I think, yeah, possibly. It's doable, and maybe it's possible, like, as an alternate deployment, you do that in some cases, but that has that downside, right? With the supervisor, technically speaking, you can test it to death, and be very confident that the supervisor never fails and never crushes. Whatever happens to the collector is fixable. The supervisor will take care of fixing that. It will roll back.
Without the supervisor, you no longer have that confidence in me.
**AK Andy Keller** 39:10 Yeah, we made a list of, kind of, the things we would need to solve, and that is one of them. I think there are ways of solving it, either writing, you know, maybe More limited cases, where… You need to know You know, first of all, you need to know where the config is that you're writing and you're changing before you restart.
Because the extension would either receive that and write it to disk and restart the collector, but the other… you know, and you could also… You know, back up the existing collector to another file.
**Tigran Najaryan** 39:45 Sure. You can do all sorts of things, but in the end, fundamentally, collector codebase is, what, orders of magnitude bigger than the supervisor?
I personally can never be as confident in the entire collector not doing something wrong during the startup.
**AK Andy Keller** 40:04 Right, there could be a panic in some components.
**Tigran Najaryan** 40:06 I can do with a, yes, with just a supervisor. That's… that's the way I see it, right? You can… you can spend a lot of effort and make improvements to the collector.
It's… in my mind, in principle, it's never fundamentally possible to make a codebase that is 100 times bigger than the supervisor, to be as robust, if you dedicate the same amount of effort to it, right?
**AK Andy Keller** 40:32 What are your thoughts for those deployment challenges of… you know, Windows services.
**Tigran Najaryan** 40:37 I would like to understand what exactly the challenges are, so it's not clear to me. Why wouldn't that work correctly? So, what's the problem?
**AK Andy Keller** 40:45 I'm certainly not a Windows expert, so… I…
**Tigran Najaryan** 40:51 So, Windows Server Understanding…
**AK Andy Keller** 40:53 Is that your, you know, your entry point now is the supervisor itself, and not…
**Tigran Najaryan** 40:58 Yeah, yeah.
**AK Andy Keller** 40:59 And so… Or take, you know, Kubernetes as an example, or, like, a container. There's… there's, there's… different, Heuristics for when you might expect that process to be… you know.
Killed and restarted, or something like that, that might be handled.
at either the system D layer, or at the Windows Service layer, or in Kubernetes.
And now you're kind of delegating that to the supervisor?
And that has made some people feel uncomfortable about… Now, the supervisor's in charge, And now, if…
**Tigran Najaryan** 41:46 I see, I see.
Yes, I think it's a fair concern, because you're absolutely right, we're delegating some of that watchdog functionality that is built in into the Windows services system, or into the Kubernetes control plane.
To the supervisor, and the question is then, Is it… is it actually as good as what you get from those systems? I think it's a fair concern, yes, I agree with that. We would have to… demonstrate clearly that that supervisor is doing a great job, being the watchdog. Because, yes, with Windows services, you get the same functionality. If your service crashes, it will get restarted automatically.
**AK Andy Keller** 42:33 We're expecting the supervisor to serve that role.
**Tigran Najaryan** 42:36 I agree with you, I don't think we, at the moment, can demonstrate that it is actually as good as the bottle-tested solutions that you get in Windows, or… whatever you get on Linux is a sys control or whatever, right? Or Kubernetes control plane, for that matter.
**AK Andy Keller** 42:55 I think it's a fair concern.
**Tigran Najaryan** 42:57 Yes.
**AK Andy Keller** 42:58 And I think the other thing we're trying to… solve is just adoption. You know, if you think of the migration case, where somebody deploys a bunch of hotel collectors, they feel really great about their deployment.
Now they want to have them managed by a control plane.
Maybe they're building their own collector. It would be really nice to just say, you need to add this extension, and then add this configuration, and now you have a managed version of that.
**Tigran Najaryan** 43:24 Yeah.
**AK Andy Keller** 43:25 Whereas now we need to… Have them, you know, either build different containers with a different entry point, or, or install a different… Component, whether, you know, a different package or something else that is going to run the supervisor instead of running the collector that they're already running.
**Tigran Najaryan** 43:43 Damn.
I think, Andy, I think it's worth exploring, if you can show that To… to have a reliable solution, all you need is some sort of a storage, local storage, so that you can keep your rollback data, and… a guarantee of a restart, right? If those two things are sufficient to have a… to have a fully reliable solution, then maybe, why not, right? So maybe you start your collector in some sort of a limited mold.
after a failure, let's say, right? You try to figure out whether you need to do a rollback without actually starting everything again, which could cause another crush and stuff like that, right? So, essentially turning the collector itself into that Much smaller thing where most of the code is essentially disabled and can't do something wrong.
Then, yes, maybe? Worth exploring, I guess.
**AK Andy Keller** 44:47 Okay.
We might… we might push a little further on it, and… and… and, You know, kind of document the blockers.
**Tigran Najaryan** 44:59 Yes, yeah. One other limitation that I think you will likely hit is under Windows, I don't think you can override an executable that is running, currently.
I think on Linux, you can do that.
**AK Andy Keller** 45:16 Yeah, so that you're talking.
**Tigran Najaryan** 45:17 Your windows broke, right?
So the upgrades are not going to be possible, I believe. You would have to have a healthy.
**AK Andy Keller** 45:23 We need to look into that a little bit. We have a process for supporting upgrade with our current distribution, but it does involve some bootstrapping code, but we basically launch another update or executable that…
**Tigran Najaryan** 45:36 you have a helper process which does this, so, sort of a limited lifetime supervisor, right? Which is only there just for the purpose of the upgrades.
**AK Andy Keller** 45:47 And it is actually capable of detecting when the new process isn't able to start.
**Tigran Najaryan** 45:53 It has to then…
**AK Andy Keller** 45:54 also roll back.
**Tigran Najaryan** 45:55 Yeah, yeah.
**AK Andy Keller** 45:57 We… you know, I think that's part of what I'm… just… You know, challenged with is… we've sort of solved all this in our own distro.
And we don't want to have our own… you know, the goal isn't to have our own distro be the only distro that… this… this is solved with, right? We want this to be… anybody can build their own collector and, and just kind of turn on remote configuration, or remote updating, and, you know, turn on op-amp, basically.
**Tigran Najaryan** 46:27 If you solved it, if you think it's successful, then sure, why not?
Offered to the collector.
I don't… Evan, I don't know what… what's your view on the.
**AK Andy Keller** 46:39 No, you're…
**Tigran Najaryan** 46:41 whether…
**AK Andy Keller** 46:43 Our solu- our current solution is very much a different… bootstrapping of the actual collector pro… the service, like, in code. So instead of… running, you know, directly. It's… It's at the entry point of the command, basically, that we're… where we're injecting the op-amp client and doing the updates and doing the configuration and all that stuff. That's why we're able to handle rollbacks and handle… so… so moving this into extension, I think, presents some challenges, but it also has the advantage of just being an add-on component. But, sorry, Evan, your thoughts?
**Evan Bradley** 47:22 So, yeah, no, I have… I have a few questions. So… I guess… I guess to address your first point about donating the bootstrapping code, I think that that would be… Well accepted, if it's fairly simple or is easy to isolate, I guess my concern is we wouldn't want to add, like, a bunch of complexity to the service just to get this remote, configuration functionality that some people may not want. I think that there would be some… some friction there.
**AK Andy Keller** 47:56 Right.
**Evan Bradley** 47:57 A couple questions around, assuming that we… we do… or we leave out the bootstrapping in the service. Have you looked into implementing an op-amp provider yet? Or are you just looking at doing the extension, or did you look into that and it wasn't a viable solution? That was my understanding of how we would achieve.
**AK Andy Keller** 48:22 interesting.
**Evan Bradley** 48:22 configuration. And that would, since it's earlier in the collector's life cycle, that would, potentially allow for keeping the collector alive.
Until we receive a further update.
Or… so, okay, let's say… let's say we start it, collector fails to start, you could hypothetically have the comp map provider stay alive and resupply configuration. I don't know if the mechanisms are there for that, but the infrastructure for enabling that kind of functionality is already there.
I guess, has that… is that an avenue that you've explored? I guess that's just my opening.
**AK Andy Keller** 48:57 Yeah, no, I haven't looked at confaps at all.
I mean, with regard to this as a solution, it was mostly, you know, can we get a hook into… The reload that's happening now.
But the current reload behavior is, if there's an error, shut down.
**Evan Bradley** 49:16 Right.
**AK Andy Keller** 49:17 So, so, you know, I think the change would be, if there's an error.
rollback. Okay, what does rollback mean? How do I… What am I rolling back?
you know, two, and how do I… where did that come from? You know?
And considering all the different ways you could be starting your collector with… You know, with different… providers, that config could be coming from anywhere, and, you know, it's not necessarily coming from disk, so we can solve the from disk problem.
Pretty easily, but it would also probably require from disk with one config, or at least one changeable config. So we're really kind of limiting the scope, but is that… Is that, like, limiting the scope, Solving the 99% use case, or are we, Or is it insufficient and not interesting?
That's not clear to me yet, but…
**Evan Bradley** 50:15 Right.
Okay, yeah, I don't… I don't… I don't know there. The other question I had was, within the extension, you were mentioning that you have your own, kind of, like, updater binary?
Do you think it would work to… somehow repurpose the supervisor to make something that the collector downloads, and then, you know, runs this, like, mini supervisor or whatever to do the update process? Or do you think that the updater binary is sufficiently different from… How the supervisor works, that wouldn't make sense.
**AK Andy Keller** 50:52 I think it's, you know, it's different in the sense that it's not trying to communicate over op-amp.
It's… its job is to basically detect that there's a new package, I guess, launched… it's launched when there's a new package, so it launches, sees the new package.
Replaces the old… you know, backs up the existing one, replaces it.
the old one with the new one tries to execute it if it fails.
undoes that process and restarts. So it's just pretty… it's just… it's just completely different code.
**Evan Bradley** 51:26 Got it.
**AK Andy Keller** 51:26 Could that… could that functionality be included somehow in the supervisor? Maybe, but there would be… A different thing, I guess.
**Evan Bradley** 51:34 Sure, no, I mean, if there's no overlap, then no, that would probably just be something separate.
**AK Andy Keller** 51:40 There's another option here, Andy.
You don't have to make supervisor the entry point.
**Tigran Najaryan** 51:47 You can make the collector the entry point, and then the collector launches the supervisor and asks the supervisor to supervise itself.
So then, you don't lose the built-in capabilities?
Of whatever is triggering that entry.
Into the… into the collector.
So you sort of augment those capabilities by a supervisor somehow.
**AK Andy Keller** 52:13 It's okay.
**Tigran Najaryan** 52:13 More complicated, you have to cooperate, essentially, with whatever the platform gives you.
But that's another possibility. So instead of completely replacing that, try to keep using that functionality, but bring the supervisor.
**AK Andy Keller** 52:27 To do things that…
**Tigran Najaryan** 52:29 Yes, yeah, yeah.
**AK Andy Keller** 52:32 I think you have a little bit of a question of what is the config, then, and how do you know I mean, I guess the extension… if the extension knows.
**Tigran Najaryan** 52:44 The extension would need to know how to run the supervisor, and that's it, and your…
**AK Andy Keller** 52:50 It's not aware.
**Tigran Najaryan** 52:51 The configuration would be to have the extension there, then the supervisor starts and does everything that it does today, then.
**AK Andy Keller** 53:04 Yeah, it's.
**Tigran Najaryan** 53:04 It's another different possible design option.
Which, it kind of… it's… Kind of close to what you have, except that instead of having that Short-leaved helper process, you have a long-lived helper process, which is the supervisor, with a bit more limited set of responsibilities.
**AK Andy Keller** 53:26 Do we still have a problem with the supervisor can't start with the… or sorry, if the collector can't start with the new config?
**Tigran Najaryan** 53:34 The supervisor stays running, and keeps watching.
And… and if… okay. I don't know what happens if your collector decides to restart.
what happens in… if you're running it as a container on Kubernetes? Would it be considered a crash restart? Would the…
**AK Andy Keller** 53:56 Yeah, I mean, I think as soon as that process goes away, you're… That container's gonna go away with it.
**Tigran Najaryan** 54:03 Okay.
**AK Andy Keller** 54:03 But then, in theory, you'll… I mean, I guess you'd get in a crash loop. You'd reach out to OpAmp, OpAmp would give you a new config, you'd try to use that config, it would crash the collector, and you would just repeat that process until somebody intervened.
**Tigran Najaryan** 54:18 Yeah.
**AK Andy Keller** 54:19 And you can still intervene at this point.
**Tigran Najaryan** 54:21 You can sue it.
**AK Andy Keller** 54:21 being at the server side, you know.
On the op-amp side, you could supply another config and recover remote… remotely.
From a crash loop in that situation.
Because you're not modifying the container, you're just… you're modifying that collector.
Come work, I'll have to think about it tomorrow.
**Tigran Najaryan** 54:44 Oh my god, yeah, yeah.
**AK Andy Keller** 54:45 It's a good idea.
I, I like the architecture. I mean, I, I… I… And we have customers using it that are very happy with the approach, and also.
really like, you know, we have a particular customer that's in an embedded environment that Really likes the idea that the collector doesn't run if there's no config.
And they actually use that. So they are just kind of spinning up the collector on an as-needed basis.
And they can spin it up and spin it down.
And not consume resources.
But, you know, in theory, I think… You know, the collector footprint is probably pretty small with No config and no pipelines.
If it can start that way, or if, you know, we do use no ops or something like that, it's probably still small, but… But okay, that was… Spent a good amount of time on that, I appreciate it. It's good to bring in.
**Tigran Najaryan** 55:48 I'm not opposed to the idea, let's say it this way, right? I think that the current architecture with a supervisor is an option, but not the only possible option. So, it's worth exploring other options.
**AK Andy Keller** 56:01 Yep.
**Tigran Najaryan** 56:12 Cool. Great.
Anything else? Anyone?
**AK Andy Keller** 56:17 I guess I'll just mention, Tigran, that I saw your comment on the, this, the connection… message, I will spike it out, and… This was basically on the reconnect scenario, trying to be more efficient.
So…
**Tigran Najaryan** 56:35 Okay.
**AK Andy Keller** 56:38 Probably won't get swept up until after the holidays.
Sure.
Speaking of which, have we already canceled our next…
**Tigran Najaryan** 56:50 Yeah, it wasn't in the holidays, right?
**AK Andy Keller** 56:54 Did you take care of it?
**Tigran Najaryan** 56:57 No, I can't do that.
Okay, great. It's on 24th, then. It is. Yeah, Christmas Eve, yeah, okay.
**AK Andy Keller** 57:03 I don't expect many attendees if it were not canceled.
**Tigran Najaryan** 57:08 Yeah, we'll cancel that.
**AK Andy Keller** 57:09 Okay. All right, great.
**Tigran Najaryan** 57:11 Thank you, everyone.
See you next year, then.
**Jade Guiton** 57:15 Thank you, everyone.
**AK Andy Keller** 57:17 Right.
